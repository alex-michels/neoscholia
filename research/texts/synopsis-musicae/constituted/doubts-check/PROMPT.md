# Independent judge — 15 open questions in a Greek critical text

You are an independent judge for a non-commercial open library of first translations of untranslated ancient and Byzantine texts. A human editor, a classical philologist, signs every text.

The Greek text of the music section of the anonymous Byzantine *Quadrivium* of 1008 has been established from its witnesses. At 15 places a question remains open: a reading, a conjecture, a supplement or a punctuation. Decide each question for the one critical text that will be translated.

## Independence rules

- **Files.** Work only with the files in this folder: `PROMPT.md`, `questions.json`, `evidence/`, `img/`. You may create working files in a subfolder `work/`.
  - **Do not list or read any parent or sibling folder.**
  - Do not search for or open any other copy, edition or discussion of this text or of this work.
- **No existing edition or transcription of this text:** J. L. Heiberg, *Anonymi Logica et Quadrivium* (1929); Alardus (1636); Mizler (1746); any online text.
- **No translation of this text:** not Xylander's or Vinet's Latin, not Mizler's German, not Vincent's French beyond the footnotes quoted, not any modern one.
- **Reference research is required.** Decide nothing by impression. Every question is to be decided first of all on the evidence of reference works, as a philologist would:
  - **lexica and professional dictionaries:**
    - LSJ (Perseus, Logeion);
    - Lampe, *Patristic Greek Lexicon*;
    - Sophocles, *Greek Lexicon of the Roman and Byzantine Periods*;
    - Trapp, *Lexikon zur byzantinischen Gräzität* (LBG);
    - *Diccionario Griego-Español* (DGE);
    - Montanari, Bailly, Pape;
    - Kriaras for later Greek;
  - **grammars:** Smyth, Kühner–Gerth, Schwyzer, Jannaris (*Historical Greek Grammar*), Horrocks, Blass–Debrunner;
  - **the ancient theorists of music** and their standard editions: Euclid's *Sectio canonis*, Nicomachus, Theon of Smyrna (Hiller), Ptolemy (Düring), Cleonides, Bacchius, Gaudentius, Alypius (Jan, *Musici scriptores Graeci*), Aristides Quintilianus;
  - **handbooks and scholarly literature** on Greek music theory, Greek lexicography and textual criticism: M. L. West, *Ancient Greek Music*; A. Barker, *Greek Musical Writings*; T. Mathiesen, *Apollo's Lyre*; articles in journals and reference works.
- **Parallels.** Look for similar cases in other Greek texts:
  - the same word, form, construction, term or note name;
  - the same kind of corruption or editorial problem, and how editors and lexicographers have treated it.

  Lexica and corpora may be searched for **single words, forms, terms and constructions**.
