# Fact-check of the notes, group 2 (Xylander X30–X58)

File checked and corrected in place: `work/composed-g2.json` (60 notes in 29 segments; X40, X46, X52, X53 have none).
Copy before the check: `work/fc2/composed-g2.before-factcheck.json`. The edit script is `work/fc2/apply_fc2.py`. Downloaded texts and dictionary pages are in `work/fc2/` and `work/fc2/dl/`.

The running ru/en text of the segments was not changed. All anchors are unchanged and were re-checked as exact substrings of ru and en after the edits.

## How the references were checked

| Source | Where it was read |
|---|---|
| Lewis & Short | Perseus (`perseus.tufts.edu`, entry pages) |
| Gaffiot 2016, DMLBS, Du Cange, LSJ | Logeion API (`anastrophe.uchicago.edu/logeion-api`) |
| Allen & Greenough | Dickinson College Commentaries (§ 305, § 397) |
| Boethius, *De institutione arithmetica* / *musica* | Friedlein (Leipzig 1867), archive.org OCR (`DeInstitutioneArithmeticaLibriDuoDeInstitutioneMusicaLibriQuinque`). Page and line numbers are taken from the running heads and the marginal line numbers. |
| Theon of Smyrna | First1KGreek TEI of Hiller's text (tlg1724.tlg001), with page and line breaks. **Every `<note>` element was removed before reading, so Hiller's apparatus (the trap) was never displayed.** |
| Gaudentius, Cleonides | Jan, *Musici scriptores Graeci* (1895), archive.org OCR (`musiciscriptoresjank`). Only the main-text lines were read: Gaudentius 8 (pp. 337–338) and Cleonides 13–14 (pp. 200–201). I searched the lines I displayed for "Psell" and found nothing. |
| Aristoxenus | Macran (1902), archive.org OCR, Greek text |
| Aristides Quintilianus | Winnington-Ingram (1963), archive.org OCR, I.8–9 |
| Pollux | Bekker (1846), archive.org OCR (`onomasticonexre00pollgoog`), p. 168 |
| Plato | Perseus Greek text (Laws 812, Timaeus 36a–b, Republic 399a) |
| Cicero, Seneca, Plautus | The Latin Library (de Or. 3.216; NQ 7.1.3; Pseudolus) |
| Canon of Holy Saturday | Triodion text (orthodoxia.online, Orthros of Holy Saturday, ode 1) |
| Cross-references X.., V.. | composed-g1/g3/g4.json; Latin from packet-g1/g3/g4.json |
| Printed letters | the diplomatic transcription (`printed`) in packet-g2.json |

**Not opened:**
- the page images, which are not in this workspace;
- Migne, PL 63 (replaced by Friedlein);
- Lampe;
- Tinctoris and Gaffurius (the TML was unavailable, and a web search did not confirm the usage);
- any source on Mersenne's law.

I did not consult the Greek text of the work or any translation of it.

## Changes, with reasons

### Changes to the note text (ru and en together)

1. **X33, note 2.** «(Боэций I.16, I.18)» / "(Boethius I.16, I.18)" became **I.7, I.18**.
   - Reason: I.16 does not say that the tone is not a consonance. Its text even lists the tone loosely with the consonances: "diapente vel diatessaron vel tonum consonantiam reddet", Friedlein p. 202.1–2.
   - The statement is in I.7, p. 194.19–22: all musical consonances lie in 2:1, 3:1, 4:1, 3:2 and 4:3, which excludes 9:8.
   - I.18 (heading "Diatessaron a diapente tono distare") supports "the difference between the fifth and the fourth".
2. **X35, note 2.** «(Боэций II.27; книга V)» / "(Boethius II.27; book V)" became **V.8–9**.
   - Reason: the place is exact in Friedlein. V.8 has Ptolemy's reproach of the Pythagoreans; V.9, p. 358.19–20, has the heading "Demonstratio secundum Ptolomaeum diapason et diatessaron consonantiam esse".
   - The source cited "V.8–9, ed. Migne". According to X31's own source, Migne's numbering in book V is one lower than Friedlein's. The Migne reference is therefore replaced by Friedlein.
