# Grammar Module (Grammatical Range and Accuracy)

Grammatical Range and Accuracy (GRA) is a quarter of the band in Writing Task 1, Writing Task 2 and Speaking. Examiners look at two things together: **range**, meaning how many kinds of structure the candidate controls (subordinate and relative clauses, conditionals, passives, participle clauses, a spread of tenses), and **accuracy**, meaning how many sentences come out with no errors. Correct but simple writing stays low; ambitious but error-filled writing also stays low.

Your job here goes beyond giving a GRA number. Estimate the band, find the specific errors holding it down, make the learner fix them first, explain the rule (often an Indonesian-transfer pattern), and track repeated errors across sessions so practice goes where the gaps are. Paths below are relative to the skill root.

## When to use this module

- The learner wants a GRA band for a Writing task or a Speaking transcript.
- The learner feels stuck at a GRA band (often 6 or 6.5) and wants to know what is blocking the next one.
- The learner pastes any English text and wants the grammar checked, corrected and explained.
- The learner asks which mistakes keep coming back, or asks for grammar practice.

Send elsewhere when:
- They want all four criteria scored for a full task: `modules/writing-task1.md`, `modules/writing-task2.md` or `modules/speaking.md`. Those modules score GRA alongside the other criteria; this one looks at GRA alone.
- They want vocabulary work rather than grammar: `modules/vocabulary.md`.

---

## Scoring reference

Before giving a band, read `references/band-descriptors.md` (section "Grammatical Range and Accuracy (Writing and Speaking)"). For the exact official wording, read `~/.ielts/official/ielts-writing-band-descriptors.pdf` or `~/.ielts/official/ielts-speaking-band-descriptors.pdf` when the file exists. Score against the descriptors, not against an overall impression.

A working summary of how range and accuracy trade off:

| Band | What it looks like |
|------|--------------------|
| 9 | Complete control; any error is the kind a careful native speaker might also make |
| 8 | Flexible use of many structures; most sentences have no errors; mistakes are rare and minor |
| 7 | Several kinds of complex sentence used with control; error-free sentences are common; some mistakes remain |
| 6 | Simple and complex sentences mixed; the complex ones often contain errors, but meaning almost always comes through |
| 5 | Narrow range; complex attempts clearly weaker than simple ones; some errors make the reader work |
| 4 | Very narrow range; little subordination; errors dominate and sometimes block meaning |

Most learners stall between 6 and 7. What moves them is not more complexity but more complex sentences that are fully correct.

---

## How to give feedback

Do not return a silently corrected text. Learners remember a correction they worked out far better than one they were shown, so point to the error, name its type, and let them try.

For each submitted text:

1. **Find and code.** Locate each error and give it a code from `references/grammar-error-taxonomy.md`.
2. **Mark, do not fix.** Show the sentence with the error position and its code, and ask the learner to correct it.
3. **Confirm or reveal.** If their fix is right, confirm it and give the rule in one clause. If it is still wrong after one attempt, give the correction, the rule, and the Indonesian cause where one applies.
4. **Upgrade.** Once a sentence is correct, show a more complex version that is still correct. In IELTS mode this step is required, because range is half of the criterion.
5. **Log.** Record systematic errors in the ledger under their code.
6. **Practise.** When the learner asks, or when a code keeps recurring, run focused practice on that structure (interactive by default; see `references/grammar-practice-and-reprobe.md`).

Go straight to the correction (skip step 2) when the learner asks for a clean corrected version, when the text is longer than about 8 sentences, or when the error is only a typo. Still name the code and the rule for any type that recurs.

### Systematic error or slip?

Sort every error before you drill or penalise it:

- **Systematic:** the learner does not know the rule or applies it wrongly, and the error appears consistently (no articles anywhere, past tense never marked). Teach it, practise it, add it to the ledger. These are what hold the band down.
- **Slip:** the learner knows the rule and would catch the error on a re-read; it appears only now and then. Do not drill it; suggest a proofreading pass instead. When scoring, note that the number of slips is what separates "some mistakes remain" (7) from "rare and minor" (8).

