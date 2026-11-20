# IELTS Study Planning

Build and maintain the learner's plan from evidence: the band gap, the weeks left, the hours they can really give, and where marks are being lost. Once practice has been logged, the profile (`plan`, `status`) decides priorities, not a generic template.

## Scope

Use this module for: a first plan or schedule, "how do I get from band X to Y", splitting time across the four papers, adding academic-paper reading to Reading preparation, mock-test timing, checkpoint reviews, and the last week before the test. It is also the intake for a new learner with no profile.

Route elsewhere for: marking a specific essay or report (`modules/writing-task2.md`, `modules/writing-task1.md`), a spoken answer or mock interview (`modules/speaking.md`), checking Listening answers (`modules/listening.md`), strategy for one Reading question type (`modules/reading.md`), topic vocabulary (`modules/vocabulary.md`), grammar errors (`modules/grammar.md`), or "what do I practise right now" (`references/drills.md`).

---

## 1. Intake

Run `python3 scripts/ielts.py status` first. If it reports no profile, collect these before planning:

- **Target overall band**, and any per-paper minimum their university, employer or visa requires (e.g. "7.0 with no band below 6.5").
- **Test date**, or the latest date that still meets their application deadline.
- **Module**: Academic or General Training (changes Reading texts, the Reading raw-score conversion, and Writing Task 1).
- **Current bands per paper**. Best evidence first: an official result, then a full timed mock, then a recent practice paper. If there is nothing, give them one timed Listening and one timed Reading section now and estimate Writing/Speaking from a short sample; label every figure as an estimate.
- **Realistic weekly hours**, split into weekday minutes and weekend blocks.

