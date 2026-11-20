# ielts-skills

An IELTS coach for AI coding agents (Claude Code, omp, and other agents that read `SKILL.md` skills). It covers all four papers for Academic and General Training. It keeps a persistent learner profile, so each session starts from your weakest skills, due reviews and current bands. The coaching notes are tuned for learners whose first language is Indonesian, but they work for anyone.

| Skill | What it does |
|---|---|
| `ielts-preparation` | Study plans, Listening/Reading error diagnosis, Writing Task 1/2 and Speaking feedback with calibrated band estimates, 41 short drills, a spaced-review vocabulary deck, grammar coaching |
| `ielts-setup` | Installs and checks everything: agent links, official band-descriptor PDFs, model choice, an `ielts` shell alias, learner intake |

## Install

```bash
npx skills add favianharya/ielts-skills -g -y
```

Then, in your agent, say **"set up IELTS"**. The `ielts-setup` skill runs `scripts/setup.py --check`, shows what it will change, asks before editing your shell rc file, and runs a four-question intake to create your profile. To run the script yourself:

```bash
python3 ~/.agents/skills/ielts-setup/scripts/setup.py --check   # report only
python3 ~/.agents/skills/ielts-setup/scripts/setup.py           # apply
```

With the omp coding agent, setup tests which Claude models answer on your machine and writes a managed alias block to `~/.zshrc` (backed up first):

```bash
alias ielts='omp --model anthropic/claude-sonnet-5-5:medium --smol anthropic/claude-haiku-5-5:low --slow anthropic/claude-opus-5-5:high'
```

Use `slow` (strongest model, high effort) when you paste an essay or speaking transcript for a score; keep scoring on one model so calibration stays meaningful. Use `smol` for drills and vocabulary reviews, and the default for coaching. In Claude Code, switch with `/model` instead.

## Use

```bash
ielts "help me prepare for IELTS"
```

Each session: `status` → due reviews → the task or one drill → `log` → one-line takeaway. Your data lives in `~/.ielts/` (`IELTS_HOME` to override) and is never sent anywhere by the skill. The profile CLI is `skills/ielts-preparation/scripts/ielts.py` (Python 3 standard library only); run it with `--help`.

## Content and sources

- All text in this repository is original. Band-descriptor summaries are written in our own words. Setup downloads the official IELTS band-descriptor PDFs from ielts.org to your machine; they are not redistributed here.
- `references/calibration.md` indexes official IELTS sample responses by band, with links and short paraphrased examiner notes. It does not include the scripts themselves.
- The skill never supplies copyrighted test material (Cambridge books, official answer keys); it writes original practice items or works from what you paste.
- Band estimates are coaching estimates, not official IELTS scores.

## Acknowledgements

The module layout was first prototyped from community IELTS skills, notably [jurgendn/agent-skills](https://github.com/jurgendn/agent-skills); the published text was rewritten independently.

## License

MIT
