# Fact-check of the notes, group 1 (Xylander X01–X29)

Every one of the 66 notes in `work/composed-g1.json` was checked against the dictionaries, grammars and texts themselves.

**Files**
- The backup taken before this pass is `work/fc1/composed-g1.before-factcheck.json`.
- The script that made the changes is `work/fc1/apply_fc.py`.
- The running ru/en text is unchanged: no note showed it to be wrong. Anchors, `basis`, `decisions`, `fixes` and `open` are also unchanged. Every anchor still occurs exactly once in its ru and en text.
- **Warning: do not run `build.py` again.** `segs_a/b/c.py` were already out of date before this pass, because the terms pass edited `composed-g1.json` directly (X25, X26, X28, X29 differ). Rebuilding would overwrite both the terms pass and this fact-check.

## What I used

- **Lewis & Short, Gaffiot 2016, DMLBS, Du Cange, Georges, LSJ and Bailly.** I read them through Logeion. Every entry cited in a source field was opened and read.
- **Allen & Greenough.** *New Latin Grammar*, the 1903 printing on archive.org: §§343, 346, 352, 409, 418, 426, 430–431.
- **Boethius.** Friedlein (1867), archive.org copy `aniciimanliitor00friegoog`. Pages are cited by Friedlein's page and line:
  - *De inst. mus.* I.2 (pp. 187–189), I.6 (p. 193), I.8 (p. 195), I.10 (pp. 197–198), I.16 (pp. 201–203), I.20 (pp. 206–212), I.21 (pp. 212–213), I.22 (pp. 214–215), I.23 (pp. 216–217), I.31 (p. 222), II.12–14 (pp. 241–243);
  - *De inst. arith.* II.40 (p. 137).
- **Theon of Smyrna.** Hiller (1878), archive.org copy `theonissmyrnaei00theogoog`, pp. 18–20, 47–49, 64, 70–71. I read the main text only, not the apparatus.
- **Cleonides.** Jan, *Musici scriptores Graeci* (1895), archive.org copy `musiciscriptores01jank`, p. 188, the text of ch. 5 only. I did not use Jan's notes or apparatus (the "Psellus" trap).
- **Aristoxenus.** *Elementa harmonica*, ed. Macran (1902), archive.org copy `aristoxenouharmo00arisuoft`, p. 112.
- **Euclid.** Heath's translation in D. E. Joyce's online edition: I def. 1, I.3, I.47, VI.13, VII defs. 1–2 and 18.
- **Other authors.**
  - Plato, *Meno* 85b (Perseus);
  - Pliny, *Naturalis historia* 12.9 (Perseus, Mayhoff);
  - Cicero, *De natura deorum* I.95 (The Latin Library);
  - Columella 5.2.7 (The Latin Library).
- **This workspace.**
  - The other segments: the Latin in `packet-g1…g4.json` and the composed text in `composed-g1…g4.json`;
  - the diplomatic transcription (`printed`);
  - `about.md`.
- **Not used.** I did not consult the Greek text of the work or any translation of it.

**Source marks.** Every source field has been rewritten.
- **[checked]** now means that I opened the place myself.
- **[from memory]** marks what I could not open.
  - The page images (`scans/`) are not in the workspace, so the claims about running heads, the marginal figure on p. 43 and the page images behind the printed lines carry "[from memory] (not rechecked by the fact-checker …)" with the name of whoever reported them. Where the diplomatic transcription confirms the claim, it is cited [checked] beside them.
  - Ptolemy, *Harmonics* III.1, title: known only through LSJ.
- **Not marked.** Internal references (cards, agreed points, rechecks) are kept without a mark; they are not sources.

## Changes, with reasons

### A. Corrections to the text of notes (9 notes; ru and en changed together)

1. **X05, note 1 (concinnare / coaptare).**
   - "классическое слово" / "a classical word" became «слово в основном доклассическое — чаще всего у Плавта — и послеавгустовское, у Цицерона его нет» / "mostly ante-classical, most often in Plautus, and post-Augustan, not in Cicero".
   - *Reason:* L&S, s.v. concinno, says "mostly anteclass. and post-Aug.; most freq. in Plaut.; not in Ter., Cic., or Quint."
