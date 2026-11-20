#!/usr/bin/env python3
"""Set up, check, or repair the ielts-preparation skill on this machine.

Steps (each idempotent; --check reports without changing anything):
  1. find the ielts-preparation skill and smoke-test its CLI
  2. link it (and ielts-setup) into ~/.claude/skills for Claude Code
  3. download the official IELTS band-descriptor PDFs to ~/.ielts/official/
  4. pick Claude models that answer on this machine (omp only)
  5. write an `ielts` alias block into the shell rc file (omp only)
  6. report whether a learner profile exists

Python 3 standard library only.
"""
import argparse
import datetime as dt
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import urllib.request

HOME = pathlib.Path.home()
IELTS_HOME = pathlib.Path(os.environ.get("IELTS_HOME", HOME / ".ielts"))
HERE = pathlib.Path(__file__).resolve().parent.parent  # .../ielts-setup
SKILL_NAMES = ("ielts-preparation", "ielts-setup")
SEARCH_DIRS = [HERE.parent, HOME / ".agents/skills", HOME / ".claude/skills", HOME / ".omp/agent/skills"]
PDFS = {
    "ielts-writing-band-descriptors.pdf": "https://ielts.org/cdn/ielts-guides/ielts-writing-band-descriptors.pdf",
    "ielts-speaking-band-descriptors.pdf": "https://ielts.org/cdn/ielts-guides/ielts-speaking-band-descriptors.pdf",
}
# Preferred models per role, best first; matched against the omp catalog by id.
TIERS = {
    "slow": ("high", ["claude-opus-5-5", "claude-opus-5", "claude-opus-4-8", "claude-opus-4-7", "claude-opus-4-6", "claude-opus-4-5"]),
    "default": ("medium", ["claude-sonnet-5-5", "claude-sonnet-5", "claude-sonnet-4-6", "claude-sonnet-4-5"]),
    "smol": ("low", ["claude-haiku-5-5", "claude-haiku-4-5"]),
}
EFFORT_ORDER = ["minimal", "low", "medium", "high", "xhigh", "max"]
BLOCK_START = "# >>> ielts-skills (managed by ielts-setup; re-run setup to change) >>>"
BLOCK_END = "# <<< ielts-skills <<<"

failed = False


def say(state, msg):
    global failed
    failed |= state == "FAIL"
    print(f"[{state:>4}] {msg}")


def find_skill():
    for d in SEARCH_DIRS:
        p = d / "ielts-preparation"
        if (p / "scripts/ielts.py").is_file():
            return p.resolve()
    return None


def step_skill():
    skill = find_skill()
    if not skill:
        say("FAIL", "ielts-preparation not found. Install it: npx skills add favianharya/ielts-skills -g -y")
        return None
    r = subprocess.run([sys.executable, str(skill / "scripts/ielts.py"), "skills", "--paper", "L"],
                       capture_output=True, text=True)
    if r.returncode:
        say("FAIL", f"CLI smoke test failed: {r.stderr.strip()[:200]}")
    else:
        say("ok", f"skill at {skill}; CLI works (python {sys.version.split()[0]})")
    return skill


def step_links(skill, check):
    claude = HOME / ".claude"
    if not claude.is_dir():
        say("skip", "Claude Code not found (~/.claude missing); omp reads ~/.agents/skills directly")
        return
    for name in SKILL_NAMES:
        src = (skill.parent / name).resolve()
        if not src.is_dir():
            continue
        dst = claude / "skills" / name
        if dst.exists():
            say("ok", f"Claude Code sees {name}")
        elif dst.is_symlink():  # dangling link
            if check:
                say("todo", f"{dst} is a broken link")
            else:
                dst.unlink()
                dst.symlink_to(src)
                say("fix", f"relinked {dst} -> {src}")
        elif check:
            say("todo", f"{name} not linked for Claude Code")
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.symlink_to(src)
            say("fix", f"linked {dst} -> {src}")


