# Scoring Calibration: Protocol and Official Anchor Index

Use this file every time you give a Writing or Speaking band estimate. Part A is the procedure that keeps estimates honest and stable. Part B is an index of official, examiner-rated samples to compare against.

Related files: `references/band-descriptors.md` (sections "Writing Task 1", "Writing Task 2", "Speaking", "Grammatical Range and Accuracy (Writing and Speaking)"; for exact wording read the official PDFs in `~/.ielts/official/` when they exist), `references/skill-map.json` (skill ids), `modules/writing-task1.md`, `modules/writing-task2.md`, `modules/speaking.md`. CLI: `python3 scripts/ielts.py`, run from the skill root.

All coach scores are estimates. Never present them as official IELTS results.

---

## Part A: Scoring protocol

Run these steps in order for every Writing Task 1, Writing Task 2 and Speaking score. Do not skip a step because the response "looks like a 6".

### 1. Learner predicts first

Before showing any score, ask the learner to predict their band per criterion (TA or TR, CC, LR, GRA for Writing; FC, LR, GRA, P for Speaking). Record both when logging:

```
python3 scripts/ielts.py log --module writing-task2 \
  --predicted W2.TR=7 W2.CC=7 W2.LR=6.5 W2.GRA=6.5 \
  --score W2.TR=6 W2.CC=6.5 W2.LR=6 W2.GRA=6 \
  --tag w2.position:1 x.collocation:3
```

Score keys: `W1.TA W1.CC W1.LR W1.GRA`, `W2.TR W2.CC W2.LR W2.GRA`, `S.FC S.LR S.GRA S.P`. Tags are skill ids or codes from `skill-map.json`; add `:N` (number of occurrences or lost marks) to the skills that cost marks. The gap between prediction and score is itself feedback: a learner who over-predicts LR every time is not noticing their own imprecise word choice.

Score before you read the learner's prediction out loud; do not let it move your score.

### 2. Gates and caps first

Check the hard limits before judging quality. A failed gate caps the affected criterion no matter how good the language is (anchor `W1-A-1C-scriptB` was rated 7 overall because strong language could not compensate for format and overview problems).

| Task | Gate | Effect | Where defined |
|---|---|---|---|
| W1 Academic | At least 150 words | Penalty to TA | `references/band-descriptors.md` (section "Writing Task 1", gates and caps) |
| W1 Academic | Overview of main trends/stages present | No clear overview puts TA in band 5 territory; a weak overview keeps TA at 6 | `references/band-descriptors.md` (section "Writing Task 1"), TA 5-7 |
| W1 Academic | Key figures reported, accurate, no opinion or letter format | Missing data or inappropriate format limits TA (`W1-A-1A-scriptA`, `W1-A-1C-scriptB`) | `modules/writing-task1.md` Step 4 |
| W1 GT | Every bullet covered and extended | Missing bullet: TA cannot reach 6; one-line bullet keeps TA at 5-6 | `modules/writing-task1.md` "Task gates and band caps" |
| W1 GT | Tone fits the reader and stays consistent; greeting and closing present | Inconsistent tone caps TA at 6; missing closing reduces TA (`W1-G-1B-scriptB`, `W1-G-1B-scriptC`) | same section |
| W2 | At least 250 words | Penalty to TR (`W2-A-CD-resp1`) | `references/band-descriptors.md` (section "Writing Task 2", gates and caps) |
| W2 | Every part of the question answered | Unanswered part pulls TR down sharply (`W2-G-2B-scriptA`, band 4) | `modules/writing-task2.md` Step 1 |
| W2 | Clear position where the question asks for one | Unclear position keeps TR at 5 or below | `references/band-descriptors.md` (section "Writing Task 2") |
| W1/W2 | Copied rubric | Not credited and does not count toward the word count (`W2-A-2B-scriptA`) | official sample comments |
| W1/W2 | Full connected prose, no bullet points or notes | Penalised (stated in the official sample PDFs) | `modules/writing-task2.md` |
| Speaking Part 2 | Speaks for most of the 2 minutes and stays on the card topic | Short turn or drifting across several topics limits FC (`S-B5-tina`) | `modules/speaking.md` Part 2 |
| Speaking | Answers the question asked | Unanswered or sidestepped questions cost FC coherence (`S-B6-stephen`, `S-B6-maxim`) | `modules/speaking.md` |
| Speaking | Memorised or rehearsed script | Do not credit memorised language toward LR/GRA; judge the spontaneous parts | `references/band-descriptors.md` (section "Speaking", gates and caps); `modules/speaking.md` "Frequent problems"; `skill-map.json` s.long-turn |
| Speaking from text only | Pronunciation cannot be judged from a transcript | Report P as "not assessed" rather than guessing | this file |

State every gate result in one line before the criterion scores: "Gates: 263 words, all parts answered, position clear."

### 3. Per criterion: evidence, best fit, then one up and one down

For each criterion:

1. Quote 2-3 pieces of evidence from the learner's own text or transcript (errors and strengths).
2. Pick the band whose descriptor fits best overall. Best fit, not the highest band where one feature appears.
3. Run the boundary check against `references/band-descriptors.md` (the section for the task; exact wording in the official PDF in `~/.ielts/official/` when it exists):
   - Why not one band higher? Name the descriptor feature that is missing or not sustained.
   - Why not one band lower? Name the feature that lifts it above the lower band.
4. If you cannot write a concrete "why not higher" sentence, you have probably under-scored; if you cannot write a concrete "why not lower", you have probably over-scored.

### 4. Anchor comparison

Pick the nearest anchor in Part B: same task type (W1 Academic, W1 GT, W2, Speaking), at or next to your provisional band. Write one sentence per response:

> Closer to anchor `W2-A-2A-scriptB` (6.5) than `W2-A-2B-scriptB` (7.5) because ideas are clear but partly built from rubric wording and grammar errors are regular, as in the 6.5 anchor.

If your provisional band disagrees with the anchor's key features (for example, you gave 7 but the response shows the "coherence lost through self-correction" pattern of the band 6 speaking anchors), revise or report a range.

### 5. Known biases in AI scoring, and the correction for each

