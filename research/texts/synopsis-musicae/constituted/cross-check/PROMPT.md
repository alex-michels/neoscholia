# Independent judge — 25 places of a Greek critical text

You are an independent judge for a non-commercial open library of first translations of untranslated ancient and Byzantine texts. A human editor, a classical philologist, signs every text.

Two editions of the Greek text of the music section of the anonymous Byzantine *Quadrivium* of 1008 were made independently. At 25 places they differ in words. They are called **edition 1** and **edition 2**. They are anonymous, and their order is random at each place: there is no reason to prefer 1 or 2. Decide, for the one critical text that will be translated, what to print at each place.

## Independence rules

- **Files.** Work only with the files in this folder: `PROMPT.md`, `places.json`, `notes.json`, `evidence/`. You may create working files in a subfolder `work/`.
  - **Do not list or read any parent or sibling folder.**
  - Do not search for or open any other copy, edition or discussion of this text or of this work.
- **No existing edition or transcription of this text:** J. L. Heiberg, *Anonymi Logica et Quadrivium* (1929); Alardus (1636); Mizler (1746); any online text.
- **No translation of this text:** not Xylander's or Vinet's Latin, not Mizler's German, not Vincent's French beyond the footnotes quoted in the evidence, not any modern one.
- **Searching.**
  - **Do not put Greek words or phrases of this text into search engines or full-text corpora.**
  - Looking up **single words** in LSJ, Lampe, Sophocles or Trapp's *Lexikon zur byzantinischen Gräzität* is allowed. If an entry quotes this text, do not use the quotation, and say that you saw it.
- **Ancient sources.** For a technical word, note name or number, use only these theorists: Euclid's *Sectio canonis*, Nicomachus, Theon of Smyrna, Ptolemy, Cleonides, Bacchius, Gaudentius, Alypius, Aristides Quintilianus. Not allowed: later Byzantine writers who may depend on this text (Michael Psellus' works on music, Michael Italicus, Zonaras, Pachymeres, Manuel Bryennius).
- **Sources.** Use only legitimate ones. Never invent a reading, a reference or a parallel.

## Witnesses

| Siglum | Witness |
|---|---|
| **Bas.** | Basel 1556, ed. Xylander: the base text and the reference grid. Places are cited by Bas. page.line. Its lines are a diplomatic transcription, misprints included. |
| **Xyl.** | Xylander's marginal notes in Bas. |
| **Par.** | Paris 1545, a reprint of the editio princeps (Venice 1532). |
| **H** | Heidelberg, Pal. gr. 281, Constantinople, AD 1040: the oldest dated witness. Diplomatic transcription: supplied letters of abbreviations in ( ), red ink ⟦r …⟧, underdot = uncertain letter, [?] = doubtful word. |
| **V** | Vatican, Pal. gr. 262, 15th century. Diplomatic, like H. |
| **P** | Paris. gr. 2448, known only from A. J. H. Vincent (1847) for three places. «Ms.» in his footnotes gives the manuscript; his printed text may be his own correction. |

**What counts as fact.** The witness lines in the evidence (`bas_lines`, `witnesses`) and Vincent's pages were established by two independent transcriptions, every difference decided against the scans. Take them as facts. The other fields are aids, not verdicts:
- `notes_on_Bas` gives printed forms and Xylander's marginal notes;
- `variant_lists` gives readings of Par. and V at places of variation;
- `corrections_in_H` lists corrections in H;
- `collation_mechanical` and `orthographic_differences` are a machine collation and can mis-align.

## The files

- `places.json` — the 25 places, without any argument. Each has:
  - `place`;
  - `bas_lines`;
  - `evidence_files`;
  - `reading_1`, `reading_2` — the two editions' readings at the place.
- `notes.json` — each edition's argument at each place, rewritten in one neutral style. **Do not open it until you have finished step 1 for all places.**
- `evidence/section-N.json` — for each section of the text:
  - the Bas. lines;
  - the aligned lines of H, Par., V;
  - the machine collation;
  - notes on Bas.;
  - variant lists;
  - where relevant, Vincent's pages of P with his footnotes.

## Principles of the edition

- **Base.** The base is Bas., corrected where its reading is a misprint, or where another witness gives a better or the original text.
- **Weighing.** H weighs most, but it is not right by default. Weigh:
  - sense and grammar;
  - the author's usage elsewhere in the section;
  - harmonic theory;
  - the agreement of witnesses (Bas. alone against H Par. V; Bas. Par. against H V).
- **Byzantine usage.** Do not correct the author's Byzantine usage into classical Greek.
- **Conjecture** only where no witness gives an acceptable text. Xylander's marginal corrections are conjectures unless a witness has them.
- **Signs:**
  - ⟨ ⟩ — added without witness support;
  - { } — to delete;
  - †…† — incurable;
  - ⟨⟨ ⟩⟩ — a P passage absent at its place from the other witnesses. Inside it, P as reported is the only witness, and Vincent's corrections are conjectures.
- **Orthography** is normalised to standard modern practice.

## How to work

1. **Step 1, without `notes.json`.** For every place, look at the witnesses in the evidence and decide what you would print. Record it as `first_view`.
2. **Step 2.** Only then open `notes.json`, read both editions' arguments, and revise if an argument convinces you. Say so in `reasoning`.

## Output

Write `verdicts-<model>.json` in this folder, with your exact model name in the file name. The values below are placeholders that show the format only.

```json
{
  "judge": { "model": "exact model name and version", "date": "YYYY-MM-DD", "web_access": "true | false" },
  "verdicts": [
    { "place": "place NN", "choice": "1 | 2 | other | doubt", "other": "the reading to print, if choice is other",
      "confidence": "high | medium | low",
      "first_view": "what you decided in step 1, from the witnesses alone",
      "reasoning": "the decisive arguments, concretely, with the witnesses",
      "apparatus": "how the rejected reading should be recorded, or none" }
  ],
  "summary": "a few sentences: which places were hardest and why"
}
```

**Choices:**
- **1 or 2** — that edition's reading.
- **other** — a different reading, or a combination of parts of both. Give it in `other`.
- **doubt** — only where no reading can be defended. Then say in `other` what should be printed meanwhile.

Decide every place. Accuracy matters more than speed.