3. **X42, note 2.** The claim that *decima quinta* was current "in theory and organ practice" was removed. It rested on "Tinctoris and Gaffurius [from memory: translator A]", which I could not verify, and the note does not need it.
   - New ru: «по словам самого Ксиландра (hodie vocant), обиходное в его время название двойной октавы»
   - New en: "by Xylander's own statement (hodie vocant), the name of the double octave current in his day"
   - The source no longer cites Tinctoris and Gaffurius.
4. **X44, note 1.** «размеренное пение» / 'measured singing' was presented as a dictionary gloss, but Lewis & Short does not give it.
   - L&S, s.v. *modulatio*, has: I 'a regular measure'; II 'a rhythmical measure, modulation; hence, singing and playing, melody' (Quint. 9.4.139; 'vocis, melody', 11.3.59).
   - The sentence now quotes L&S: «L&S даёт «ритмическая мера», а отсюда «пение и игра, мелодия» (с примерами из Квинтилиана)» / "L&S gives 'a rhythmical measure', hence 'singing and playing, melody' (citing Quintilian)".
5. **X51, note 2.** The quotation "enarmonium vero optime atque apte coniunctum, magis coaptatum" joined two separate places of Boethius I.21 (Friedlein 213.1–2 and 213.15) as if they were continuous. An ellipsis is inserted, in ru and en: "… coniunctum … magis coaptatum".
6. **X57, note 2.** The vague "compare … with the parts of melodic composition in Cleonides" now gives the place and its point.
   - Cleonides 14 (Jan pp. 200–201) lists ἀγωγή, πλοκή, πεττεία and τονή.
   - τονή is defined as ἡ ἐπὶ πλείονα χρόνον μονή of the voice on one note. This is the exact counterpart of *mansio*, which the same note already compares with Aristoxenus' μονή.
   - Both ru and en now name the four parts and gloss πεττεία and τονή.

### Corrections of the source field

- **X32, note 1.** "Plaut. Pseud. 205" became **Pseudolus 208**.
  - Gaffiot gives obsono 1, "Pl. Ps. 208"; L&S gives "Ps. 1, 2, 74".
  - In the Latin Library text, the line "quom sermoni huius obsonas" stands after 205a.
- **X31, note 2.**
  - The Boethius reference "V.11–12 … = V.10–11 in ed. Migne (Latin Wikisource): … consonantiae …" was replaced by Friedlein V.11, p. 361.8–12 and V.12, p. 362.10–15.
  - Friedlein reads **Consonae** (not *consonantiae*). This agrees with the ru/en text "(consonae)".
  - Theon's place was refined from p. 48.15–20 to **48.16–20**; Thrasyllus' report runs from 47.18 to 49.5.
  - Gaudentius' definition is pinned to p. 338.3–7.
- **X54, note 2.**
  - "Aristoxenus, Elementa harmonica I.23; Aristides Quintilianus I.9 [from memory]" is now checked.
    - **Aristoxenus**, El. harm. I, on the three genera: τελευταίῳ γὰρ αὐτῷ καὶ μόλις μετὰ πολλοῦ πόνου συνεθίζεται ἡ αἴσθησις. The number "I.23" could not be confirmed and was dropped; the Meibom page is not verified.
    - **Aristides** I.9, Winnington-Ingram p. 16.10–17: the enharmonic is "impossible for the many", and some gave up melody by diesis.
  - Added as a parallel: Theon, Hiller pp. 55.15–56.3, reporting Aristoxenus ("ὅθεν οὐδʼ εἰς χρῆσιν ῥᾳδίως ἔρχεται").

### Sources upgraded from [from memory] after opening

- X33 n1: L&S *principium*, I and II.A.
- X37 n1: L&S *fides* (2), II: 'in sing., i. q. nervus, chorda'.
- X38 n1: A&G § 305 (agreement of the relative).
- X50 n1: L&S *confundo* I.

### Page and line refinements (claims correct, references made exact)

**Boethius, ed. Friedlein:**

