# Xylander version: revision log (passes 5–6)

The input was `xylander-draft.json` and the output is `xylander-revised.json`, in the same format. The 58 segments are all present, in order. The file still has 74 notes, 12 doubts, 80 terms and 5 text issues. It contains no local paths.

## How the revision was done

- **Critical revision.** Every segment was compared word by word with the Latin reading text (`latin-texts.json`, key `xylander`), in Russian and in English separately.
  - Every number and ratio in `checks` was recomputed (cents = 1200·log2 r): 9:8, √(9/8), (9/8)^¼, 17:16, 33:32, 4:3 − 2 × 9:8 = 256:243, the 11.73- and 23.46-cent excesses, 8:3, 3:1, 4:1, the 6–24 series, 5:1, 5:2, 5:3, 5:4, and the X32 note pairs 8/1, 11/4, 12/5, 15/8. **All are correct; no changes were needed.**
  - The scan of p. 43 was checked. It confirms *Numerorum*, *quod propositũ dupli esse cõstat* and *compositæ*, and the two marginal dot figures are as the X23 note describes them (4 × 4 cut after the second row; 8 rows of 4 cut after the fourth row).
- **Sources reopened.** The following references in the notes were reopened:
  - Boethius, *De inst. mus.*, ed. Friedlein: I.4, I.8, I.10–11, I.16, I.20–22, I.31;
  - Theon, ed. Hiller: pp. 47–49;
  - Lewis & Short, Gaffiot, DMLBS, Du Cange and LSJ (through Logeion): the entries below, among others;
  - Shchetnikov's Russian Nicomachus, ch. 4 (ΣΧΟΛΗ II.1, 2008).

  Every reference not listed under "Notes and references corrected" was confirmed.
- **Stylistic revision.** Done separately for Russian and for English.

## Changes to the translation

| Seg. | Lang. | Change | Why |
|---|---|---|---|
| X04 | EN | "Music itself, in itself, is…" → "Now music itself is in itself…" | *Caeterum* had no rendering; the doubled "itself, in itself" was clumsy. |
| X04 | RU | «…пропорциональность, будучи, разумеется, гармонией вселенной» → «…пропорциональность: она, разумеется, и есть гармония вселенной» | Heavy participle; the explanatory sense of *nimirum … existens* is kept. |
| X05 | EN | "…call the divine nature itself as well the harmony…" → "…call the divine nature itself, too, the harmony…" | Word order. |
| X07 | RU | «вкратце порассуждаем» → «вкратце поведём речь» | «порассуждать» is colloquial. |
| X09 | RU | «или их соотнесённость» → «или соотнесённость» | «их» was an addition without brackets (the English already brackets [their]). |
| X12 | EN | "just as a point in geometry is not either" → "any more than a point in geometry" | Idiom. |
| X13 | EN | "nay" → "indeed" | Archaism. |
| X14 | EN | Relative clause recast: "the names that the notes obtain … are different" | The relative clause was separated from its noun. |
| X15 | EN | "without a break" → "immediately" (*continuo*) | Agrees with the Russian «сразу же». |
| X18 | RU | «прибавка … к высокому» → «прибавка … в сторону высокого» (*ad acutum*) | «к высокому» reads as "added to the high". |
| X18 | EN | "double in respect of the diesis" → "double in comparison with the diesis" | Clearer; matches the Russian, and DMLBS *respectus* 5b. |
| X19 | RU, EN | *utique* now rendered: «безусловно», "certainly" | It had been omitted. |
| X23 | RU | «(ибо невозможно, чтобы восемь было…, или дать…)» → «(ибо невозможно ни восьми быть арифметически квадратом, ни дать квадратный корень этого числа)» | A «чтобы»-clause was coordinated with an infinitive. |
| X23 | EN | "impossible that eight should … be a square, or to give…" → "impossible for eight to be arithmetically a square, or to give…" | Same fault. |
| X32 | RU | «как когда восьмой…» → «например, когда восьмой…» | «как когда» is clumsy. |
| X34 | RU | Dropped the 3rd and 4th «же» (Октава же…, Октава же с квартой…) | Four «же» in a row; the Latin *vero/autem* are weak connectives. |
| X38 | RU | «сверхчетвертной» → «сверхчетвертный» | Wrong masculine form of «сверхчетвертное». |
| X39 | EN | "tension of highness" → "tension of acuteness" (*acuitas*) | Unidiomatic. The note and the `terms` entry are updated. |
| X42 | RU | Third *aliud*: «другая» → «ещё одна» | «одна … другая … другая». |
| X46 | RU | Added «ведь» | *enim* had been omitted (the English has "for"). |
| X50 | EN | "the genus of the fourth will be blended which is called chromatic" → "will be blended the genus of the fourth which is called chromatic" | The relative clause was separated from its noun. |
| X52 | EN | "Nor in any other way are … , too, made by harmony" → "Nor is it in any other way that … , too, are made by harmony" | Word order. |
| X56 | RU | «варьируется и разводится на» → «видоизменяется и распадается на»; «а вскоре и» → «а затем и» (*mox*) | «разводится» is the wrong word; *mox* here means "then". |
| X56 | EN | "drawn apart into" → "split into"; "presently" → "then" | Idiom; "presently" is ambiguous. |
| X58 | RU, EN | «Конец музыки.» → «Конец «Музыки».»; "End of the music." → "End of the Music." | *Musica* is the name of the section (heading X01, running head DE MVSICA). The note now says so. |

