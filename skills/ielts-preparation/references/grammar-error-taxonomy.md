# Grammar Error Codes and Indonesian-L1 Causes

Every grammar mistake the coach marks gets one code from this file. The codes are the keys of the error ledger (`python3 scripts/ielts.py error add --skill <CODE>`) and valid `--tag` values for `log`; the CLI maps each code to the skill id shown below (see `references/skill-map.json`). Never invent a new code or rename one: the ledger only counts a recurring weakness if it is tagged the same way every time.

How to choose a code:
- Pick the narrowest code that explains the mistake. A sentence with two separate faults gets two codes.
- Separate grammar from vocabulary: if the sentence is grammatical but sounds unnatural, it is `WC` or `COLL`, not a grammar code.
- Give the Indonesian cause only when it really applies to this learner's sentence. A wrong L1 explanation is worse than none.

## Why Indonesian speakers make these errors

Most frequent errors trace back to a handful of differences between Bahasa Indonesia and English:

- No articles. *Ini buku* is "this is a book"; *itu* and *ini* point, they are not "the".
- Verbs do not change. *Saya makan, dia makan, kemarin dia makan*: one form for every person and every time. Time comes from words such as *kemarin*, *sudah*, *sedang*, *akan*.
- Plural is optional and never repeated after a number: *dua mahasiswa*, not *dua mahasiswa-mahasiswa*.
- No obligatory "be" before an adjective or noun: *Kota ini ramai* is a full sentence.
- Modifiers follow the noun: *rumah besar*, *mahasiswa universitas*.
- One third-person pronoun, *dia*, for both sexes; no empty subject like "it" or "there".
- A few prepositions (*di*, *ke*, *dari*, *pada*, *dengan*) cover the work of many English ones.

Naming the specific contrast ("Indonesian marks the time with *kemarin* and leaves the verb alone; English changes the verb as well") is what turns a one-off correction into a habit.

---

## Noun phrase

### ART: articles (a, an, the, no article)
- **Skill:** `g.articles` · **Drill:** `grammar-ladder`
- **Covers:** a missing article before a singular countable noun; "the" used for a general idea; "a" before a plural or uncountable noun.
- **Wrong → right:** *My father works as engineer in Surabaya.* → *as **an** engineer*. *The technology changes how we learn.* (technology in general) → ***Technology** changes how we learn.*
- **Indonesian cause:** there is no article system to transfer, so articles are dropped or guessed. Optional words like *seorang* or *sebuah* are counters, not articles. This is usually the most frequent code for this learner.
- **Quick test:** a singular countable noun cannot stand alone; it needs a, an, the, or another determiner (my, this, every).

### NUM: number and countability
- **Skill:** `x.plural` · **Drills:** `plural-gap-check`, `grammar-ladder`
- **Covers:** no plural -s after a number or quantifier; plural -s on an uncountable noun; many/much, few/little mixed up.
- **Wrong → right:** *Two of my friend study in Australia.* → *Two of my **friends***. *She gave me some useful advices.* → *some useful **advice***.
- **Indonesian cause:** after *dua*, *banyak* or *beberapa* the noun stays singular, so an English -s looks redundant. Indonesian also has no grammatical split between countable and uncountable nouns, so *advice, information, equipment, research* get pluralised.
- **Quick test:** number, "many", "several", "a number of", "one of the" + countable noun means plural, every time.

### PLURAL: singular/plural form in a completion answer
- **Skill:** `x.plural` · **Drill:** `plural-gap-check`
- **Covers:** Listening or Reading answers marked wrong because the word was written singular when the gap needed plural, or the reverse. Use `NUM` for the same fault in Writing or Speaking.
- **Wrong → right:** gap *"The flat has three ___"*, answer *bedroom* → ***bedrooms***.
- **Indonesian cause:** same as `NUM`; the number before the gap does not trigger an -s for an Indonesian ear.
- **Quick test:** read the words around the gap; a number or plural verb next to it decides the form.

---

## Verb phrase

### SVA: subject-verb agreement
- **Skill:** `g.agreement` · **Drill:** `grammar-ladder`
- **Covers:** third-person -s missing or added wrongly; verb agreeing with the nearest noun instead of the real subject.
- **Wrong → right:** *My mother cook breakfast every morning.* → *My mother **cooks***. *The number of tourists have increased.* → *The number of tourists **has** increased.*
- **Indonesian cause:** the verb is identical for *saya*, *kamu* and *dia*, so the -s has nothing to attach to and disappears in fast speech.
- **Quick test:** find the head noun of the subject (number, not tourists); if it is he, she, it or singular, a present verb takes -s.

### TENSE: tense choice
- **Skill:** `g.tense-aspect` · **Drills:** `grammar-ladder`, `tense-timeline`
- **Covers:** a verb in the wrong time frame, most often present form for a finished past event.
- **Wrong → right:** *Last month I join an English course.* → *I **joined***. *In 2010 the factory produce 300 tonnes.* → *the factory **produced***.
- **Indonesian cause:** *bulan lalu* or *pada tahun 2010* already tells the time, and the Indonesian verb never changes, so the English past form feels unnecessary once a time word is present.
- **Quick test:** a finished-time marker (yesterday, last, ago, in 2010) needs a past verb as well as the time word.

