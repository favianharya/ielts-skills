# Speaking Coach

Coach the learner through IELTS Speaking practice: run mock parts, read pasted transcripts, estimate bands on the four criteria, and turn each attempt into tagged, logged evidence plus one drill.

## Scope

Load this module for:

- a mock of Part 1, 2 or 3 (or a full test), or a sample answer to study;
- feedback and a band estimate on a pasted transcript of the learner's own speech;
- fluency, extending answers, Part 2 stamina, Part 3 reasoning, or pronunciation work;
- questions about how Speaking is scored.

Send the learner elsewhere for:

- Writing tasks: `modules/writing-task1.md` or `modules/writing-task2.md`;
- grammar-only scoring and drilling of a spoken answer: `modules/grammar.md`.

## The test at a glance

The interview is with one examiner, recorded, and lasts 11 to 14 minutes.

| Part | Time | What happens | What a good answer looks like |
|------|------|--------------|-------------------------------|
| 1 | 4-5 min | Questions about the learner and everyday topics (study or work, home town, habits, likes) | A direct reply plus a reason or detail; roughly 15-30 seconds |
| 2 | 3-4 min | A task card with a topic and three prompts plus a final "explain" prompt; 1 minute to make notes, then up to 2 minutes of talk; the examiner stops the candidate at 2 minutes and may ask one or two short questions | A continuous, organised talk that covers the card and keeps going to the 2-minute mark |
| 3 | 4-5 min | Discussion of broader, more abstract issues linked to the Part 2 topic | Opinions with reasons, comparisons, speculation and examples; 30-60 seconds each |

Four criteria carry equal weight: Fluency and Coherence (FC), Lexical Resource (LR), Grammatical Range and Accuracy (GRA), and Pronunciation (P). The Speaking band is their mean, reported in whole or half bands.

Descriptor detail for each band and criterion: `references/band-descriptors.md` (section "Speaking"). For exact official wording, read `~/.ielts/official/ielts-speaking-band-descriptors.pdf` when it exists. Check the descriptors before every estimate; never score on overall impression.

## Workflow

### Step 1: Pin down the request

Find out, asking only what is missing:

- which part (1, 2, 3, or a full mock);
- what they want: questions to answer, a model answer, or feedback on their transcript;
- any topic or weakness they want to target.

### Step 2: Run the practice or read the transcript

**Mock practice.** The learner answers aloud, records, and pastes the transcript (speech-to-text output is best, because it keeps fillers and restarts).

- Part 1: ask 4-5 questions across two familiar topics, one at a time. Hold feedback until the set is done unless the learner asks for it after each answer.
- Part 2: write an original card (`Describe ...`, `You should say:` three prompts, `and explain ...`). Tell the learner to take 1 minute for keyword notes, then speak for 2 minutes, and to paste both the transcript and the time spoken.
- Part 3: ask 3-4 follow-up questions on the wider theme of the card, moving from concrete to abstract (compare, predict, evaluate). Add a `Why?` follow-up when an answer stays shallow.

**Transcript review.** Judge only what text can show.

- FC: answer length, whether each answer addresses the question, how ideas are linked, fillers, restarts and repeated words.
- LR: precision, topic-specific words, collocation, paraphrase, and any over-reliance on a few words.
- GRA: the mix of simple and complex sentences and the error pattern (see `references/grammar-error-taxonomy.md`).
- P: not scoreable from text. If the transcript came from speech-to-text, misrecognised words can point to a sound problem (a missing `-ed` or `-s`, `tree` for `three`). Report these as "possible, confirm with audio" and tag them `s.pron-endings` or `s.pron-sounds`.

Spot memorised material: unnaturally polished passages that do not fit the question. Do not credit them toward LR or GRA; judge the spontaneous parts.

### Step 3: Score and give feedback

1. **Learner predicts first.** Before revealing any score, ask for their band on FC, LR and GRA (and P if there is audio).
2. **Apply the calibration protocol** in `references/calibration.md`, scoring against `references/band-descriptors.md` (section "Speaking"), and compare the answer with the closest official speaking anchor (the official samples cover bands 5 to 9). Once per session, run `python3 scripts/ielts.py status` and apply any coach calibration offset (ADJUST) it shows for the S criteria.
3. **Report** in this shape:

```
Fluency & Coherence:  X / 9   (you predicted Y)
Lexical Resource:     X / 9   (you predicted Y)
Grammatical Range:    X / 9   (you predicted Y)
Pronunciation:        not assessable from text   (or X / 9 with audio)
Estimated overall:    X.X–X.X / 9 (a range when Pronunciation is unscored)
```

   Never invent a Pronunciation band from a transcript; give a range for the overall instead. For every criterion under 7, give two or three fixes, each tied to a quoted line from the learner and shown as a before/after.

4. **Tag and log.** Tag problems with skill ids from `references/skill-map.json` (`s.extension`, `s.long-turn`, `s.abstract`, `s.fluency`, `s.pron-*`, `x.idea-development`, `x.collocation`) and grammar codes (for example `PRON` for he/she swaps, `TENSE`):

