# About the text

## 1. The work

- **What it is.** An anonymous Byzantine school compendium. A synopsis of logic is followed by synopses of the four mathematical sciences: arithmetic, music, geometry and astronomy. Music is the second of the four. Its heading is *Τῆς μουσικῆς σύνοψις ἠκριβωμένη*.
- **Date.** The author twice gives "the present year" as 6516 of the Byzantine world era, i.e. AD 1007/1008, both times in the astronomy section. The oldest dated manuscript, Heidelberg, Pal. gr. 281, was written in 1040.
- **Author.** The editor of the first printed edition (Venice 1532), Arsenios of Monemvasia, left it open whether the author was Michael Psellus, "as most think", or a Euthymios. Later prints put Psellus on the title page. This is impossible, since Psellus was born in 1018. Here the author is called **the Anonymous** and the work **the Quadrivium of 1008**.

## 2. The text you translate

`greek-text.json` holds a new critical text of the music section, established in 2026 from the witnesses below. Every witness was transcribed twice, independently. Where the witnesses or the readings disagreed, the decision rests on the witnesses, the author's usage, grammar, the lexica and the ancient theorists.

| Siglum | Witness |
|---|---|
| **Bas.** | Basel [1556], printed by Oporinus, edited by Wilhelm (Guilielmus) Xylander; pages 23–33. It is the base text and gives the reference grid (page.line). It was set from the earlier printed text (Venice 1532 or its reprint, Par.). |
| **Xyl.** | Xylander's notes in the margin of Bas. They are his conjectures, and they appear in the apparatus. |
| **Par.** | Paris 1545 (Jacques Bogard), a reprint of the first edition (Venice 1532). |
| **H** | Heidelberg, Pal. gr. 281, AD 1040. The oldest witness. |
| **V** | Vatican, Pal. gr. 262, 15th century. |
| **P** | Paris, gr. 2448, late 13th/early 14th century; it contains the whole music section. This edition uses it only as reported by Vincent in 1847 (*Notices et extraits des manuscrits* 16.2; do not open it, see PROMPT.md, rule 2). Vincent printed three passages that the other witnesses lack, with some adjacent words, and gave P's own readings in footnotes, so P is cited only at those places. The words found only in P are printed within ⟨⟨ ⟩⟩. They are P's text and are not claimed for the text of 1008. |
| **Vinc.** | A correction that Vincent printed in his text of P. |

The **apparatus** in `greek-text.json` is positive: `lemma witnesses] variant witnesses`, with om. (omits), add. (adds), del. (deletes) and coni. (a conjecture of this edition). Where the printed text rests on a conjecture or on one witness, the apparatus says so.
- The lemma before `]` is always the printed text. Readings after `]` or `|` are not printed.
- A coni. after `]` or `|` is a conjecture that was considered and not adopted.
- "Vinc. in nota" is a suggestion in Vincent's footnote; (dub.) means he was tentative.
- fort. = perhaps; `{ }` = words one might delete; prius / alterum = the first / second occurrence.
- P (Vinc.) = P's reading as Vincent reports it. "Vinc. 338.4" = Vincent 1847, page 338, line 4.

## 3. Signs in the Greek

- `|25.7|` marks the start of line 7 on page 25 of Bas. It is a reference, not part of the text. It also stands inside a word where Bas. divides the word at a line end.
- `⟨ ⟩` encloses words that no witness has and that the edition adds.
- `⟨⟨ ⟩⟩` encloses a passage found only in P.
- `†…†` encloses a corrupt word that the edition cannot heal.
- Punctuation and paragraphs are the edition's, set for sense.
- Bas., Par. and V have figures of dots in the margin at 26.14 and 26.18 (a square of 4 × 4 and a rectangle of 4 × 8). The edition does not print them.

## 4. What the edition keeps as transmitted

The edition does not bring the author's usage into line with classical Greek or with the standard handbooks. Where the witnesses agree, it keeps unusual forms and terms as they stand, even where a handbook writer would put it differently. Translate what is printed. If you think the author erred, or a scribe did, say so in a note or a doubt. Do not correct it in the translation.

## 5. Russian terminology in published translations of other theorists (for orientation)

The forms below are V. G. Tsypin's, from his own published Russian translations and articles on *other* Greek theorists (Aristoxenus, Ptolemy, Aristides Quintilianus, Ps.-Plutarch). They are not translations of this text. Use them as one reference among others. Choose your own Russian terms, keep them consistent, and justify them in `terms`.

| Greek | Tsypin |
|---|---|
| προσλαμβανόμενος | просламбаномен |
| ὑπάτη / παρυπάτη / λιχανὸς ὑπάτων | гипата / парипата / лихана низших |
| ὑπάτη / παρυπάτη / λιχανὸς μέσων | гипата / парипата / лихана средних |
| μέση, παραμέση | меса, парамеса |
| τρίτη / παρανήτη / νήτη διεζευγμένων | трита / паранета / нета отделённых |
| … συνημμένων / … ὑπερβολαίων | … соединённых / … высших |
| σύστημα τέλειον (μεῖζον) | (большая) полная система |
| γένος διατονικόν, χρωματικόν, ἐναρμόνιον | диатоника, хроматика, энармоника |
| συμφωνία / διαφωνία | консонанс / диссонанс |
| δίεσις, λεῖμμα | диеса, лимма |
| σύνθετον / ἀσύνθετον διάστημα | составной / несоставной интервал |
| ἁρμονική / ἁρμονικοί | гармоника / гармоники (the theorists) |

Another school of Russian translators (L. V. Aleksandrova, T. G. Myakin, on Ptolemy) uses partly different forms, e.g. паргипата, диатон, эпогдоон, эпитрит, полуторное.

For English, the standard terminology of the field is A. Barker, *Greek Musical Writings* II (1989). It translates other theorists, not this text.
