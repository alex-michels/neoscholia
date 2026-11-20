# About the texts and the conventions

## 1. The work

- **What it is.** An anonymous Byzantine school compendium of 1007/1008 (the author names "the present year" 6516 of the Byzantine era in the astronomy section). A synopsis of logic is followed by synopses of the four mathematical sciences: arithmetic, music, geometry and astronomy.
- **The music section** is a compact textbook of harmonics:
  - note, interval, system, harmony;
  - the names of the notes;
  - the division of the tone;
  - incomposite and composite intervals;
  - the consonances and their ratios;
  - how the ratios were found on strings, weights and wind instruments;
  - the systems and the three genera of the fourth;
  - modes and kinds of melody.
- **Attribution.** The sixteenth-century printings put the work under the name of Michael Psellus, and both Latin versions call him Psellus. This is impossible (Psellus was born in 1018). Keep the name where the Latin has it; you may say so in a note.

## 2. The two Latin versions

| Version | Translator | Printing used here |
|---|---|---|
| **Xylander** | Guilielmus Xylander (Wilhelm Holtzmann, 1532–1576), humanist, later professor of Greek at Heidelberg. | Basel: Oporinus, [1556], a Greek and Latin volume of the four mathematical sciences "of Psellus". The Latin of the music section is on pp. 40–49, headed *Exacta summa hic, evidensque Musicae*. His marginal notes «Vide Annot.» refer to annotations printed elsewhere in the volume; they are not supplied (see PROMPT.md, rule 2). |
| **Vinet** | Élie Vinet (1509–1587), humanist, principal of the Collège de Guyenne at Bordeaux. | His Latin version of the four sciences was first printed in the 1550s; here it is the printing of Tournon, 1591, pp. 41–53. The music section is divided into five chapters with headings, and the chapters into numbered paragraphs (cited I.1, II.3 and so on). |

The two versions differ in vocabulary and often in the construction of a passage. Translate each on its own terms.

## 3. The file `latin-texts.json`

- **Segments.** Each version is divided into segments, in order; together they are the whole text. The boundaries were set so that the two versions can later be set side by side; a segment may begin or end inside a Latin sentence. Each segment has:
  - `id`;
  - `starts_paragraph`, if the segment begins a paragraph of the printing: for Vinet his printed paragraph number (I.1 and so on); for Xylander, whose printing has five long paragraphs without numbers, the numbers 1–5; `title` and `closing formula` mark the title and the last line;
  - `heading: true` for Vinet's chapter headings;
  - `ref`, page.line of the printing where the segment begins and ends;
  - `latin`, the reading text;
  - `printed`, the printed lines on which the segment stands. These are whole lines, so neighbouring segments may share a line.
- **`latin`, the reading text.**
  - Normalised spelling: u/v, i/j; ae and oe for æ, œ and the e caudata; no printers' accents.
  - Abbreviations expanded; obvious misprints corrected.
  - Decorative capitals after an initial in normal case; Vinet's chapter numbers as Roman numerals (printed «CAPVT 1.» etc.).
  - Vinet writes the interval names with a hyphen (*Dia-tessaron*, *Dia-pente*, *Dia-pason*).
- **`printed`, the diplomatic transcription.** Long s as s and abbreviations expanded, but u/v, i/j, accents, capitals, punctuation, line-end hyphens and misprints as printed.
- **How the texts were established.** Each printing was transcribed twice, independently, and every difference was decided against the page images. The reading text was then checked word by word against the agreed diplomatic text. `corrections` lists every place where the reading text departs from the printed letters.
- **Page images.** `scans/` holds the printed pages: `xylander-pNN.jpg` (pp. 40–49) and `vinet-pNN.jpg` (pp. 41–53).

## 4. Conventions of the translation

These conventions are the project's and apply to all its translations. Follow them; where you think one misrepresents the Latin at a given place, follow it all the same and say so in a note.

### 4.1 The general rule

The running text uses the **established term of the field that a modern reader understands**. The Latin word, calques, literal renderings and explanations go into the notes. Example: «кварта, квинта, октава» / "the fourth, the fifth, the octave" in the text; *diatessaron* "through four" in a note.

- Where the field has no term, a plain description in the text is better than a term borrowed from another discipline.
- Do not coin words that are not attested in the literature.
- Where a translator explains a name (its etymology or its parts), keep the explanation readable: give the established term and the literal rendering side by side, or explain in a note.

### 4.2 Intervals and their names

| Latin (as in the texts) | Russian | English |
|---|---|---|
| diatessaron (Vinet: Dia-tessaron) | кварта | the fourth |
| diapente (Dia-pente) | квинта | the fifth |
| diapason (Dia-pason) | октава | the octave |
| disdiapason, bis diapason | двойная октава | the double octave |
| diapason (cum) diatessaron | октава с квартой | the octave and a fourth |
| diapason (cum) diapente | октава с квинтой | the octave and a fifth |
| tonus | тон | tone |
| semitonium, hemitonium | полутон | semitone |
| diesis | диеса | diesis |
| tridiesis | тридиеса | tridiesis |
| trisemitonium, trihemitonium | трёхполутон | trihemitone |
| ditonus, ditonium | дитон | ditone |
| tritonus, tritonium | тритон | tritone |
| intervallum | интервал | interval |
| compositum / incompositum (non compositum) intervallum | составной / несоставной интервал | composite / incomposite interval |