2. **X06, note 1 (nimirum).**
   - "Nimirum вводит вывод из сказанного" / "introduces an inference from what precedes" became «подаёт утверждение как бесспорное („несомненно, разумеется“); здесь оно подытоживает сказанное» / "presents the statement as beyond dispute ('doubtless, of course'); here it sums up what precedes".
   - *Reason:* L&S, s.v. nimirum: "to introduce an assertion as indisputable … without doubt, certainly". Gaffiot: "assurément, certainement". Neither gives an inferential sense.
3. **X07, note 1 (Boethius' three musics).**
   - "(I.2: mundana, humana, instrumentalis)" became "mundana, humana, and the music 'established in certain instruments', quae in quibusdam constituta est instrumentis; Boethius does not use the adjective instrumentalis". The Russian was changed to match.
   - *Reason:* Boethius I.2 (Friedlein p. 187.21–23; p. 189.6–11 "instrumentorum musica") has no *instrumentalis*. A search of the whole Friedlein text finds no instance of the adjective. *Musica instrumentalis* is a later term.
4. **X08, note 2 (Thrasyllus in Theon).**
   - The gloss "that is, of a voice fit for harmony" / «то есть голоса, пригодного для гармонии» became Thrasyllus' own explanation of ἐναρμόνιος: "Thrasyllus calls a voice 'attuned' when it lies within the musical range, so that there are notes both higher and lower than it".
   - *Reason:* Hiller pp. 47.20–48.8. There ἐναρμόνιος is defined as a voice that can be found higher than the high and lower than the low; the thunder example shows sound outside that range. "Fit for harmony" was a free gloss that made the parallel to *harmoniae particeps* look closer than Theon's text allows.
   - The reference was widened to pp. 47.18–48.8.
5. **X10, note 1 (complexus).**
   - The gloss «объятие, охват, совокупность» / "embrace, encompassing, combination" became «охват, объятие», в переносном смысле «связь» / "an encompassing, embrace, figuratively 'connection'"; the words "rendered 'combination'" were kept.
   - *Reason:* L&S, s.v. complexus, gives "a surrounding, encompassing … embrace" (I) and "a connection (in discourse)" (II.A). "Combination" and «совокупность» are not dictionary senses but the translators' rendering.
6. **X14, note 2 (nomenclature).**
   - "in the diatonic genus hypaton diatonos" became "in the diatonic genus **lichanos hypaton diatonos**".
   - "Boethius also has names with diatonos" became "in the diatonic genus Boethius too calls them diatonos meson, diatonos diezeugmenon, diatonos hyperboleon". The Russian was changed to match.
   - *Reason:* Boethius I.22, p. 214.6–8: "si in diatono genere aptetur, dicitur lichanos hypaton diatonos". The diatonic names with *diatonos* are on pp. 214.13–14, 215.4 and 215.11–12.
   - The source pages were corrected from "I.22, p. 214.6–16" to "pp. 214.4–215.14".
7. **X24, note 2 (diametrus).**
   - "(the Greek usage, normal in Latin geometry)" became "(the Greek usage, cf. διάμετρος in Plato, Meno 85b; so too in medieval Latin geometry, whereas in classical Latin the word means the diameter of a circle)". The Russian was changed to match.
   - *Reason:*
     - L&S and Gaffiot, s.v. diametros, give only "diameter". Columella 5.2.7, cited by L&S, uses it of a circle.
     - LSJ, s.v. διάμετρος II, gives "diagonal of a parallelogram, Pl. Men. 85b".
     - DMLBS, s.v. diameter, diametrus 2c, gives "diagonal of square" (medieval).
     - "Normal in Latin geometry" was therefore not supported for classical Latin.
8. **X27, note 5 (coalescere).**
   - "Vinet confusio (V32, V57, V59)" became "Vinet the participle confusis (V32) and the noun confusio (V57, V59)". The Russian was changed to match.
   - *Reason:* V32 has *coniunctis confusisque* (participle of *confundo*). *Ex confusione* stands only in V57 and V59.
9. **X28, note 1 (Greek and Latin interval names).**
   - The cross-reference now says exactly what X30 and X35 do.
     - The Greek name is rendered literally where it stands beside its Latin equivalent: X30 *diapason cum diatessaron … hoc est, octava cum quarta …*; X35 *diatessaron seu quartae*.
     - The established term plus the literal sense in brackets is used in X29 and **at the start of X30** (*diapason dicitur, quod per octo nervos transit*, composed «октавой [«через все»]» / "the octave ['through all']").
   - *Reason:* the old note said that X30 as a whole gives the Greek names literally. The beginning of X30 follows the X29 pattern.
   - "Hackneyed" was kept. It is supported by L&S, s.v. tero, P. a. tritus ("familiar, common, commonplace, trite"), which is now cited beside Gaffiot ("souvent employé, usité, commun").

### B. Corrections to source fields only (7 notes; note text verified)

10. **X04, note 2.**
    - "Boethius, De inst. mus. II.12–14, pp. 242–244" became II.12, p. 241.15–19, and II.13, p. 243.2–15.
      - The definitions *Proportio … duorum terminorum ad se quaedam comparatio* and *Proportionalitas est aequarum proportionum collectio* are on p. 241, not 242–244.
    - Added *De inst. arith.* II.40, p. 137.8–17 (*proportionalitas … similis habitudo*), which supports "likeness" in the note.
11. **X05, note 3.**
    - "Lewis & Short, s.v. inconvenienter [from memory]" became Gaffiot (Aug. Trin. 2.9) and DMLBS sense 2 ("inappropriately, unfittingly (freq. w. neg.)").
    - *Reason:* L&S has no entry *inconvenienter*.
12. **X13, note 2.** The note glosses *strepitus*, but the source cited only L&S *crepitus*. Added L&S, s.v. strepitus I ("a (wild, confused) noise, din").
13. **X18, note 1.**
    - Boethius I.16 "pp. 201–204" became pp. 202.17–203.11, the place of 16 : 17 : 18. I.16 ends on p. 203.11.
    - The Aristoxenian count, previously [from memory], is now checked: *El. harm.* I, ed. Macran p. 112 (the tone is divided into half, third and quarter; the smallest is δίεσις ἐναρμόνιος ἐλαχίστη).
14. **X19, note 1.** Same correction of the Boethius I.16 pages.
15. **X19, note 2.** Boethius I.6 "pp. 192–193" became p. 193.5–20. I.6 begins on p. 193.3; p. 192 is I.4–5.
16. **X24, note 1.**
    - I removed "Allen & Greenough §352a [checked] (reviewer astra)". §352.a deals with the genitive of the charge or penalty (*dupli condemnare*), not with *propositum dupli*.
    - The note's claim that *dupli* is the genitive "of the double" is supported by L&S, s.v. duplus II.A, which stays.

### C. Precision only (no correction needed)

- **Exact pages and lines added:**
  - Boethius I.2 (pp. 187.18–189.12), I.8 (p. 195.2–5), I.10 (p. 198.6–8), I.20 (p. 207.24–30: two tetrachords share mese in the heptachord, *mesen nervum secundo numeramus*, which supports the X15 note), I.21 (pp. 212.23, 213.17), I.23 (pp. 216.18–217.2);
  - Theon, Hiller pp. 47.20, 64.6;
  - Cleonides, Jan p. 188.3–12.
- **X02, note 3.** DMLBS "sense b" became senses 1 ("commensurability") and 1b ("just proportion, symmetry, harmony"). Gaffiot (Boet. Mus. 1.31) was added.
- **Earlier [from memory] marks, now opened and verified:**
  - X12: Euclid I def. 1;
  - X18, note 3: L&S genus II.B.1.b, novenarius;
  - X24, note 2: Plato, *Meno* 82b–85b;
  - X27, note 3: L&S potentia III, facultas I; DMLBS potentia 1b;
  - X27, note 5: L&S coalesco I.
- **X14, note 3.** LSJ μόνος I became I–II ("alone" and "only").
- **X28, note 1.** LSJ διά A.I.1 was added.

### D. Verified without change (main points)

- **Cross-references to other segments.** Every one was checked against the Latin in the packets and the composed text: all X and V references in the 66 notes. The only discrepancies are those corrected above (V32 in X27, note 5; X30 in X28, note 1).
- **Numbers.**
  - √(9/8) ≈ 1.0607; (9/8)^¼ ≈ 1.0299; √72 ≈ 8.485; √288 ≈ 16.97; √8 ≈ 2.828; √32 ≈ 5.657;
  - 17:16 and 33:32 (V22); 81:64; 729:512; 8 + 8 − 1 = 15; s²/2 and 2s² with s = 4 giving 16, 8, 32;
  - tone = 2 semitones = 4 dieses; the fourth = 4 notes / 3 steps, the fifth = 5 / 4, the octave = 8 / 7;
  - notes 1, 8 and 15 are proslambanomenos, mese and nete hyperbolaion. All correct.
- **Printed readings** (diplomatic transcription): 40.1–2 (heading without author), 41.22 *mese monos* in lower case, 42.5 *continuò*, 43.3 *Numerorum*, 43.14 *quod propositum dupli esse constat*, 43.17 *compositae*.

## Table of all notes

| Segment | Note | Verdict | Sources opened |
|---|---|---|---|
| X01 | 1 | verified (running-heads claim not rechecked: page images unavailable) | L&S summa; printed 40.1–2 |
| X02 | 1 | verified | L&S contineo; A&G §§409, 431; V03 |
| X02 | 2 | verified | Boethius I.2 (Friedlein pp. 187–188) |
| X02 | 3 | verified (source made precise) | L&S, Gaffiot, DMLBS commensuratio; Boethius I.31 p. 222; X03, X04; V03 |
| X02 | 4 | verified | Latin and composed X04, X25, X32, X35, X37, X38, X41; L&S proportionalitas |
| X04 | 1 | verified | L&S omnino |
| X04 | 2 | corrected (source) | L&S, Gaffiot, DMLBS proportionalitas; Boethius Arith. II.40 p. 137; Mus. II.12–13 pp. 241–243 |
| X04 | 3 | verified | V05 |
| X05 | 1 | corrected | L&S concinno, coapto; X12, X32, X44, X45, X47, X56 |
| X05 | 2 | verified | about.md §4.5; X31–X33 |
| X05 | 3 | corrected (source) | L&S (no entry), Gaffiot, DMLBS, Georges inconvenienter |
| X06 | 1 | corrected | L&S miraculum, dignor, nimirum; Gaffiot nimirum; Pliny NH 12.9; A&G §418.b n. 1 |
| X07 | 1 | corrected | Boethius I.2 pp. 187–189 (and search of the whole Friedlein text) |
| X07 | 2 | verified | L&S tempero; V08, V58, V60 |
| X07 | 3 | verified | L&S congruentia; V08 |
| X07 | 4 | verified | Cicero ND I.95; L&S, Gaffiot beatitas; V08 |
| X07 | 5 | verified | L&S considero; V09 |
| X08 | 1 | verified | L&S intensio, tenor; Boethius I.8 p. 195; Hiller p. 47; X37, X39 |
| X08 | 2 | corrected | Hiller pp. 47–48; X12; V11 |
| X09 | 1 | verified | L&S, DMLBS respectus; X18, X38; V12 |
| X09 | 2 | verified | Hiller p. 48; Boethius I.8 p. 195 |
| X10 | 1 | corrected | L&S complexus; Hiller p. 48; V13; X42 |
| X10 | 2 | verified | L&S certus; V13 |
| X11 | 1 | verified | Hiller p. 48; X44; V14 |
| X12 | 1 | verified | Euclid I def. 1; V15 |
| X13 | 1 | verified | X12, X31–X33; about.md §4.5 |
| X13 | 2 | corrected (source) | L&S strepitus, crepitus; V16; Boethius I.8 p. 195 |
| X14 | 1 | verified | L&S nomenclatio; X29, X34 |
| X14 | 2 | corrected | Boethius I.20 p. 212, I.22 pp. 214–215; X16, X32; V17 |
| X14 | 3 | verified | LSJ μόνος; printed 41.22; V17 |
| X15 | 1 | verified (Ptolemy's title known only through LSJ) | LSJ πεντεκαιδεκάχορδος; Logeion (no ἑκκαιδεκάχορδος in LSJ or Bailly); Hiller p. 64 |
| X15 | 2 | verified | Boethius I.20 p. 207; A&G §426.3; arithmetic |
| X15 | 3 | verified | Latin X15, X29, X30, X41, X42 |
| X15 | 4 | verified | printed 42.5; L&S continuus (adv. continuo) |
| X16 | 1 | verified | X14, X36; arithmetic |
| X18 | 1 | corrected (source) | Boethius I.16 pp. 201–203, I.21 p. 213; Aristoxenus ed. Macran p. 112; X19–X20; V22; arithmetic |
| X18 | 2 | verified | about.md §4.3; L&S accessio |
| X18 | 3 | verified | L&S genus, novenarius; X44–X45 |
| X19 | 1 | corrected (source) | Boethius I.16 pp. 202–203; arithmetic |
| X19 | 2 | corrected (source) | Euclid VII defs. 1–2; Boethius I.6 p. 193 |
| X19 | 3 | verified | Hiller pp. 18–20, 70–71; X42, X43; V23 |
| X20 | 1 | verified | about.md §4.3; V24 |
| X20 | 2 | verified | Euclid VI.13; arithmetic |
| X21 | 1 | verified | Euclid I.3; V25 |
| X23 | 1 | verified | printed 43.3; A&G §346; V27 |
| X23 | 2 | unverifiable (page image of p. 43 not available in the workspace) | none available |
| X23 | 3 | verified | arithmetic; Euclid VII def. 18; about.md §4.3 |
| X24 | 1 | corrected (source) | printed 43.14; L&S duplus; A&G §§343, 352; V29 |
| X24 | 2 | corrected | Euclid I.47; LSJ διάμετρος; DMLBS diameter; L&S, Gaffiot diametros; Columella 5.2.7; Plato Meno 85b; arithmetic |
| X24 | 3 | verified | L&S geometres; Gaffiot, DMLBS geometer |
| X25 | 1 | verified | Boethius I.10 p. 198; V30 |
| X25 | 2 | verified | arithmetic |
| X26 | 1 | verified | printed 43.17; X27, X29, X49; V31 |
| X26 | 2 | verified | L&S, Gaffiot auctio; V31 |
| X26 | 3 | verified | arithmetic from X18 |
| X26 | 4 | verified | DMLBS rhythmus; V31 |
| X27 | 1 | verified | Boethius I.23 pp. 216–217; Cleonides 5, Jan p. 188; X26, X49 |
| X27 | 2 | verified | Du Cange diversus; L&S diverto (P. a. diversus); V32 |
| X27 | 3 | verified | L&S potentia, facultas; DMLBS potentia |
| X27 | 4 | verified | Boethius I.21 p. 212; X44, X56, X57; V32 |
| X27 | 5 | corrected | L&S coalesco; X49, X51; V32, V57, V59 |
| X28 | 1 | corrected | Gaffiot tritus; L&S tero (P. a. tritus); LSJ διά; about.md §§4.1–4.2; X29, X30, X35; V33 |
| X29 | 1 | verified | DMLBS immediatus; V34 |
| X29 | 2 | verified | X37 |
| X29 | 3 | verified | L&S invenio; X14, X30, X44, X51 |
| X29 | 4 | verified | arithmetic of the text |

**Totals:** 66 notes checked. 49 verified, 16 corrected (9 in their text, 7 in their source), 0 deleted, 1 unverifiable.