| Bias | What it looks like | Correction |
|---|---|---|
| Over-rewarding length | A long essay or long speaking turn feels "developed" | Length is not development. Ask: is each idea extended with a reason, example or consequence? `W2-A-CD-resp2` (7.5) has relevant ideas, while the long Part 3 turns of `S-B6-maxim` still sit at 6 because answers drift from the question. |
| Fluent-sounding but imprecise vocabulary | "Fancy" words that are slightly wrong (`come into great attention`) | Count imprecise or wrong collocations. Imprecision restricts LR even at high levels (`S-B7.5-aashish` was limited to 7.5 by LR); several imprecise items cap LR around 6 (`S-B6-stephen`). |
| Memorised templates and linking phrases | "It is undeniable that...", "Firstly... Secondly... Moreover..." at every sentence start | Mechanical or sentence-initial linkers are a band 5-6 feature (`W1-A-1C-scriptA`, `S-B5-katsuharu`); overused sequencers held back even a 7.5 (`W2-A-CD-resp2`). Do not credit templates as range. Judge the learner's own sentences. |
| "Readable" grammar | Errors do not block meaning, so the text feels like 7 | "Errors do not impede communication" is a band 6 description (`S-B6-stephen`, `S-B6-maxim`). Band 7 needs frequent error-free sentences; band 8 needs most sentences error-free. Count error-free sentences out of total and state the ratio. |
| Under-penalising partial task response | Strong language hides a missing part or bullet | Apply the gate in step 2 first. `W1-G-1B-scriptB` had higher-level language but a missing bullet held it at 5.5; `W2-G-2B-scriptA` skipped one question and got 4. |
| Under-penalising a missing overview | Detailed, accurate description with no summary | No clear overview keeps TA at 5 (`W1-A-1C-scriptA`) and limited a high-language response (`W1-A-1C-scriptB`). |
| Under-penalising tone drift (GT letters) | Formal letter slides into chatty phrases | Inconsistent tone caps TA at 6 and also hurts LR; check opening, body and closing separately. |
| Leniency drift across a long session | Later scripts get higher bands for similar quality | After every 3-4 scores in one session, re-read the first scored response and the nearest anchor; if the same features would now get a higher band, correct the later scores downward. |
| Anchoring to the learner's previous score | New score lands at last score plus or minus 0.5 | Score from the current evidence first, without looking at history; compare with past scores only after the bands are written down. |
| Rewarding effort or improvement | "Much better than last time" becomes a higher band | Improvement belongs in feedback, not in the band. The descriptor decides the band. |

### 6. Report a range when evidence is mixed

If a criterion shows features of two bands, report a range (for example LR 6.0-6.5) and say which feature would settle it. Overall estimates should also be ranges when two or more criteria are ranges. Never write "your IELTS score is"; write "estimated band" and remind the learner that only certificated examiners give official scores.

For a single writing task, the coach's task-level band is the mean of the four criteria, reported to the nearest half band. This is a coaching convention, not a published IELTS rounding rule.

### 7. Bias tracking with external references

Whenever an externally scored reference exists (official sample, a teacher's score, the learner's real test result), log the coach score against it:

```
python3 scripts/ielts.py calibrate add --task W2 \
  --coach TR=6,CC=6.5,LR=6,GRA=6,OVERALL=6 \
  --reference OVERALL=6.5 \
  --source official:W2-A-2A-scriptB
```

- Keys: `TA TR CC LR GRA` (Writing), `FC LR GRA P` (Speaking), plus `OVERALL`. The official anchors in Part B publish only the overall task or part band, so their reference is `OVERALL` only; a teacher or real test result may supply per-criterion values.
- Source formats: `official:<anchor-id>`, `teacher:<name-or-date>`, `test:<date>`.
- `calibrate report` shows the mean offset (coach minus reference) per `<task>.<key>` (for example `W2.OVERALL`, `S.LR`); only keys present in both `--coach` and `--reference` are compared. Positive means the coach is too lenient.
- Rule: if |mean offset| is at least 0.5 on a key over at least 3 comparisons, say so explicitly in the next score report ("Calibration: my LR has run 0.5 high against references; adjusted") and shift that key's estimates toward the reference by the mean offset, rounded to the nearest 0.5. Re-check after each new comparison; remove the adjustment when the offset falls below 0.5.

### 8. Periodic blind self-check

Every ~10 Writing or Speaking scores, blind-score one official anchor from Part B:

1. Pick the anchor closest to the learner's current estimated band and task type, rotating so the same anchor is not reused until the others of that type have been used.
2. Fetch the source and read only the script or transcript. Stop before the heading "Examiner comment(s)". In the speaking web page, read from "View transcript" down to, but not including, "Examiner comments". In the computer-delivered Academic PDF, each response comes before its comment on the same page.
3. Score it with steps 2-6, writing every criterion and the overall before reading the comment.
4. Read the examiner comment and log: `calibrate add --task <W1|W2|S> --coach ... --reference OVERALL=<official band> --source official:<anchor-id>`.
5. If off by 0.5 or more, write one line on which feature you misjudged.

Text-accessible anchors (best for blind scoring): the 12 speaking transcripts and the 4 computer-delivered Academic responses (`W1-A-CD-resp1`, `W1-A-CD-resp2`, `W2-A-CD-resp1`, `W2-A-CD-resp2`). In the 2023 paper sample PDFs the candidate scripts did not come out as text when extracted (they appear to be images of handwriting, and only the examiner comments extract). Use them for blind scoring only if you can view the page image; otherwise use them as feature anchors only. Speaking transcripts allow FC, LR and GRA judgements; P needs the video (linked on the same page).

---

## Part B: Official anchor index

### Sources

| Code | Source | Status |
|---|---|---|
| SPK | IELTS.org, "Resources to help set your IELTS score requirements", Speaking section: https://ielts.org/organisations/ielts-for-organisations/understanding-ielts-scoring/resources-for-setting-your-ielts-scores | Loaded; 12 samples, video + transcript + examiner comments |
| AW | IELTS Academic Writing Sample Tasks (2023): https://ielts.org/cdn/Sample-tests/ielts-academic-writing-sample-tasks-2023.pdf | Loaded; 26 pages; tasks pp. 3-7, 12 scripts pp. 9-26 |
| AWCD | IELTS Academic Writing, computer-delivered sample, example responses to Parts 1 and 2: https://ielts.org/cdn/computer-delivered-sample-tests-academic-writing/ielts-academic-writing-example-responses-to-parts-1-and-2-with-band-scores-and-examiner-comments.pdf | Loaded; 5 pages; 4 responses. The task prompts sit in the interactive Inspera player linked from https://ielts.org/take-a-test/preparation-resources/sample-test-questions/academic-test and were not retrievable as text, so task summaries below are inferred from the responses. |
| GTW | IELTS General Training Writing Sample Tasks (2023): https://ielts.org/cdn/Sample-tests/ielts-general-training-writing-sample-tasks-2023.pdf | Loaded; 24 pages; tasks pp. 3-6, 11 scripts pp. 8-24 |