## Notes and references corrected

| Seg. | Correction |
|---|---|
| X02 | p. 198.4 (*epitritam proportionem*) belongs to Boethius I.10, not I.11. The source now reads "I.10, p. 198.4, and I.11, p. 198.12" [checked in Friedlein]. |
| X09 | DMLBS *respectus* "sense 1b" is "aspect, point of view". The sense "relation" is **sense 4 "(phil.) relation"**. The note and source are corrected, and sense 5b ("in comparison with") is added for *respectu dieseos* (X18). The `terms` evidence is updated [checked]. |
| X19 | Euclid VII def. 1 (the definition of the unit) does not state the doctrine. It is replaced by Theon of Smyrna, ed. Hiller, pp. 18.15–19.7 and 20.1–4 (the unit is indivisible as number, the one in sensible things divisible as body), with pp. 70.14–71.10 as a contrast (for Theon the 9:8 tone cannot be halved exactly, because 9 − 8 is an indivisible unit, nor on the canon). Xylander affirms a geometrical division [checked]. |
| X24 | *Geometer* is not Neo-Latin. Gaffiot s.v. *geometer* cites Boethius (*Top. Arist.*), and DMLBS s.v. *geometer* marks it Late Latin and common in medieval Latin. The note now says "late Latin form, usual in medieval Latin" [checked]. In the doubt, the grammatical evidence now reads "genitive of quality/measure (A&G §345) or of value (§417) [from memory]". |
| X38 | A construal (c) is added to the doubt and to `text_issues`. It needs no emendation: *qua* goes with *quantitatis* and *se* with *habet* (*se habere*, "to stand"), giving "the excess of quantity in which it stands in relation to the preceding notes". The translation keeps (a), because the word order favours *se praecedentium*; the sense is the same. |
| `terms` | *acuitas* now "acuteness". *decima quinta*: evidence specified (still [from memory]). |
| `contamination` | The entry said the downloaded Jan OCR had been deleted. Another copy of it is still in the team's working folder. The reviser did not open it, and checked the Gaudentius definition only through LSJ s.v. παράφωνος II (Gaud. *Harm.* 8). The entry is amended. |
| `translator`, `summary` | `subagents` now records the revision. One sentence on the revision is added to the summary. |

## Checked and left unchanged

These are deliberate choices of the draft. They were weighed in the revision and kept:

- ***proportio* = «пропорция» / "proportion".** Bower usually says "ratio". But the draft keeps *ratio* and *proportio* apart consistently and explains why in a note, and «пропорция» for a single ratio is current in Russian historical musicology.
- ***genus* = «род» / "genus"** throughout, also for kinds of interval (X18) and of consonance (X31). This is consistent and explained in a note; in English "kind" would read more easily in X18 and X31.
- **Russian «диапазон / дисдиапазон»** for the transliterated Greek names (X28–X30). This is the Russian word that derives from διὰ πασῶν. «диапасон» also occurs in the literature, but no authoritative source preferring it was found.
- **«призвучное» / «противозвучное», 'sounding-to' / 'sounding-against'** for Xylander's own coinages *assonans* / *obsonans* (X32). They are literal calques in quotation marks, flagged in the doubts as non-established. A literal rendering of a coinage seems justified despite about.md §4.1, but a reviewer should look at it.
- **Text issues.** The text issues (X23 *Numerorum*, X24 *propositum dupli*, X26 *compositae*, X34 comma, X38 *qua*) are well argued. The reading text is translated in each case.

## For the next reviewer

Check first:

- X04, Russian restructuring;
- X32, the calques;
- X38, the construal of *qua … habet*;
- the English "genus" in X18 and X31.