def step_pdfs(check):
    out = IELTS_HOME / "official"
    for name, url in PDFS.items():
        f = out / name
        if f.is_file() and f.stat().st_size > 10_000:
            say("ok", f"official PDF {f}")
            continue
        if check:
            say("todo", f"official PDF missing: {f}")
            continue
        try:
            out.mkdir(parents=True, exist_ok=True)
            req = urllib.request.Request(url, headers={"User-Agent": "ielts-setup"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            if not data.startswith(b"%PDF"):
                raise ValueError("response is not a PDF")
            f.write_bytes(data)
            say("fix", f"downloaded {f}")
        except Exception as e:  # network problems must not stop setup
            say("warn", f"could not download {url} ({e}); the skill falls back to its own summaries")


def catalog():
    r = subprocess.run(["omp", "models", "--json"], capture_output=True, text=True, timeout=120)
    if r.returncode:
        return []
    return [m for m in json.loads(r.stdout).get("models", []) if m.get("kind") == "chat"]


def norm_id(model_id):
    return model_id.split("@")[0].replace(".", "-")


def probe(selector):
    try:
        r = subprocess.run(["omp", "-p", "--model", selector, "Reply with only the word OK"],
                           capture_output=True, text=True, timeout=120)
    except subprocess.TimeoutExpired:
        return False
    return r.returncode == 0 and "OK" in r.stdout


def pick_effort(want, levels):
    if not levels or want in levels:
        return want
    i = EFFORT_ORDER.index(want)
    by_distance = sorted(levels, key=lambda l: abs(EFFORT_ORDER.index(l) - i) if l in EFFORT_ORDER else 99)
    return by_distance[0]


def step_models(overrides, check):
    """Return {role: 'selector:effort'} or None when omp is unavailable."""
    if not shutil.which("omp"):
        say("skip", "omp not installed: no alias needed. In Claude Code pick models with /model "
                    "(Opus for scoring, Sonnet for coaching, Haiku for drills)")
        return None
    models = catalog()
    chosen = {}
    for role, (effort, prefs) in TIERS.items():
        if overrides.get(role):
            chosen[role] = overrides[role]
            say("ok", f"{role}: {chosen[role]} (given)")
            continue
        ranked = []
        for pref in prefs:
            ms = [m for m in models if norm_id(m["id"]) == pref]
            ms.sort(key=lambda m: (m["provider"] != "anthropic", m["provider"]))
            ranked += ms
        if not ranked:
            say("FAIL", f"{role}: no Claude model from {prefs} in `omp models`; log in to Anthropic in omp first")
            continue
        for m in ranked[:4]:
            sel = f"{m['selector']}:{pick_effort(effort, m.get('thinking') or [])}"
            if check or probe(f"{m['selector']}:{pick_effort('low', m.get('thinking') or [])}"):
                chosen[role] = sel
                say("ok", f"{role}: {sel}" + (" (catalog only, not probed)" if check else " (answered)"))
                break
            say("warn", f"{role}: {m['selector']} did not answer, trying next")
        else:
            say("FAIL", f"{role}: none of the candidate models answered")
    return chosen if len(chosen) == len(TIERS) else None


def default_rc():
    # Agents often run with an empty or different $SHELL; the login shell is what the user's terminal opens.
    try:
        import pwd  # not available on Windows
        shell = pwd.getpwuid(os.getuid()).pw_shell
    except (ImportError, KeyError):
        shell = ""
    shell = os.path.basename(shell or os.environ.get("SHELL", ""))
    return HOME / {"zsh": ".zshrc", "bash": ".bashrc"}.get(shell, ".profile")


def step_alias(models, rc, name, check):
    line = (f"alias {name}='omp --model {models['default']} --smol {models['smol']} --slow {models['slow']}'")
    block = f"{BLOCK_START}\n{line}\n{BLOCK_END}\n"
    text = rc.read_text() if rc.exists() else ""
    pattern = re.compile(re.escape(BLOCK_START) + r".*?" + re.escape(BLOCK_END) + r"\n?", re.S)
    outside = pattern.sub("", text)
    if re.search(rf"^\s*alias\s+{re.escape(name)}=", outside, re.M) or (
            shutil.which(name) and not pattern.search(text)):
        say("FAIL", f"'{name}' is already defined outside the managed block; re-run with --alias-name <other>")
        return
    new = pattern.sub(block, text) if pattern.search(text) else text + ("\n" if text and not text.endswith("\n") else "") + "\n" + block
    if new == text:
        say("ok", f"alias '{name}' up to date in {rc}")
        return
    if check:
        say("todo", f"alias '{name}' missing or outdated in {rc}: {line}")
        return
    if rc.exists():
        backup = rc.with_name(rc.name + ".ielts-backup-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"))
        shutil.copy2(rc, backup)
        say("ok", f"backed up {rc} to {backup}")
    rc.write_text(new)
    say("fix", f"wrote alias to {rc}: {line}")
    say("note", f"open a new terminal or run: source {rc}")


def step_profile(skill):
    if (IELTS_HOME / "profile.json").is_file():
        r = subprocess.run([sys.executable, str(skill / "scripts/ielts.py"), "status"], capture_output=True, text=True)
        say("ok", "profile: " + (r.stdout.splitlines() or ["?"])[0])
    else:
        say("todo", f"no learner profile in {IELTS_HOME}; run the intake, then: "
                    f"python3 {skill}/scripts/ielts.py init --target ... --test-date ... --module academic|gt")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="report only; change nothing and skip model probes")
    ap.add_argument("--no-alias", action="store_true", help="do not touch the shell rc file")
    ap.add_argument("--rc", type=pathlib.Path, help="shell rc file (default from $SHELL, e.g. ~/.zshrc)")
    ap.add_argument("--alias-name", default="ielts")
    for role in TIERS:
        ap.add_argument(f"--{role}", metavar="SELECTOR:EFFORT", help=f"use this model for the {role} role, skip probing")
    a = ap.parse_args()

    skill = step_skill()
    if skill:
        step_links(skill, a.check)
    step_pdfs(a.check)
    if not a.no_alias:
        models = step_models({r: getattr(a, r) for r in TIERS}, a.check)
        if models:
            step_alias(models, (a.rc or default_rc()).expanduser(), a.alias_name, a.check)
    if skill:
        step_profile(skill)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
