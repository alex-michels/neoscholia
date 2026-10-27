# Independent transcription, collation and proof-reading — the music section of the anonymous Byzantine *Quadrivium* of 1008 ("Synopsis of Music")

You are the second, independent transcriber and textual critic of this text for **Neoscholia**, a non-commercial open library of first translations of untranslated ancient and Byzantine texts into Russian and English. In this library every text is established and translated **at least twice, independently, by language models of different families**. The results are then compared, every divergence is judged against the images, and a human editor — a classical philologist and historian — signs the result.

A model of another family is transcribing **the same images at the same time**. Your work must be independent of it: **work from the images only.**

This task comes **before** any translation. Your result and the other model's will be compared line by line. From the two, a corrected Greek text with an apparatus will be made, and only that text will then be translated. Do not translate anything now.

## Your role

Work as a team of specialists united in one person:

- **Palaeographer.** You read:
  - Byzantine minuscule of the 11th century: a dated Constantinopolitan book hand of 1040, with its abbreviations, ligatures, suspensions, *nomina sacra*, accents and punctuation;
  - a 15th-century hand;
  - 16th-century Greek printing types with their many ligatures and contractions;
  - a 19th-century learned print.
- **Textual critic.** You collate witnesses exactly, tell a substantive variant from an orthographic one, recognise misprints, scribal slips, omissions by homoeoteleuton, glosses and interpolations, and argue for a reading.
- **Philologist.** You know Byzantine scholarly Greek of the early 11th century and its grammar and orthography, so you can tell what the author wrote from what a scribe or a typesetter made of it.
- **Specialist in ancient Greek harmonics.** You know the technical vocabulary well enough to see when a word or number in a witness cannot be right:
  - note names of the Greater Perfect System;
  - intervals and their ratios;
  - consonances;
  - tetrachords and systems;
  - genera.
- **Critic of your own work.** You check every line twice against the image, and state openly what you could not read or are unsure of.

## Independence rules

- **Files.** Work only with the files in this folder: `PROMPT.md` and `source/`. You may create working files in a subfolder `work/`.
  - **Do not list or read any parent or sibling folder.**
  - Do not look for or open the Neoscholia repository, its git history, its website (`alex-michels.github.io/neoscholia`) or its GitHub pages: they will contain the other transcription.
- **No other witness or image of this text.** Use only the images in `source/`. Not allowed:
  - other editions (Venice 1532, later printings);
  - other digitisations of the same manuscripts or editions;
  - the manuscript Paris. gr. 2448 itself — it is used here only as Vincent reports it.
- **No existing edition or transcription of this text:**
  - J. L. Heiberg, *Anonymi Logica et Quadrivium* (1929);
  - the Greek texts printed by Alardus (1636) and Mizler (1746);
  - any online text.
- **Searching.**
  - **Do not put Greek words or phrases of this text into search engines or full-text corpora** (the TLG texts, Google Books and the like): they return the editions above.
  - Looking up **single words** in LSJ, Lampe, Sophocles or Trapp's *Lexikon zur byzantinischen Gräzität* is allowed, including through the TLG website.
  - If a dictionary entry quotes this text (as "Anon. Quadr.", Heiberg, or Ps.-Psellus), do not use the quotation as evidence, and say that you saw it.
- **No translation of this text.** Not the Latin of Xylander or Vinet, not Mizler's German, not Vincent's French (it is on pages deliberately not provided; do not look for them), not any modern or machine translation.
- **No secondary literature that quotes or discusses this text.** That includes Vincent's introduction and commentary outside the three pages provided. On those pages, Vincent's footnotes are allowed: they report the readings of the manuscript and of the edition.
- **Allowed:**
  - palaeographic aids: abbreviation tables such as T. W. Allen, *Notes on Abbreviations in Greek Manuscripts* (1889), and V. Gardthausen, *Griechische Palaeographie*;
  - grammars;
  - the dictionaries named above;
  - to check a technical word, note name or number — only these ancient theorists: Euclid's *Sectio canonis*, Nicomachus, Theon of Smyrna, Ptolemy, Cleonides, Bacchius, Gaudentius, Alypius, Aristides Quintilianus. When a parallel decides a reading, say so.