| Note | Place | Exact reference |
|---|---|---|
| X35 n2, X36 n1 | I.4, *duplex superbipartiens, ut sunt tres ad octo* | 192.14–17 (was 192.14–16) |
| X36 n1 | I.4, *superbipartiens* alone = 5:3 | 191.25–27 |
| X36 n1, X38 n3 | Arithm. I.28, *superbipartiens tertias* | p. 60.4–8 |
| X36 n2 | I.10, hammers XII, VIIII, VIII, VI | pp. 197–198 |
| X34 n1 | III.2–3 headings: two tones taken from 4:3 leave less than half a tone | 267.12–16 |
| X34 n2 | I.17, minor semitone 243:256 | 204.8–9 |
| X34 n2 | II.31, the comma numbers | pp. 266–267 |
| X47 | I.21, *per semitonium, tonum et tonum* | 213.5–6 |
| X50 n2 | I.21, *in mollius decidens* | 212.27–213.1 |
| X51 n2 | I.21, *per diesin et diesin et ditonum* | 213.14–17 |

**Theon, ed. Hiller:**

| Note | Place | Exact reference |
|---|---|---|
| X33 n2 | the tone and the diesis are "a beginning of consonance, not yet consonance" | 49.2–5 |
| X41 n4 | width of the cavities | 57.4–5 (was 57.1–7) |
| X55 | Adrastus on Plato's diatonic system | 63.25–65.9 (was 63.25–65.6) |
| X41 n1 | the same list of methods ascribed to Pythagoras (an added parallel) | 56.9–57.7 |

**Other details:**
- Diplomatic-transcription references are added for X38, X50, X54, X56 and X58. X50's "corrections list" was not available here and is replaced by the diplomatic transcription.

## Checks that confirmed the notes (selection)

**Arithmetic and ratios**, all correct:
- 4:3 ÷ (9:8)² = 256:243, about 90.2 cents, against a half tone of about 102.0 cents.
- (9:8)⁶ ÷ 2 = 531441:524288, Boethius' own comma numbers in II.31.
- 8:3 = 2 × 4:3; 5:2 = 2½; the series 6, 8, 9, 12, 16, 18, 24.
- Note counts: 11, 12 and 15 for the octave and a fourth, the octave and a fifth and the double octave; 8 + 8 − 1 = 15.
- The genera: ½ + ½ + 1½ and ¼ + ¼ + 2, each 2½ tones.
- The pairs of X32: 8–1, 11–4, 12–5, 15–8 on the list of X14, each seven steps.

**Cross-references to other segments:**
- All references to X01, X04, X08, X09, X14, X15, X19, X27, X28 and X29 say what the notes claim.
- So do all references to V35, V37, V38, V39, V44, V49, V50, V57, V58, V59, V62, V63, V64 and V65. For example: V35 *repetitis*; V37 *impari temporis spatio*, *secundum proportiones et rationes*; V38 *nondum*; V39 *modica … toni parte*; V44 *superpartiens*; V49 *facultates*, *vis* and no number of strings; V50 *quae in ipsis sunt*; V57/V59 *ex confusione*; V58 *moestius luctuosiusque*; V62 *usus rarior*; V63 Plato unnamed; V64 *modulus*; V65 *lentioribus*, *pausis*, *manus*.

**Dictionary claims, all confirmed:**
- L&S: *assono*, *obsono* (2), *succedo*, *intensio* (I.B, II; Sen. NQ 7.1.3 confirmed in the text), *qua* (II.B–C), *bes*, *amplitudo*, *coaptatio*, *coalitus* (2), *modulatio*, *obliquus*, *mansio*, *tactus* (with Cic. de Or. 3.216 confirmed in the text), *alter*, *concipio*, *exodium*, *gemino*.
- Gaffiot: *adsono*, *obsono*, *superbipartiens*.
- DMLBS: *superbipartiens* b, *acuitas* c, *clavus* (3) 1g.
- Du Cange: *acuitas*.
- LSJ: παράφωνος, ἀντίφωνος, ἐξόδιος, μονή.
- A&G § 397b.

