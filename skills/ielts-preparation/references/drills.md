# Drills Catalog

Short, high-repetition drills (5-15 min each), one per drill id in `skill-map.json`. Each drill trains one or more micro-skills; the skill ids under **Trains** are the ids to tag when logging. Run all CLI commands from the skill root (`python3 scripts/ielts.py ...`).

## Session protocol (15-25 min)

1. **Warm-up (3-8 min):** `python3 scripts/ielts.py due`. Run `vocab-review` on the due items (cap at 15). If nothing is due, skip.
2. **One drill (8-15 min):** `python3 scripts/ielts.py status`, pick the drill with the rule below, and run one round at the level `status` shows for it (`<id> L<level> <last pct>`; a drill not yet listed starts at L1).
3. **Log (1 min):** one `log` line for the round (exact lines are in each section). Add any new word or collocation the drill exposed with `vocab add`.
4. **Takeaway (1 line):** the learner writes one sentence: what they will do differently next time ("Check for a plural -s after every number").

Do not stack three drills in one session. One drill done well, logged, beats a long mixed session.

## Choosing a drill

- Default: run the drill named at the end of the top-leverage line in `status` (`next: <drill> (L<level>)`), at that level.
- If choosing by hand: pick the **highest-leverage skill** from `status`, then take that skill's **first drill in skill-map order that is not yet in maintenance**. If all its drills show `maint`, move to the next skill.
- Prefer items built from the learner's own past errors (the `due` list, tagged lost marks in `status`, sentences from their essays and transcripts). Fill the rest of the round with original items.

## Interleaving

Once a skill's drill shows **L3 or `maint`** in `status` (it has mastered L2), stop running that drill in isolation. Mix its items with items from 1-2 other drills of the same paper that are also at L3 or `maint` (e.g. `tfng-decision` + `heading-match` + `completion-grammar-fit` for Reading; `overview-sprint` + `trend-sentence` for Writing Task 1). The learner must first decide what kind of item it is, which is what the real test demands. Log each drill id in the mixed round on its own line, with its own correct/total.

## Rules for every drill

- **Item generation:** write ORIGINAL items. Never copy Cambridge or official test material; short quoted phrases (< 15 words) from the learner's own pasted work are fine.
- **Production over recognition:** the learner writes, says, or corrects something; a bare letter choice is never enough on its own (ask for the deciding words or a reason).
- **Feedback:** one item at a time. The learner attempts first; then the coach gives a one-line verdict + fix + rule. No key before the attempt; no batch of answers at the end.
- **Ladder:** L1 guided/cued -> L2 independent -> L3 timed or interleaved. Where a drill uses a worked example, fade it: full worked example at L1, partly completed at L2, none at L3.
- **Mastery and levels are tracked by the CLI, not the coach.** Each `log --module drill --drill ID --correct N --total M` stores the session percentage against that drill's current level. Default rule: >= 80% in 2 consecutive sessions moves the drill to the next level; after L3 it moves to **maintenance** (`<id> maint` in `status`): one interleaved round a week. Read the level from `status` before every drill; never set or change it by hand (there is no level flag).
- **Logging:** `--correct` = items fully correct; `--total` = items attempted. Tag every skill the round trained as `--tag <skill-id>:<items lost on that skill>` (use `:0` when none were lost). When the drill trains several skills, split the lost items between their tags.
- **Indonesian L1:** where an item targets a known transfer error, give the L1 reason in one clause in the feedback line.

## Optional audio with macOS `say`

Listening and pronunciation drills can use the built-in voices: `Daniel` (UK), `Karen` (Australia), `Moira` (Ireland), `Samantha` (US). IELTS Listening uses a range of native-speaker accents, so rotate voices.

```bash
say -v Daniel -r 160 "The coach leaves at quarter to seven from Platform 13."
say -v Karen -r 150 "Number one. [[slnc 2000]] Fifteen pounds fifty."   # [[slnc ms]] inserts a pause
say -v Daniel -r 160 -f /tmp/items.txt                                   # read items from a file
```

- `-r` is words per minute: about 140 at L1, 160 at L2, 180-190 at L3.
- The command text is visible in the tool log; ask the learner to look away or keep the tool output collapsed until they have answered.
- Audio is optional. Without it, the coach reads nothing aloud: the learner works from text, which trains strategy but not the ear; say so in the takeaway.
- Synthetic voices reduce and link words less than real speakers. For connected-speech work at L3, use a real recording the learner has a transcript for (for example BBC Learning English episodes, which publish transcripts).

## Speaking drills in a text chat

The coach cannot hear the learner. Speaking drills run as: speak aloud with a timer, record (phone voice memo or macOS Voice Memos), then paste an automatic transcript (phone or macOS dictation) plus the recorded duration. Dropped endings and wrong sounds often show up as transcription errors ("I work yesterday"); treat that as a useful proxy, not proof.

---

## Cross-paper skills

### paraphrase-match — Paraphrase Match

- **Trains:** `x.paraphrase`
- **Format:** 8 items, 8 min. The learner reads a short text and, for each question phrase, writes the exact words in the text that express the same meaning.
- **How to generate items:** write a 120-180-word passage or a 6-line dialogue transcript on an IELTS-type topic. Write 8 question phrases, each a paraphrase of one text phrase using a different technique: synonym (`expensive` -> `costly`), word form (`the cost rose` -> `an increase in price`), structure (active -> passive), and generalisation (`buses and trains` -> `public transport`). Recycle phrases the learner missed in past Listening/Reading errors tagged `PARA`.
- **Feedback rule:** after each answer: correct/incorrect + the matching text words + the technique used, in one line.
- **Ladder:** L1 the technique is labelled beside each question. L2 no labels, untimed. L3 6 min, and two items are traps where the text uses the same word with a different meaning; the learner must reject the word match.
- **Score & log:** correct = the quoted words fully cover the paraphrased meaning (not just a shared word).
  `python3 scripts/ielts.py log --module drill --drill paraphrase-match --correct 7 --total 8 --tag x.paraphrase:1`
- **Mastery:** default.

### paraphrase-produce — Paraphrase Produce

- **Trains:** `x.paraphrase`
- **Format:** 6 items, 10 min. The learner rewrites a sentence without reusing its key content words.
- **How to generate items:** use Task 1/Task 2 prompt sentences (original ones), Speaking questions, or sentences from the learner's own writing where they copied prompt words. Mark the 2-3 key words to change.
- **Feedback rule:** one line per item: is the meaning kept, which key word was still copied, a better option if one exists.
- **Ladder:** L1 the coach names the technique (synonym / word form / structure) and shows one full worked example: `The graph shows the number of tourists` -> `The line graph illustrates how many people visited`. L2 the learner chooses the technique; the worked example is half done (`The chart compares...` -> `The bar chart ___ the ___ of ...`). L3 two different paraphrases per item in 90 seconds each, no example.
- **Score & log:** correct = meaning unchanged, key words changed, grammar correct, natural.
  `python3 scripts/ielts.py log --module drill --drill paraphrase-produce --correct 5 --total 6 --tag x.paraphrase:1`