How to read the entries:

- Official band: the band IELTS gives the sample. All these sources publish one band per task (Writing) or per test part (Speaking). None publishes per-criterion bands; the per-criterion bullets below paraphrase what the examiner comment says about that criterion.
- "Limiting" lines quote or paraphrase the examiner's own statement of what held the band down, where one is given. Lines marked [INFERENCE] are the coach's reading, not the examiner's.
- Markers are short phrases quoted from the sample or the examiner comment (under 15 words) to help recognise the pattern. No full scripts or transcripts are reproduced here; read them at the source.
- Skills: ids from `skill-map.json` most relevant to the anchor's limiting features.
- IELTS states these samples "should not be regarded as definitive examples of any particular band score". Use them as reference points, not templates.

Counts: Speaking 12, Writing Task 1 Academic 9, Writing Task 1 General Training 6, Writing Task 2 (Academic 7 + General Training 5) 12. Total 39.

### Speaking (SPK)

All Speaking samples are rated on one part only (Part 2 or Part 3), not a full test.

#### S-B5-tina: Band 5

- Source: SPK, "Band 5 | Tina, Vietnam". Part 2, describe an interest or hobby you enjoy.
- FC: keeps talking for most of the long turn, but hesitation, repetition and self-correction recur. She describes several interests instead of one, so the turn is hard to follow in places. Linking markers are accurate but from a narrow set (first, so, because, as well).
- LR: limited range, just adequate for the familiar topic; some good items appear; some usage errors.
- GRA: narrow range of patterns with a few if/when clauses; basic structures fairly accurate, but tense errors and omissions are frequent.
- P: strong accent, poorly formed sounds, systematic dropping of word endings, often syllable-timed rhythm and sometimes too fast, causing some strain for the listener.
- Limiting (examiner): grammatical limitations and pronunciation problems restrict the rating to 5 despite her ability to keep going.
- Markers: "widen my knowledge"; "do volunteers"; "I enjoy with it".
- Skills: s.long-turn, g.tense-aspect, s.pron-endings, s.pron-stress. Dropped endings and syllable timing are typical risks for Indonesian speakers; this is the clearest anchor for them.

#### S-B5-katsuharu: Band 5

- Source: SPK, "Band 5 | Katsuharu, Japan". Part 3, social benefits of hobbies, work-leisure balance in Japan.
- FC: keeps the flow going despite hesitation, but answers are not extended. Markers are mechanical and nearly always sentence-initial. Some reformulation and occasional loss of coherence; simple speech is fluent.
- LR: answers are personalised; repetitive vocabulary (hobby, relax, enjoy, work) shows low confidence; still just enough to talk about general trends.
- GRA: a limited set of structures repeated, including if-clauses, with little complexity beyond them; basic control but recurring errors.
- P: generally clear, some mispronounced sounds and words; rhythm often interrupted; stress and intonation not always appropriate.
- Limiting (examiner): rated "a good example of a Band 5 performance".
- Markers: "some of them has problem"; "work extremely hard"; "zer" for 'their'.
- Skills: s.extension, s.abstract, g.agreement, g.complex-range.

#### S-B6-stephen: Band 6

- Source: SPK, "Band 6 | Stephen, China". Part 3, social benefits of hobbies, leisure time in China.
- FC: willing to speak at length, but coherence is lost at moments through repetition, self-correction and hesitation; he cannot answer one question. Varied markers, not always appropriate. Falls back on fillers such as "how to say".
- LR: wide enough to discuss topics at length, including some natural colloquial items; several collocation errors, which rarely cause comprehension problems.
- GRA: mix of short and complex sentence forms; control variable and errors recur, but they do not impede communication.
- P: generally clear, with good chunking, stress and intonation; some words hard to catch because of sound errors (th, final consonants).
- Limiting (examiner): "a good example of a Band 6".
- Markers: "kill the spare time"; "broaden your friendship"; "cut down the working shifts".
- Skills: x.collocation, s.fluency, g.tense-aspect, s.pron-sounds.

#### S-B6-maxim: Band 6

- Source: SPK, "Band 6 | Maxim, Russia". Part 3, current and future hobbies, work-leisure balance.
- FC: keeps going and gives long answers, but sometimes does not answer the question directly; hesitation and repetition limit fluency; range of markers, not always accurate.
- LR: enough to discuss topics at some length; some uncertainty ("how to say?") and inaccurate word choice, but ideas generally come across.
- GRA: mix of simple and complex attempted; control is variable; verb omissions and small errors grow more frequent towards the end. The examiner calls GRA his weakest feature, although his range would suit a higher band.
- P: his best feature; generally clear, with effective stress, rhythm and intonation despite lapses.
- Limiting (examiner): "In this part, the test taker's performance reaches Band 6."
- Markers: "but on the other side"; "in nearest future"; "a lot of job to do".
- Skills: g.verb-form, x.plural, s.fluency. Useful example of an uneven profile: strong P, weak GRA, overall 6.

#### S-B6.5-michal: Band 6.5

- Source: SPK, "Band 6.5 | Michal, Poland". Part 2, describe a well-known person you like or admire.
- FC: speaks at length without losing coherence; some hesitation and reformulation but little repetition; sequences information and links ideas with a range of markers.
- LR: a range including less common items, used with some flexibility and awareness of collocation; inappropriate choices do not block meaning, and the examiner says the range lifts the rating.
- GRA: range of complex structures and embedded clauses with some flexibility; tenses not always accurate, but error-free structures are frequent.
- P: strong accent, regular f for th; only individual words mispronounced; fillers sometimes distort stress; generally clear.
- Limiting: the examiner does not name one. [INFERENCE] Tense accuracy and the th substitution are the most likely brakes on a 7.
- Markers: "a pop icon"; "fight for their rights"; "founds" for 'funds'.
- Skills: s.long-turn (positive model of a sustained turn), g.tense-aspect, s.pron-sounds.