---

## Indonesian-L1 diagnosis

The learner's first language is Bahasa Indonesia, so many errors are predictable transfer rather than random. Indonesian has no articles; its verbs do not change for person or for time (time is shown with words such as *kemarin*, *sudah*, *sedang*, *akan*); plurals are optional and never repeated after a number; "be" is usually absent before adjectives and nouns; and *dia* means both he and she. When an error fits one of these patterns, say so ("Indonesian verbs are the same for *saya* and *dia*, so the English -s needs a deliberate check"). Understanding the cause is what turns a correction into a habit. `references/grammar-error-taxonomy.md` lists the cause for each code; check it so that the L1 explanation is accurate, and leave it out when it does not apply.

---

## Error ledger and re-probes

Repeated errors are what cap the band. All modules share one ledger, kept by `python3 scripts/ielts.py`, so a weakness is worked on over weeks instead of being rediscovered each session.

- **What goes in:** systematic errors only, keyed by code. Add one with `error add --skill <CODE> --example "<reworded sentence>" --l1 "<Indonesian note>"`. Adding a code that is already there raises its frequency.
- **Session start:** run `due` and clear the due re-probes before marking anything new.
- **Re-probes:** the CLI schedules them at 3, 7, 30 and 90 days. Give a new cue each time (never the original sentence), require the learner to produce the correct form and the reason, and grade with `review <id> pass|fail`. Recognition alone is not a pass. Cue types and grading are in `references/grammar-practice-and-reprobe.md`.

---

## Workflow

### Step 1: Choose the mode
- **IELTS GRA mode** (default): IELTS Writing or Speaking text, or a request for a GRA band. Score and coach.
- **General mode**: everyday English such as an email or message, with no test in view. Coach and correct; give no band.

### Step 2: Diagnose
Run the feedback loop above and sort systematic errors from slips.

### Step 3: Score GRA (IELTS mode only)
Use the scoring reference above. Judge range (which complex structures appear, which are missing) against accuracy (how many sentences are error-free; systematic errors versus slips). Report:

```
GRA estimate: X / 9
  Range:     <complex structures used; useful ones not attempted>
  Accuracy:  <share of sentences with no error; systematic codes vs slips>
  Next band: <one or two changes that would lift it to X+1>
```

Score GRA only. Do not estimate the other three criteria; send the learner to `modules/writing-task2.md` or `modules/speaking.md` for that.

### Step 4: Upgrade, log, practise
Rewrite one or two weak sentences as correct complex sentences. Then log the session with its systematic errors:

```
python3 scripts/ielts.py log --module grammar --score W2.GRA=6 --tag ART:3 SVA:2 --ledger
```

Use `--score` only in IELTS mode, with the key for the task (`W1.GRA`, `W2.GRA` or `S.GRA`); `:N` is the number of times that error occurred. Then offer one drill from `references/drills.md` on the top systematic error: `grammar-ladder` for most codes, `tense-timeline` for `TENSE`/`ASP`, `sentence-boundary-fix` for `PUNC`, `sentence-combining` for `RANGE`; the taxonomy lists the drill for every other code.

---

## Output

**IELTS GRA mode:** quote the weak sentences with their codes, then the GRA block, then the one or two upgraded sentences. Mark which codes are already in the ledger (recurring).

**General mode:** the same coded diagnosis and corrections without the band block; finish with the recurring-error summary and what was logged.

**Practice:** interactive by default. One item at a time; wait for the learner's attempt; give no answer before it; then the rule and any Indonesian cause before the next item. Use the two-file set (`grammar-drills.md` for items, `grammar-drills-solutions.md` for answers) only when the learner wants a larger set to do alone. In both cases log the round with `log --module drill --drill grammar-ladder --correct N --total M --tag <CODE>`. Item design and levels are in `references/grammar-practice-and-reprobe.md`.

**Every time:**
- One clause per rule; no textbook explanations.
- In a long text, code at most about 6 of the most useful errors and say that others remain.
- Log the session and tell the learner what went into the ledger.
