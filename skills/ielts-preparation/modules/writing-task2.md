# IELTS Writing Task 2 Coach

Writing Task 2 is the essay paper: one prompt, 40 minutes, at least 250 words, written in connected paragraphs. It counts for about two thirds of the Writing band (double the weight of Task 1), so a half-band gain here moves the Writing score more than the same gain in Task 1. Your job as coach is to get the learner to answer the exact question asked, hold a clear position, and develop each idea far enough to earn the band they are aiming for.

## Scope

Use this module when the learner:
- pastes a Task 2 prompt and wants help planning, drafting, or reviewing an essay;
- submits an essay for a band estimate and feedback;
- asks how to handle a particular question type, write a thesis, build a body paragraph, or finish with a conclusion;
- wants to paraphrase a prompt or stop repeating the same words.

Route elsewhere when the request is about:
- graphs, tables, processes, maps or GT letters: `modules/writing-task1.md`;
- recurring grammar errors as a topic in their own right: `modules/grammar.md`;
- vocabulary building and deck review: `modules/vocabulary.md`;
- Speaking: `modules/speaking.md`.

## How Task 2 is marked

Four criteria, equally weighted: Task Response (TR), Coherence and Cohesion (CC), Lexical Resource (LR), and Grammatical Range and Accuracy (GRA). The band-by-band summary is in `references/band-descriptors.md` (section "Writing Task 2"); grammar detail shared with Speaking is in the section "Grammatical Range and Accuracy (Writing and Speaking)". When `~/.ielts/official/ielts-writing-band-descriptors.pdf` exists, read it for the exact official wording before you commit to a band. Never score from general impression.

What most often decides 6 versus 7:
- **TR:** at 6 every part is addressed but some ideas stay thin or the conclusion drifts; at 7 the position is clear from start to finish and each main idea is extended and supported.
- **CC:** at 6 linking works but feels mechanical or referencing is unclear; at 7 ideas progress logically, each paragraph has one clear focus, and linkers are chosen for meaning.
- **LR:** at 6 the learner tries less common words but with noticeable slips; at 7 less common items are used with awareness of collocation and style.
- **GRA:** at 6 there is a mix of simple and complex sentences with errors that rarely block meaning; at 7 complex structures are frequent and many sentences are error-free.

## The five question types

Identify the type first; it fixes what the essay owes the reader. The default shape is four paragraphs (introduction, two body paragraphs, conclusion), and the thesis always goes in the introduction.

| Type | Typical wording | What the essay must do | Body paragraph split |
|------|-----------------|------------------------|----------------------|
| Opinion | "To what extent do you agree or disagree?", "Is this a positive or negative development?" | Take a stance and keep it; a partial stance ("largely agree") is fine if stated and justified | Two reasons for the stance, or main reasons plus one conceded point that is then answered |
| Discussion | "Discuss both these views and give your own opinion." | Present each view fairly AND state where you stand | View A, then view B; signal your own view in the introduction and confirm it in the conclusion |
| Advantages and disadvantages | "What are the advantages and disadvantages?", "Do the advantages outweigh the disadvantages?" | Cover both sides; if "outweigh" appears, give a judgement | Benefits, then drawbacks; with "outweigh", the weightier side can come second and get more space |
| Problem-solution / cause-solution | "What problems does this cause? What can be done?", "Why is this happening? How can it be addressed?" | Explain the problems or causes, then propose solutions that match them | Problems or causes, then solutions; link each solution back to a named problem |
| Two-part (direct questions) | Two separate questions, e.g. "Why do people do this? Is it a good thing?" | Answer both questions directly, giving each roughly equal weight | One paragraph per question |

Coach notes:
- A discussion essay without the writer's own opinion, or an "outweigh" essay without a verdict, has left part of the task unanswered. Treat that as a TR gate.
- Sitting on the fence is not a position. "It depends" is acceptable only if the essay says what it depends on and stays with that view.
- Two-part prompts sometimes hide the second question in the same sentence ("Why ... and what ..."). Count the question marks and the verbs.

## Workflow

### Step 1 — Dissect the prompt

Before any writing, have the learner answer four questions in one or two lines each:
1. **Type:** which of the five above?
2. **Parts:** what separate things must be answered? Write each one as a question.
3. **Limits:** which words narrow the topic (*in developing countries*, *only*, *young people*, *always*)? An essay that ignores them goes partly off-topic.
4. **Position:** what will the learner argue, in one sentence?

If the learner misses a part or a limiting word, point it out before they plan. For repeated misses, the drill is `prompt-dissection`.

