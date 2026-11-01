# About the text, the translation and the German translation

## The work

Τῆς μουσικῆς σύνοψις ἠκριβωμένη, "A Precise Synopsis of Music", is the music section of an anonymous Byzantine *Quadrivium*: a short teaching compendium of logic and the four mathematical sciences.
- **Date.** In the astronomy section the author twice names the "present" year 6516 from the Creation (1007/1008).
- **Attribution.** The sixteenth-century printed editions put it under the name of Michael Psellos, and Mizler does the same ("Psellus").
- **Contents.** It is a compact textbook of harmonics:
  - note, interval, system, harmony;
  - the note names;
  - the division of the tone;
  - incomposite and composite intervals;
  - the consonances and their ratios;
  - how the ratios were found;
  - the systems and the three genera of the fourth;
  - modes and kinds of melody.

## The established Greek text (`units.json`, `edition.json`)

The Greek text in `units.json` has been newly established. It is divided into 67 units, U001–U067, in seven sections.

**Sigla:**

| Siglum | Source |
|---|---|
| Bas. | Basel 1556, ed. W. Xylander, Greek with Latin translation. Base text; every unit carries its Bas. page.line. |
| Xyl. | Xylander's marginal notes in Bas. |
| Par. | Paris 1545, a reprint of the editio princeps (Venice 1532). |
| H | Heidelberg, Pal. gr. 281, dated 1040. |
| V | Vatican, Pal. gr. 262, 15th c. |
| P | Paris. gr. 2448, known only from Vincent's publication (1847). |
| Vinc. | Vincent's publication of P and his corrections of it. |

**Signs in the Greek and in both translations:**
- ⟨ ⟩: a word supplied by the editor.
- ⟨⟨ ⟩⟩: a passage found only in P (U028–U032, U042–U044, U050).
- † †: an uncorrected corruption.
- [ ] in the translations: words added for clarity.
- [n:m]: the numerical value of a ratio name.

**`edition.json` is an extract from the edition.** It gives, section by section:
- the apparatus entries: the lemma, then the variants, with sigla;
- the places where the established text departs from Bas.: the Bas. reading, the adopted reading and the sources of the adopted reading.

It is selective. It does not record punctuation or most orthographic variation, and the edition's notes and its description of the sources are not supplied.

**"Edition" in the notes.** In the notes' `source` fields, "Edition" means this edition. Some notes cite details of the sources that are not in `edition.json`: punctuation, letter forms, marginal figures. Treat these as the edition's statements, not as evidence you have seen.

**Other sources you may consult:**
- **Heiberg's critical edition** (*Anonymi Logica et Quadrivium*, Copenhagen 1929) was not used for the established text. You may consult it if you find a legitimate digital copy.
- **Vincent (1847)** may be consulted for the Greek of the P passages. Do not use his French translation.

## The Russian and English translation (`units.json`)

Each unit has `ru`, `en` and `notes`. Each note has:
- `anchor_ru` and `anchor_en`: the words of the translation it belongs to;
- `ru` and `en`: the note itself;
- `source`: its references. The short references (author and year) are resolved in `bibliography.json`.

Both translations were made directly from the established Greek text and follow the conventions below. These conventions are declared choices. You may argue against a choice, but call it a choice, not an error, unless you show that it misrepresents the Greek.

- **Terms.** The text uses the term established in the field. Literal renderings and the Greek go into the notes.
  - Russian: «кварта, квинта, октава» for διὰ τεσσάρων, διὰ πέντε, διὰ πασῶν.
  - English: "the fourth, the fifth, the octave".
  - Greek appears in the text only at U033 and U035, where the author explains the names, and at U054.
- **The δίς names.** δὶς διὰ τεσσάρων, δὶς διὰ πέντε and δὶς διὰ πασῶν are rendered by their referents:
  - Russian: «октава с квартой», «октава с квинтой», «двойная октава»;
  - English: "the octave and a fourth", "the octave and a fifth", "the double octave".

  Only at U035, where the author explains these names, do the literal «двойная кварта / квинта / октава» / "double fourth / fifth / octave" appear.
