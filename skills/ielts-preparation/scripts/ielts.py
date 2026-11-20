#!/usr/bin/env python3
"""IELTS learner profile: attempts, spaced reviews, drill levels, leverage, calibration.

State lives in $IELTS_HOME (default ~/.ielts): profile.json, log.jsonl,
reviews.json, calibration.jsonl. Skill ids and error codes come from
references/skill-map.json next to this script's parent directory.
Standard library only. Set IELTS_TODAY=YYYY-MM-DD to override the date.
"""
import argparse
import datetime as dt
import itertools
import json
import math
import os
import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
SKILL_MAP = json.loads((SKILL_DIR / "references" / "skill-map.json").read_text())
SKILLS = {s["id"]: s for s in SKILL_MAP["skills"]}
CODES = {c.upper(): s["id"] for s in SKILL_MAP["skills"] for c in s["codes"]}
HOME = Path(os.environ.get("IELTS_HOME", Path.home() / ".ielts"))

PAPERS = ["L", "R", "W", "S"]
TASK_CRITERIA = {
    "W1": ["TA", "CC", "LR", "GRA"],
    "W2": ["TR", "CC", "LR", "GRA"],
    "S": ["FC", "LR", "GRA", "P"],
}
ERROR_LADDER = [3, 7, 30, 90]          # days after each passed re-probe
VOCAB_LADDER = [1, 3, 7, 14, 30, 90]   # days after each passed review
LEVERAGE_WINDOW = 28                   # days of log considered
LEVERAGE_HALF_LIFE = 14                # older lost marks count half per 14 days

# Minimum raw score (/40) for each band. Listening and Academic Reading follow the
# widely published conversion; General Training Reading needs more correct answers.
RAW_TABLES = {
    "L": [(39, 9), (37, 8.5), (35, 8), (32, 7.5), (30, 7), (26, 6.5), (23, 6), (18, 5.5), (16, 5), (13, 4.5), (10, 4)],
    "R-academic": [(39, 9), (37, 8.5), (35, 8), (33, 7.5), (30, 7), (27, 6.5), (23, 6), (19, 5.5), (15, 5), (13, 4.5), (10, 4)],
    "R-gt": [(40, 9), (39, 8.5), (37, 8), (36, 7.5), (34, 7), (32, 6.5), (30, 6), (27, 5.5), (23, 5), (19, 4.5), (15, 4)],
}


# ---------- basics ----------

def today():
    return dt.date.fromisoformat(os.environ["IELTS_TODAY"]) if os.environ.get("IELTS_TODAY") else dt.date.today()


def iso(d):
    return d.isoformat()


def die(msg):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(2)


def load(name, default):
    p = HOME / name
    return json.loads(p.read_text()) if p.exists() else default