Render each interval name by the established name of the interval the translator means. Where a name taken literally would denote another interval in standard usage, explain in a note.

### 4.3 Ratios

The ratio follows in square brackets **at every occurrence** of a ratio name in the running text, also where the Latin gives no numbers: «полуторное [3:2]». The bracket gives the ratio that the Latin names, as you compute it from the text.

| Latin | Russian | English |
|---|---|---|
| duplus, dupla, duplex | двукратное [2:1] | duple [2:1] |
| triplus, triplex | трёхкратное [3:1] | triple [3:1] |
| quadruplus, quadruplex | четырёхкратное [4:1] | quadruple [4:1] |
| quincuplus, quincuplex | пятикратное [5:1] | quintuple [5:1] |
| sesquialter, sesquialtera | полуторное [3:2] | sesquialter [3:2] |
| sesquitertius, sesquitertia | сверхтретное [4:3] | sesquitertian [4:3] |
| sesquiquartus | сверхчетвертное [5:4] | sesquiquartan [5:4] |
| sesquioctavus, sesquioctava | сверхосминное [9:8] | sesquioctave [9:8] |
| semisesquioctava | полусверхосминное (no bracket where the text says what it is) | semisesquioctave |
| duplex superpartiens, duplus superpartiens | двукратное сверхчастное [8:3] | duple superpartient [8:3] |

- The Russian forms are the calques of the Russian translations of the theorists by V. G. Tsypin and S. N. Lebedev (Lebedev's of Boethius and Guido among them). In their usage «сверхчастное» renders *superpartiens* and «сверхчастичное» *superparticularis*; A. I. Shchetnikov uses «сверхчастное» the other way round, for *superparticularis*. Agree the adjective with its noun, or with «отношение» understood.
- The English forms are those of C. M. Bower’s translation of Boethius, *Fundamentals of Music* (1989): duple, sesquialter, sesquitertian, sesquiquartan, sesquioctave, superparticular, superpartient. The Latin versions themselves use the Boethian names, so the Greek-based English forms (hemiolic, epitritic, epogdoic) are not used here.
- Where the Latin names a ratio not in this table, form its name on the same pattern in each language and record it in `terms`.
- Ordinary «двойной», «вдвое» for *duplus*, *duplo* where no ratio name is meant stays ordinary.

### 4.4 Notes of the two-octave system

| Latin (as in the texts) | Russian | English |
|---|---|---|
| proslambanomenos | просламбаномен | proslambanomenos |
| hypate hypaton | гипата низших | hypate hypaton |
| parhypate hypaton | парипата низших | parhypate hypaton |
| hypate diatonos | гипата диатоническая | hypate diatonos |
| hypate meson | гипата средних | hypate meson |
| parhypate meson | парипата средних | parhypate meson |
| diatonos meson | диатоническая средних | diatonos meson |
| mese | меса | mese |
| paramesos, paramese | парамес (paramesos) / парамеса (paramese), as printed | paramesos / paramese, as printed |
| trite diezeugmene | трита отделённая | trite diezeugmene |
| diatonos diezeugmene | диатоническая отделённая | diatonos diezeugmene |
| nete diezeugmene | нета отделённая | nete diezeugmene |
| trite / diatonos / nete hyperbolaeon | трита / диатоническая / нета высших | trite / diatonos / nete hyperbolaion |

Keep the names as the version gives them. Where a name differs from the usual nomenclature, say so in a note.

### 4.5 Other terms

| Latin | Russian | English |
|---|---|---|
| sonus, sonitus (a musical note) | звук | note |
| systema | система | system |
| tetrachordum, pentachordum, octachordum | тетрахорд, пентахорд, октахорд | tetrachord, pentachord, octachord |
| harmonia | гармония | harmony |
| genus diatonicum, chromaticum, harmonicum | диатонический, хроматический, гармонический род | the diatonic, chromatic, harmonic genus |
| consonantia; consonare | консонанс; консонировать | consonance; to be consonant |
| intensio et remissio, as a pair (of pitch) | повышение и понижение | raising and lowering |
| acutus / gravis (of pitch) | высокий / низкий | high / low |

- Other words, including *intensio* on its own and the words of melody and song (*melodia*, *cantilena*, *modulatio*, *cantus*), are yours to render by context. Keep each Latin word's rendering consistent within a version, and record your choice in `terms`.
- The numbers in square brackets after a ratio name are the only numerals you add. Do not add modern note letters or cents to the running text.

### 4.6 Signs and form

- Words added for clarity in [square brackets].
- Vinet's chapter headings (`heading: true`) are translated as headings.
- In `translation.md`, start a new paragraph where a segment has `starts_paragraph`.

## 5. Russian and English terminology (for orientation)

- **Russian:** V. G. Tsypin's translations of Ptolemy's *Harmonics* with Porphyry's commentary (2013) and of Cleonides' *Introduction to Harmonics* (2014); S. N. Lebedev's translations of Boethius, *De institutione musica* (2012), and of Guido's *Micrologus* (2023); A. I. Shchetnikov's translations of Nicomachus, Theon of Smyrna and the *Sectio canonis*.
- **English:** for Greek harmonics, A. Barker, *Greek Musical Writings* II (1989); for Latin theory, C. M. Bower's translation of Boethius, *Fundamentals of Music* (1989).