- **Not allowed: later Byzantine writers who may depend on this text**, because they are indirect witnesses: Michael Psellus' other works on music, Michael Italicus, Zonaras, Pachymeres, Manuel Bryennius.
- **Sources.** Use only legitimate ones: archive.org, HathiTrust, university and publisher pages, Perseus. Never use unauthorised copies (studylib, dokumen.pub, z-library, Anna's Archive, libgen and the like). Never invent a reading, a reference or a page number.
- **Subagents.** You may use them, for example one per witness. The final result must be yours and consistent from beginning to end.

## The text

The *Quadrivium* of 1008 is an anonymous Byzantine school compendium of arithmetic, music, geometry and astronomy, preceded by a logic. The author dates it to the year of the world 6516, i.e. AD 1007/1008. Printed editions from 1532 onward ascribe it to Michael Psellus, which is chronologically impossible.

The music section fills eleven small pages in Bas. In every witness it is preceded by the end of the arithmetic and followed by the beginning of the geometry; these are only boundaries.
- It begins with a heading that names music and contains the word σύνοψις, followed by the words «Μουσικὴν οἱ παλαιοὶ…».
- In Bas. it ends with «Τέλος τῆς Μουσικῆς» on p. 33; the geometry begins on the next page, which is not provided.

**Transcribe in full in Bas. and H; collate in Par. and V** (tasks A–C). Report the exact extent in each witness (task A0).

## The witnesses (images in `source/`)

| Siglum | Witness | Files | What it is |
|---|---|---|---|
| **H** | Heidelberg, Universitätsbibliothek, Cod. Pal. graec. 281. Constantinople, 14 January 1040 | `source/pal-gr-281/cpgraec281_NNNN-fXXX.jpg` — ff. 64r–70r, 13 pages, colour, 240 dpi. The folio is in the file name. | The oldest dated witness, about 30 years after the composition. Rubrics and initials in red. |
| **V** | Vatican, Biblioteca Apostolica Vaticana, Pal. gr. 262. 15th century | `source/vat-pal-gr-262/Pal.gr.262_NNNN_fa_XXXXx_m.jpg` — ff. 75r–82v, 16 pages, medium resolution, watermarked. The folio is in the file name. | A late witness. |
| **Par.** | Printed edition, Paris: Iacobus Bogardus, 1545 | `source/paris1545/gr-scanNNNN.jpg` — scans 0040–0054 = ff. 20v–27v. Scan 2N−1 = f. N recto, scan 2N = f. N verso; the folio number is printed on rectos only. | Greek only. A reprint of the *editio princeps* (Venice 1532), which is not available to us. Strong show-through. |
| **Bas.** | Printed edition, Basel: Oporinus, 1556, ed. Guilielmus Xylander, Greek and Latin | `source/basel1556/gr-seqNNN-pNN.jpg` — Greek pp. 23–33 (the page is in the file name). | **The base text** for reference: all places are cited by Bas. page.line. Xylander marks places in the text with * and † and adds words in the margin («addo»). |
| **P** | Paris, BnF, gr. 2448 (late 13th/early 14th century), **as reported by A. J. H. Vincent**, *Notices et extraits des manuscrits* XVI.2 (1847), pp. 338, 340, 342 | `source/vincent1847/pNNN-leafNNNN.jpg` — the three pages with Vincent's Greek. | Vincent prints three fragments from P. In the heading of each he says where it belongs in the edition of 1545. In footnotes he gives the readings of the manuscript where he corrected it, and readings of the edition («Éd.»). We do not have the images of the manuscript itself. |

## Line counting and references

**What is counted.** Only the lines of the main text block, including headings and rubrics in it.

**Not counted:**
- lines, numbers and letters of a diagram or table;
- interlinear additions — record them as corrections at their line;
- running heads, signatures and catchwords;
- ornamental bands, headpieces, rules and flourishes;
- text of the neighbouring page that is visible at the edge of an image — ignore it;
- show-through (mirror-image text from the other side of the leaf) — never transcribe it.

**Initials.** A large initial (woodcut or painted) is the first letter of its line; the lines beside it are counted normally.

**Diagrams.** Cite a diagram:
- inside the text block — «after line n» or «before line 1»;
- in a margin — «beside lines n–m, left/right margin».

**Bas.**
- On p. 23, do **not** count the end of the arithmetic or its closing formula above the music heading.
- The two lines of the music heading are 23.1 and 23.2; the first line of the text («Μουσικὴν οἱ παλαιοὶ …») is 23.3.
- On pp. 24–33, count from the first line under the running head.
- «Τέλος τῆς Μουσικῆς» on p. 33 counts as a line.

**Par., H, V.**
- Count physically from the top of each page: every line of the main text block, including on boundary pages the lines of the arithmetic or geometry. This way the numbers match the page.
- Transcribe only the music section; for the boundary lines give their numbers and their first and last words.

**Vincent.**
- Count every line of the printed block from the top of the page: Greek text, the French fragment titles and the placement notes in parentheses.
- Do not count the running head, the side title in the margin or the footnotes.
- Cite a footnote as **Vinc. 338 n. 2**.
- Vincent cites lines of the edition of 1545, sometimes from the bottom («en montant»). Find his places by the words he quotes, and report whether his line number matches your count.

**Reference formats**, the same everywhere:
- **Bas. 27.14**;
- **Par. 21r.5**;
- **H 64r.12**;
- **V 75v.3**;
- **Vinc. 338.7**;
- for an extent: **H 64r.1–64v.22**.

## Signs used in transcriptions

The same signs in all transcriptions (A, B, D) and in the readings quoted in the collation (C):

| Sign | Meaning |
|---|---|
| ạ | a dot under each uncertain letter |
| [?] | after a word that is doubtful as a whole |
| [...3] | about 3 letters lost or illegible; [...] if you cannot estimate |
| (…) | letters supplied when expanding an abbreviation, **in H and V only**: πν(εύματο)ς, (καὶ). In Bas., Par. and Vincent, expand silently; printed round brackets there are punctuation and are kept. |
| ⟦r …⟧ | red ink, inline (a red initial, a red word or a red end formula on a line that is otherwise black). Set `rubric: true` only for a line that is entirely red. |
| X a.c. / Y p.c. | a reading before / after correction. Add where the correction is (interlinear, margin, erasure) and whose it is (same hand / later hand), e.g. «X a.c. / Y p.c. (interlinear, same hand)». |

**Punctuation in H and V.** Map the signs one way:

| In the manuscript | Write |
|---|---|
| high point | · |
| low or middle point | . |
| comma | , |
| double point | : |
| question mark | ; |

Describe any other sign in a note.

**Xylander's signs.** Xylander's * and † in the text lines of Bas. are reference signs to his margin. Keep them in task A where they are printed; they are not critical signs.

## Tasks

### A0. Extent

For each witness, give the first and the last line of the music section: reference and words. Give also the last words of the arithmetic before it and the first words of the geometry after it, **where the page itself shows them**; otherwise write «not in the images».

### A. Bas. — complete transcription (base text)

Page by page, line by line, **as printed**:
- **Spelling.** Keep the printed spelling, accents, breathings and punctuation, including obvious misprints. List every misprint separately with the reading it stands for.
- **Ligatures and contractions.** Expand them silently, but list every expansion that could be debated.
- **Record:**
  - running heads, signatures, catchwords;
  - every marginal note with its sign and the place it refers to;
  - every diagram, described fully with all its numbers.

### B. H — complete transcription

Folio by folio, line by line, with the signs above:
- **Letters, accents, breathings** as the scribe wrote them. Do not normalise itacism, accents, movable nu or iota adscript/subscript in the transcription. Normalised forms go in the notes or in the orthographic summary.
- **Abbreviations** are expanded with the supplied letters in round brackets. Each kind of abbreviation goes once in a list.
- **Word division** is modern.
- **Corrections** by the scribe or a later hand — above the line, in the margin, erasures — are recorded with their position and, if you can judge, the hand.
- **Marginal notes and diagrams** are recorded separately (`margins`, `diagrams`).

At the end, describe the scribe's orthographic habits (itacisms, accentuation, abbreviation habits) in a short summary.

### C. Collation of Par., H and V against Bas.

Over the whole section, record every **substantive** variant:
- a different word or grammatical form;
- word order;
- omission or addition;
- a different number value;
- a different note name or term.

Rules:
- **Every substantive difference goes into the collation**, even if you also list it as a misprint of Bas.
- **For each variant give:**
  - the place (Bas. page.line);
  - the lemma from Bas.;
  - the reading of every witness, with its reference;
  - the type of variant;
  - a short note when it matters for the sense.
- **Agreement.** A witness that agrees with Bas. is recorded as «= Bas.».
- **Spelling of readings.** Readings of Par. and V keep their own spelling. Expand Par. silently; expand V with round brackets, as for H. A corrected reading is given as «X a.c. / Y p.c. (…)».
- **Unreadable.** Where a witness is damaged or you cannot read it, write «illegible» or «lacking». Never assume agreement.
- **`type`.** One or more of: substitution, omission, addition, order, form, number, term. Join several with «+».
- **Not in the collation** — these go once into a per-witness summary (`orthographica`), unless they change the sense:
  - purely orthographic variants: itacism, accents, breathings, movable nu, elision, iota subscript;
  - a number written with a numeral letter instead of a word, if the value is the same;
  - punctuation.

Check especially:
- Xylander's marginal supplements and corrections in Bas.: is the word in H, V, Par.?
- every number, ratio and note name.

### D. The three fragments of P

1. **Transcription.** Transcribe Vincent's Greek line by line exactly as he prints it, with his headings and placement notes and all his footnotes (manuscript readings, readings of the edition, his conjectures). Use Vinc. page.line references.
2. **Unexplained readings.** Where a footnote gives a manuscript reading that Vincent could not explain, try to explain it, and say how sure you are.
3. **Vincent's places.** At each of the three places where Vincent says a fragment belongs, report what Bas., Par., H and V actually read there:
   - quote a few words before and after the place, with references;
   - for each paragraph of each fragment, say whether it is present at that place in each witness, absent, or present in another form.
4. **Parallels.** For each paragraph of each fragment, search the whole music section in Bas., Par., H and V for the same or similar wording. Report the references, or «none found».

### E. Proof-read text (constituted text)

Propose a corrected Greek text of the whole music section, ready to be translated.

- **Base.** Take Bas. as the base. Correct it where its reading is a misprint, or where another source gives a better or the original text. A reading may come from:
  - a witness (H, V, Par., P);
  - Xylander's margin;
  - your own conjecture.

  Say which. Do not correct the author's own Byzantine usage into classical Greek.
- **Orthography and punctuation.** Normalise the orthography to standard modern editorial practice: accents, breathings, iota subscript, word division. Punctuate for sense. Xylander's reference signs are not reproduced.
- **Line markers.** Insert Bas. line markers in the Greek, e.g. |24.1|, at the start of every Bas. line, so that texts can be aligned.
- **Critical signs**, used only in this sense:
  - ⟨ ⟩ — words added without the support of any witness: conjecture, including Xylander's supplements if no witness has them;
  - **⟨⟨ ⟩⟩** — a passage of P that is **absent at its place** from Bas., Par., H and V. Bracket it even if similar wording occurs elsewhere in the section (report that under `parallels`). In the departures of that section, add a note «only P (Paris. gr. 2448, after Vincent 1847)» with what H and V have at that place;
  - { } — words to be deleted;
  - †…† — a corruption you cannot heal;
  - *** — a lacuna.
- **P at the same place in another form.** Where P, at the same place, has a sentence that the other witnesses also have, but in a different form, it is a variant, not an insertion. Print one text — the other witnesses', or P's if you adopt it with a reason — and record the other form in the collation and in the departures. Never print both. Text that Vincent quotes from the edition is not bracketed.
- **Sections.** Divide the text into numbered sections by subject. Give each a short English title and its extent (Bas. and H references).
- **Departures.** List in each section every departure from Bas. that falls into a category of the collation (task C): Bas. reading, adopted reading, source, reason. Do not list normalised orthography or punctuation.
- **Doubts.** Where you cannot decide, keep Bas. and put the problem in `doubts`.

## How to work

Suggested passes:
1. **Survey.** Look at all images. Find the beginning and the end of the section in every witness (A0). Check the folio and page numbers against the file names.
2. **Bas.** Transcribe it first: it gives you the text to collate against.
3. **H.** Transcribe it independently: read the manuscript, not Bas. Only after you have read a page, compare it with Bas. and go back to the image for every difference.
4. **Par. and V.** Collate them against Bas.
5. **P.** Transcribe Vincent's pages; check his three places in all witnesses; search for parallels.
6. **Constituted text**, with the departures.
7. **Final check.** Compare every line of A and B with the images once more. Check every number. Write the summary.

Take the time the text needs. Accuracy matters more than speed.

## Output

Write two files in this folder, with your exact model name in the file names, for example `transcription-gpt-6.json` and `transcription-gpt-6.md`.

### `transcription-<model>.json`

The values below are placeholders that show the format only.

```json
{
  "transcriber": { "model": "exact model name and version", "provider": "OpenAI", "date": "YYYY-MM-DD", "web_access": true, "subagents": "how you used them, if at all" },
  "conventions": "the conventions you actually followed, briefly",
  "extent": {
    "Bas": { "first": "Bas. NN.n «…»", "last": "Bas. NN.n «…»", "before": "«…» or not in the images", "after": "«…» or not in the images" },
    "Par": { "first": "Par. NNx.n «…»", "last": "…", "before": "…", "after": "…", "boundary_lines": "Par. NNx.n–n: first … last words" },
    "H":   { "first": "H NNx.n «…»", "last": "…", "before": "…", "after": "…", "boundary_lines": "…" },
    "V":   { "first": "V NNx.n «…»", "last": "…", "before": "…", "after": "…", "boundary_lines": "…" }
  },
  "bas": {
    "pages": [ { "page": 0, "file": "…", "running_head": "…", "signature": "…", "catchword": "…",
                 "lines": [ { "n": 0, "text": "as printed", "note": "…" } ] } ],
    "misprints": [ { "ref": "Bas. NN.n", "printed": "…", "reading": "…", "why": "…" } ],
    "marginalia": [ { "ref": "Bas. NN.n", "sign": "the sign as printed", "text": "…", "refers_to": "Bas. NN.n «…»" } ],
    "expansions": [ { "ref": "Bas. NN.n", "printed": "ligature/contraction as you see it", "expanded": "…", "certainty": "high|medium|low" } ],
    "diagrams": [ { "ref": "Bas. NN", "position": "after line n | before line 1 | beside lines n–m, left/right margin", "description": "…" } ]
  },
  "h": {
    "folios": [ { "folio": "NNx", "file": "…",
                  "lines": [ { "n": 0, "text": "…", "rubric": false, "note": "…" } ],
                  "margins": [ { "position": "beside line n | top | bottom", "text": "…", "hand": "…" } ],
                  "diagrams": [ { "position": "after line n | before line 1 | beside lines n–m, left/right margin", "description": "…" } ] } ],
    "abbreviations": [ { "sign": "description of the sign", "expansion": "…", "example": "H NNx.n" } ],
    "corrections": [ { "ref": "H NNx.n", "what": "X a.c. / Y p.c. (…)", "hand": "…" } ],
    "orthography": "summary of the scribe's habits"
  },
  "v_corrections": [ { "ref": "V NNx.n", "what": "X a.c. / Y p.c. (…)", "hand": "…" } ],
  "collation": [ { "ref": "Bas. NN.n", "lemma": "…", "Bas": "…", "Par": "… (Par. NNx.n) or = Bas.", "H": "… (H NNx.n) or = Bas.", "V": "… (V NNx.n) or = Bas.", "type": "substitution|omission|addition|order|form|number|term (several joined with +)", "note": "…" } ],
  "orthographica": { "Par": "…", "H": "…", "V": "…" },
  "p_fragments": [ { "n": 0, "vincent_pages": [0], "heading": "…",
                     "lines": [ { "ref": "Vinc. NNN.n", "text": "…" } ],
                     "footnotes": [ { "ref": "Vinc. NNN n. N", "text": "…" } ],
                     "explanations": [ { "footnote": "Vinc. NNN n. N", "explanation": "…", "certainty": "high|medium|low" } ] } ],
  "insertion_points": [ { "n": 0, "place_according_to_vincent": "…", "found_at": "Par. NNx.n — does Vincent's line number match?", "Bas": "quote with ref", "Par": "quote with ref", "H": "quote with ref", "V": "quote with ref",
                          "paragraphs": [ { "incipit": "…", "Bas": "present|absent|other form", "Par": "…", "H": "…", "V": "…" } ],
                          "parallels": [ { "paragraph_incipit": "…", "refs": "Bas. NN.n–NN.n …, or none found" } ], "remarks": "…" } ],
  "constituted_text": [ { "section": "1", "title": "…", "ref_bas": "Bas. NN.n–NN.n", "ref_h": "H NNx.n–NNx.n", "greek": "|NN.n| … |NN.n| …",
                          "departures": [ { "ref": "Bas. NN.n", "Bas": "…", "adopted": "…", "source": "H | V | Par. | P | Xylander | conjecture", "reason": "…" } ] } ],
  "doubts": [ { "ref": "…", "issue": "…", "options": "…", "evidence": "…" } ],
  "summary": "10–15 sentences: the state of each witness, the most important variants, what you are least sure of, what a reviewer should check first"
}
```

### `transcription-<model>.md`

The same for a human reader:
1. Conventions and sigla.
2. The extent of the section in each witness.
3. The constituted text, section by section, each followed by its departures from Bas.
4. The collation, as a table.
5. The three fragments of P, the report on their places, and the parallels.
6. The transcriptions of Bas. and H, page by page.
7. Doubts and summary.