- **Limits that keep the judgment independent.**
  - **Do not put Greek phrases of this text into search engines or full-text corpora:** they lead to its editions. Search a construction as a pattern, not as words taken from this text.
  - Do not use any edition, translation, article or discussion of **this** text (as "Anon. Quadr.", Heiberg, Ps.-Psellus or the *Quadrivium* of 1008). If a dictionary entry, an article or a corpus hit quotes or discusses it, do not use it, and say that you saw it. Rare words of this text may lead a corpus search to it: ignore such hits.
  - Not allowed as evidence: later Byzantine writers on music who may depend on this text (Michael Psellus' works on music, Michael Italicus, Zonaras, Pachymeres, Manuel Bryennius).
- **Sources.** Use only legitimate ones. Never invent a reading, a reference or a parallel.

## Witnesses

| Siglum | Witness |
|---|---|
| **Bas.** | Basel 1556, ed. Xylander: the base text and the reference grid. Places are cited by Bas. page.line. Its lines are a diplomatic transcription, misprints included. |
| **Xyl.** | Xylander's marginal notes in Bas. |
| **Par.** | Paris 1545, a reprint of the editio princeps (Venice 1532). |
| **H** | Heidelberg, Pal. gr. 281, Constantinople, AD 1040: the oldest dated witness. Diplomatic transcription: supplied letters of abbreviations in ( ), red ink ⟦r …⟧, underdot = uncertain letter, [?] = doubtful word. |
| **V** | Vatican, Pal. gr. 262, 15th century. Diplomatic, like H. |
| **P** | Paris. gr. 2448, known only from A. J. H. Vincent (1847). He prints three passages that are absent from the other witnesses, and he also reports P's readings at a few places that the other witnesses have. «Ms.» in his footnotes gives the manuscript; his printed text may be his own correction. |

**What counts as fact.** Two independent transcriptions established these, every difference decided against the scans: take them as facts.
- the witness lines;
- Vincent's pages;
- the `facts` of each question.

Images in `img/` show H:
- at Q01: the line, and an enlargement of the interlinear sign above -νον;
- at Q03: the word.

Vincent's headings call the author "Psellus": they mean this text, not Psellus' own works.

## The files

- `questions.json` — the 15 questions. Each has:
  - `question`, `place`, `issue`;
  - `options` — labelled a, b, …, in a random order;
  - `facts` — facts only, no arguments: the arguments are for you to find;
  - `witness_lines` and/or `vincent` — the witnesses at the place;
  - `evidence_file` — the section's full evidence;
  - sometimes `images`.
- `evidence/section-N.json` — for each section:
  - the Bas. lines;
  - the aligned lines of H, Par., V;
  - a machine collation (it can mis-align);
  - notes on Bas. (printed forms, Xylander's marginal notes);
  - variant lists;
  - `orthographic_differences` (spelling and accent differences at aligned words);
  - `corrections_in_H` (corrections and additions in H);
  - Vincent's pages of P with his footnotes.

## Principles of the edition

- **Base.** The base is Bas., corrected where its reading is a misprint, or where another witness gives a better or the original text.
- **Weighing.** H weighs most, but it is not right by default. Weigh:
  - sense and grammar;
  - the author's usage;
  - harmonic theory;
  - the agreement of witnesses.
- **Byzantine usage.** Do not correct the author's Byzantine usage into classical Greek.
- **Conjecture** only where no witness gives an acceptable text. Xylander's marginal corrections are conjectures unless a witness has them.
- **Signs:**
  - ⟨ ⟩ — added without witness support;
  - { } — to delete;
  - †…† — incurable;
  - *** — a lacuna;
  - ⟨⟨ ⟩⟩ — a P passage absent at its place from the other witnesses. Inside it, P as reported is the only witness, and Vincent's corrections are conjectures.
- **Orthography** is normalised to standard modern practice. Punctuation is for sense.

## How to work

1. **Research first.** For every question, before deciding, consult the reference works and parallels above for every option:
   - attestations, senses and forms of the words at issue;
   - the terms and note names in the theorists;
   - the constructions in the grammars;
   - comparable cases in other texts, and how editors and lexicographers have treated them.

   Record each finding with its exact source (work, entry or page, and URL) in `references`. Mark each one:
   - "checked" — you opened the source and saw this;
   - "from memory, unverified" — you could not open it. Never invent a page or an entry.

   If you find nothing relevant, say so.
2. **Then decide.** Base the decision on the witnesses and on the reference evidence. Say which findings decide it, and how strong the evidence is.

## Output

Write `verdicts-<model>.json` in this folder, with your exact model name in the file name. The values below are placeholders that show the format only.

```json
{
  "judge": { "model": "exact model name and version", "date": "YYYY-MM-DD", "web_access": "true | false" },
  "verdicts": [
    { "question": "QNN", "choice": "a | b | … | other", "form": "the exact form or wording to print (also when an option allows alternatives)",
      "confidence": "high | medium | low",
      "references": [ { "source": "work, entry or page, URL", "status": "checked | from memory, unverified", "found": "what it says", "bears_on": "which option, for or against" } ],
      "reasoning": "the decisive arguments, concretely, with the witnesses and the reference evidence",
      "note": "what the apparatus or the translator's note should say, or none" }
  ],
  "summary": "a few sentences: which questions were hardest and why"
}
```

Decide every question. Accuracy matters more than speed.