#### S-B7-hendrik: Band 7

- Source: SPK, "Band 7 | Hendrik, Germany". Part 3, famous people in Germany, celebrities in advertising, celebrity responsibility.
- FC: keeps the flow going without noticeable effort and no coherence loss; variety of markers. Overuses the filler "yeah"; referencing sometimes inaccurate.
- LR: wide range including less common and idiomatic items and effective collocation; sometimes lacks precision in words and expressions.
- GRA: good range of simple and complex structures; many error-free sentences; errors in subject-verb agreement, articles and relative pronouns.
- P: clear and easy to follow; sentence stress and intonation convey meaning; noticeable accent; a few mispronounced words lose clarity.
- Limiting (examiner): "a clear example of a Band 7".
- Markers: "he stands for something"; "everything what happens"; "the people who admires him".
- Skills: g.agreement, g.articles, s.pron-sounds.

#### S-B7-alexandra: Band 7

- Source: SPK, "Band 7 | Alexandra, Colombia". Part 3, advantages and disadvantages of fame, media and celebrities.
- FC: quite fluent with appropriate, extended answers; good range of markers; hesitation is mainly about content, not language, and does not affect coherence.
- LR: strongest criterion; wide range including less common, idiomatic and colloquial items; a few errors and inappropriate uses.
- GRA: good range of simple and complex structures used flexibly; a number of error-free sentences; noticeable errors in articles, prepositions, subject-verb agreement and tense.
- P: noticeable accent but generally clear; stress and intonation used well; tendency to syllable-timing stops her keeping a natural rhythm over longer utterances.
- Limiting (examiner): "only just achieves Band 7, owing to a weaker performance in grammar."
- Markers: "selling their soul to the devil"; "if someone recognise you"; "it won't be happen".
- Skills: g.agreement, g.verb-form, g.prepositions, s.pron-stress. Syllable-timing is also an Indonesian-L1 risk.

#### S-B7.5-aashish: Band 7.5

- Source: SPK, "Band 7.5 | Aashish, Nepal". Part 3, famous people then and now, celebrities in advertising, effects on young people.
- FC: fluent, engages without obvious effort; most hesitation and self-correction is content-related and only rarely a search for words; flexible, natural markers.
- LR: sufficient and flexible, with idioms, collocations and awareness of style; some inappropriate usage restricts this criterion, and the examiner names it the weakest.
- GRA: wide range; the majority of sentences error-free; very occasional errors do not affect meaning.
- P: wide range of features; effective stress and intonation; a few poorly formed sounds (th) and word-stress slips with minimal effect.
- Limiting (examiner): vocabulary is the weakest feature, "limiting his rating to Band 7.5".
- Markers: "misused their fame and power"; "come into great attention"; "bit of both".
- Skills: x.collocation, x.less-common-vocab.

#### S-B8-monika: Band 8

- Source: SPK, "Band 8 | Monika, Germany". Page label says Part 3, Famous people; the questions are on popular hobbies, work-leisure balance and social benefits of hobbies.
- FC: very fluent; long, complex, detailed answers without loss of coherence, repetition or searching for language; wide range of markers used naturally and precisely.
- LR: high precision and flexibility with stylistically appropriate language; only occasional inaccuracies or slight inappropriacies.
- GRA: wide range of complex structures, the majority error-free; some inappropriate tense choices and occasional non-systematic errors.
- P: easy to understand throughout despite an accent; occasional phoneme errors have minimal effect; uses intonation and contrastive stress.
- Limiting (examiner): occasional inappropriate usage; overall "a strong example of a Band 8".
- Markers: "anchor point"; "competition is quite big"; "it's depending on what your hobby is".
- Skills: s.abstract and s.pron-stress (positive models).

#### S-B8-kopi: Band 8

- Source: SPK, "Band 8 | Kopi, Botswana". Part 3, famous people in Botswana, celebrities in advertising and politics, effects on youth.
- FC: fluent with occasional hesitation while he weighs his answer; complex, detailed responses without coherence loss; range of markers.
- LR: wide vocabulary used skilfully, precisely and accurately; a few inappropriate word forms and choices.
- GRA: full range of sentence forms used naturally, accurately and appropriately; only very occasional inaccuracies.
- P: easy to understand; slight accent; occasional misplaced stress and vowel errors with minimal effect.
- Limiting (examiner): "strong performance across all criteria make him a clear Band 8".
- Markers: "a ripple effect"; "I wouldn't put it past them"; "old generation" for 'older generation'.
- Skills: none limiting. [INFERENCE] Several of his replies are very short, which shows that a few brief answers on unfamiliar content do not cap FC when the longer answers are coherent and effortless.

#### S-B8.5-kenn: Band 8.5

- Source: SPK, "Band 8.5 | Kenn, Singapore". Part 3, famous people in Singapore, celebrity endorsement, effects on young people.
- FC: fluent for most of the time; develops topics coherently; only slight content-related hesitation.
- LR: precise and sophisticated throughout.
- GRA: wide range used naturally and accurately; very occasional minor errors.
- P: full range of features, including emphatic and contrastive stress; effortless to understand.
- Limiting (examiner): "Only this test taker's occasional hesitations prevent him reaching Band 9."
- Markers: "negative repercussions"; "susceptible to"; "endorsing a cause".

#### S-B9-anuradha: Band 9

- Source: SPK, "Band 9 | Anuradha, Malaysia". Part 3, famous people in Malaysia past and future, advertising, effects on young people, public opinion.
- FC: fluent with only rare repetition or self-correction; hesitation is for ideas, not language; fully appropriate cohesive features.
- LR: full flexibility and precision on all topics; wide idiomatic range.
- GRA: precise and accurate at all times; full, natural range of structures.
- P: full range of features with precision and subtlety; sustained rhythm; effortless to understand.
- Limiting: none; "a clear Band 9".
- Markers: "strikes a chord"; "have a tendency to be exposed to"; "the norm".

### Writing Task 1, Academic (AW, AWCD)