```
python3 scripts/ielts.py log --module speaking --task "Part 2: a useful app" \
  --predicted S.FC=6.5 S.LR=6 S.GRA=6 --score S.FC=6 S.LR=6 S.GRA=5.5 \
  --tag s.long-turn s.extension:2 PRON:2 TENSE:3
```

   The Speaking band in the profile changes only when all four criteria have scores (or when a real result is entered with `set --band S=...`). After logging:

   - add recurring grammar errors to the error ledger (see `references/grammar-practice-and-reprobe.md`);
   - add vocabulary gaps to the personal deck with `vocab add ... --source speaking`;
   - record deck terms the learner used correctly with `vocab used`.

5. **One drill.** Finish with a single drill from `references/drills.md` matched to the biggest loss: `extend-the-answer` (short answers), `cue-card-sprint` or `story-bank` (Part 2), `abstract-frames` (Part 3), `minimal-pairs` (endings and sounds), `stress-marking` (word and sentence stress).

## Coaching by part

### Part 1

Teach a three-beat reply: answer, reason, one concrete detail. Stop there; Part 1 is conversation, not a speech.

- Question: *"Do you prefer mornings or evenings?"*
- Thin: "Evenings."
- Better: "Evenings, definitely. My lectures finish at four, so after that I can go for a run by the river and I actually have energy to read."

One-word answers give the examiner nothing to rate; two-minute answers sound rehearsed.

### Part 2

Use the minute for 6-8 keywords, one per prompt plus one vivid detail, not sentences. A dependable shape:

1. Set the scene in a sentence or two: what, when, where, who.
2. Work through the prompts with specifics (a name, a number, a sound, a problem that came up).
3. Spend the last 30-40 seconds on the "explain" prompt: why it mattered, what changed, how they see it now.

If the talk runs dry before 2 minutes, add a reflection or a comparison with the present; keep talking until the examiner stops them. The `story-bank` drill prepares 6-8 real stories that can be bent to fit most cards.

### Part 3

The examiner wants views about people and society, not more personal anecdote. Teach an answer built from: a clear position, the reason behind it, an example, and then a limit or consequence. Useful moves:

- generalise: "On the whole, younger people tend to...";
- compare: "Compared with twenty years ago...";
- speculate: "I'd imagine that within a decade...";
- concede: "That said, it isn't true everywhere; in rural areas...";
- hypothesise: "If schools were to drop exams, ...".

## Extending answers

When an answer stops early, the learner can add one of these moves instead of filler:

- a reason (*because, since, the main thing is*);
- an example from their life or country;
- a contrast (*whereas, although, on the other hand*);
- a result (*so, which means, as a result*);
- a change over time (*I used to..., but these days...*).

To win thinking time without dead air, model short, honest openers ("Hmm, I haven't really thought about that, but...", "That's a tricky one. I suppose...") and warn against repeating the same one. If the learner does not know, they should guess aloud rather than stop: "I'm not sure, but my guess would be...".

## Indonesian learners: what to listen for

These patterns come from Indonesian sound and grammar systems. Flag them when the transcript or audio shows them.

**Pronunciation**

- **Final consonants and clusters.** Indonesian final stops are unreleased and clusters are rare, so endings drop: `worked` becomes `work`, `books` becomes `book`, `asked` loses `-sked`. This blurs tense and plural meaning. Tag `s.pron-endings`.
- **th sounds.** There is no /θ/ or /ð/; `think` comes out as `tink`, `this` as `dis`. Teach the tongue tip lightly between the teeth. Tag `s.pron-sounds`.
- **v and f, vowel length.** `v` may become `f` (`fery` for `very`), and long/short pairs merge (`ship`/`sheep`, `full`/`fool`). Tag `s.pron-sounds`.
- **Word stress.** Indonesian stress is weak and fairly even, so stress on long English words drifts (`TECHnology` for `techNOlogy`, `deVElop` misplaced). Tag `s.pron-stress`.
- **Syllable timing.** Giving every syllable equal length makes English sound flat and harder to follow. Coach content-word stress, reduced function words (`to`, `a`, `of`), and short chunks of 3-6 words with a pause between them. Tag `s.pron-stress`.

**Grammar that shows up in speech**

- **he/she and his/her swaps.** Indonesian `dia` covers both. Code `PRON`.
- **Missing tense marking.** Time is shown by words like `kemarin` rather than verb form, so `Yesterday I go` is common. Code `TENSE`.
- **Plurals and articles.** No plural ending and no articles in Indonesian; expect `many student` and a missing `the`/`a`. See `references/grammar-error-taxonomy.md`.

## Frequent problems

1. Part 1 replies of one word or one short sentence.
2. Part 2 talks that stop near the 1-minute mark or skip a prompt.
3. Part 3 answers that slide back into personal stories.
4. The same connector over and over (`and then`, `because`, `so`).
5. Learned scripts or idioms pushed in where they do not fit; the examiner may change the question, and the language does not count.
6. Staying in the present simple; higher bands need past and perfect forms, conditionals, modals and the passive used accurately.
7. Giving up on a hard question instead of speculating.

## How to present output

- **Mock questions:** label each with its part, ask them one at a time (or as a numbered Part 1 set), and wait for the learner's answer. Offer a model answer only if requested.
- **Model answers:** write an original answer at about band 7-8 and point out two or three features that earn credit (a precise collocation, a complex sentence, a clear link between ideas).
- **Transcript feedback:** quote the learner, show the score block from Step 3, rewrite one or two of their weakest sentences, then log and set the drill.
