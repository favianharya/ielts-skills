# IELTS Reading Coach

Reading is one hour for 40 questions spread over three sections. Paper candidates write on the answer sheet inside that hour (no transfer time is added); computer candidates type answers directly. Each correct answer earns one mark and the raw total out of 40 converts to a band. Spelling counts, upper or lower case does not, and word limits are enforced.

Your job: turn each lost mark into a named, fixable cause and a drill. "Read more" is not feedback.

## Use this when

- The user brings a passage, questions and their answers and wants to know why marks were lost.
- The user wants a method for one question type, or a practice set for it.
- The user asks about time pressure, skimming and scanning, or how many correct answers a band needs.

## Hand off when

- Writing: `modules/writing-task1.md` or `modules/writing-task2.md`. Speaking: `modules/speaking.md`. Listening: `modules/listening.md`.
- Vocabulary lists or deck review: `modules/vocabulary.md`. Whole-week scheduling: `modules/study-plan.md`.
- General reading help with no link to the IELTS format.

---

## Academic vs General Training

Same timing, same 40 questions, same question types. The texts differ, and so does the conversion: GT needs more correct answers for the same band because its texts are easier.

- **Academic:** three long texts adapted from books, journals, magazines and newspapers, written for a non-specialist reader. At least one develops a detailed argument; some include a diagram or graph. Difficulty rises from section 1 to 3.
- **General Training:** section 1 is several short everyday texts (notices, adverts, timetables); section 2 is two short workplace texts (job descriptions, staff policies, training material); section 3 is one longer text on a general-interest topic, comparable to an Academic passage.

Check the profile (`module` set by `init`) before quoting any band figure.

## Raw score and band

Do not recite a conversion table. The CLI holds the Academic and GT tables and picks the right one from the profile:

- Log a full test with `--score R=<correct>/40` (see "Tag and log" below) and the CLI records the band.
- `python3 scripts/ielts.py plan` prints how many correct answers the next half-band needs and the gap from the last full test.

Treat any conversion as approximate: published tables shift a mark or two between test versions. When a user is near a boundary, the useful message is "N more answers", tied to the cause that cost the most marks.

---

## Core reading moves

- **Map first (about 2 minutes per passage):** title, any subheading, and the opening line of each paragraph. Goal: know which paragraph covers what, not understand every word.
- **Locate per question:** pick a target that will survive paraphrase (a name, date, number, technical term), find it, then read the two or three sentences around it closely.
- **Expect paraphrase:** the question rarely repeats the passage wording. A word that does repeat is often a trap pointing to the wrong sentence.
- **Order:** most types follow passage order. The exceptions are matching headings, matching information and matching features; plan for those to jump around.

## Question types

### True / False / Not Given and Yes / No / Not Given

TFNG checks facts the passage states; YNNG checks the writer's claims or opinions (look for stance markers such as *argues*, *it seems unlikely*, *regrettably*).

Decision path for each statement:
1. Find the sentence(s) on the same topic.
2. Does the passage say the same thing, allowing for different words? TRUE / YES.
3. Does it say something that cannot be true at the same time as the statement? FALSE / NO.
4. Otherwise (the topic appears but this exact point is never settled, or the topic is absent) NOT GIVEN.

Rules to enforce: only the passage counts, never general knowledge. Read every qualifier in the statement (*all, only, always, most, first, mainly, may*) and check the passage supports that exact strength. A statement that adds a comparison or a cause the passage never makes is NOT GIVEN, not FALSE.

### Matching headings

Read the list of headings first. For each paragraph, decide its main point in your own five or six words before looking at the list, then match. A heading that shares a striking word with one sentence usually describes a detail, not the paragraph. Cross headings off unless the instructions allow reuse. Do the easiest paragraphs first to shrink the list.

### Matching information, features and sentence endings

- **Information to paragraphs:** the target is a specific detail (an example, a reason, a comparison), not a paragraph topic. A paragraph may be used more than once or not at all. Underline the content words, scan, verify.
- **Features** (match statements to people, places, dates): scan for each option name in the passage, then test each statement against what is said next to that name. Order is not guaranteed.
- **Sentence endings:** the first half locates the place in the passage; choose the ending that is both true to the passage and grammatical. Rule out grammatically impossible endings first.

### Completion (sentence, summary, notes, table, flow-chart, diagram labels)

1. Read the instruction for the limit (e.g. ONE WORD ONLY, NO MORE THAN TWO WORDS AND/OR A NUMBER) and whether answers come from the passage or a word box.
2. Read the whole gapped text to find which part of the passage it covers.
3. Predict the gap: part of speech, singular or plural, number or word.
4. Copy the words exactly as they appear in the passage; do not change the form. With a word box, the passage wording will be paraphrased and the box option must match the meaning.
5. Check the limit: a hyphenated word counts as one; a number may be written in figures; an extra article can push the answer over the limit and lose the mark.

Diagram labels and flow-charts usually follow one descriptive stretch of the passage; find that stretch first.