**Authors, all confirmed in the texts:**
- Plato: Laws 812d–e, Timaeus 36a–b, Republic 399a.
- Gaudentius 8.
- Pollux IV.108.
- The canon of Holy Saturday, ode 1.
- Cleonides 14.
- Aristoxenus: μονή τις καὶ στάσις τῆς φωνῆς, which LSJ gives as p. 12 M.

## Left as they are, and not verifiable here

- **X30 n4 and X56 n2** (the marginal "Vide Annot." on pp. 44 and 49) and **X58 n1** (the running head DE MVSICA and the catchword GE-): these rest on the page images, which are not in this workspace. The translators' reports are kept, and the sources are now marked [from memory] with the attribution.
- **X41 n3** (Mersenne's law): standard physics and correct, but no reference was opened ([from memory]).
- **X56 n2**: Lampe s.v. ἐξόδιος is not opened ([from memory: reviewer claude]).
- **X57 n3**: *tactus* = 'beat' in sixteenth-century theory is not opened ([from memory]). It is a caveat, not a claim of the translation.

## Observations for the editor (no change made)

- Theon (Hiller pp. 55.15–57.10) is the closest parallel to several passages:
  - X41: the methods, including γνωριμώτερον = *forte manifestius*, στροφὴ τῶν κολλάβων = *conversio clavorum*, and ἐπίτασις καὶ ἄνεσις τοῦ πνεύματος = *intensio et remissio spiritus*;
  - X51: Aristoxenus says the enharmonic is called ἁρμονία διὰ τὸ εἶναι ἄριστον;
  - X54–X55: the difficulty of the enharmonic; the diatonic is simple, noble and natural, and so Plato takes it.
  
  I added these only to the source fields of X41 n1, X54 n2 and X55.
- Boethius I.16 (p. 202.1–2) loosely lists the tone among the consonances. Any future note that cites I.16 for "the tone is not a consonance" should cite I.7 instead.

## Table of all notes

| Segment | Note | Verdict | Sources opened |
|---|---|---|---|
| X30 | 1 | verified | L&S *gemino*; V35 Latin |
| X30 | 2 | verified | X28 and its note; about.md § 4.1–4.2 |
| X30 | 3 | verified | arithmetic; X32 |
| X30 | 4 | unverifiable (margin, page image) | about.md § 2; printed lines 44.13–20 (margin not transcribed) |
| X31 | 1 | verified | LSJ παράφωνος, ἀντίφωνος; Latin X31–X32 |
| X31 | 2 | corrected (source) | Theon (Hiller) 47–49; Gaudentius 8 (Jan 337–338, main text); Plato Laws 812d–e; Boethius V.11–12 (Friedlein 361–362) |
| X32 | 1 | corrected (source) | L&S *assono*, *obsono* (2); Gaffiot *adsono*, *obsono*; Plautus Pseudolus 208 |
| X32 | 2 | verified | Latin X32; V37 |
| X32 | 3 | verified | A&G § 397b; L&S *succedo*; V37 |
| X32 | 4 | verified | X04 note 2 |
| X32 | 5 | verified | X14, X31; arithmetic |
| X33 | 1 | verified | L&S *principium* |
| X33 | 2 | corrected (text + source) | Theon 49 (Hiller); V38; Boethius I.7, I.16, I.18 (Friedlein 194, 201–202, 204) |
| X34 | 1 | verified | arithmetic; Boethius I.21 (213), III.2–3 headings (267); V39; X47 |
| X34 | 2 | verified | arithmetic; Boethius I.17, I.19, II.31 (headings and 266–267), III.3 |
| X35 | 1 | verified | X28, X30; about.md § 4.1 |
| X35 | 2 | corrected (text + source) | arithmetic; Boethius I.4 (192), II.27 heading, V.8–9 (358) |
| X36 | 1 | verified | arithmetic; Boethius Arithm. I.28 (60), Mus. I.4 (191–192); Gaffiot, DMLBS *superbipartiens* |
| X36 | 2 | verified | arithmetic; X35; Boethius I.10 (197–198) |
| X37 | 1 | verified | X38; X15 note 3; L&S *fides* (2) |
| X37 | 2 | verified | X08, X29, X39, X41; L&S *intensio* |
| X38 | 1 | verified | L&S *qua*; A&G § 305; printed 46.16; V44 |
| X38 | 2 | verified | arithmetic; X37 |
| X38 | 3 | verified | L&S *bes*; Boethius Arithm. I.28; X36; V44; printed 46.18 |
| X38 | 4 | verified | Boethius I.4 (192.4–5); about.md § 4.3 |
| X39 | 1 | verified | DMLBS *acuitas*; Du Cange *acuitas*; X37 |
| X39 | 2 | verified | X38, X40 |
| X41 | 1 | verified | Boethius I.11 (198); Theon 56–57 (Hiller) |
| X41 | 2 | verified | DMLBS *clavus* (3) 1g; L&S and Gaffiot *clavus* |
| X41 | 3 | verified (physics, from memory) | none |
| X41 | 4 | verified | L&S *amplitudo*; Theon 57 (Hiller) |
| X41 | 5 | verified | L&S *intensio*; Seneca NQ 7.1.3; about.md § 4.5 |
| X42 | 1 | verified | X43; V49 |
| X42 | 2 | corrected (text + source; unsupported claim removed) | Latin X42, X28; arithmetic; web search for Gaffurius (no confirmation) |
| X42 | 3 | verified | X14, X15; V49; arithmetic |
| X43 | 1 | verified | L&S *concipio*; V50 |
| X43 | 2 | verified | X09, X19, X42, X48 |
| X44 | 1 | corrected (text + source) | L&S *modulatio* |
| X44 | 2 | verified | Boethius I.21 (212.25); Latin X45, X48, X55; about.md § 4.5 |
| X45 | 1 | verified | L&S *coaptatio* |
| X45 | 2 | verified | Boethius I.21 (213.8–14) |
| X45 | 3 | verified | X47–X51 |
| X47 | 1 | verified | X34; arithmetic; Boethius I.21 (213.5–6) |
| X48 | 1 | verified | Boethius I.21 (213.7–8); X45, X46 |
| X49 | 1 | verified | L&S *coalitus* (2), Gaffiot *coalitus*; X27 note 5 |
| X49 | 2 | verified | arithmetic; X27 |
| X50 | 1 | verified | L&S *confundo*; V57, V59; printed 48.20; X27 note 5 |
| X50 | 2 | verified | V58; Boethius I.21 (212.27–213.1) |
| X51 | 1 | verified | L&S *alter*; X47, X49; V59 |
| X51 | 2 | corrected (quotation) | arithmetic; Boethius I.21 (213.1–2, 14–17) |
| X54 | 1 | verified | printed 49.7 |
| X54 | 2 | corrected (source) | V62; Aristoxenus El. harm. I (Macran); Theon 55–56 (Hiller); Aristides I.9 (W.-I. 16); Boethius I.21 (212–213) |
| X55 | 1 | verified | V63; Plato Timaeus 36a–b, Republic 399a; Theon 56, 63–65 (Hiller); Boethius I.21 (212.26) |
| X56 | 1 | verified | V64 |
| X56 | 2 | verified (margin detail unverifiable) | Pollux IV.108 (Bekker 168); L&S *exodium*, *Paean*; LSJ ἐξόδιος; canon of Holy Saturday, ode 1 |
| X56 | 3 | verified | printed 49.16, 49.18 |
| X57 | 1 | verified | L&S *obliquus*; V65 |
| X57 | 2 | corrected (reference made exact, text + source) | L&S *mansio*; LSJ μονή; Aristoxenus (Macran); V65; Cleonides 13–14 (Jan 200–201, main text) |
| X57 | 3 | verified | L&S *tactus*; Cicero de Or. 3.216; V65 |
| X58 | 1 | unverifiable (running head and catchword, page image) | printed 49.25; X01 |

**Totals:** 60 notes checked. 49 verified (one of them, X41 n3, from memory, and one, X56 n2, with an unverifiable margin detail), 9 corrected, 0 deleted, 2 unverifiable. One unsupported claim was removed inside X42 n2.
