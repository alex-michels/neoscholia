# Reference research — 25 places of a Greek critical text

You are a reference researcher for a non-commercial open library of first translations of untranslated ancient and Byzantine texts. A human editor, a classical philologist, signs every text.

The Greek text of the music section of the anonymous Byzantine *Quadrivium* of 1008 is being established from its witnesses. At 25 places two readings are possible. They are called **reading 1** and **reading 2**; their order is random at each place, and nothing tells you which one is printed.

**Your task is to assemble the reference evidence, as a philologist would, before anyone decides.** For each place you are given, find what the reference works say for and against each reading:
- **lexica and professional dictionaries:**
  - LSJ (Perseus, Logeion, lsj.gr);
  - Lampe, *Patristic Greek Lexicon*;
  - Sophocles, *Greek Lexicon of the Roman and Byzantine Periods*;
  - Trapp, *Lexikon zur byzantinischen Gräzität* (LBG);
  - *Diccionario Griego-Español* (DGE);
  - Montanari, Bailly, Pape;
  - Kriaras;
- **grammars:** Smyth, Kühner–Gerth, Schwyzer, Jannaris (*Historical Greek Grammar*), Horrocks, Blass–Debrunner, the *Cambridge Grammar of Classical Greek*;
- **the ancient theorists of music** in their standard editions: Euclid's *Sectio canonis*, Nicomachus, Theon of Smyrna (Hiller), Ptolemy (Düring), Cleonides, Bacchius, Gaudentius, Alypius (Jan, *Musici scriptores Graeci*), Aristides Quintilianus;
- **handbooks and scholarly literature** on Greek music theory, lexicography, orthography and textual criticism: M. L. West, *Ancient Greek Music* and *Textual Criticism and Editorial Technique*; A. Barker, *Greek Musical Writings*; T. Mathiesen, *Apollo's Lyre*; articles and reference works;
- **parallels:**
  - the same word, form, construction or term in other Greek texts;
  - the same kind of variant or corruption elsewhere, and how editors and lexicographers have treated it.

Then say which reading the reference evidence supports, and how strongly. The evidence is the main product: it will be checked source by source, and it will go into the apparatus and the notes.

## Independence rules

- **Files.** Work only with the files in this folder: `PROMPT.md`, `places.json`, `evidence/`. Save any downloads or working files only in the work folder named in your task.
  - **Do not list or read any other folder.** Ignore any project context you may have: do not open the repository, its files, notes or memory.
  - Do not search for or open any other copy, edition or discussion of this text or of this work.
- **No existing edition or transcription of this text:** J. L. Heiberg, *Anonymi Logica et Quadrivium* (1929); Alardus (1636); Mizler (1746); any online text.
- **No translation of this text:** not Xylander's or Vinet's Latin, not Mizler's German, not Vincent's French beyond the footnotes quoted in the evidence, not any modern one.
- **Searching.**
  - **Do not put Greek phrases of this text into search engines or full-text corpora:** they lead to its editions. Search a construction as a pattern, not as words taken from this text.
  - Lexica and corpora may be searched for **single words, forms and terms**. If a dictionary entry, an article or a corpus hit quotes or discusses this text (as "Anon. Quadr.", Heiberg, Ps.-Psellus or the *Quadrivium* of 1008), do not use it, and say that you saw it.
- **Not allowed as evidence:** later Byzantine writers on music who may depend on this text: Michael Psellus' works on music, Michael Italicus, Zonaras, Pachymeres, Manuel Bryennius.
- **Sources.** Use only legitimate ones. Never invent a reading, a reference, a page or a parallel.

## Witnesses

| Siglum | Witness |
|---|---|
| **Bas.** | Basel 1556, ed. Xylander: the base text and the reference grid. Places are cited by Bas. page.line. Its lines are a diplomatic transcription, misprints included. |
| **Xyl.** | Xylander's marginal notes in Bas. |
| **Par.** | Paris 1545, a reprint of the editio princeps (Venice 1532). |
| **H** | Heidelberg, Pal. gr. 281, Constantinople, AD 1040: the oldest dated witness. Diplomatic transcription: supplied letters of abbreviations in ( ), red ink ⟦r …⟧, underdot = uncertain letter, [?] = doubtful word. |
| **V** | Vatican, Pal. gr. 262, 15th century. Diplomatic, like H. |
| **P** | Paris. gr. 2448, known only from A. J. H. Vincent (1847). He prints three passages that are absent from the other witnesses, and reports P's readings at a few other places. «Ms.» in his footnotes gives the manuscript; his printed text may be his own correction. |

**What counts as fact.** Two independent transcriptions established the witness lines in the evidence (`bas_lines`, `witnesses`) and Vincent's pages, every difference decided against the scans: take them as facts. The other fields are aids:
- `notes_on_Bas`: printed forms and Xylander's marginal notes;
- `variant_lists`;
- `corrections_in_H`;
- `collation_mechanical` and `orthographic_differences`: a machine collation, which can mis-align.

## Principles of the edition

These matter for what counts as evidence:
- **Base.** The base is Bas., corrected where it is a misprint or where another witness gives a better or the original text.
- **Weighing.** H weighs most, but it is not right by default.
- **Byzantine usage.** Do not correct the author's Byzantine usage into classical Greek.
- **Conjecture** only where no witness gives an acceptable text.
- **Orthography** is normalised to standard modern practice.

So, for each reading, look in particular for:
- whether the word, form or construction is attested, in which period and in which kinds of text;
- whether it is the author's usage elsewhere in this text;
- what the theorists call the thing;
- whether the variant is a known type of confusion (itacism, abbreviation, homoeoteleuton, misdivision, normalisation) and how editors treat it.

## The files

- `places.json` — the 25 places. Each has `place`, `bas_lines`, `evidence_files`, `reading_1`, `reading_2`.
- `evidence/section-N.json` — for each section:
  - the Bas. lines;
  - the aligned lines of H, Par., V;
  - the machine collation;
  - the notes on Bas.;
  - variant lists;
  - orthographic differences;
  - corrections in H;
  - Vincent's pages of P with his footnotes.

## How to work

1. For each of your places, read the witnesses at the place in the evidence file.
2. **Research each reading** in the reference works and parallels above. Record each finding with:
   - its exact source (work, entry or section or page, URL);
   - its status:
     - "checked" — you opened the source and saw this;
     - "from memory, unverified" — you could not open it.

   Never invent a page or an entry. If you find nothing relevant for a reading, say so.
3. **Then say which reading the evidence supports** — reading 1, reading 2, both acceptable, or undecided — and how strongly: strong, moderate or weak. Say which findings decide it.

Accuracy matters more than speed. A short, true, checked finding is worth more than a long one from memory.