Tasks:
- 1A (AW p. 3): chart of men and women in further education in Britain in three periods, full-time vs part-time.
- 1B (AW p. 4): graph of radio and television audiences across the day in 1992.
- 1C (AW p. 5): diagram of the brick manufacturing process.
- CD Part 1 (AWCD pp. 2-3): [inferred from responses] chart of school trips per year made by children in one country by mode (car, walking, cycling, walking and bus, bus only), 1990 vs 2010.

#### W1-A-CD-resp2: Band 4

- Source: AWCD p. 3 (second Part 1 response). Script text available.
- TA: attempts the task, but key features are not adequately covered; one category (walking and bus) is never mentioned; little detail.
- CC: organisation hard to identify, no clear progression; most cohesive devices are inaccurate.
- LR: not minimally adequate; basic and repetitive; poor spelling control causes confusion.
- GRA: limited range of sentence forms; some accurate structures, but frequent errors impede meaning.
- Markers: "tripe mad" for 'trips made'; "In contrest"; "the children use car".
- Skills: w1.selection, x.spelling, g.sentence-boundaries.

#### W1-A-1A-scriptA: Band 5

- Source: AW p. 9. Task 1A. Script not extractable as text.
- TA: a good attempt at the overall trends, but no figures from the chart are given, so key information is missing.
- CC: quite difficult to follow; punctuation errors cause confusion.
- LR: not addressed in the comment.
- GRA: fairly simple structures; attempts at complex sentences are unsuccessful.
- Markers: "the reader is lacking some important information".
- Skills: w1.data-language, g.sentence-boundaries, g.complex-range.

#### W1-A-1C-scriptA: Band 5

- Source: AW p. 13. Task 1C. Script not extractable as text.
- TA: basic process accurately described, but no overview and some key features not adequately covered; the opening sentence may be an attempted overview but only confuses.
- CC: clear overall progression; effective but mechanical linkers and sequencers; some substitution and referencing; sentences not always well linked.
- LR: minimally adequate; spelling mostly accurate; inappropriate word choices, omissions and word-form errors.
- GRA: some subordination and complex nominalisation attempted; generally limited structures with frequent errors.
- Limiting (examiner): "a good example of a Band 5 performance".
- Markers: "effective, though mechanical, use of linkers and sequencers".
- Skills: w1.overview, x.word-form, g.complex-range.

#### W1-A-1A-scriptB: Band 6

- Source: AW p. 10. Task 1A. Script not extractable as text.
- TA: describes global trends and detailed figures; some information missing and minor inaccuracies.
- CC: flows quite smoothly, but connectives are overused or inappropriate and some points do not link up.
- LR: trend language well handled; problems with expression and word choice.
- GRA: quite good accuracy and structural control, but limited complexity and variety.
- Markers: "connectives are overused or inappropriate".
- Skills: w1.selection, x.cohesion, g.complex-range.

#### W1-A-1B-scriptA: Band 6

- Source: AW p. 11. Task 1B. Script not extractable as text.
- TA: own-words introduction; good coverage of the data with a brief contrast of trends; no overview of the most important features, which the examiner says is needed for a higher content mark (for example the morning radio peak versus the evening TV peak).
- CC: can be followed, but repetitive and cohesive devices are overused.
- LR: some flexibility and precision.
- GRA: long sentences that lack complexity; tense, verb-form and spelling errors interfere slightly.
- Markers: "summarise the most important features of the graph in an overview".
- Skills: w1.overview, x.cohesion, g.tense-aspect.
- [INFERENCE] Overall 6 despite the weak overview implies TA was below the other criteria; per-criterion bands are not published.

#### W1-A-CD-resp1: Band 6

- Source: AWCD p. 2 (first Part 1 response). Script text available.
- TA: the selected key features are covered and highlighted, but reporting is mechanical and figures support only some descriptions; relevant overview in the final paragraph.
- CC: generally coherent with some repetition; cohesive devices effective; clear overall progression.
- LR: enough for some flexibility, with some less common items; a wider range is needed for a higher band.
- GRA: mix of simple and complex sentences, fairly accurate; not enough variety for a higher band.
- Markers: "A striking feature in this chart is"; "There isn't a significant change".
- Skills: w1.data-language, x.less-common-vocab, g.complex-range.

#### W1-A-1B-scriptB: Band 7

- Source: AW p. 12. Task 1B. Script not extractable as text.
- TA: handles both the individual trends and the overall comparison; the opening could add who was studied and when.
- CC: good variety of cohesive devices; easy to follow, although expression is sometimes clumsy.
- LR: varied; errors in word form.
- GRA: complex structures; errors in tense and voice that do not impede communication.
- Markers: "the overall comparison of these trends".
- Skills: x.word-form, g.tense-aspect.

#### W1-A-1C-scriptB: Band 7

- Source: AW pp. 14-15. Task 1C. Script not extractable as text.
- TA: inappropriate format at times (letter-style opening, personal comments) limits TA; process adequately described but with irrelevant information and no clear overview.
- CC: logical organisation, clear progression; range of cohesive devices used appropriately; occasional referencing and linking errors; paragraphing would clarify the stages.
- LR: wide range of sophisticated, precise lexis; occasional word-choice flaws make some expressions awkward.
- GRA: wide range used fluently; most sentences error-free.
- Limiting (examiner): despite high language proficiency, "the flaws in format and organisation limit the rating" to 7.
- Markers: "the letter-style opening and personal comments".
- Skills: w1.overview, x.register, w2.paragraphing.

#### W1-A-1C-scriptC: Band 8.5

- Source: AW pp. 16-17. Task 1C. Script not extractable as text.
- TA: fully satisfies the task; all key features of each stage presented accurately; overview present, but a fuller one summarising the key stages would be needed for the top score.
- CC: very easy to read, seamless cohesion; paragraphing, linking and referencing skilfully managed.
- LR: wide range used with full flexibility and accuracy; sophisticated.
- GRA: wide range, fully flexible and accurate; only rare minor errors.
- Markers: "seven consecutive steps"; "a fuller overview would be needed".
- Skills: w1.overview (even at 8.5 the overview is what stops a 9).

### Writing Task 1, General Training (GTW)

Tasks:
- 1A (GTW p. 3): letter to the college accommodation officer about problems sharing a room; describe the situation, explain the problems, say what accommodation you would prefer.
- 1B (GTW p. 4): letter to the librarian with suggestions; what you like, what you don't like, suggestions for improvement.