def save(name, data):
    HOME.mkdir(parents=True, exist_ok=True)
    tmp = HOME / (name + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    tmp.replace(HOME / name)


def append_jsonl(name, rec):
    HOME.mkdir(parents=True, exist_ok=True)
    with open(HOME / name, "a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def read_jsonl(name):
    p = HOME / name
    if not p.exists():
        return []
    return [json.loads(line) for line in p.read_text().splitlines() if line.strip()]


def profile():
    p = load("profile.json", None)
    if p is None:
        die(f"no profile in {HOME}; run: ielts.py init")
    return p


def round_half(x):
    """IELTS rounding: nearest 0.5, with .25 and .75 rounding up."""
    return math.floor(x * 2 + 0.5 + 1e-9) / 2


def fmt(b):
    return "-" if b is None else f"{b:.1f}"


def resolve(tag):
    """'g.articles', 'ART', 'g.articles/ART' -> (skill_id, code or None)."""
    t = tag.strip()
    if "/" in t:
        sid, code = t.split("/", 1)
        if sid not in SKILLS:
            die(f"unknown skill id '{sid}'")
        return sid, code.upper()
    if t in SKILLS:
        return t, None
    if t.upper() in CODES:
        return CODES[t.upper()], t.upper()
    close = [s for s in SKILLS if t.lower() in s] or [c for c in CODES if t.upper() in c]
    die(f"unknown skill or code '{tag}'" + (f"; did you mean: {', '.join(close[:5])}" if close else "; run: ielts.py skills"))


def parse_kv(items):
    out = {}
    for it in items or []:
        for part in it.split(","):
            if not part.strip():
                continue
            if "=" not in part:
                die(f"expected KEY=VALUE, got '{part}'")
            k, v = part.split("=", 1)
            out[k.strip()] = v.strip()
    return out


def reading_table(prof):
    return RAW_TABLES["R-gt" if prof.get("module") == "gt" else "R-academic"]


def raw_to_band(table, raw):
    for minimum, band in table:
        if raw >= minimum:
            return band
    return 3.5


def band_to_raw(table, band):
    for minimum, b in table:
        if b <= band:
            return minimum if b == band else None
    return None


# ---------- profile ----------

def set_band(prof, key, band, source, date=None):
    prof.setdefault("current", {})[key] = band
    prof.setdefault("history", []).append({"date": date or iso(today()), "key": key, "band": band, "source": source})


def recompute_writing(prof):
    """Writing paper band from task estimates; only once both tasks have one (Task 2 counts double)."""
    cur = prof.get("current", {})
    w1, w2 = cur.get("W1"), cur.get("W2")
    if w1 is not None and w2 is not None:
        cur["W"] = round_half((w1 + 2 * w2) / 3)


def overall(prof):
    cur = prof.get("current", {})
    vals = [cur.get(p) for p in PAPERS]
    return None if None in vals else round_half(sum(vals) / 4)


def apply_scores(prof, scores, source):
    """scores: {'L': '27/40' | '27' | '6.5', 'W2.TR': '6', 'S': '6.5', ...}. Returns parsed dict."""
    parsed = {}
    for k, v in scores.items():
        key = k.upper()
        if key in ("L", "R"):
            if "/" in v or float(v) > 9:
                raw = int(v.split("/")[0])
                table = RAW_TABLES["L"] if key == "L" else reading_table(prof)
                band = raw_to_band(table, raw)
                parsed[key] = {"raw": raw, "band": band}
                prof.setdefault("current", {})[key + "_raw"] = raw
            else:
                band = float(v)
                parsed[key] = {"band": band}
            set_band(prof, key, band, source)
        elif key in ("W1", "W2", "S", "W"):
            parsed[key] = {"band": float(v)}
            set_band(prof, key, float(v), source)
        elif "." in key and key.split(".")[0] in TASK_CRITERIA:
            task, crit = key.split(".", 1)
            if crit not in TASK_CRITERIA[task]:
                die(f"{task} criteria are {', '.join(TASK_CRITERIA[task])}")
            parsed[key] = {"band": float(v)}
            prof.setdefault("current", {}).setdefault("criteria", {})[key] = float(v)
        else:
            die(f"unknown score key '{k}' (use L, R, W1, W2, W, S, or W1.TA / W2.TR / S.FC style criteria)")
    # complete criterion sets produce a task band
    for task, crits in TASK_CRITERIA.items():
        keys = [f"{task}.{c}" for c in crits]
        if all(k in parsed for k in keys) and task not in parsed:
            band = round_half(sum(parsed[k]["band"] for k in keys) / 4)
            parsed[task] = {"band": band}
            set_band(prof, task, band, source)
    if any(k in parsed for k in ("W1", "W2")) and "W" not in parsed:
        recompute_writing(prof)
    return parsed


def cmd_init(a):
    if (HOME / "profile.json").exists() and not a.force:
        die(f"profile already exists in {HOME} (use --force to reset the profile only)")
    prof = {"created": iso(today()), "l1": "Indonesian", "module": a.module, "target": {"overall": a.target},
            "test_date": a.test_date, "current": {}, "history": [], "drills": {}}
    for k, v in parse_kv(a.band).items():
        set_band(prof, k.upper(), float(v), a.source)
    recompute_writing(prof)
    save("profile.json", prof)
    load("reviews.json", None) or save("reviews.json", {"items": {}})
    print(f"profile created in {HOME}")


def cmd_set(a):
    prof = profile()
    if a.target is not None:
        prof["target"]["overall"] = a.target
    for k, v in parse_kv(a.min).items():
        prof["target"].setdefault("min", {})[k.upper()] = float(v)
    if a.test_date:
        prof["test_date"] = a.test_date
    if a.module:
        prof["module"] = a.module
    if a.band:
        apply_scores(prof, parse_kv(a.band), a.source)
    save("profile.json", prof)
    print("profile updated")


# ---------- reviews (errors + vocab) ----------

def reviews():
    return load("reviews.json", {"items": {}})


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:40]


def bump_error(items, sid, code, example=None, l1=None, note=None):
    iid = f"e-{sid}" + (f"-{code.lower()}" if code else "")
    t = today()
    it = items.get(iid)
    if it is None:
        it = items[iid] = {"type": "error", "skill": sid, "code": code, "label": SKILLS[sid]["name"],
                           "frequency": 0, "status": "active", "first_seen": iso(t), "stage": 1,
                           "due": iso(t + dt.timedelta(days=ERROR_LADDER[0])), "examples": [], "history": []}
    else:
        it["status"], it["stage"] = "active", 1
        it["due"] = iso(t + dt.timedelta(days=ERROR_LADDER[0]))
    it["frequency"] += 1
    it["last_seen"] = iso(t)
    if example:
        it["examples"] = (it["examples"] + [example])[-3:]
    if l1:
        it["l1_note"] = l1
    if note:
        it["note"] = note
    return iid


def cmd_error_add(a):
    sid, code = resolve(a.skill)
    rv = reviews()
    iid = bump_error(rv["items"], sid, code, a.example, a.l1, a.note)
    save("reviews.json", rv)
    it = rv["items"][iid]
    print(f"{iid}: frequency {it['frequency']}, next re-probe {it['due']}")


def schedule(it, passed):
    t = today()
    if it["type"] == "error":
        if passed:
            if it["stage"] >= len(ERROR_LADDER):
                it["status"], it["due"] = "resolved", None
            else:
                it["stage"] += 1
                it["status"] = "improving"
                it["due"] = iso(t + dt.timedelta(days=ERROR_LADDER[it["stage"] - 1]))
        else:
            it["stage"], it["status"] = 1, "active"
            it["due"] = iso(t + dt.timedelta(days=1))
    else:
        if passed:
            if it["stage"] >= len(VOCAB_LADDER):
                it["status"], it["due"] = "mastered", None
            else:
                it["due"] = iso(t + dt.timedelta(days=VOCAB_LADDER[it["stage"]]))
                it["stage"] += 1
        else:
            it["stage"] = 0
            it["due"] = iso(t + dt.timedelta(days=1))


def cmd_review(a):
    rv = reviews()
    it = rv["items"].get(a.item)
    if it is None:
        die(f"no review item '{a.item}'")
    passed = a.result == "pass"
    schedule(it, passed)
    it["history"].append({"date": iso(today()), "result": a.result, **({"note": a.note} if a.note else {})})
    save("reviews.json", rv)
    print(f"{a.item}: {a.result} -> {it['status']}, next due {it['due'] or 'none'}")


def due_items(rv, t):
    return [(iid, it) for iid, it in rv["items"].items()
            if it.get("due") and it["due"] <= iso(t) and it["status"] not in ("resolved", "mastered")]


def cmd_due(a):
    t = today()
    items = due_items(reviews(), t)
    errors = sorted([x for x in items if x[1]["type"] == "error"], key=lambda x: (-x[1]["frequency"], x[1]["due"]))
    vocab = sorted([x for x in items if x[1]["type"] == "vocab"], key=lambda x: x[1]["due"])
    errors = errors[: a.max_errors]
    vocab = vocab[: max(0, a.max - len(errors))]
    if a.json:
        print(json.dumps({"errors": dict(errors), "vocab": dict(vocab)}, indent=2, ensure_ascii=False))
        return
    if not errors and not vocab:
        print("nothing due today")
        return
    if errors:
        print(f"Error re-probes ({len(errors)}) - use a FRESH sentence, never the original example:")
        for iid, it in errors:
            ex = f' e.g. "{it["examples"][-1]}"' if it.get("examples") else ""
            print(f"  {iid}  [{it['code'] or it['skill']}] {it['label']} x{it['frequency']} stage {it['stage']}{ex}")
    if vocab:
        print(f"Vocabulary ({len(vocab)}) - production first: show meaning/gap, learner produces the term:")
        for iid, it in vocab:
            gloss = f" / {it['l1']}" if it.get("l1") else ""
            print(f"  {iid}  {it['term']} = {it['meaning']}{gloss}  (stage {it['stage']})")


def cmd_vocab(a):
    rv = reviews()
    items = rv["items"]
    if a.vocab_cmd == "add":
        sid = resolve(a.skill)[0] if a.skill else ("x.collocation" if " " in a.term.strip() else "x.less-common-vocab")
        iid = "v-" + slug(a.term)
        if iid in items:
            print(f"{iid} already in deck (stage {items[iid]['stage']}, due {items[iid]['due']})")
            return
        items[iid] = {"type": "vocab", "term": a.term, "meaning": a.meaning, "example": a.example, "l1": a.l1,
                      "source": a.source, "skill": sid, "status": "learning", "stage": 0, "used": 0,
                      "added": iso(today()), "due": iso(today() + dt.timedelta(days=VOCAB_LADDER[0])), "history": []}
        save("reviews.json", rv)
        print(f"{iid} added, first review {items[iid]['due']}")
    elif a.vocab_cmd == "used":
        iid = "v-" + slug(a.term)
        it = items.get(iid)
        if it is None:
            die(f"'{a.term}' is not in the deck")
        it["used"] += 1
        schedule(it, True)  # correct productive use counts as a passed review
        it["history"].append({"date": iso(today()), "result": "used"})
        save("reviews.json", rv)
        print(f"{iid}: used correctly x{it['used']}, next due {it['due'] or 'none (mastered)'}")
    else:
        rows = [(iid, it) for iid, it in items.items() if it["type"] == "vocab"]
        if a.due:
            rows = [r for r in rows if r[1]["due"] and r[1]["due"] <= iso(today())]
        for iid, it in sorted(rows, key=lambda r: (r[1]["due"] or "9999")):
            print(f"{iid}\t{it['term']}\tstage {it['stage']}\tused {it['used']}\tdue {it['due'] or '-'}\t{it['source'] or ''}")
        print(f"{len(rows)} cards")


# ---------- attempts ----------

def update_drill(prof, drill, pct):
    d = prof.setdefault("drills", {}).setdefault(drill, {"level": 1, "streak": 0, "sessions": []})
    d["sessions"] = (d["sessions"] + [{"date": iso(today()), "level": d["level"], "pct": round(pct, 2)}])[-20:]
    d["streak"] = d["streak"] + 1 if pct >= 0.8 else 0
    msg = f"{drill}: {pct:.0%} at level {d['level']}"
    if d["streak"] >= 2:
        d["streak"] = 0
        if d["level"] < 3:
            d["level"] += 1
            msg += f" -> mastered, move to level {d['level']}"
        else:
            d["level"] = "maintenance"
            msg += " -> mastered at level 3, maintenance (weekly, interleaved)"
    return msg


def cmd_log(a):
    prof = profile()
    if a.drill and a.drill not in {d for s in SKILLS.values() for d in s["drills"]}:
        die(f"unknown drill '{a.drill}' (see references/drills.md)")
    tags = []
    for t in a.tag or []:
        name, _, lost = t.partition(":")
        sid, code = resolve(name)
        if lost:
            try:
                lost_v = float(lost)
            except ValueError:
                die(f"tag '{t}': the part after ':' must be a number of lost marks, e.g. {name}:2")
        elif a.drill and a.total is not None and a.correct is not None:
            lost_v = float(a.total - a.correct)
        else:
            lost_v = 1.0
        tags.append({"skill": sid, "code": code, "lost": lost_v})
    rec = {"date": iso(today()), "module": a.module, "task": a.task, "tags": tags, "note": a.note}
    msgs = []
    if a.score:
        rec["scores"] = apply_scores(prof, parse_kv(a.score), a.source)
    if a.predicted:
        rec["predicted"] = {k.upper(): float(v) for k, v in parse_kv(a.predicted).items()}
    if a.drill:
        if a.correct is None or a.total is None:
            die("--drill needs --correct and --total")
        rec["drill"] = {"id": a.drill, "correct": a.correct, "total": a.total}
        msgs.append(update_drill(prof, a.drill, a.correct / a.total))
    if a.ledger and tags:
        if a.example and len(tags) > 1:
            msgs.append("--example ignored: it can only belong to one tag (use `error add` per error)")
        rv = reviews()
        for tg in tags:
            iid = bump_error(rv["items"], tg["skill"], tg["code"], a.example if len(tags) == 1 else None)
            msgs.append(f"ledger: {iid} x{rv['items'][iid]['frequency']}")
        save("reviews.json", rv)
    append_jsonl("log.jsonl", rec)
    save("profile.json", prof)
    if "scores" in rec:
        msgs.append("scores: " + ", ".join(f"{k} {fmt(v['band'])}" + (f" ({v['raw']}/40)" if "raw" in v else "")
                                           for k, v in rec["scores"].items()))
    if "predicted" in rec and "scores" in rec:
        diffs = [f"{k} {rec['predicted'][k] - rec['scores'][k]['band']:+.1f}" for k in rec["predicted"] if k in rec["scores"]]
        if diffs:
            msgs.append("your prediction vs coach: " + ", ".join(diffs))
    print("logged" + ("; " + "; ".join(msgs) if msgs else ""))


# ---------- analysis ----------

def leverage(log, t):
    agg = {}
    for rec in log:
        age = (t - dt.date.fromisoformat(rec["date"])).days
        if age > LEVERAGE_WINDOW:
            continue
        w = 0.5 ** (age / LEVERAGE_HALF_LIFE)
        for tg in rec.get("tags", []):
            a = agg.setdefault(tg["skill"], {"lost": 0.0, "weighted": 0.0, "papers": set()})
            a["lost"] += tg["lost"]
            a["weighted"] += tg["lost"] * w
            a["papers"].add(rec["module"])
    rows = []
    for sid, a in agg.items():
        breadth = len(SKILLS[sid]["papers"])
        rows.append((a["weighted"] * (1 + 0.25 * (breadth - 1)), sid, a))
    return sorted(rows, key=lambda r: -r[0])


def next_drill(prof, sid):
    for d in SKILLS[sid]["drills"]:
        st = prof.get("drills", {}).get(d)
        if st is None or st["level"] != "maintenance":
            return d, (st or {}).get("level", 1)
    return SKILLS[sid]["drills"][0], "maintenance"


def bias(pairs):
    out = {}
    for k, diff in pairs:
        out.setdefault(k, []).append(diff)
    return {k: (sum(v) / len(v), len(v)) for k, v in out.items()}


def prediction_bias(log):
    pairs = []
    for rec in log:
        for k, p in rec.get("predicted", {}).items():
            if k in rec.get("scores", {}):
                pairs.append((k, p - rec["scores"][k]["band"]))
    return bias(pairs)


def calibration_bias():
    pairs = []
    for rec in read_jsonl("calibration.jsonl"):
        for k, c in rec["coach"].items():
            if k in rec["reference"]:
                pairs.append((f"{rec['task']}.{k}", c - rec["reference"][k]))
    return bias(pairs)


def cmd_status(a):
    prof, t = profile(), today()
    cur = prof.get("current", {})
    log = read_jsonl("log.jsonl")
    days = (dt.date.fromisoformat(prof["test_date"]) - t).days if prof.get("test_date") else None
    print(f"IELTS {prof.get('module', 'academic')} | target {fmt(prof['target'].get('overall'))}"
          + (f" | test {prof['test_date']} ({days} days)" if days is not None else ""))
    ov = overall(prof)
    print("Current: " + "  ".join(f"{p} {fmt(cur.get(p))}" for p in PAPERS) + f"  -> overall {fmt(ov)}")
    if cur.get("criteria"):
        print("Criteria: " + "  ".join(f"{k} {fmt(v)}" for k, v in sorted(cur["criteria"].items())))
    rv = reviews()
    dues = due_items(rv, t)
    ne = sum(1 for _, it in dues if it["type"] == "error")
    print(f"Due today: {ne} error re-probes, {len(dues) - ne} vocab cards" + (" -> run: due" if dues else ""))
    rows = leverage(log, t)[: a.top]
    if rows:
        print(f"Top leverage skills (last {LEVERAGE_WINDOW} days, recent and cross-paper weighted):")
        for i, (score, sid, ag) in enumerate(rows, 1):
            d, lvl = next_drill(prof, sid)
            print(f"  {i}. {sid:22} lost {ag['lost']:g} in {','.join(sorted(ag['papers']))}  "
                  f"affects {','.join(SKILLS[sid]['papers'])}  score {score:.1f}  next: {d} (L{lvl})")
    else:
        print("No tagged attempts yet - log some practice to rank skills.")
    recent = [(d, s) for d, s in prof.get("drills", {}).items()
              if (t - dt.date.fromisoformat(s["sessions"][-1]["date"])).days <= 14]
    recent.sort(key=lambda x: x[1]["sessions"][-1]["date"], reverse=True)
    if recent:
        print("Drills (last 14 days): " + "  ".join(
            f"{d} L{s['level']} {s['sessions'][-1]['pct']:.0%}" if s["level"] != "maintenance" else f"{d} maint"
            for d, s in recent[:8]) + (f"  (+{len(recent) - 8} more)" if len(recent) > 8 else ""))
    pb = prediction_bias(log)
    if pb:
        print("Your prediction bias (you - coach): " + "  ".join(f"{k} {m:+.1f} (n={n})" for k, (m, n) in sorted(pb.items())))
    cb = calibration_bias()
    if cb:
        print("Coach calibration (coach - reference): " + "  ".join(
            f"{k} {m:+.2f} (n={n})" + (" ADJUST" if abs(m) >= 0.5 and n >= 3 else "") for k, (m, n) in sorted(cb.items())))


def step_cost(paper, band, nth):
    """Heuristic effort for one half-band step: L/R cheaper than W/S, higher bands cost more,
    and each extra step on the same paper costs 25% more (gains concentrate poorly)."""
    base = 1.0 if paper in ("L", "R") else 2.0
    mult = 1 if band < 6 else 1.5 if band < 7 else 2.5 if band < 8 else 4
    return base * mult * (1 + 0.25 * nth)


def cmd_plan(a):
    prof = profile()
    cur = prof.get("current", {})
    missing = [p for p in PAPERS if cur.get(p) is None]
    if missing:
        die(f"need a current band for {', '.join(missing)}: ielts.py set --band L=6 R=6.5 W=5.5 S=6")
    target = a.target or prof["target"].get("overall")
    if target is None:
        die("no target: ielts.py set --target 7")
    mins = prof["target"].get("min", {})
    options = []
    steps = range(0, 9)  # up to +4.0 per paper
    for combo in itertools.product(steps, repeat=4):
        new = {p: min(9.0, cur[p] + 0.5 * k) for p, k in zip(PAPERS, combo)}
        if round_half(sum(new.values()) / 4) < target or any(new[p] < mins.get(p, 0) for p in PAPERS):
            continue
        cost = sum(step_cost(p, cur[p] + 0.5 * i, i) for p, k in zip(PAPERS, combo) for i in range(k))
        options.append((cost, sum(combo), new))
    if not options:
        die("target not reachable")
    options.sort(key=lambda o: (o[0], o[1]))
    seen, shown = set(), 0
    print(f"Current overall {fmt(overall(prof))} -> target {fmt(target)}"
          + (f" (minimums: {', '.join(f'{k} {v}' for k, v in mins.items())})" if mins else ""))
    print("Cheapest routes (effort units are heuristic: L/R half-bands are cheaper than W/S, and cost rises with level):")
    for cost, _, new in options:
        key = tuple(new[p] for p in PAPERS)
        if key in seen:
            continue
        seen.add(key)
        gains = ", ".join(f"{p} {fmt(cur[p])}->{fmt(new[p])}" for p in PAPERS if new[p] > cur[p]) or "none"
        print(f"  effort {cost:4.1f}: {gains}")
        shown += 1
        if shown == 3:
            break
    for p, table in (("L", RAW_TABLES["L"]), ("R", reading_table(prof))):
        nxt = cur[p] + 0.5
        need = band_to_raw(table, nxt)
        have = cur.get(p + "_raw")
        if need:
            print(f"{p} {fmt(cur[p])}->{fmt(nxt)} needs {need}/40" + (f" (last {have}/40: +{need - have} answers)" if have else ""))


def cmd_calibrate(a):
    if a.cal_cmd == "add":
        task = a.task.upper()
        if task not in TASK_CRITERIA:
            die("task must be W1, W2 or S")
        coach = {k.upper(): float(v) for k, v in parse_kv(a.coach).items()}
        ref = {k.upper(): float(v) for k, v in parse_kv(a.reference).items()}
        for k in list(coach) + list(ref):
            if k not in TASK_CRITERIA[task] + ["OVERALL"]:
                die(f"{task} keys are {', '.join(TASK_CRITERIA[task])}, OVERALL")
        append_jsonl("calibration.jsonl", {"date": iso(today()), "task": task, "coach": coach, "reference": ref, "source": a.source})
        diffs = ", ".join(f"{k} {coach[k] - ref[k]:+.1f}" for k in coach if k in ref)
        print(f"calibration logged ({a.source}): coach - reference {diffs}")
    else:
        cb = calibration_bias()
        if not cb:
            print("no calibration records yet")
            return
        for k, (m, n) in sorted(cb.items()):
            flag = "  ADJUST: shift estimates toward reference" if abs(m) >= 0.5 and n >= 3 else ""
            print(f"{k:8} {m:+.2f} over {n}{flag}")


def cmd_skills(a):
    if a.id:
        sid, _ = resolve(a.id)
        s = SKILLS[sid]
        print(f"{sid}: {s['name']}\n  papers {', '.join(s['papers'])}; criteria {', '.join(s['criteria'])}\n"
              f"  codes {', '.join(s['codes'])}; drills {', '.join(s['drills'])}\n  detect: {s['detect']}")
        return
    for s in SKILL_MAP["skills"]:
        if a.paper and a.paper.upper() not in s["papers"]:
            continue
        print(f"{s['id']:22} {','.join(s['papers']):14} {'/'.join(s['codes']):14} {s['name']}")


# ---------- CLI ----------

def main():
    ap = argparse.ArgumentParser(prog="ielts.py", description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init", help="create the learner profile")
    p.add_argument("--target", type=float)
    p.add_argument("--test-date")
    p.add_argument("--module", choices=["academic", "gt"], default="academic")
    p.add_argument("--band", nargs="*", help="L=6 R=6.5 W=5.5 S=6")
    p.add_argument("--source", default="self", help="self | mock | official | coach")
    p.add_argument("--force", action="store_true")
    p.set_defaults(fn=cmd_init)

    p = sub.add_parser("set", help="update target, test date, module, bands")
    p.add_argument("--target", type=float)
    p.add_argument("--min", nargs="*", help="per-paper minimums, e.g. W=6.5")
    p.add_argument("--test-date")
    p.add_argument("--module", choices=["academic", "gt"])
    p.add_argument("--band", nargs="*", help="L=27/40 R=6.5 W2=6 S=6 ...")
    p.add_argument("--source", default="official")
    p.set_defaults(fn=cmd_set)

    p = sub.add_parser("log", help="record an attempt, drill, or scored task")
    p.add_argument("--module", required=True,
                   choices=["listening", "reading", "writing-task1", "writing-task2", "speaking", "vocabulary", "grammar", "drill", "mock"])
    p.add_argument("--task", help="short description, e.g. 'Cam-style S3 MC' or 'W2 opinion: remote work'")
    p.add_argument("--tag", nargs="*", help="SKILL_OR_CODE[:LOST], e.g. l.numbers:2 ART x.paraphrase:3")
    p.add_argument("--score", nargs="*", help="L=27/40 R=30 W2.TR=6 W2.CC=6.5 ... S.FC=6 ...")
    p.add_argument("--predicted", nargs="*", help="learner's own prediction, same keys as --score")
    p.add_argument("--source", default="coach", help="source for --score bands: coach | mock | teacher | official")
    p.add_argument("--drill")
    p.add_argument("--correct", type=int)
    p.add_argument("--total", type=int)
    p.add_argument("--ledger", action="store_true", help="also add/bump each tag as an error re-probe item")
    p.add_argument("--example", help="representative wrong sentence for the ledger (rewritten, not the original)")
    p.add_argument("--note")
    p.set_defaults(fn=cmd_log)

    p = sub.add_parser("due", help="review items due today (errors first, then vocab)")
    p.add_argument("--max", type=int, default=12)
    p.add_argument("--max-errors", type=int, default=2)
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_due)

    p = sub.add_parser("review", help="grade a due item")
    p.add_argument("item")
    p.add_argument("result", choices=["pass", "fail"])
    p.add_argument("--note")
    p.set_defaults(fn=cmd_review)

    p = sub.add_parser("error", help="error ledger")
    es = p.add_subparsers(dest="err_cmd", required=True)
    q = es.add_parser("add")
    q.add_argument("--skill", required=True, help="skill id or code")
    q.add_argument("--example")
    q.add_argument("--l1", help="Indonesian-transfer note")
    q.add_argument("--note")
    q.set_defaults(fn=cmd_error_add)

    p = sub.add_parser("vocab", help="personal vocabulary deck")
    vs = p.add_subparsers(dest="vocab_cmd", required=True)
    q = vs.add_parser("add")
    q.add_argument("--term", required=True)
    q.add_argument("--meaning", required=True)
    q.add_argument("--example")
    q.add_argument("--l1", help="Indonesian gloss")
    q.add_argument("--source", help="listening | reading | writing | speaking | drill | manual")
    q.add_argument("--skill")
    q.set_defaults(fn=cmd_vocab)
    q = vs.add_parser("used", help="learner used the term correctly in their own writing/speaking")
    q.add_argument("term")
    q.set_defaults(fn=cmd_vocab)
    q = vs.add_parser("list")
    q.add_argument("--due", action="store_true")
    q.set_defaults(fn=cmd_vocab)

    p = sub.add_parser("status", help="bands, due counts, top leverage skills, biases")
    p.add_argument("--top", type=int, default=5)
    p.set_defaults(fn=cmd_status)

    p = sub.add_parser("plan", help="cheapest band route to the target overall")
    p.add_argument("--target", type=float)
    p.set_defaults(fn=cmd_plan)

    p = sub.add_parser("calibrate", help="coach vs reference scores")
    cs = p.add_subparsers(dest="cal_cmd", required=True)
    q = cs.add_parser("add")
    q.add_argument("--task", required=True, help="W1 | W2 | S")
    q.add_argument("--coach", required=True, nargs="+", help="TA=6,CC=6.5,LR=6,GRA=6")
    q.add_argument("--reference", required=True, nargs="+", help="same keys, official/teacher/real-test scores")
    q.add_argument("--source", required=True, help="official:<anchor-id> | teacher | test-result")
    q.set_defaults(fn=cmd_calibrate)
    q = cs.add_parser("report")
    q.set_defaults(fn=cmd_calibrate)

    p = sub.add_parser("skills", help="list the skill map, or show one skill")
    p.add_argument("id", nargs="?")
    p.add_argument("--paper", help="L | R | W1 | W2 | S")
    p.set_defaults(fn=cmd_skills)

    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