- **Mastery:** default.

### collocation-fix — Collocation Fix

- **Trains:** `x.collocation`, `g.prepositions`
- **Format:** 8 items, 8 min. The learner rewrites each sentence with the natural collocation or dependent preposition.
- **How to generate items:** start from the learner's `WC`, `COLL`, and `PREP` errors; otherwise write sentences with one miscollocation each: `do a mistake`, `make a research`, `strong rain`, `discuss about`, `depend of`, `interested about`, `rose until 40%`. Cover verb+noun, adjective+noun, and verb+preposition.
- **Feedback rule:** one line: the natural form + a second example of it. Indonesian L1 note where it fits (`tergantung dari` -> `depend of/from`; `berdiskusi tentang` -> `discuss about`).
- **Ladder:** L1 the wrong word is underlined. L2 the learner finds and fixes the error. L3 production: given a node word (`decision`, `impact`, `rate`), write a correct sentence on an IELTS topic with a strong collocation (e.g. `have a significant impact on`), 60 seconds each.
- **Score & log:** correct = natural collocation and correct preposition. Split lost items by tag.
  `python3 scripts/ielts.py log --module drill --drill collocation-fix --correct 6 --total 8 --tag x.collocation:1 g.prepositions:1`
  Add each missed collocation: `python3 scripts/ielts.py vocab add --term "make a decision" --meaning "decide" --example "The council made a decision to close the road." --source collocation-fix --skill x.collocation`
- **Mastery:** default.

### word-family-ladder — Word Family Ladder

- **Trains:** `x.word-form`
- **Format:** 8 gaps, 8 min. The learner writes the right form of a given root in each gap.
- **How to generate items:** pick roots from the learner's `WF` errors or Academic Word List families (`economy, economic, economical, economically, economist`; `compete, competition, competitive, competitively`; `vary, variety, various, variation`). Write one sentence per gap where the grammar forces the form (after an article -> noun; before a noun -> adjective; modifying a verb -> adverb).
- **Feedback rule:** one line: the form + the grammar clue that decides it. Indonesian L1 note where relevant: Indonesian affixes (pe-, ke-an, -kan) do not map onto English suffixes, so learn the whole family.
- **Ladder:** L1 the needed part of speech is printed under the gap. L2 no cue. L3 rewrite whole sentences changing the form (`The economy grew rapidly` -> `There was rapid economic growth`), 6 items, 60 seconds each.
- **Score & log:** correct = right form and spelling.
  `python3 scripts/ielts.py log --module drill --drill word-family-ladder --correct 7 --total 8 --tag x.word-form:1`
- **Mastery:** default.

### spelling-dictation — Spelling Dictation