### Step 2 — Plan (about 5 minutes)

A workable plan fits on a few lines:
- the thesis sentence;
- one controlling idea for each body paragraph, phrased as a topic sentence;
- for each controlling idea, the reason it is true and one concrete illustration (a realistic scenario, a consequence, a comparison). Invented statistics are a risk; a specific, plausible case is safer.

Check the plan against Step 1: does every part of the prompt have a home in a paragraph? Is anything in the plan off the question? Fix the plan, not the essay.

Suggested time split for the exam: 5 minutes planning, about 30 minutes writing, 5 minutes checking (articles, plurals, verb endings, and the word count).

### Step 3 — Draft or review

**Drafting.**
- *Introduction (2-3 sentences):* restate the topic in fresh words, then give the thesis. No background essay, no copied prompt; copied wording is not credited.
- *Body paragraphs:* topic sentence, then explanation (why or how), then illustration, then a closing sentence that ties back to the thesis. One controlling idea per paragraph.
- *Conclusion (1-3 sentences):* restate the position and the main reasons. No new arguments.
- *Length:* aim for 260-300 words. Under 250 is penalised; much longer usually means less time for checking, not a higher band.
- *Form:* full prose only. No headings, bullet points, or numbered lists.

Short illustration of an underdeveloped versus a developed point (prompt about four-day working weeks):
- Thin: "A four-day week is good for workers because they are less tired."
- Developed: "A shorter week gives employees a full extra day to recover, so they return on Monday more focused. A nurse on a compressed schedule, for example, is less likely to make a dosing error at the end of a shift. Rested staff therefore protect the quality of the service, not just their own well-being."

**Reviewing a learner's essay.** Work in criterion order, because higher-order problems make lower-order fixes pointless:
1. TR: all parts answered? Position stated, and the same at the end as at the start? Each main idea extended, or just asserted?
2. CC: one focus per paragraph? Logical order? Linkers chosen for meaning, and is every *it / this / they* clear?
3. LR and GRA: repetition, wrong collocations, word-form errors; sentence variety; systematic grammar errors (see the Indonesian-L1 notes below).

### Step 4 — Score and feedback

1. **Learner predicts first.** Before showing any score, ask: "What band do you think you got for TR, CC, LR, GRA?" (one line). Skip only if the user refuses.
2. **Score with the calibration protocol** in `../references/calibration.md`: gates and caps first (word count, every part of the question answered, clear position), then per criterion quote evidence, pick the best-fit descriptor, and check "why not one higher / one lower" against `../references/band-descriptors.md` (section "Writing Task 2"; for exact wording read the official PDF in `~/.ielts/official/` when it exists); compare with the nearest official anchor. Run `python3 scripts/ielts.py status` once per session and, if it flags a coach calibration offset (ADJUST) for a W2 criterion, correct for it and say so.
3. Report:

```
Task Response:        X / 9   (you predicted Y)
Coherence & Cohesion: X / 9   (you predicted Y)
Lexical Resource:     X / 9   (you predicted Y)
Grammatical Range:    X / 9   (you predicted Y)
Estimated overall:    X.X / 9   — estimate, range X.X–X.X if evidence is mixed
```

Where a criterion sits under 7, name two or three concrete changes, each anchored to a sentence quoted from the learner's essay. If the prediction was off by ≥1 band on a criterion, name the descriptor feature they misjudged — that is the self-editing skill being trained.

4. **Tag and log.** Tag each problem with a skill id from `../references/skill-map.json` (`w2.task-analysis`, `w2.position`, `w2.paragraphing`, `x.idea-development`, `x.cohesion`, `x.collocation`, `x.less-common-vocab`, grammar codes such as `ART`, `SVA`, …), then:

```
python3 scripts/ielts.py log --module writing-task2 --task "opinion: remote work" \
  --predicted W2.TR=7 W2.CC=6.5 W2.LR=6.5 W2.GRA=6 \
  --score W2.TR=6 W2.CC=6 W2.LR=6 W2.GRA=5.5 \
  --tag x.idea-development:2 w2.position ART:4 x.collocation:2
```

Add systematic grammar errors to the ledger (`error add --skill <CODE> --example ...`), LR fixes to the vocabulary deck (`vocab add ... --source writing`), and record deck terms used correctly (`vocab used "<term>"`). Close with **one** drill from `../references/drills.md` for the top tag (e.g. `peel-builder`).

### Step 5 — Revise and re-score (when the user resubmits)

Feedback ends with the learner rewriting, not with you rewriting.