Then create the profile (paths are relative to this skill's root):

```
python3 scripts/ielts.py init --target 7 --test-date 2027-03-01 --module academic \
  --band L=6.5 R=6 W=5.5 S=6 --source mock
```

Use `set --min W=6.5` when an institution requires a per-paper minimum, and `set --band ... --source official` after a real test.

**Is the timeline realistic?** As a rough guide, a half-band rise in one paper takes a learner studying about 15 hours a week somewhere around a month to six weeks; a full band around two to three months; one and a half bands four to five months; two bands six months or more. Halve the weekly hours and the timeline roughly doubles. Listening and Reading usually move first because volume and technique pay off quickly; Writing and Speaking need repeated feedback loops and move later. If the date cannot carry the gap, say so plainly and offer the options: a later sitting, a lower interim target, or more hours.

For what each band demands on the Writing and Speaking criteria, and how to set per-paper targets that average to the overall, see `references/band-descriptors.md` (section "Setting targets from bands"); when `~/.ielts/official/` holds the official band-descriptor PDFs, read those for exact wording.

---

## 2. Triage: where the hours go

The overall band is the mean of the four papers rounded to the nearest half band, so a gain in any paper counts. Decide where to spend time like this:

1. **Choose the route with `python3 scripts/ielts.py plan`.** It returns the three cheapest combinations of half-band gains that reach the target overall while respecting per-paper minimums, and converts Listening/Reading gaps into extra correct answers. Its effort units are a heuristic: L/R half-bands cost less than W/S, each step costs more at higher bands, and loading every gain onto one paper is penalised. Recommend the cheapest route that is also **balanced**, and tell the learner why ("two more half-bands in Reading are cheaper than one in Writing").
2. **Choose the micro-skills with `status`.** Inside each paper it ranks the skills losing the most marks recently, and it weights skills that cost marks in several papers more heavily (`x.paraphrase` hurts Listening, Reading and Lexical Resource at once). Put practice on the top two or three and use their drills.
3. **Keep every paper alive.** Strong papers get maintenance time, not zero time.
4. **Start Writing in week one.** It needs draft, feedback, rewrite cycles, so it cannot be crammed late.
5. **Exploit Listening and Reading.** Volume plus question-type technique gives the best return per hour, and the gap is concrete ("three more correct answers").
6. **Speak little and often.** Ten minutes most days beats one long weekly session.

**Fallback split, only before anything has been logged.** Once `plan` and `status` have data, follow them instead.

| Weakest paper | 35% | 25% each | 15% |
|---|---|---|---|
| Writing | Writing | Reading, Listening | Speaking |
| Reading | Reading | Writing, Listening | Speaking |
| Listening | Listening | Writing, Reading | Speaking |
| Speaking | Speaking | Writing, Listening | Reading |
| No clear weakness | 25% to every paper | | |

---

## 3. Weekly structure

Every study day opens with the daily drill session from `references/drills.md` (15–25 minutes): `due` reviews first, then one drill on the top leverage skill from `status`, then `log`. Fill the rest of the week around that.

**Example: working professional, about 9 hours a week, target +1 band, weakest in Writing and Reading.**

| When | Activity | Time | Module |
|---|---|---|---|
| Mon–Fri, daily | Drill session (reviews + one drill) | 20 min | `references/drills.md` |
| Mon–Fri, commute | English audio: podcast, lecture, news; no answering | 20 min | Listening exposure |
| Mon | Academic-paper session (below) | 40 min | `modules/reading.md` |
| Tue | Task 2: plan and write under time | 40 min | `modules/writing-task2.md` |
| Wed | One Listening section, then transcript check of every wrong answer | 30 min | `modules/listening.md` |
| Thu | Task 1 report (or GT letter) and self-score before feedback | 25 min | `modules/writing-task1.md` |
| Fri | Speaking Part 2 long turn + Part 3 follow-ups, recorded | 20 min | `modules/speaking.md` |
| Sat | Timed Reading section (3 passages, 60 min) or full Writing paper, then error review | 90 min | `modules/reading.md` / writing modules |
| Sun | Rewrite the week's weakest Task 2 paragraph; Part 1 questions aloud; deck review | 40 min | writing, speaking, `modules/vocabulary.md` |

Weekly minimums for each paper (scale up for the weakest):

- **Writing:** one or two Task 2 essays and one Task 1, rotating question and visual types; study the structure and cohesion of one high-band response each week; the learner predicts their band before every marking.
- **Reading:** two or three single passages focused on the question type `status` flags, one timed full section, plus academic-paper sessions.
- **Listening:** daily exposure beyond test material, two or three official-format sections checked against the transcript, and a two-minute dictation once a week for connected speech.
- **Speaking:** Part 1 answers aloud most days, a timed Part 2 (one minute preparation, two minutes talking) three times a week, Part 3 discussion once or twice using ideas from the week's reading, and one recording replayed for fluency and range.

### Academic-paper sessions for Reading

Academic Reading passages come from books, journals, magazines and newspapers written for a general educated reader, so accessible research writing is close practice: long multi-clause sentences, hedged claims, evidence and qualification. Good sources are review articles, research-based science journalism, policy reports from bodies such as the World Bank or OECD, and the introduction and conclusion of papers in fields the learner likes. Pick fields that match common passage themes: environment, technology, health, education and psychology, economics, history and archaeology. Full technical understanding is not the goal.

Run each session to a fixed shape (about 40 minutes):

1. **Map (5 min).** Read only the title, abstract, headings, and the opening and closing sentence of each section. Write one sentence: what the authors claim and how they support it. This trains main-idea and headings questions.
2. **Close read (20 min).** Read two or three sections carefully. Mark claims, evidence phrases ("the data show", "was associated with") and hedges ("may", "appears to"). Then answer: what supports the main claim, and what limits it? Deciding what the text does and does not commit to is exactly True/False/Not Given and Yes/No/Not Given reasoning.
3. **Capture (5 min).** Choose up to five useful academic phrases with their collocations and add the ones the learner will actually reuse to the personal deck with `vocab add --term ... --meaning ... --l1 ... --source reading`.
4. **Summarise (10 min).** Write four or five sentences in their own words, selecting only the key points (useful Task 1 overview practice), and name which question types the text would suit (a process suits flow-chart completion; a debated claim suits YNNG).

Frequency: twice a week for a 6.0 target, three times for 7.0, four or five for 7.5 and above. Begin with review articles and science journalism; move to primary research as comfort grows.

---

## 4. Checkpoints and mock tests

**Mock cadence.** One full timed mock (all four papers in one sitting where possible, using official IELTS practice material) at the start if there is no baseline, then every three to four weeks. In the final four weeks, move to one full mock a week. Between mocks, single timed sections are enough.

**At each checkpoint:**

1. Score each paper and log it (`log --module listening --score L=29/40 --tag ...`, same for reading; writing and speaking through their modules). A full mock can also be recorded in one entry: `log --module mock --task "Mock 2" --score L=29/40 R=31/40 W=6 S=6 --source mock`.
2. Run `status` and `plan`: compare bands with the previous checkpoint, read the top leverage skills, and see whether the cheapest route has changed.
3. Rebalance: move hours to the new top leverage skills and cut time on papers already at target (keep maintenance).
4. Check prediction bias in `status`. If the learner over-predicts Writing or Speaking by 0.5 or more, have them predict before every scored piece until the bias shrinks (`references/calibration.md`).

**Evidence of progress:** Reading and Listening raw scores rising and sections finished in time; fewer Not Given mistakes; fewer Section 3–4 mishearings. Task 1 always has an overview; Task 2 holds one clear position; less repeated vocabulary. Speaking turns get longer without searching for words. In `status`, error items move to `improving` or `resolved` and drills reach level 2–3.

---

## 5. The final week

- No new strategies. Two short timed sections a day at most, plus the drill session.
- Do one last full mock no later than four days before the test so there is time to review it; rest the day before.
- Re-read the learner's own error ledger and their best rewritten paragraphs instead of fresh material.
- Rehearse logistics: test format (computer or paper), centre location and travel time, ID document, and the Speaking slot, which may be on a different day.
- After results arrive, record them with `set --band ... --source official` and, if a resit is needed, rerun `plan`.

---

## 6. Indonesian learner realities

- **Time budget.** Most learners are working professionals with 6–10 hours a week. Plan around 20–30 minute weekday blocks (commute audio, lunch-break drills) and one or two longer weekend blocks for timed papers. Ask about overtime peaks, Ramadan schedules and Lebaran travel and lighten those weeks in advance rather than letting the plan collapse.
- **Speaking without a partner.** Use phone recordings and self-review against `modules/speaking.md`; a weekly online or office conversation partner helps fluency more than extra solo hours.
- **Grammar that costs marks in both Writing and Speaking.** Missing articles, unmarked plurals and third-person -s, and past tense left unmarked because Indonesian does not inflect verbs. Plan these as recurring drill targets (`g.articles`, `g.agreement`, `g.tense-aspect`, `x.plural`; see `modules/grammar.md`), not one-off lessons.
- **Pronunciation.** Dropped final consonants and -ed/-s endings lower both Pronunciation and perceived grammar; schedule `s.pron-endings` drills alongside grammar work.
- **Reading load.** Long English texts are slower than in Bahasa Indonesia at first; the academic-paper sessions and timed sections build stamina, so start them early.

---

## Plan output

Give the learner:

1. **Diagnosis:** current bands, target, gap, weeks left, weekly hours, weakest papers and skills, and whether the timeline is realistic.
2. **Route:** the cheapest balanced route from `plan`, with the reason.
3. **Hours per paper per week**, following that route (the fallback split only if nothing is logged).
4. **A seven-day schedule** with durations and the module behind each activity, including the daily drill session (due reviews, then one drill on the top leverage skill; see `references/drills.md`) and academic-paper session days with their topic areas.
5. **Mock dates and the first checkpoint**, with what a good result at that checkpoint looks like for this learner.

A plan the learner will not follow is worse than none. If they have only five hours a week, say it directly and stretch the timeline instead of overloading the week.