- **Trains:** `x.spelling`, `l.numbers`
- **Format:** 10 items, 6 min. The learner writes each word or spelled-out name as heard.
- **How to generate items:** words from the learner's `SPELL` errors and `due` list first; then high-frequency Listening/Writing words (`accommodation`, `environment`, `government`, `necessary`, `Wednesday`, `February`, `library`, `restaurant`, `questionnaire`, `temperature`). For names, spell letter by letter as in Listening Part 1 (`That's H-A-R-G-R-E-A-V-E-S`), including `double L`. Optional audio: `say -v Karen -r 140 "Accommodation. [[slnc 3000]] The surname is, H, A, R, G, R, E, A, V, E, S."`
- **Feedback rule:** one line: the correct spelling + the trap (double letter, silent letter, vowel). Indonesian L1 note: Indonesian letter names differ (Indonesian `e` sounds like English `A`, `i` like English `E`, `g`/`j` like English `J`/`G`), so A/E/I and G/J are the usual confusions.
- **Ladder:** L1 words only, slow (-r 130), each said twice. L2 words + spelled names, -r 160, once. L3 words inside a full sentence at -r 180, answer written straight into a gap.
- **Score & log:** correct = exact spelling (British or American spelling both accepted in IELTS; capitals not required). Tag names/codes as `l.numbers`, words as `x.spelling`.
  `python3 scripts/ielts.py log --module drill --drill spelling-dictation --correct 8 --total 10 --tag x.spelling:1 l.numbers:1`
- **Mastery:** default. Misspelt words go to `vocab add ... --skill x.spelling`.

### plural-gap-check — Plural Gap Check

- **Trains:** `x.plural`
- **Format:** 10 items, 6 min. Completion gaps where the learner writes the noun in the correct form, plus a self-check of a short text.
- **How to generate items:** gaps after numbers, quantifiers, and `one of the` (`three ___ (bedroom)`, `a number of ___`, `one of the main ___`, `much ___ (information)`), and completion-style gaps where only the plural fits the sentence (`Visitors should bring their own ___`). Include uncountables (`advice`, `equipment`, `research`) as boundary cases. Reuse the learner's lost Listening/Reading answers tagged `NUM`/`PLURAL`.
- **Feedback rule:** one line: the form + the clue (number, quantifier, verb agreement). Indonesian L1 note: Indonesian does not mark plural after a number (`tiga kamar`), so add the -s on purpose.
- **Ladder:** L1 the clue word is bolded. L2 no cue. L3 a 60-80-word text with 6 hidden number/countability errors to find and fix in 3 minutes.
- **Score & log:** correct = right number form and spelling.
  `python3 scripts/ielts.py log --module drill --drill plural-gap-check --correct 9 --total 10 --tag x.plural:1`
- **Mastery:** default.

### peel-builder — PEEL Builder

- **Trains:** `x.idea-development`
- **Format:** 3-4 points, 12 min. For each given point the learner writes Point - Explain - Example - Link (4 sentences).
- **How to generate items:** take bare one-line points from the learner's own essays or GT letter bullets; otherwise write Task 2 points (`Public transport should be free because it reduces traffic`).
- **Feedback rule:** one line per point: which move is missing or weak (explanation that only repeats the point; example that is not specific).
- **Ladder:** L1 full worked example first (P: Free buses would reduce congestion. E: Many commuters drive only because fares are high, so removing fares makes the bus the cheaper option. E: When Tallinn made public transport free for residents in 2013, ridership rose. L: Therefore, fare-free transport directly targets the cause of traffic.), then the learner writes. L2 P and E are given; the learner writes Example and Link. L3 no scaffold; 3 minutes per point.
- **Score & log:** correct = all four moves present, the example is specific (a place, group, number, or realistic case), and the link returns to the question.
  `python3 scripts/ielts.py log --module drill --drill peel-builder --correct 3 --total 4 --tag x.idea-development:1`
- **Mastery:** default.

### cohesion-repair — Cohesion Repair

- **Trains:** `x.cohesion`
- **Format:** 6 items, 10 min. The learner rewrites short passages so linking and referencing are clear and natural.
- **How to generate items:** 2-4-sentence passages, one fault each: double connector (`Although it is cheap, but...`), wrong logical linker (`Moreover` for a contrast), mechanical overuse (`Firstly... Secondly... Moreover... Furthermore...` on every sentence), unclear `this/it/they`, repetition that a pronoun or `such` + noun should fix. Use the learner's `CONJ`/`COH` sentences first.
- **Feedback rule:** one line: the fault + the repaired version. Indonesian L1 note for double connectors: it copies `Meskipun..., tetapi...`; English uses one of the two.
- **Ladder:** L1 the fault type is named. L2 not named. L3 a 120-word paragraph with 4 mixed faults, 5 minutes.
- **Score & log:** correct = fault fixed without adding a new one.
  `python3 scripts/ielts.py log --module drill --drill cohesion-repair --correct 5 --total 6 --tag x.cohesion:1`
- **Mastery:** default.

### register-switch — Register Switch

- **Trains:** `x.register`, `w1.gt-letter`
- **Format:** 8 items, 8 min. The learner rewrites a sentence into a target register (formal, semi-formal, informal).
- **How to generate items:** sentences from GT letters and essays: `I wanna complain about the noise` -> formal; `I am writing to inform you that I shall be unable to attend` -> informal for a friend; contractions, phrasal verbs (`put up with` -> `tolerate`), slang, and over-formal phrases in a friendly letter. Include opening/closing pairs: formal `Dear Sir or Madam` - `Yours faithfully`; named formal `Dear Mr Lee` - `Yours sincerely`; informal `Dear Anna` - `Best wishes`.
- **Feedback rule:** one line: register verdict + one improved version.
- **Ladder:** L1 the target register and the words to change are marked. L2 only the target register is given. L3 a GT prompt is given and the learner writes the opening line, the purpose sentence, and the closing in the right register in 2 minutes; 4 prompts.
- **Score & log:** correct = consistent register for the reader, meaning kept. Tag letter-specific items `w1.gt-letter`.
  `python3 scripts/ielts.py log --module drill --drill register-switch --correct 7 --total 8 --tag x.register:1 w1.gt-letter:0`
- **Mastery:** default.

### upgrade-the-word — Upgrade the Word

- **Trains:** `x.less-common-vocab`
- **Format:** 8 items, 10 min. The learner replaces a plain word with a more precise, less common word or collocation AND writes when it would be wrong.
- **How to generate items:** take common words from the learner's essays and transcripts (`big problem`, `very important`, `a lot of people`, `good effect`, `bad`). Each item is the learner's sentence with one word marked.
- **Feedback rule:** one line: precise / imprecise + why. Penalise "fancy" words used imprecisely (`a plethora of crime`): descriptors reward precision, not rarity.
- **Ladder:** L1 the coach offers three candidates (one correct, one wrong register, one wrong meaning); the learner picks and then writes a new sentence with it. L2 no candidates. L3 rewrite a 60-word paragraph upgrading 3 words of the learner's choice, 4 minutes.
- **Score & log:** correct = precise meaning, right collocation, right register.
  `python3 scripts/ielts.py log --module drill --drill upgrade-the-word --correct 6 --total 8 --tag x.less-common-vocab:2`
  Keep each good upgrade: `vocab add --term "a pressing issue" ... --skill x.less-common-vocab`.
- **Mastery:** default.

### vocab-review — Spaced Vocabulary Review

- **Trains:** `x.collocation`, `x.spelling`, `x.less-common-vocab`
- **Format:** all items from `python3 scripts/ielts.py due` (cap 15), 5-10 min. Production first: the learner produces the word, then uses it.
- **How to generate items:** for each due item, present ONE cue, rotating cue types across sessions: the English meaning, an Indonesian gloss, or a gap sentence (`The government should ___ ___ ___ the housing shortage.` -> `take steps to tackle`). Never show the term itself.
- **Feedback rule:** after each item: pass/fail + the correct term + the stored example. Then the learner writes one NEW sentence using it (not the stored example); fix it in one line.
- **Ladder:** L1 first letter and word count given. L2 cue only. L3 the learner uses two due items in one sentence on an IELTS topic.
- **Score & log:** pass = term produced with correct spelling AND the new sentence uses it naturally; anything else = fail. Record each item immediately:
  `python3 scripts/ielts.py review ITEM_ID pass` / `python3 scripts/ielts.py review ITEM_ID fail`
  Then one line for the session, tags split by item skill:
  `python3 scripts/ielts.py log --module drill --drill vocab-review --correct 11 --total 13 --tag x.collocation:1 x.spelling:1 x.less-common-vocab:0`
- **Mastery:** default (levels advance through `log`); item scheduling is handled separately by `review`. The drill stays the daily warm-up even in maintenance.

---

## Listening

### signpost-tracking — Signpost Tracking

- **Trains:** `l.locate`
- **Format:** one 150-250-word monologue or dialogue + 6-8 questions in order, 8 min. The learner writes each answer AND the signpost phrase that came just before it.
- **How to generate items:** write an original Part 2/Part 4-style script with clear signposts (`Moving on to...`, `The second point is...`, `As for the café...`, `Finally...`). Play with `say -v Daniel -r 160 -f /tmp/script.txt`, or without audio show the script one sentence at a time.
- **Feedback rule:** one line per question: answer + the signpost the learner should have used to know the question had arrived.
- **Ladder:** L1 the signposts are printed beside the questions. L2 no printed signposts. L3 -r 180, and the answer to one question is deliberately very short; the learner must notice the next signpost, abandon the missed question, and keep going (real tests do not pause).
- **Score & log:** correct = right answer for that question (spelling must be right).
  `python3 scripts/ielts.py log --module drill --drill signpost-tracking --correct 6 --total 8 --tag l.locate:2`
- **Mastery:** default.

### distractor-spotting — Distractor Spotting

- **Trains:** `l.distractor`, `l.attitude`
- **Format:** 8 mini-exchanges, 8 min. The learner writes the FINAL answer and the signal words that changed it.
- **How to generate items:** 2-4-line exchanges with one correction, rejection, or change of mind: `The meeting's on Tuesday - oh no, sorry, it moved to Thursday`; `We considered the museum, but it's closed on Mondays, so let's do the gallery`. For `l.attitude`, Section 3-style two-speaker items: suggestion vs agreed decision, who agrees with whom (`A: Shall we survey students? B: Hmm, a bit slow. Interviews?` `A: Fair enough.`). Use two voices to separate speakers: `say -v Daniel -r 160 "..."` then `say -v Karen -r 160 "..."`.
- **Feedback rule:** one line: final answer + the signal (`actually`, `sorry`, `no, wait`, `in the end`, `that's a better idea`).
- **Ladder:** L1 printed transcript, untimed. L2 audio or one-time reveal, answer within 10 seconds. L3 -r 180, mixed with `signpost-tracking` items.
- **Score & log:** correct = final answer AND signal words. Tag decision/agreement items `l.attitude`, corrections `l.distractor`.
  `python3 scripts/ielts.py log --module drill --drill distractor-spotting --correct 6 --total 8 --tag l.distractor:1 l.attitude:1`