1. **Try-fix gate** — list 3–5 weak sentences or missing functions (unclear position, undeveloped main idea, unanswered part of the question). Do not give the fix until the learner has tried, unless they ask for immediate answers.
2. **One criterion per round** — each revision round targets the single criterion furthest below target, in this order: Task Response → Coherence & Cohesion → Lexical Resource + Grammatical Range & Accuracy. Keep the learner's position and ideas; do not swap in a model essay.
3. **Guided edit** — after their attempt, show a micro-edit table `Original | Edit | Why | Tag` with tags `[keep]` `[replace]` `[+add]` `[-trim]`. Edit only what's needed; give a full rewrite only on request.
4. **Re-score against the previous draft** — compare with the earlier draft in the conversation: report per-criterion movement (`TR 6 → 6.5`), which errors returned, which are fixed, and the next criterion to target.
5. **Micro-practice** — up to 3 short exercises on the most frequent problem; the learner answers first, then show the key.

## Language support

Offer these as tools, not templates. Examiners discount memorised stock phrases, and a linker in every sentence is itself a CC weakness.

**Linking by function** (pick one that matches the logic, and vary placement):
- adding a further point: *also, in addition, what is more*
- contrast: *however, yet, whereas, by contrast*
- concession: *although, even though, admittedly ... but*
- consequence: *so, as a result, this means that, which in turn*
- illustration: *for example, for instance, such as, take ... as an example*
- wrapping up: *in conclusion, overall, on balance*

Reference words (*this policy*, *such schemes*, *these workers*) often link better than a linker does.

**Restating the prompt.** Change the structure, not only single words, and keep the meaning exact:
- "Many cities now ban cars from their centres." → "A growing number of urban authorities are closing central districts to private vehicles."
- Keep technical or topic words that have no true synonym (*tax*, *university*, *the internet*); forced synonyms cost LR.

**Stating a position.**
- Direct: *I believe ...*, *In my view ...*, *I largely disagree that ...*
- Weighed: *Although X has some merit, Y matters more because ...*
- Hedged claims inside the argument: *tends to*, *is likely to*, *in many cases*.

## Band-6 traps to flag

1. **Part of the task missing:** usually the own-opinion in a discussion essay or the second question in a two-part prompt.
2. **Position that shifts:** agrees in the introduction, balances in the body, half-disagrees in the conclusion.
3. **Listing instead of developing:** three reasons in one paragraph, none explained. Two developed ideas beat four bare ones.
4. **Over-general claims:** "Everyone knows technology destroys families." Ask for a reason, a limit, or an illustration.
5. **Mechanical linking:** *Firstly / Secondly / Moreover / Furthermore* at the start of every sentence while the logic between ideas is unclear.
6. **Memorised openers and closers** that could fit any prompt ("In this modern era, ..."). They add words without adding an answer.
7. **Short essay:** under 250 words; check the count before scoring.
8. **Copied prompt wording** in the introduction, or note-style bullets anywhere.

## Indonesian-L1 notes for Task 2

Task 2 topics are abstract (education, environment, technology, society), which exposes predictable transfer errors. Name the contrast when you correct them; details and ledger codes are in `references/grammar-error-taxonomy.md`, and re-test routines in `references/grammar-practice-and-reprobe.md`.
- **Articles (`ART`):** general abstract nouns take no article (*Education is ...*, not *The education is ...*), but specific ones do (*the education system in Indonesia*). Singular countable nouns need *a/the* (*a government*, not *government* alone).
- **Plurals and countability (`NUM`):** *many country*, *some problem*; uncountables used as plurals (*informations*, *advices*, *researches*).
- **Agreement (`SVA`):** *the number of students increase*, *technology make*; *people* is plural.
- **Tense in examples (`TENSE`):** a past illustration needs past forms (*Last year my city introduced ...*), not present.
- **Paired connectors (`CONJ`):** *Although ..., but ...* and *Because ..., so ...* copy *walaupun ..., tetapi* and *karena ..., maka*; keep one connector.
- **Word form (`WF`):** *economy* vs *economic*, *success* vs *successful*, *develop* vs *development*.

## Output formats

**Model essay** (only on request, or after the learner has attempted their own): write an original essay for the learner's prompt, label the paragraphs (Introduction, Body 1, Body 2, Conclusion), give the word count, then add a short note on why the structure fits the question type and which language choices the learner could borrow.

**Feedback on the learner's essay:** quote the original wording for each issue and show an improved version of that sentence; then the score block from Step 4; then the top three priorities for the next essay, in criterion order.