#### W1-G-1B-scriptA: Band 3

- Source: GTW p. 10. Task 1B. Script not extractable as text.
- TA: with effort, ideas linked to two bullets can be found; the first bullet is not covered; purpose of the letter unclear; minimal ideas repeated.
- CC: no logical organisation; linkers present but often incorrect.
- LR: inadequate; word-choice and spelling errors impede meaning, some words cannot be deciphered.
- GRA: errors predominate; no correct sentences except those relying on the task wording.
- Limiting (examiner): "a good example of a Band 3 performance".
- Markers: "errors predominate and there are no correct sentences".
- Skills: w1.gt-letter, x.spelling, g.sentence-boundaries.

#### W1-G-1A-scriptA: Band 5.5

- Source: GTW p. 8. Task 1A. Script not extractable as text.
- TA: in letter format and addresses the task; bullet 2 well covered with several problems; repeats task wording; needs more detail, especially for bullet 3; appropriate opening, clear purpose.
- CC: organisation not wholly logical; points not always well linked.
- LR: generally adequate and appropriate.
- GRA: complex structures attempted, but sentences mostly simple; frequent errors cause some difficulty.
- Markers: "there is some repetition of the task rubric".
- Skills: w1.gt-letter, x.paraphrase, g.complex-range.

#### W1-G-1B-scriptB: Band 5.5

- Source: GTW p. 11. Task 1B. Script not extractable as text.
- TA: bullet 1 completely omitted and no closing, so the letter format is incomplete; both reduce TA. The other two bullets are well covered.
- CC: fairly natural, clear progression; paragraphing would help; good range of cohesive devices and referencing.
- LR: range used effectively; noticeable spelling errors that rarely impede.
- GRA: mixed sentence types, many complex attempts; uneven control; punctuation errors.
- Limiting (examiner): higher-level features are present, but the missing bullet and closing "limit the overall rating".
- Markers: "the first bullet point is completely omitted".
- Skills: w1.gt-letter, x.spelling, g.sentence-boundaries.

#### W1-G-1B-scriptC: Band 6

- Source: GTW pp. 12-13. Task 1B. Script not extractable as text.
- TA: all bullets covered, purpose clear, tone assertive but consistently polite; no closing, which affects TA.
- CC: clear overall progression, but the order of ideas inside paragraphs sometimes reduces clarity and some sentences are not fluently linked.
- LR: good range, more than adequate; collocation and word-choice errors alongside accurate choices and modification.
- GRA: mix of simple and complex; errors in punctuation, articles and subject-verb agreement limit this criterion.
- Limiting (examiner): weaknesses in format, organisation and grammatical control limit the rating to 6.
- Markers: "The tone, though assertive, is consistently polite."
- Skills: g.articles, g.agreement, x.collocation.

#### W1-G-1A-scriptB: Band 7

- Source: GTW p. 9. Task 1A. Script not extractable as text.
- TA: relevant; bullets 1 and 2 covered in detail with several problems; bullet 3 could be illustrated more fully (what kind of accommodation, not just a single room).
- CC: logically organised; appropriate linking makes it read quite fluently.
- LR: used well, accurate spelling, some less common words and expressions.
- GRA: more complex structures appear; some errors that do not greatly affect the reader.
- Markers: "borrows"; "having to share".
- Skills: w1.gt-letter (bullet 3 extension).

#### W1-G-1B-scriptD: Band 7

- Source: GTW pp. 14-15. Task 1B. Script not extractable as text.
- TA: strong; appropriate letter format; all bullets clearly presented and illustrated.
- CC: clear throughout; cohesive devices, referencing and substitution used flexibly with occasional error; lack of effective paragraphing prevents the highest CC ratings.
- LR: good range used with some flexibility; less common expressions and awareness of collocation; occasional word form and choice errors.
- GRA: variety of structures, simple and complex; regular errors in articles, prepositions and some verb phrases limit this criterion.
- Limiting (examiner): the density of grammatical error keeps it from "fully satisfying the descriptors of the higher band".
- Markers: "the absence of effective paragraphing".
- Skills: g.articles, g.prepositions, g.verb-form, w2.paragraphing. Articles and prepositions are the classic Indonesian-L1 errors; this anchor shows they can hold an otherwise strong letter at 7.

### Writing Task 2, Academic and General Training (AW, AWCD, GTW)

The Task 2 criteria are identical for both modules, so the anchors are listed together by band.

Tasks:
- A-2A (AW p. 6): children from families with less money are better prepared for adult life than children of wealthy parents; to what extent do you agree or disagree?
- A-2B (AW p. 7): do the disadvantages of international tourism outweigh the advantages?
- A-CD Part 2 (AWCD pp. 4-5): [inferred from responses] opinion essay on whether people's health will improve or get worse in the future.
- G-2A (GTW p. 5): who should pay for the care of old people in care homes, the government or the family?
- G-2B (GTW p. 6): why is shopping so popular, and what effects does its popularity have on individuals and on society?

#### W2-G-2B-scriptA: Band 4

- Source: GTW p. 20. Task G-2B. Script not extractable as text.
- TR: the first question (why shopping is popular) is not addressed; effects on individuals are discussed but not effects on society; main ideas do not relate directly to the question.
- CC: relationships between ideas can be followed, but there is no progression towards answering the question; cohesive devices sometimes wrong, causing repetition.
- LR: some relevant vocabulary, but range inadequate; intrusive spelling errors cause strain.
- GRA: basic structures present; frequent errors in syntax, verb phrases and articles.
- Limiting (examiner): failure to address the task plus vocabulary and grammar weaknesses limit it to 4.
- Markers: "The first part of the task ... is not addressed."
- Skills: w2.task-analysis, x.spelling, g.articles.

#### W2-A-2A-scriptA: Band 4

- Source: AW p. 18. Task A-2A. Script not extractable as text.
- TR: related to the topic, but a confusing introduction makes the position hard to identify; few ideas, with unclear examples.
- CC: no overall progression; ideas not coherently linked; cohesive devices help only minimally.
- LR: basic range, inadequate control; task wording reused inappropriately; frequent word-choice and collocation errors cause severe problems.
- GRA: very limited range; high density of grammar and punctuation errors; rare, very inaccurate subordination.
- Markers: "the test taker's position is difficult to identify".
- Skills: w2.position, x.collocation, g.complex-range.