- **Mastery:** default.

### number-dictation — Number Dictation

- **Trains:** `l.numbers`
- **Format:** 10 items, 5 min. The learner writes each number, date, time, price, phone number, or postcode as heard.
- **How to generate items:** mix `13/30`, `15/50`, `16/60` pairs; prices (`£15.50`, `$1,250`); dates (`the 22nd of March`); times (`quarter to seven`, `18:45`); phone numbers with `double five` and `oh`; postcodes (`CB2 8RF`). Optional audio: `say -v Daniel -r 160 "The fee is fifteen pounds fifty. [[slnc 3000]] My number is oh seven seven, double five, three nine one."`
- **Feedback rule:** one line: the correct form + the cue (teen numbers have stress on the end: thir-TEEN; tens on the start: THIR-ty).
- **Ladder:** L1 bare numbers, -r 140. L2 numbers in sentences, -r 160. L3 a speaker gives one number and then corrects it (combine with `distractor-spotting`), -r 180.
- **Score & log:** correct = exact value in an accepted format. Digits are fine; common date formats (`22 March`, `March 22`, `22nd March`) are normally accepted; avoid all-numeric dates like `22/3`.
  `python3 scripts/ielts.py log --module drill --drill number-dictation --correct 9 --total 10 --tag l.numbers:1`
- **Mastery:** default.

### direction-follow — Direction Follow

- **Trains:** `l.map`
- **Format:** one plan + 6-8 locations, 8 min. The learner writes the letter for each place described.
- **How to generate items:** draw an ASCII plan (a grid with an entrance, a compass `N` arrow, a path, and letters A-H on unnamed buildings). Write directions from a fixed starting point: `As you come in through the main gate, the gift shop is immediately on your left`, `opposite`, `beyond`, `in the north-east corner`, `at the end of the corridor`, `between X and Y`. Optional audio for the directions with `say`.
- **Feedback rule:** one line: correct letter + the phrase that fixed the position.
- **Ladder:** L1 the starting point and facing direction are marked on the plan. L2 not marked; the first sentence states it. L3 the learner writes directions to 3 places the coach chooses, then answers 5 coach items within the time of one hearing.
- **Score & log:** correct = right letter; at L3 also = the learner's own directions lead to the right place.
  `python3 scripts/ielts.py log --module drill --drill direction-follow --correct 7 --total 8 --tag l.map:1`
- **Mastery:** default.

### chunk-dictation — Chunk Dictation

- **Trains:** `l.connected-speech`
- **Format:** 6-8 sentences of 8-14 words, 8 min. The learner writes every word.
- **How to generate items:** original sentences packed with weak forms (`to`, `of`, `and`, `can`, `was`, `for`), linking (`turn it off`), elision (`next day`, `last week`), and contractions (`would've`, `there's been`). Optional audio: `say -v Karen -r 170 "We should've asked for a bit of extra time to finish it off."` At L3 use a 30-60-second real clip the learner has a transcript for.
- **Feedback rule:** one line: the missed chunk + what made it hard (e.g. `of` became /ə/). Indonesian L1 note: Indonesian rarely links a final consonant to the next vowel or reduces vowels, so short function words are the ones lost.
- **Ladder:** L1 the sentence plays twice, -r 150, with the number of words given. L2 once, -r 170. L3 a real recording, 2 plays.
- **Score & log:** correct = whole sentence word-perfect (minor spelling slips count; missing words do not).
  `python3 scripts/ielts.py log --module drill --drill chunk-dictation --correct 5 --total 8 --tag l.connected-speech:3`
- **Mastery:** default.

### word-limit-check — Word Limit Check

- **Trains:** `l.format`, `r.completion`
- **Format:** 10 items, 6 min. The learner writes an answer that fits the instruction and the gap, or fixes an invalid one.
- **How to generate items:** pair an instruction (`ONE WORD ONLY`, `NO MORE THAN TWO WORDS AND/OR A NUMBER`, `NO MORE THAN THREE WORDS`) with a source sentence and a gap. Mix in candidate answers that break the limit (`the old library` for ONE WORD), drop a needed part of a number (`15` for `15 kg` when the unit is not printed), or use an article that pushes the count over. Rules: hyphenated words count as one word; a number written in digits counts as a number; answers must be spelled correctly; in Reading, completion answers come from the passage unless a word box is given.
- **Feedback rule:** one line: valid/invalid + the count.
- **Ladder:** L1 the instruction is underlined and the learner counts aloud. L2 normal. L3 mixed with `completion-grammar-fit` items, 30 seconds each.
- **Score & log:** correct = fits limit, grammar, and spelling. Tag Listening items `l.format`, Reading items `r.completion`.
  `python3 scripts/ielts.py log --module drill --drill word-limit-check --correct 9 --total 10 --tag l.format:1 r.completion:0`
- **Mastery:** default.

---

## Reading

### tfng-decision — TFNG Decision

- **Trains:** `r.tfng`
- **Format:** 8 statements, 8 min. The learner writes TRUE/FALSE/NOT GIVEN (or YES/NO/NOT GIVEN) and quotes the deciding words, or writes `no information about <X>` for Not Given.
- **How to generate items:** write a 3-5-sentence original passage (~80 words) and 6-8 statements: some exact paraphrases (TRUE), some contradictions (FALSE), some on the topic but not addressed (NOT GIVEN). Build traps around qualifiers (`all/some`, `always/often`, `only`, `the first`), comparatives, and cause vs correlation. YNNG items use a writer's claims (`The author believes...`).
- **Feedback rule:** one line: verdict + the deciding words. FALSE needs a contradiction in the text; NOT GIVEN means the text says nothing either way. Never use outside knowledge.
- **Ladder:** L1 the sentence that holds the answer is numbered for each statement. L2 no pointer. L3 a 250-word passage, 7 statements in 6 minutes, with YNNG items mixed in.
- **Score & log:** correct = right verdict AND valid evidence.
  `python3 scripts/ielts.py log --module drill --drill tfng-decision --correct 7 --total 8 --tag r.tfng:1`
- **Mastery:** default.

### heading-match — Heading Match