### ASP: aspect (simple, continuous, perfect)
- **Skill:** `g.tense-aspect` · **Drills:** `tense-timeline`, `grammar-ladder`
- **Covers:** correct time frame but wrong aspect: present for a situation that started in the past and continues; past simple where the past perfect is needed; continuous with a state verb.
- **Wrong → right:** *I study English for five years.* (and still do) → *I **have been studying** English for five years.* *When I arrived, the class already started.* → *the class **had** already **started***. *I am understanding the point.* → *I **understand** the point.*
- **Indonesian cause:** *sudah* and *sejak* carry completion and duration on their own, so *sudah* tends to become "already" + past simple and *sejak* + an unchanged verb becomes "since" + present. English needs the perfect to carry that meaning.
- **Quick test:** "since" or "for" + a situation still true now means present perfect; the earlier of two past events often takes "had".

### VF: verb form
- **Skill:** `g.verb-form` · **Drill:** `grammar-ladder`
- **Covers:** -ing versus to-infinitive after a verb, adjective or preposition; wrong participle in passives and perfects; missing "be".
- **Wrong → right:** *I avoid to eat late at night.* → *I avoid **eating***. *The city more crowded than before.* → *The city **is** more crowded.* *This bridge was build in 1995.* → *was **built***.
- **Indonesian cause:** the copula is normally absent before adjectives (*Kota ini lebih ramai*), so "is/are" goes missing. The *di-* passive attaches to the base verb (*dibangun*), which encourages "was" + base form. Indonesian has no gerund/infinitive contrast, so which form follows "avoid", "plan" or "look forward to" must be learned word by word.
- **Quick test:** every clause needs a finite verb; after a preposition use -ing; passive = be + past participle.

### MOD: modals and conditionals
- **Skill:** `g.verb-form` · **Drill:** `grammar-ladder`
- **Covers:** a modal followed by an inflected verb or "to"; "will" inside the if-clause; mismatched conditional forms.
- **Wrong → right:** *The government should builds more schools.* → *should **build***. *If the price will go up, people buy less.* → *If the price **goes** up, people **will** buy less.* *If I had more time, I will travel.* → *I **would** travel.*
- **Indonesian cause:** *bisa*, *harus* and *akan* sit before a verb that never changes, so there is no L1 model for the strict "modal + bare verb" rule, and learners who have just learned third-person -s overapply it after a modal. Indonesian conditionals do not shift verb forms between real and imagined situations, so "had ... would" backshift has no equivalent.
- **Quick test:** after can, should, must, will, might: bare verb only. Future meaning in an if-clause still takes the present tense.

---

## Sentence and clause

### WO: word order
- **Skill:** `g.word-order` · **Drill:** `grammar-ladder`
- **Covers:** modifiers after the noun; question order inside a reported question; adverbs in the wrong slot.
- **Wrong → right:** *Many students university work part-time.* → *Many **university students***. *Can you tell me what time is it?* → *what time **it is***. *I very like coffee.* → *I like coffee **very much***.
- **Indonesian cause:** Indonesian puts the head noun first (*mahasiswa universitas*, *mobil merah*), the reverse of English. *Saya sangat suka kopi* translates word for word as "I very like coffee".
- **Quick test:** describing words come before the noun; inside "tell me / I wonder / I know", use statement order.

### PRON: pronouns and reference
- **Skill:** `g.pronouns` · **Drill:** `grammar-ladder`
- **Covers:** he/she and his/her swapped; missing dummy subject "it" or "there"; a pronoun repeating the subject.
- **Wrong → right:** *My mother is a nurse; he works night shifts.* → ***she** works*. *Is important to sleep well.* → ***It** is important*. *Have many cafés near my campus.* → ***There are** many cafés.*
- **Indonesian cause:** *dia* and *-nya* are the same for men and women, so gender slips are frequent in Speaking. *Penting untuk tidur cukup* and *Ada banyak kafe* need no subject, and *ada* is also used for "have", which produces "Have many...".
- **Quick test:** every English clause needs a subject; check every he, she, his and her against the person meant.

### PUNC: sentence boundaries
- **Skill:** `g.sentence-boundaries` · **Drill:** `sentence-boundary-fix`
- **Covers:** comma splices, run-on sentences and fragments, i.e. punctuation that breaks the grammar. Leave purely stylistic commas alone.
- **Wrong → right:** *Many people own two motorbikes, this causes congestion.* → *...two motorbikes**, which** causes congestion.* (or a full stop). *For example, my hometown.* (fragment) → *My hometown is one example.*
- **Indonesian cause:** usually a writing habit rather than transfer; do not give an L1 note unless the learner's sentence clearly shows one.
- **Quick test:** two complete clauses joined only by a comma need a full stop, a semicolon, a conjunction or a subordinator.