#### W2-G-2A-scriptA: Band 5

- Source: GTW pp. 16-17. Task G-2A. Script not extractable as text.
- TR: many relevant ideas, but not always developed and sometimes unclear; the writer's view is apparent.
- CC: organisation weak in places; paragraphing does not group ideas around a central topic; still a logical flow of points.
- LR: some appropriate vocabulary, many errors throughout.
- GRA: some complex structures, but sentence control very weak, so parts such as the conclusion are very hard to follow.
- Note (examiner): messy handwritten corrections made the script hard to read; cross out and rewrite cleanly.
- Markers: "sentence control is very weak".
- Skills: x.idea-development, w2.paragraphing, g.sentence-boundaries.

#### W2-A-2B-scriptA: Band 5.5

- Source: AW pp. 23-24. Task A-2B. Script not extractable as text.
- TR: the first five lines are copied from the task and get no credit; relevant position; development unclear in places; some ideas underdeveloped.
- CC: ideas clearly organised with overall progression; some effective cohesion including referencing, but mechanical linkers in places; paragraphs sometimes too short.
- LR: range attempted and adequate, but weak control and frequent spelling errors keep LR down.
- GRA: mix of simple and complex with frequent subordinate clauses; variable control; noticeable errors that rarely impede.
- Limiting (examiner): paragraphing flaws and vocabulary errors limit it to 5.5 despite some higher-band features.
- Markers: "no credit is given for copied rubric".
- Skills: x.paraphrase, x.spelling, w2.paragraphing.

#### W2-A-CD-resp1: Band 5.5

- Source: AWCD p. 4 (first Part 2 response). Script text available.
- TR: clear position from the start with relevant ideas, which need more development; under the 250-word minimum.
- CC: generally coherent with clear progression; cohesive devices effective; paragraphing not always logical.
- LR: range attempted, but imprecise word choice and errors in spelling and word formation; some first-language interference, though meaning stays clear.
- GRA: mix of sentence forms, but too many errors for a higher band.
- Markers: "alimentation habbits"; "inequivoque sintom"; "I completly disagree with the written statment".
- Skills: x.idea-development, x.spelling, x.word-form. Shows the word-count gate and L1-transfer vocabulary together.

#### W2-G-2B-scriptB: Band 6

- Source: GTW pp. 21-22. Task G-2B. Script not extractable as text.
- TR: main parts addressed, but the first (why) is covered more fully than the second (effects); relevant ideas lacking clarity, which prevents a higher band.
- CC: clear overall progression because ideas are logically organised; range of markers used effectively, with errors in some basic connectives.
- LR: attempts a range including less common expressions, with mixed success; some unclear or repetitive expressions; adequate overall.
- GRA: mix of simple and complex; grammar and punctuation errors show limited control but rarely reduce communication.
- Markers: "there is a lack of clarity which prevents a higher band score".
- Skills: w2.task-analysis (balance between parts), x.less-common-vocab, x.cohesion.

#### W2-A-2A-scriptB: Band 6.5

- Source: AW pp. 19-20. Task A-2A. Script not extractable as text.
- TR: arguments generally well developed, appropriate ideas, clear position; the first paragraph and the start of the second are mainly copied from the task; slips into generalisation near the end.
- CC: generally clear progression with a good arrangement of opposing arguments; better paragraphing needed; referencing usually accurate; weaker use of linkers.
- LR: varied, used with some flexibility, including less common and idiomatic phrases; not always precise; reusing task wording shows weak paraphrase.
- GRA: a range of structures, but regular errors (without loss of overall clarity).
- Limiting (examiner): weaknesses in organisation and grammatical control limit it to 6.5.
- Markers: "reveals a lack of ability to paraphrase".
- Skills: x.paraphrase, w2.paragraphing, g.complex-range.

#### W2-A-2B-scriptB: Band 7.5

- Source: AW pp. 25-26. Task A-2B. Script not extractable as text.
- TR: addresses both aspects with a clear position throughout; relevant, well-extended, supported ideas; occasional lapses, such as drifting into solutions to the disadvantages.
- CC: logical, clear progression; range of cohesive devices used effectively; some under-use of connectives and substitution and lapses in referencing.
- LR: wide, flexible, precise; occasional awkward or inappropriate choices do not limit the rating.
- GRA: good range with a high level of accuracy and frequent error-free sentences; minor systematic errors; punctuation unhelpful at times.
- Limiting (examiner): task response and lexical resource are the strengths that make this a good example of 7.5.
- Markers: "present solutions to the disadvantages".
- Skills: w2.task-analysis (staying on the question asked), g.sentence-boundaries.

#### W2-A-CD-resp2: Band 7.5

- Source: AWCD p. 5 (second Part 2 response). Script text available.
- TR: clear position at the outset; ideas explored to support it; an alternative position is considered and rejected.
- CC: logical organisation, clear progression; cohesive devices generally flexible, but sequencers overused in paragraph 2; long paragraphs 2 and 3 could be split.
- LR: wide range with good less common items and hedging (softening); spelling and word-formation errors are rare.
- GRA: variety of complex structures with frequent error-free sentences; some errors; some overuse of short sentences.
- Markers: "They tend to"; "This appears to be because"; "This prevents people to go outside".
- Skills: x.cohesion (sequencer overuse), w2.paragraphing, g.verb-form. Good model of hedging language.

#### W2-G-2A-scriptB: Band 8

- Source: GTW pp. 18-19. Task G-2A. Script not extractable as text.
- TR: analyses the topic from four angles and fully answers the question; ideas relevant and well supported.
- CC: very well organised; easy to read.
- LR: some inaccuracies in word choice, with minimal impact.
- GRA: occasional spelling and grammar errors, which prevent the highest band.
- Markers: "analyses the topic from four different angles".
- Note: the examiner comment is brief; use this anchor for TR and CC more than for LR and GRA detail.

#### W2-A-2A-scriptC: Band 8.5

- Source: AW pp. 21-22. Task A-2A. Script not extractable as text.
- TR: very well addressed and explored in depth; position clear throughout and directly answers the question; ideas well supported, apart from some over-generalisation in the second-to-last paragraph. Not discussing wealthy children is noted but not required.
- CC: very well organised, appropriate paragraphing; sophisticated cohesion with minimal lapses (such as using "e.g." in an essay).
- LR: wide, natural range with full flexibility; many examples of modification, collocation and precise choice.
- GRA: varied, sophisticated syntax; only occasional errors.
- Markers: "a wide and very natural range of vocabulary".