- **Trains:** `r.headings`
- **Format:** 5 paragraphs, 10 min. The learner first writes a 5-8-word gist for each paragraph, then picks a heading.
- **How to generate items:** write 5 original paragraphs (80-120 words) on one topic, plus 7-8 headings: one correct per paragraph and 2-3 distractors that match a detail or repeat a word from a paragraph without covering it.
- **Feedback rule:** one line: correct heading + why the distractor only covers a detail.
- **Ladder:** L1 the learner sees one full worked example (gist -> heading -> why the distractor fails) and the topic sentence of each paragraph is bolded. L2 gist then heading, no bolding. L3 heading only, 60 seconds per paragraph, 8 distractor-heavy headings.
- **Score & log:** correct = right heading (gist is required at L1-L2 but not scored).
  `python3 scripts/ielts.py log --module drill --drill heading-match --correct 4 --total 5 --tag r.headings:1`
- **Mastery:** default.

### scan-race — Scan Race

- **Trains:** `r.scan`
- **Format:** 8 items, 4-5 min. The learner finds names, dates, numbers, and "which paragraph contains..." information and writes the answer + paragraph letter.
- **How to generate items:** write a 300-400-word original text in lettered paragraphs, dense with names, dates, and figures. Write questions that paraphrase the target (`the year the scheme was extended` for `In 2009 the programme was expanded`). Include 2 matching-information items (`a reference to an unexpected cost`).
- **Feedback rule:** one line: answer + paragraph + the scan anchor (capital letter, number, or a key noun's synonym).
- **Ladder:** L1 the learner underlines the scan anchor in each question first, 6 minutes. L2 4 minutes. L3 3 minutes, with 3 matching-information items whose answers are not in order.
- **Score & log:** correct = right answer and paragraph within the time; unanswered = wrong.
  `python3 scripts/ielts.py log --module drill --drill scan-race --correct 6 --total 8 --tag r.scan:2`
- **Mastery:** default; unanswered items count as wrong, so the time box is built into the percentage.

### completion-grammar-fit — Completion Grammar Fit

- **Trains:** `r.completion`
- **Format:** 8 gaps, 8 min. Before answering, the learner predicts each gap's word class (and singular/plural); then fills it from the text.
- **How to generate items:** write a 150-200-word passage and an 80-word summary that paraphrases it with 8 gaps; for some gaps the nearest text word has the wrong form (`develop` in the text, a noun needed in the gap).
- **Feedback rule:** one line: answer + whether the prediction was right + the grammar clue (`an ___` -> singular noun starting with a vowel sound).
- **Ladder:** L1 worked example for gap 1 (prediction, location, answer). L2 the prediction for gap 1 only is given. L3 no prediction step written; 5 minutes; a word box with extra distractor words replaces the text for half the items.
- **Score & log:** correct = right word, fits the gap grammatically, within the limit, spelled correctly.
  `python3 scripts/ielts.py log --module drill --drill completion-grammar-fit --correct 6 --total 8 --tag r.completion:2`
- **Mastery:** default.

### mcq-eliminate — MCQ Eliminate

- **Trains:** `r.mcq`
- **Format:** 4 questions x 4 options, 8 min. The learner chooses AND writes a 3-6-word reason for rejecting each wrong option.
- **How to generate items:** write a 200-word passage (or a short dialogue for Listening practice) and, per question, four options built to type: one correct paraphrase, one word-match trap (same words, wrong meaning), one true-but-does-not-answer-the-question, one contradicted or not mentioned.
- **Feedback rule:** one line per question: answer + which trap each wrong option was.
- **Ladder:** L1 the trap types are listed and the learner labels each option. L2 reasons in own words. L3 5 questions in 6 minutes, reasons only for the option they almost chose.
- **Score & log:** correct = right answer AND valid reasons for the rejected options.
  `python3 scripts/ielts.py log --module drill --drill mcq-eliminate --correct 3 --total 4 --tag r.mcq:1`
- **Mastery:** default.

### timed-passage — Timed Passage

- **Trains:** `r.timing`
- **Format:** an original passage with mixed question types; the learner records the minute they finish each question group. This is the only drill that can run beyond 15 minutes (at L3).
- **How to generate items:** write an original passage at Academic (or GT Section 3) level with 3 question types from the learner's practised drills. Real tests give 60 minutes for 3 passages and 40 questions, with no extra time to transfer answers, so the working pace is about 20 minutes per passage.
- **Feedback rule:** after the whole set (this drill is the exception to per-item feedback): one line per wrong answer + one line on pacing (which group overran, where to skip and return).
- **Ladder:** L1 400 words, 7 questions, 10 minutes, with a 5-minute checkpoint. L2 400 words, 7 questions, 9 minutes, no checkpoint. L3 800 words, 13 questions, 20 minutes, then 17 minutes.
- **Score & log:** correct = right answers within the time; unanswered = wrong. Tag `r.timing` with the unanswered count and each question type with its errors.
  `python3 scripts/ielts.py log --module drill --drill timed-passage --correct 10 --total 13 --tag r.timing:1 r.tfng:1 r.headings:1`
- **Mastery:** default; unanswered items count as wrong, so the time box is built into the percentage.

---

## Writing Task 1

### overview-sprint — Overview Sprint

- **Trains:** `w1.overview`
- **Format:** 6-8 visuals, 2 minutes each. The learner writes a 1-2-sentence overview with no specific figures.
- **How to generate items:** invent small datasets as text: a 4-row x 3-year table; a line chart given as data points; a 5-step process; a before/after map list. Make one or two clear main features in each (overall rise, one category far above the rest, a reversal, a stage count, a shift from farmland to housing).
- **Feedback rule:** one line: does it state the main trend(s) or key contrast, without data, accurately? Plus a better version if not.
- **Ladder:** L1 full worked example first: table of car, bus, bike, walk commuters 2000-2020 -> `Overall, car use rose steadily and remained the most common way to commute, while walking declined to become the least popular.` L2 partially completed: `Overall, ___ increased, whereas ___ ...` for the first item. L3 no example; 90 seconds per item, mixed chart types.
- **Score & log:** correct = main trend/feature and the key comparison, no numbers, no errors in the data reading. A Task 1 report with no clear overview is limited in Task Achievement, so treat this as high leverage.
  `python3 scripts/ielts.py log --module drill --drill overview-sprint --correct 7 --total 8 --tag w1.overview:1`
- **Mastery:** default.

### feature-picking — Feature Picking

- **Trains:** `w1.selection`
- **Format:** 4 datasets, 12 min. For each, the learner lists the 3-4 key features and writes one comparison sentence per feature.
- **How to generate items:** invent tables or charts with 4-6 categories and 3-4 time points, with a mix of the highest, lowest, the biggest change, a crossover, and an exception.
- **Feedback rule:** one line per dataset: which key feature was missed or which trivial one was chosen; whether sentences compare rather than list.
- **Ladder:** L1 the coach shows a worked selection for dataset 1 (four features + why each matters) and asks for a ranking of 6 given features for the rest. L2 learner selects; the first comparison sentence is half written. L3 3 minutes per dataset, mixed with `overview-sprint` (overview + features).
- **Score & log:** correct = all key features covered with accurate comparisons, nothing trivial included.
  `python3 scripts/ielts.py log --module drill --drill feature-picking --correct 3 --total 4 --tag w1.selection:1`
- **Mastery:** default.

### trend-sentence — Trend Sentence

- **Trains:** `w1.data-language`
- **Format:** 8 data points, 8 min. The learner writes one accurate sentence per data change.
- **How to generate items:** give pairs or series (`Sales: 2010 40 units, 2020 65 units`; `Share: 25% -> 18%`; `Steady at 30 until 2015, then peaked at 55`). Require variety: verb + adverb (`rose sharply`), noun phrase (`a sharp rise in`), `by/to/from`, approximation (`just under a third`), `account for`, `the figure for`, and future projections (`is projected to reach`).
- **Feedback rule:** one line: accurate or not, preposition, tense. Indonesian L1 note: Indonesian marks change with `sebesar`/`menjadi`, which map to `by`/`to`; check them every time.
- **Ladder:** L1 worked example: `40 -> 65` -> `Sales rose by 25 units to 65 between 2010 and 2020.`; structure is specified per item. L2 half the items specify the structure. L3 the learner must use 8 different structures in 6 minutes, no repetition of `increase/decrease`.
- **Score & log:** correct = figure, preposition, tense, and form all right.
  `python3 scripts/ielts.py log --module drill --drill trend-sentence --correct 6 --total 8 --tag w1.data-language:2`
- **Mastery:** default.

### process-map-language — Process and Map Language

- **Trains:** `w1.data-language`
- **Format:** 8 items, 10 min. The learner turns process steps into passive sentences with sequencers, or map changes into sentences.
- **How to generate items:** process: 5-8 steps as base-form notes (`collect bottles -> wash -> crush -> melt -> mould`). Map: before/after lists (`2000: farmland, small road`; `2020: housing estate, road widened, school built north of the lake`).
- **Feedback rule:** one line: passive correct, sequencer natural, tense right (process: present simple passive; maps: past simple or present perfect passive). Indonesian L1 note: `di-` passives carry no `be`, so check that `is/are/was/were/has been` is there.
- **Ladder:** L1 worked example: `wash` -> `Once collected, the bottles are washed.`; the sequencer is given for each item. L2 sequencer given for half. L3 write a full 4-sentence process or map body paragraph in 5 minutes, with participle and `which` clauses.
- **Score & log:** correct = correct passive form, correct location/sequence language, accurate to the input.
  `python3 scripts/ielts.py log --module drill --drill process-map-language --correct 7 --total 8 --tag w1.data-language:1`
- **Mastery:** default.

### letter-bullet-expand — Letter Bullet Expand

- **Trains:** `w1.gt-letter`
- **Format:** 2 GT prompts, 12 min. For each: one purpose sentence + 2-3 sentences per bullet (8 items total).
- **How to generate items:** write original GT Task 1 prompts with a situation, a recipient, and three bullets (`Write to your landlord. Explain the problem with the heating. Say how it affects you. Suggest what should be done.`). Mix formal, semi-formal, and informal recipients. The real task is at least 150 words in about 20 minutes.
- **Feedback rule:** one line per item: covered or not, extended with a specific detail or not, tone right or not.
- **Ladder:** L1 worked example for prompt 1 (all bullets, with the specific details highlighted). L2 bullet 1 written; the learner expands bullets 2-3. L3 2 prompts, 6 minutes each, including a clear request or next step at the end.
- **Score & log:** correct = purpose clear in the first lines; each bullet answered with at least one specific detail; register consistent.
  `python3 scripts/ielts.py log --module drill --drill letter-bullet-expand --correct 7 --total 8 --tag w1.gt-letter:1`
- **Mastery:** default.

---

## Writing Task 2

### prompt-dissection — Prompt Dissection

- **Trains:** `w2.task-analysis`
- **Format:** 5 prompts, 10 min. For each the learner writes: question type, topic, every task part as a question to answer, limiting words, and planned position.
- **How to generate items:** write original prompts across the five types: opinion (agree/disagree), discuss both views and give your opinion, advantages vs disadvantages (`do the advantages outweigh...`), problem/cause and solution, and two-part direct questions. Add limiting words (`in cities`, `young people`, `only`) and two-part traps.
- **Feedback rule:** one line: missed task part or limiting word, if any.
- **Ladder:** L1 worked dissection of prompt 1. L2 the first prompt is half dissected. L3 90 seconds per prompt, mixed with `thesis-sprint` (dissect + thesis).
- **Score & log:** correct = every task part and limiting word found, type right.
  `python3 scripts/ielts.py log --module drill --drill prompt-dissection --correct 4 --total 5 --tag w2.task-analysis:1`
- **Mastery:** default.

### thesis-sprint — Thesis Sprint

- **Trains:** `w2.position`
- **Format:** 6 prompts, 90 seconds each. The learner writes a one-sentence thesis that answers every part and states a clear position.
- **How to generate items:** original prompts of all five types; include the learner's past prompts where the position drifted.
- **Feedback rule:** one line: clear position? every part answered? copied prompt wording?
- **Ladder:** L1 worked example: prompt on free public transport -> `Although free fares would be costly, I believe the reduction in traffic and pollution makes them worthwhile.`; the learner fills a frame (`While ___, I believe ___ because ___.`). L2 the frame is shown for prompt 1 only. L3 60 seconds; then the learner writes a matching one-line conclusion; consistency between the two is scored.
- **Score & log:** correct = clear, consistent position covering every part, paraphrased.
  `python3 scripts/ielts.py log --module drill --drill thesis-sprint --correct 5 --total 6 --tag w2.position:1`
- **Mastery:** default.

### topic-sentence-match — Topic Sentence Match

- **Trains:** `w2.paragraphing`
- **Format:** 6 items, 10 min. The learner writes the missing topic sentence for a body paragraph, or removes the off-topic sentence.
- **How to generate items:** write 80-110-word body paragraphs; for half remove the topic sentence; for the other half insert one sentence that belongs to a different idea. Use the learner's paragraphs that mixed two ideas.
- **Feedback rule:** one line: does the topic sentence control everything in the paragraph?
- **Ladder:** L1 three candidate topic sentences are given; the learner picks and improves one. L2 the learner writes it. L3 given a prompt and thesis, the learner writes two topic sentences + one support sentence each, 4 minutes.
- **Score & log:** correct = one controlling idea that matches the paragraph and the thesis.
  `python3 scripts/ielts.py log --module drill --drill topic-sentence-match --correct 5 --total 6 --tag w2.paragraphing:1`
- **Mastery:** default.

---

## Speaking

### extend-the-answer — Extend the Answer

- **Trains:** `x.idea-development`, `s.extension`, `s.fluency`
- **Format:** 8 questions, 10 min. The learner answers aloud (Part 1: about 20-30 seconds; Part 3: 45-60 seconds), recording, then pastes the transcript.
- **How to generate items:** original Part 1 questions on familiar topics (work/study, hometown, routines, food, technology) and Part 3 questions (`Why do some people prefer to live in cities?`). Reuse questions where the learner gave one-sentence answers.
- **Feedback rule:** one line: which extension moves were used (answer, reason, example, contrast or result) and any filler that replaced content (`how to say`, `I think I think`).
- **Ladder:** L1 worked example on screen: `Do you like cooking?` -> `Yes, especially on weekends. During the week I'm too busy, but on Sundays I cook rendang for my family because it reminds me of home.`; the learner follows the answer-reason-example pattern. L2 the pattern is named but not shown. L3 random Part 1 and Part 3 questions, no planning pause.
- **Score & log:** correct = direct answer + at least 2 extension moves within the time, no padding. Split lost items: development gaps -> `x.idea-development`/`s.extension`; long pauses or filler -> `s.fluency`.
  `python3 scripts/ielts.py log --module drill --drill extend-the-answer --correct 6 --total 8 --tag s.extension:1 s.fluency:1 x.idea-development:0`
- **Mastery:** default.

### cue-card-sprint — Cue Card Sprint

- **Trains:** `s.long-turn`, `s.fluency`
- **Format:** 2-3 cards, 12-15 min. Per card: 1 minute of note-taking (keywords only), then 2 minutes of speaking recorded; the learner pastes the transcript and the duration.
- **How to generate items:** original cue cards in the standard shape (`Describe a ...`, `You should say:` three prompts, `and explain ...`), spread across the story-bank categories. Prefer categories the learner has not yet covered.
- **Feedback rule:** one line: duration, bullets covered, where it stalled.
- **Ladder:** L1 worked example of 1-minute notes for card 1 (6-8 keywords, one per bullet + a detail), and the learner may glance at a story-bank note. L2 no example, story-bank notes closed. L3 an unexpected card from a category the learner's stories do not fit directly; adapt a story in the 1 minute.
- **Score & log:** correct card = at least 1:45 of speech, all prompts covered, no long breakdowns, no recited script. The real Part 2 gives 1 minute to prepare and 1-2 minutes to speak; the examiner stops the candidate at 2 minutes.
  `python3 scripts/ielts.py log --module drill --drill cue-card-sprint --correct 2 --total 3 --tag s.long-turn:1 s.fluency:0`
- **Mastery:** default.

### story-bank — Story Bank

- **Trains:** `s.long-turn`
- **Format:** build 6-8 real personal stories over several sessions; then 10-minute adaptation rounds. Explicitly NOT memorised scripts: each story is 5-7 bullet notes the learner keeps (in their own notes file or app).
- **How to generate items:** one category per session: person, place, object, event, experience/challenge, achievement, media (book, film, website, app), routine/habit. The coach asks prompting questions; the learner writes bullets: who/what/where/when; one vivid specific detail (a name, a sound, a number); a problem or turning point; a feeling; why it matters now; 2-3 useful phrases (added with `vocab add --source story-bank --skill s.long-turn` if new). Then list 3-4 cue cards each story could answer (`a gift you received` and `an object you value` can share a story).
- **Feedback rule:** one line per story: real and specific? enough material for 2 minutes? a turning point? Adaptation rounds: one line per card on whether the chosen story fits the card's final `explain` prompt.
- **Ladder:** L1 the coach writes one full worked story-note as a model; the learner builds one story with prompting questions. L2 the learner builds a story alone; the coach checks it. L3 adaptation round: 8 random cue cards; for each the learner names the story and the 1-line bend in 20 seconds.
- **Score & log:** building sessions: correct = story meets the checklist. Adaptation rounds: correct = a usable story with a valid bend.
  `python3 scripts/ielts.py log --module drill --drill story-bank --correct 6 --total 8 --tag s.long-turn:2`
- **Mastery:** default (building sessions and adaptation rounds log to the same drill id); the bank is complete when all 8 categories have a story.

### abstract-frames — Abstract Frames

- **Trains:** `s.abstract`
- **Format:** 6 Part 3 questions, 10 min. The learner answers aloud in 45-60 seconds using a target frame, then pastes the transcript.
- **How to generate items:** original Part 3 questions linked to Part 2 topics. Frames: compare (`Compared with my parents' generation, people today...`), generalise (`By and large`, `tend to`), speculate (`It's likely that`, `I'd imagine`), cause/effect (`This is largely because`, `which in turn`), hypothesis (`If governments were to...`), past vs future (`used to... whereas in future...`).
- **Feedback rule:** one line: frame used correctly? general rather than personal? grammar of the frame (e.g. `were to` + base verb)?
- **Ladder:** L1 worked example answer with the frame highlighted; the frame is assigned for each question. L2 the learner chooses the frame. L3 no cue, with a follow-up `Why?` after each answer.
- **Score & log:** correct = general answer with a reason, frame used accurately, at least 3 sentences.
  `python3 scripts/ielts.py log --module drill --drill abstract-frames --correct 5 --total 6 --tag s.abstract:1`
- **Mastery:** default.

### minimal-pairs — Minimal Pairs

- **Trains:** `s.pron-endings`, `s.pron-sounds`
- **Format:** 10 items, 8 min. The learner reads target sentences aloud into dictation (speech-to-text) and pastes the result; the coach checks whether the target word came out.
- **How to generate items:** sentences where meaning depends on the sound or ending: `I worked there for two years` (vs `work`), `She books the tickets` (vs `book`), `I think it's three` (th vs `t`), `the van` / `the fan`, `ship` / `sheep`, `walked` /t/, `played` /d/, `wanted` /ɪd/. Draw from the learner's `PRON-END`/`PRON-SND` notes. Optional model audio: `say -v Daniel -r 140 "worked. work. worked."`
- **Feedback rule:** one line: was the target heard by the dictation software + one tip (hold the final consonant; tongue between teeth for th; top teeth on lip for v). Indonesian L1 note: Indonesian final stops are unreleased and consonant clusters are rare, so `-ed`/`-s` drop; there is no /θ ð/ (`th` -> t/d) and `v` often becomes `f`; no long/short vowel contrast (ship/sheep).
- **Ladder:** L1 single words, model played first. L2 sentences, no model. L3 the learner speaks a 30-second Part 1 answer about last weekend (rich in -ed) and every past verb is checked.
- **Score & log:** correct = target transcribed correctly. Tag endings vs sounds separately.
  `python3 scripts/ielts.py log --module drill --drill minimal-pairs --correct 7 --total 10 --tag s.pron-endings:2 s.pron-sounds:1`
- **Mastery:** default.

### stress-marking — Stress Marking

- **Trains:** `s.pron-stress`
- **Format:** 10 items, 8 min. The learner marks word stress in capitals (or sentence stress and chunk breaks with `/`) and then reads aloud, recording.
- **How to generate items:** word families that shift stress (`PHOtograph`, `phoTOgraphy`, `photoGRAPHic`; `deVElop`; `ecoNOmic`, `eCOnomy`), IELTS words often mis-stressed (`enVIronment`, `TECHnology` is wrong -> `techNOlogy`), and sentences for chunking and content-word stress (`I'd LIKE to / STUDY abROAD / because...`). Optional model audio: `say -v Karen -r 140 "photography"`.
- **Feedback rule:** one line: correct stress + one tip (content words are stressed, function words reduced). Indonesian L1 note: Indonesian stress is light and fairly even, so English sounds flat and syllable-timed unless the stressed syllable is made longer and louder.
- **Ladder:** L1 words with the syllable count given. L2 words and sentences, no count. L3 the learner marks and reads a 40-word Part 2 opening of their own, with chunk breaks and the main stress per chunk.
- **Score & log:** correct = right marking (the coach cannot hear stress, so score the marking; the recording is for the learner's self-check against the model).
  `python3 scripts/ielts.py log --module drill --drill stress-marking --correct 8 --total 10 --tag s.pron-stress:2`
- **Mastery:** default.

---

## Grammar

### grammar-ladder — Grammar Ladder

- **Trains:** `x.plural`, `g.articles`, `g.agreement`, `g.tense-aspect`, `g.verb-form`, `g.prepositions`, `g.word-order`, `g.pronouns`
- **Format:** 6-8 items on ONE code per round, 8 min. Interactive (one item at a time) by default; design rules and the two-file offline mode are in `grammar-practice-and-reprobe.md`.
- **How to generate items:** start from the learner's own erroneous sentence for that code (reworded), then add original items. Target cases: `a/the/zero` article; `he go`/`the results shows`; `enjoy to read`, `can goes`, missing `be` (`She very busy`), `will` in if-clauses; `depend of`, `discuss about`, `in/on/at`; `a car red`, `I know where is he`; he/she swaps, missing dummy `it/there`.
- **Feedback rule:** one line: fix + rule in one clause + L1 note where it applies. Indonesian L1 notes: no articles (`ART`); no plural marking after numbers (`NUM`); verbs never change for person (`SVA`) or time (`TENSE`), time is shown by words like `sudah`/`kemarin`; no copula (`Dia sibuk` -> `She busy`); noun before adjective (`mobil merah` -> `car red`); `dia` covers he and she (`PRON`); `di` covers in/on/at.
- **Ladder:** L1 recognise/correct: a sentence where the target error is the only error. L2 produce in a frame: given words or a prompt, write a correct sentence. L3 produce freely + boundary case where the naive rule fails (zero article with uncountables; `everyone has`; irregular past), timed at 45 seconds per item, or interleaved with another mastered code.
- **Score & log:** correct = the target structure right and no new error of the same code. Tag the skill id that matches the code.
  `python3 scripts/ielts.py log --module drill --drill grammar-ladder --correct 6 --total 8 --tag g.articles:2`
- **Mastery:** default. The CLI tracks one level for `grammar-ladder` as a whole, not per code: each round targets the code with the most lost marks in `status`, at the drill's current level. Codes that stop recurring are kept alive by re-probes per `grammar-practice-and-reprobe.md`.

### tense-timeline — Tense Timeline

- **Trains:** `g.tense-aspect`
- **Format:** 8 items, 8 min. The learner reads a short timeline and writes one sentence per item with the right tense and aspect.
- **How to generate items:** personal timelines (`2018 moved to Bandung; 2020 started job; still there; next year: Master's`) for `since/for` + present perfect, past simple for finished time, past continuous for background, and future forms. Task 1 timelines: past data -> past simple; data up to now -> present perfect; projections -> `is expected to`/`will`; `by 2030 ... will have`.
- **Feedback rule:** one line: tense + the time signal that decides it. Indonesian L1 note: Indonesian verbs never change for time, so the time word (`yesterday`, `since`) must trigger a verb change in English.
- **Ladder:** L1 the time signal is bolded and the tense named. L2 only the timeline. L3 a 60-second spoken answer to `Tell me about your studies/work so far and your plans`, transcribed and checked, or a Task 1 paragraph with past, present, and projected data.
- **Score & log:** correct = right tense, aspect, and verb form.
  `python3 scripts/ielts.py log --module drill --drill tense-timeline --correct 7 --total 8 --tag g.tense-aspect:1`
- **Mastery:** default.

### sentence-boundary-fix — Sentence Boundary Fix

- **Trains:** `g.sentence-boundaries`
- **Format:** 8 items, 8 min. The learner rewrites run-ons, comma splices, and fragments correctly.
- **How to generate items:** learner's own `PUNC` sentences first; then originals: comma splice (`Prices rose, people bought less.`), run-on, fragment starting with `Because`/`Which`/`For example`, and over-long sentences joined only by `and`.
- **Feedback rule:** one line: the fault + one fix. Name the four repair tools: full stop, semicolon, conjunction (`and, but, so`), subordinator (`because, although, which`).
- **Ladder:** L1 the fault type is labelled. L2 unlabelled, one correct sentence mixed in as a trap. L3 fix each item two different ways, or find all boundary faults in a 100-word paragraph in 4 minutes.
- **Score & log:** correct = grammatically complete sentences, meaning kept, punctuation right.
  `python3 scripts/ielts.py log --module drill --drill sentence-boundary-fix --correct 7 --total 8 --tag g.sentence-boundaries:1`
- **Mastery:** default.

### sentence-combining — Sentence Combining

- **Trains:** `g.complex-range`
- **Format:** 6 items, 10 min. The learner combines 2-3 simple sentences into one accurate complex sentence.
- **How to generate items:** sets of simple sentences from the learner's own writing (or originals on IELTS topics), each with a target structure: relative clause (`which/who/where`), participle clause (`Having finished...`, `Built in 1990, ...`), concessive (`Although/While`), conditional (second/third), passive, `not only... but also`, cleft (`What concerns me is...`).
- **Feedback rule:** one line: accurate or not + the breakdown point (a comma missing before a non-defining `which`, a dangling participle).
- **Ladder:** L1 worked example: `The bridge was built in 1990. It carries 50,000 cars a day.` -> `The bridge, which was built in 1990, carries 50,000 cars a day.`; the structure is named for each item. L2 the structure is named; no example. L3 the learner picks the structure and must use at least 4 different structures across the 6 items, 60 seconds each. Descriptors reward a mix of complex structures used accurately, not complexity alone.
- **Score & log:** correct = target structure, no grammar error, meaning kept.
  `python3 scripts/ielts.py log --module drill --drill sentence-combining --correct 5 --total 6 --tag g.complex-range:1`
- **Mastery:** default.