- **Ratio names.**
  - Russian: calques in the form established in Russian translations of Greek theory, with the value in brackets. Examples: «сверхтретное [4:3]», «полуторное [3:2]», «сверхосминное [9:8]», «двукратное [2:1]», «двукратное сверхчастное [8:3]».
  - English: Greek-based terms, for example "epitritic [4:3]", "hemiolic [3:2]", "epogdoic [9:8]".
- **Systems.** ἑκκαιδεκάχορδον / πεντεκαιδεκάχορδον are «шестнадцатизвуковая / пятнадцатизвуковая система» / "sixteen-note / fifteen-note system". τετράχορδον, πεντάχορδον and ὀκτάχορδον stay «тетрахорд, пентахорд, октахорд».
- **Adjacent and non-adjacent.** ἄμεσα / ἔμμεσα διαστήματα are «интервалы между смежными / несмежными звуками» / "intervals between adjacent / non-adjacent notes".
- **Other terms:**
  - δύναμις: «значение» / "value"; ἰσχύς: «сила» / "force";
  - τριημιτόνιον: «трёхполутон» / "trihemitone";
  - μέλος: «напев» / "melody (μέλος)"; μελῳδία: «мелодия» / "melody";
  - σύμφθαρσις: «слияние» / "fusion".
- **Note names.**
  - Russian: in the forms of V. G. Tsypin's translations («просламбаномен», «гипата низших», «просто меса», «парамес»).
  - English: transliterated ("proslambanomenos", "hypate hypaton").

## Mizler's edition and translation (1746)

**The publication.** Lorenz Christoph Mizler, *Musikalische Bibliothek*, vol. III, part 2 (Leipzig, 1746), pp. 171–200, headed "Des Psellus vollständiger kurzer Inbegriff der Musik".
- The Greek and the German are printed in two columns, with notes keyed to the text.
- Mizler has no separate introduction. His first note, keyed to the word "Psellus" in the heading, begins at the foot of p. 171 and continues on pp. 172–173. In it he speaks:
  - on p. 172, about Alard's edition (Schleusingen, 1636);
  - on p. 173, about Xylander's Basel edition and his rule that Xylander's notes are marked "X".
- The text ends on p. 200 with "Ende".

**The digital copy.** archive.org, item `bub_gb_VGRDAAAAcAAJ` (the Bayerische Staatsbibliothek copy, digitised by Google). It is public domain and contains the whole of vol. III. The pagination is continuous through the volume.

**Leaves and pages.**

| Leaves | Pages |
|---|---|
| 214 | p. 171, the first page of the article, with the heading and no running head. `bub_gb_VGRDAAAAcAAJ_page_numbers.json` mislabels it "209". |
| 215–243 | pp. 172–200 |
| 212 | the title page of part 2 |
| 213 | the contents of part 2 |
| 176–211 | errata, plates and blanks, with machine-guessed page numbers. Ignore them. |

**Fetching the pages.**
- Fetch only leaves 214–243. Single page images are at `https://archive.org/download/bub_gb_VGRDAAAAcAAJ/page/n214.jpg` … `n243.jpg`; add `_w2000` before `.jpg` for a larger size. Check that `n216` shows p. 173.
- The whole-volume files are large (`_jp2.zip` about 500 MB, the PDF about 76 MB).
- `bub_gb_VGRDAAAAcAAJ_djvu.txt` is an OCR of the Fraktur that is poor, often wrong, and loses the Greek. Use it only to find things.

## The editions Mizler may have used

Consult these only to explain Mizler's Greek text and his translation:

| Edition | Copy | Where |
|---|---|---|
| Basel 1556, ed. Xylander (Bas.) | HathiTrust `ien.35552000251339` | Greek pp. 23–33; Xylander's Latin pp. 40–49 of the separately paginated Latin part |
| Paris 1545 (Par.) | MDZ `bsb10169572` | — |
| Alard, *De veterum musica liber singularis* (Schleusingen, 1636) | MDZ `bsb10598123` | scans 209–235: the Greek pp. 177–189, the Latin pp. 189–203 |

MDZ images: `https://api.digitale-sammlungen.de/iiif/image/v2/<id>_<scan number, 5 digits>/full/full/0/default.jpg`.