### RANGE: limited or failed complex structures
- **Skill:** `g.complex-range` · **Drill:** `sentence-combining`
- **Covers:** an answer built almost entirely from short simple sentences; a complex structure (relative clause, participle clause, passive, conditional, concession) attempted and broken.
- **Wrong → right:** *Jakarta is very big. It has many people. It has bad traffic.* → *Jakarta, **which** is home to more than ten million people, suffers from severe congestion.* *The man which lives next door...* → *The man **who** lives next door...*
- **Indonesian cause:** *yang* serves as who, which and that, and it has no comma distinction between identifying and extra-information clauses, so relative-pronoun choice and the commas around a non-defining clause need deliberate attention.
- **Quick test:** count the different complex structures in the answer, then check each one is accurate. Variety without accuracy does not raise the band.

### CONJ: connectors
- **Skill:** `x.cohesion` · **Drill:** `cohesion-repair`
- **Covers:** two connectors doing one job; a linker with the wrong logic; a connector used as if it could join two sentences with a comma.
- **Wrong → right:** *Because the rent is cheap, so many students live there.* → drop **so** (or drop **because**). *Even though the city is noisy, but I like it.* → drop **but**.
- **Indonesian cause:** Indonesian routinely pairs connectors (*karena ... maka ...*, *meskipun ... tetapi ...*), and the pair transfers directly.
- **Quick test:** one link between two clauses needs one connector.

### COH: cohesion and reference across sentences
- **Skill:** `x.cohesion` · **Drill:** `cohesion-repair`
- **Covers:** "this", "it" or "they" with no clear antecedent; linkers used mechanically or with the wrong meaning; paragraphs without a clear focus.
- **Wrong → right:** *Prices rose and wages stayed flat. This made many families...* → ***This gap** made many families...* *The rent is high. Moreover, the flat is very cheap.* → ***However**, the flat is very cheap.*
- **Indonesian cause:** formal Indonesian leans on *hal ini* ("this matter") and *selain itu* as all-purpose links, which become a bare "This" and an overused "Moreover".
- **Quick test:** after "this", add a noun that names what it refers to; check that each linker matches the logic (addition, contrast, cause, result).

---

## Word level

### PREP: prepositions
- **Skill:** `g.prepositions` · **Drills:** `grammar-ladder`, `collocation-fix`
- **Covers:** wrong, missing or extra preposition; prepositions fixed to a verb, adjective or noun.
- **Wrong → right:** *I am interested with economics.* → *interested **in***. *The museum opened on 2015.* → ***in** 2015*. *The article mentions about climate change.* → *mentions climate change*.
- **Indonesian cause:** *di* covers in, on and at; *pada* is often translated as "on" (*pada tahun 2015*); *tertarik dengan* gives "interested with"; *menyebutkan tentang* gives "mention about".
- **Quick test:** learn the preposition with its partner word as one chunk; when the error recurs, it belongs in the ledger.

### WF: word form
- **Skill:** `x.word-form` · **Drill:** `word-family-ladder`
- **Covers:** right word family, wrong part of speech (noun for adjective, adjective for adverb, and so on).
- **Wrong → right:** *It is a very danger road.* → *a very **dangerous** road*. *The economy grew rapid.* → *grew **rapidly***.
- **Indonesian cause:** many Indonesian words work in several word classes without changing (*cepat* is both fast and quickly), and colloquial *bahaya* replaces *berbahaya*, so English suffixes (-ous, -ly, -tion, -ment) get left off.
- **Quick test:** ask what slot the word fills (before a noun = adjective; describing a verb = adverb) and choose the matching form.

### WC: word choice
- **Skill:** `x.collocation` · **Drills:** `collocation-fix`, `vocab-review`
- **Covers:** a grammatically possible word with the wrong meaning or the wrong member of a near-synonym pair (make/do, say/tell, borrow/lend).
- **Wrong → right:** *I have to make my homework tonight.* → ***do** my homework*. *Can you borrow me your charger?* → *Can you **lend** me...*
- **Indonesian cause:** one Indonesian word often covers two English ones: *membuat* = make, used for *membuat PR*; *pinjam* is used for both borrow and lend.
- **Quick test:** check which person gives and which receives, or which verb the noun normally takes. Not strictly grammar, but flag it: it limits Lexical Resource.

### COLL: collocation
- **Skill:** `x.collocation` · **Drills:** `collocation-fix`, `vocab-review`
- **Covers:** words that are each correct but are not the partners English uses (adjective + noun, verb + noun, adverb + adjective).
- **Wrong → right:** *Social media gives a big influence to teenagers.* → *Social media **has a strong influence on** teenagers.* *The traffic is very crowded.* → *The traffic is very **heavy***.
- **Indonesian cause:** direct translation of *memberi pengaruh besar* and *lalu lintas padat*.
- **Quick test:** say the phrase as a chunk you have seen in English texts; if unsure, record the correct chunk with `vocab add`.

---

## Codes and the ledger

Log a code only for a systematic error (the learner applies a rule wrongly or does not know it), not for a slip they would catch on a re-read. A code that comes back across sessions is a real gap: drill it and let the re-probes in `references/grammar-practice-and-reprobe.md` keep it alive. For this learner, watch the transfer codes first: `ART`, `NUM`, `SVA`, `TENSE`, `ASP`, `VF`, `PREP`, `PRON`.