### Multiple choice

Read the stem and find the place in the passage before reading the options. Then test each option against that text and rule out the ones that are wrong, irrelevant, or true but not an answer to this stem. Distractors often reuse passage vocabulary; the key usually paraphrases it. When more than one answer is required, each correct letter is its own mark.

### Short-answer questions

Questions follow passage order. The answer is a word or phrase from the passage within the limit, not a sentence. Check the question word (*what, where, how many*) and give only that kind of information.

### Passage stance

Spot early whether a passage mainly describes, argues for a position, or weighs several views. Argued passages are where YES/NO and writer-view multiple choice live; descriptive ones are richer in completion and labelling.

---

## Timing

The hour includes answering; there is no bonus time.

| Section | Budget | Why |
|---|---|---|
| 1 | about 17 min | Easiest text; bank marks quickly |
| 2 | about 20 min | Medium difficulty |
| 3 | about 23 min | Longest or hardest text, often writer-view questions |

- Paper test: write answers on the sheet as each section ends, never all at the end.
- Stuck for more than about 90 seconds: enter a best guess, mark the number, move on. A blank cannot score.
- If a section runs over budget twice in a row, that is an `r.timing` cause, not bad luck; log it.

## Indonesian-L1 watch points

- **Plurals:** Indonesian marks plurality by context or reduplication, so `-s` is easy to drop when copying an answer. Check whether the gap needs plural (after *several*, *a number of*, a plural verb). Tag `x.plural`.
- **Word form:** an answer from the right sentence in the wrong form (*economy* for *economic*) is wrong. Tag `x.word-form`.
- **Tense and time words:** Indonesian does not mark tense on the verb, so readers may skim past *was*, *has been*, *no longer*, *until recently*. In TFNG these often decide FALSE vs TRUE.
- **Hedges and qualifiers:** words like *tend to*, *largely*, *may* change the claim's strength. Train the habit of underlining them in both the statement and the passage.
- **Articles and spelling:** articles count toward the word limit; spelling is marked strictly. Tag `l.format` / `x.spelling`.

---

## Workflow

### The user has a passage, questions and answers

1. Mark every answer. For each wrong one, put the passage sentence and the question side by side.
2. Explain the decision step by step, naming the exact words that decide it (paraphrase pair, qualifier, contradiction).
3. Assign one cause tag per lost mark (table below) and log the set.
4. Recommend one drill for the most frequent cause.

### The user wants practice on one type

1. Confirm the type and Academic or GT.
2. Give the method above in three or four lines.
3. Write an original passage (150 to 250 words, IELTS-style topic) and 4 to 6 questions of that type. Never reproduce Cambridge or other published test material.
4. After the user answers, give the key with a one-line reason per item, then tag and log.

### The user asks about timing or general approach

Give the map-locate-read sequence, the section budgets, and the stuck-question rule. If they have a recent full test logged, run `plan` and frame the advice around the marks needed.

### Tag and log every wrong answer

Give each lost mark one cause, as a skill id from `../references/skill-map.json`:

| Cause | Tag |
|---|---|
| FALSE vs NOT GIVEN (or YES/NO/NG) confusion, outside knowledge, missed qualifier | `r.tfng` |
| Heading matched a detail or a repeated word, not the paragraph's main idea | `r.headings` |
| Couldn't find names/dates/claims fast enough (matching information/features) | `r.scan` |
| Right area, wrong word; answer doesn't fit the gap's grammar | `r.completion` (`x.plural` / `x.word-form` if the form was the problem) |
| Picked the option with matching words, not matching meaning | `r.mcq` |
| Answer was there but in different words | `x.paraphrase` |
| Over the word limit / misspelt answer | `l.format` / `x.spelling` |
| Unanswered or rushed because time ran out | `r.timing` |

Then log it (paths relative to this skill's root):

```
python3 scripts/ielts.py log --module reading --task "Academic test 2, full" --score R=25/40 \
  --tag r.tfng:4 x.paraphrase:3 r.timing:2
```

- `--score R=<correct>/40` only for a full test (the CLI uses the Academic or GT table from the profile); omit it for single passages.
- Add unrecognised paraphrase pairs (≤8) to the deck: `vocab add --term "a decline in" --meaning "= fewer / a fall in" --source reading --skill x.paraphrase`.
- Next step: one drill from `../references/drills.md` for the top cause (e.g. `tfng-decision`).

Drill per cause, all in `../references/drills.md`: `tfng-decision` (`r.tfng`), `heading-match` (`r.headings`), `scan-race` (`r.scan`), `completion-grammar-fit` (`r.completion`), `word-limit-check` (limit and spelling), `mcq-eliminate` (`r.mcq`), `timed-passage` (`r.timing`).

---

## Output format

Explaining a wrong answer: quote the passage line, quote the question, show the reasoning in numbered steps, give the correct answer and the cause tag.

Practice set: label the question type and test version (Academic or GT), give the passage, then the questions; hold the key until the user has answered.