#### W2-G-2B-scriptC: Band 8.5

- Source: GTW pp. 23-24. Task G-2B. Script not extractable as text.
- TR: directly answers the question; each part explored in depth; a personal comment at the end does not relate directly to the question, treated as a minor lapse.
- CC: clear progression; minimal lapses.
- LR: wide range used flexibly and precisely; very rare errors.
- GRA: wide range, flexible and accurate; occasional minor errors or omissions; most structures error-free.
- Markers: "lapses in coherence and cohesion are minimal".

---

## Band boundary cheat-sheet

These are the features that most often separate adjacent bands in the anchors above. Use them for the "why not one higher / one lower" check in Part A step 3.

### Speaking

| Boundary | Lower band shows | Higher band shows | Anchors |
|---|---|---|---|
| 5 / 6 | Answers not extended, or a long turn that loses its topic; vocabulary repeated and personalised; a small set of structures repeated; endings dropped and syllable-timed rhythm cause strain | Willing to speak at length; enough vocabulary for general topics; mix of short and complex forms; generally clear with sensible chunking | S-B5-tina, S-B5-katsuharu vs S-B6-stephen, S-B6-maxim |
| 6 / 7 | Coherence lost through repetition, self-correction or searching for words ("how to say"); collocation errors; errors recur though meaning is clear | Flow without noticeable effort, no coherence loss; less common and idiomatic items with collocation awareness; many error-free sentences; stress and intonation carry meaning | S-B6-stephen, S-B6.5-michal vs S-B7-hendrik, S-B7-alexandra |
| 7 / 8 | Systematic errors (agreement, articles, prepositions); noticeable imprecision; fillers overused; syllable-timing over long turns | Hesitation only for content; precise, stylistically appropriate vocabulary; most sentences error-free, remaining errors non-systematic; accent has minimal effect | S-B7-alexandra, S-B7.5-aashish vs S-B8-monika, S-B8-kopi |
| 8 / 9 | Occasional content hesitation; occasional slight inappropriacy | Hesitation rare; full precision and subtlety in every criterion | S-B8.5-kenn vs S-B9-anuradha |

### Writing Task 1, Academic

| Boundary | Lower band shows | Higher band shows | Anchors |
|---|---|---|---|
| 4 / 5 | A whole category missing; no identifiable organisation; spelling errors confuse | Main trends or stages described; progression visible, even if mechanical | W1-A-CD-resp2 vs W1-A-1A-scriptA, W1-A-1C-scriptA |
| 5 / 6 | No overview, or trends with no figures; complex sentences fail | Overview present (even if in the last paragraph); figures support key features; fairly accurate mixed structures | W1-A-1C-scriptA, W1-A-1A-scriptA vs W1-A-CD-resp1, W1-A-1A-scriptB |
| 6 / 7 | Mechanical reporting; overused connectives; limited structural variety; weak or missing overview | Individual trends plus overall comparison; varied cohesion; complex structures with non-impeding errors | W1-A-1B-scriptA, W1-A-CD-resp1 vs W1-A-1B-scriptB |
| 7 / 8+ | Format problems (letter openings, personal comments), irrelevant detail, no clear overview, even with strong language | Every stage accurate; seamless cohesion; rare errors; an overview that summarises the key stages (a fuller one needed for 9) | W1-A-1C-scriptB vs W1-A-1C-scriptC |

### Writing Task 1, General Training

| Boundary | Lower band shows | Higher band shows | Anchors |
|---|---|---|---|
| 3 / 5.5 | Purpose unclear, a bullet missing, almost no correct sentences | Clear purpose and letter format; most of the task covered | W1-G-1B-scriptA vs W1-G-1A-scriptA |
| 5.5 / 6 | A bullet omitted or barely covered; task wording repeated; frequent errors | All bullets covered with clear purpose and consistently polite tone | W1-G-1B-scriptB, W1-G-1A-scriptA vs W1-G-1B-scriptC |
| 6 / 7 | Missing closing; muddled order inside paragraphs; errors in articles and agreement | Appropriate format; every bullet illustrated with detail; logical, fluent linking; less common expressions | W1-G-1B-scriptC vs W1-G-1A-scriptB, W1-G-1B-scriptD |
| 7 / 8 | Third bullet thin; no paragraphing; regular article, preposition and verb-phrase errors | No GT Task 1 anchor above 7 in these sources; use the band descriptors | W1-G-1A-scriptB, W1-G-1B-scriptD |

### Writing Task 2 (both modules)

| Boundary | Lower band shows | Higher band shows | Anchors |
|---|---|---|---|
| 4 / 5 | Part of the question ignored, or position hard to identify; spelling causes strain | All parts touched; view apparent; logical flow of points | W2-G-2B-scriptA, W2-A-2A-scriptA vs W2-G-2A-scriptA |
| 5 / 6 | Ideas listed but not developed or unclear; copied rubric; under 250 words; paragraphs too short or unfocused; frequent spelling errors | Main parts addressed with relevant ideas; clear progression; adequate vocabulary with control | W2-G-2A-scriptA, W2-A-2B-scriptA, W2-A-CD-resp1 vs W2-G-2B-scriptB |
| 6 / 7 | Unequal coverage of the parts; unclear ideas; task wording reused instead of paraphrased; regular grammar errors | Both or all parts extended and supported; clear position throughout; precise vocabulary with hedging; frequent error-free sentences | W2-G-2B-scriptB, W2-A-2A-scriptB vs W2-A-2B-scriptB, W2-A-CD-resp2 |
| 7 / 8 | Drift away from the question asked; overused sequencers; minor systematic errors; long unbroken paragraphs | Topic analysed from several angles, fully answered; very easy to read; only occasional inaccuracies | W2-A-2B-scriptB, W2-A-CD-resp2 vs W2-G-2A-scriptB |
| 8 / 9 | Some over-generalisation or an off-question personal ending; occasional errors | No published band 9 Task 2 anchor in these sources; use the band descriptors | W2-A-2A-scriptC, W2-G-2B-scriptC |
