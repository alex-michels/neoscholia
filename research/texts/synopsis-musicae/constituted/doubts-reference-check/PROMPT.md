# Reference research — an open question in a Greek critical text

You are a reference researcher for a non-commercial open library of first translations of untranslated ancient and Byzantine texts. A human editor, a classical philologist, signs every text.

The Greek text of the music section of the anonymous Byzantine *Quadrivium* of 1008 has been established from its witnesses. At some places a question is still disputed: a reading, a conjecture, a supplement or a punctuation. Earlier research found some references; they are listed in `prior-references.json` and are **not yet verified**.

**Your task is to find out whether the reference evidence decides your question.** Concretely:
1. **Look for evidence not yet found**, above all evidence that could be decisive. Your task names some leads; follow them, and others you think of.
2. **Test the strongest prior claims on each side.** Open the sources, read them in context, and say whether they hold, are weaker than claimed, or are wrong.
3. **Weigh the whole evidence** and say:
   - which option it supports;
   - how strongly;
   - whether anything is decisive.

Be even-handed: look as hard for evidence against each option as for it.

## Reference works

- **Lexica and professional dictionaries:**
  - LSJ (Perseus, Logeion, lsj.gr);
  - Lampe, *Patristic Greek Lexicon*;
  - Sophocles, *Greek Lexicon of the Roman and Byzantine Periods*;
  - Trapp, *Lexikon zur byzantinischen Gräzität* (LBG);
  - *Diccionario Griego-Español* (DGE);
  - Montanari, Bailly, Pape;
  - Kriaras.
- **Grammars and syntax:**
  - Smyth, Kühner–Gerth, Schwyzer;
  - Jannaris, *Historical Greek Grammar*; Horrocks;
  - Blass–Debrunner;
  - Denniston, *The Greek Particles*;
  - the *Cambridge Grammar of Classical Greek*.
- **The ancient theorists of music** in their standard editions: Euclid's *Sectio canonis*, Nicomachus, Theon of Smyrna (Hiller), Ptolemy (Düring), Cleonides, Bacchius, Gaudentius, Alypius (Jan, *Musici scriptores Graeci*), Aristides Quintilianus, the *Anonyma Bellermanniana*.
- **Handbooks and scholarly literature:**
  - Greek music theory: M. L. West, *Ancient Greek Music*; A. Barker, *Greek Musical Writings*; T. Mathiesen, *Apollo's Lyre*;
  - palaeography and textual criticism: M. L. West, *Textual Criticism and Editorial Technique*;
  - manuscript catalogues;
  - editorial conventions;
  - articles and reference works.
- **Parallels:**
  - the same word, form, construction, term or note name in other Greek texts;
  - the same kind of corruption or editorial problem elsewhere, and how editors and lexicographers treated it.

## Independence rules

- **Files.** Work only with the files in this folder: `PROMPT.md`, `questions.json`, `prior-references.json`, `evidence/`. Save downloads and working files only in the work folder named in your task.
  - **Do not list or read any other folder.** Ignore any project context you may have: do not open the repository, its files, notes or memory.
  - Do not search for or open any other copy, edition or discussion of this text or of this work.
- **No existing edition or transcription of this text:** J. L. Heiberg, *Anonymi Logica et Quadrivium* (1929); Alardus (1636); Mizler (1746); any online text.
- **No translation of this text:**
  - not Xylander's or Vinet's Latin, not Mizler's German, not any modern one;
  - not Vincent's French on this text beyond the footnotes quoted in the evidence.

  Vincent's volume (*Notices et extraits* 16.2) may be opened for his general conventions and for his editions of other texts. Skip his section on Paris. gr. 2448 and its passages of this text (his "Psellus"), beyond the footnotes already quoted in the evidence.
- **Searching.**
  - **Do not put Greek phrases of this text into search engines or full-text corpora:** they lead to its editions. Search a construction as a pattern, not as words taken from this text.
  - Lexica and corpora may be searched for **single words, forms and terms**. Fixed technical terms of two or three words (note names, interval names, ratio names) count as terms and may be searched; report and discard any hit on this text. If a dictionary entry, an article or a corpus hit quotes or discusses this text (as "Anon. Quadr.", Heiberg, Ps.-Psellus or the *Quadrivium* of 1008), do not use it, and say that you saw it.
- **Not allowed as evidence:** later Byzantine writers on music who may depend on this text: Michael Psellus' works on music, Michael Italicus, Zonaras, Pachymeres, Manuel Bryennius.
- **Sources.** Use only legitimate ones. Never invent a reading, a reference, a page or a parallel.

## Witnesses

| Siglum | Witness |
|---|---|
| **Bas.** | Basel 1556, ed. Xylander: the base text and the reference grid. Places are cited by Bas. page.line. Its lines are a diplomatic transcription, misprints included. |
| **Xyl.** | Xylander's marginal notes in Bas.: his own corrections and supplements, not a manuscript witness. |
| **Par.** | Paris 1545, a reprint of the editio princeps (Venice 1532). |
| **H** | Heidelberg, Pal. gr. 281, Constantinople, AD 1040: the oldest dated witness. Diplomatic transcription: supplied letters of abbreviations in ( ), red ink ⟦r …⟧, underdot = uncertain letter, [?] = doubtful word. |
| **V** | Vatican, Pal. gr. 262, 15th century. Diplomatic, like H. |
| **P** | Paris. gr. 2448, known only from A. J. H. Vincent, «Notice sur divers manuscrits grecs relatifs à la musique», *Notices et extraits des manuscrits* 16.2 (1847). He prints three passages that are absent from the other witnesses, and reports P's readings at a few other places. «Ms.» in his footnotes gives the manuscript; his printed text may be his own correction. |

**What counts as fact.** Two independent transcriptions established these, every difference decided against the scans: take them as facts.
- the witness lines;
- Vincent's pages;
- the `facts` of each question.

## Principles of the edition

- **Base.** The base is Bas., corrected where its reading is a misprint, or where another witness gives a better or the original text.
- **Weighing.** H weighs most, but it is not right by default.
- **Byzantine usage.** Do not correct the author's Byzantine usage into classical Greek.
- **Conjecture** only where no witness gives an acceptable text.
- **Signs:**
  - ⟨ ⟩ — added without witness support;
  - { } — to delete;
  - †…† — incurable;
  - ⟨⟨ ⟩⟩ — a P passage absent at its place from the other witnesses.
- **Orthography** is normalised to standard modern practice. Punctuation is for sense.

## The files

- `questions.json`:
  - each question: `question`, `place`, `issue`, `options` (labelled a, b, …), `facts`, `witness_lines` and/or `vincent`, `evidence_file`;
  - the options are in a random order, and nothing tells you which one is printed now.
- `prior-references.json`:
  - the references found earlier, per question, each with an `id`;
  - `bears_on` uses the option labels of `questions.json`;
  - not yet verified: the `status` field records the earlier researcher's own claim, not a verification.
- `evidence/section-N.json`, the full evidence of each section:
  - the Bas. lines and the aligned lines of H, Par., V;
  - a machine collation;
  - notes on Bas.;
  - variant lists;
  - orthographic differences;
  - corrections in H;
  - Vincent's pages of P with his footnotes.

## Recording findings

Record every finding with:
- its exact source (work, entry or section or page, URL);
- its status:
  - "checked" — you opened the source and saw this;
  - "from memory, unverified" — you could not open it.

Never invent a page or an entry. If you looked for something and found nothing, say so: a well-searched absence is evidence too.

Accuracy matters more than speed.
