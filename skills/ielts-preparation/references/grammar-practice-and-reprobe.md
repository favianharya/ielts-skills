# Grammar Practice and Spaced Re-probes

A correction made once rarely sticks. This file covers the two tools that make it stick: practice built from the learner's own mistakes (Part 1) and re-probes that bring an old mistake back at growing intervals (Part 2). Both work on the codes in `references/grammar-error-taxonomy.md` and on the single error ledger kept by `scripts/ielts.py`, which every module shares (a Listening plural error and a Writing article error wait in the same queue). The general drill catalogue is `references/drills.md`; its grammar drill is `grammar-ladder`. This file adds the grammar-specific item design.

Run CLI commands from the skill root.

---

## Part 1: Practice from the learner's errors

Build items around the exact structure the learner got wrong. A generic worksheet on "articles" is the fallback, not the default.

### Delivery

**Interactive (default).** Run the round inside the conversation.
- Show one item at a time, labelled with its code (`[ART]`), and wait for the learner's written attempt before showing anything else.
- Give no answer until they have tried. Then: right or wrong, the fix, the rule in one clause, and the Indonesian cause if it applies. Move to the next item.
- Stop after 5 to 8 items so a round stays short.
- Because you hold the answers back, no answer key is needed.

**Two files (offline).** Use only when the learner asks for a larger set to work through alone.
- `grammar-drills.md` in the learner's workspace: the items only, each with its code and its level.
- `grammar-drills-solutions.md`: the answer and one-line rule for each item, kept in a separate file so the learner can test themselves first.

Item design, levels and logging are the same in both modes.

### Item design

- 5 to 8 items per code. A set may cover two or three active codes, but each item targets one.
- Every item asks the learner to write or repair a sentence. Choosing an option or naming a rule only checks recognition; it does not train production.
- At least one item is a reworded version of a sentence the learner actually got wrong, so the practice is visibly tied to their own writing or speech.
- Climb three levels (these match the `grammar-ladder` levels in `references/drills.md`; the CLI decides which level the learner is on):
  1. **Repair:** a sentence whose only fault is the target error.
  2. **Build from a frame:** a prompt or a set of words; the learner writes a correct sentence.
  3. **Free sentence with a trap:** an open prompt that includes a case where the simple rule fails (no article with an uncountable noun, "everyone" taking a singular verb, an irregular past form).

### `grammar-drills.md` example

```markdown
# Grammar practice - <date>
Codes: [TENSE], [PREP]

## [TENSE] past tense
1. (repair) Last year my sister move to Bandung for work.
2. (frame) Use "graduate" + "2022" in one sentence about yourself.
3. (trap) Write one sentence about something you "bring" to class yesterday.

## [PREP] prepositions
...
```

### `grammar-drills-solutions.md` example

```markdown
# Answers - <date>

## [TENSE]
1. "...my sister moved to Bandung..." - "last year" is finished time, so the verb must be past.
2. e.g. "I graduated in 2022." - a year in the past takes the past simple (and "in" before a year).
3. e.g. "Yesterday I brought my laptop to class." - "bring" is irregular: brought, not "bringed".
```

### Logging a round

```
python3 scripts/ielts.py log --module drill --drill grammar-ladder --correct N --total M --tag <CODE>
```

`grammar-ladder` has one level for all codes; the CLI moves it up after two strong rounds. Other grammar drills (`tense-timeline`, `sentence-boundary-fix`, `sentence-combining`, `plural-gap-check`) are logged with their own id, as shown in `references/drills.md`.

---

## Part 2: Spaced re-probes

The CLI stores the schedule in the learner's ledger. The coach's job is to choose what goes in, write a new cue each time an item comes due, and grade it.

### Adding errors

Add only systematic errors (a rule the learner does not know or applies wrongly). Slips stay out.

```
python3 scripts/ielts.py error add --skill ART --example "She is teacher at a school near my house." \
  --l1 "Indonesian has no articles; singular countable nouns need a/the."
```

`--skill` accepts any code in `references/grammar-error-taxonomy.md` or any skill id in `references/skill-map.json`. Rewrite the learner's sentence for `--example` rather than pasting it. Adding a code that is already in the ledger raises its frequency and restarts it at stage 1.

### How the schedule moves

- A new item is due 3 days after it is added. Each pass pushes it out: 7 days, then 30, then 90. Passing at 90 days marks it `resolved`.
- A fail sends it back to stage 1, due the next day, status `active`.
- `python3 scripts/ielts.py due` shows up to 2 due errors (most frequent first) ahead of vocabulary items. Clear them at the start of the session, before any new marking.

### Writing the cue

Never reuse the original sentence or the previous cue; the learner would answer from memory. `due` shows the stage and the latest example; change the angle with the stage:

1. **Transfer:** the same error type in a new topic or structure.
2. **Trap:** a case where the usual fix is wrong.
3. **Change one thing:** alter one feature of a sentence (singular to plural, present to past) and ask what else must change.
4. **Explain:** the learner writes the correct form and states the rule that decides it in one clause.

Every cue requires a written or spoken sentence plus the reason.

### Grading

```
python3 scripts/ielts.py review e-g.articles-art pass   # unaided, correct form + reason
python3 scripts/ielts.py review e-g.articles-art fail   # wrong, or needed a hint
```

When the same code turns up again in newly marked work, record it again with `error add` (or `log ... --tag ART --ledger`). Its frequency rises and its schedule starts over.
