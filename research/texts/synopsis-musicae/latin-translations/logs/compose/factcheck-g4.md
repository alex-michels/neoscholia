# Fact-check of the notes, group 4 (Vinet V34–V66)

File checked: `work/composed-g4.json` (33 segments, 55 notes). Backup of the state before this check: `work/fc4/composed-g4.before-factcheck.json`. The changes were applied by `work/fc4/apply_fc4.py`.

## Method

- **Latin.** Each segment's Latin was read in `packet-g4.json` (`latin`; `printed` where a note cites printed lines). The conventions were read in `about.md`.
- **Cross-references.** Every V/X reference was checked against the Latin of all four packets and against `composed-g1.json` to `composed-g3.json`. This covers the renderings of V04, V11, V15, V32 and X29–X57, and the notes to V05, V11, V18, V22, V31, V32 and V33.
- **Dictionaries and grammars, opened and read.**
  - Lewis & Short and LSJ (Perseus and Logeion).
  - Georges, Gaffiot 2016 and DMLBS (Logeion).
  - Allen & Greenough, Dickinson College Commentaries edition: §§ 135, 305, 510 (with the cross-reference to §§ 509–510) and 540.
- **Theorists and other authors, opened and read.**
  - Boethius, *De institutione arithmetica* and *De institutione musica*, ed. Friedlein (1867), archive.org scan text (page and line numbers as printed).
  - Theon of Smyrna, ed. Hiller (1878), archive.org scan text.
  - Gaudentius and the *Sectio canonis*, ed. von Jan (1895), archive.org scan text.
  - Ps.-Aristotle, *Problemata* XIX, in E. S. Forster's translation (Oxford 1927, with Bekker pages), together with LSJ's citation of the Greek.
  - Pollux IV.108, ed. Bethe (1900).
  - Plato, *Timaeus* 36b and *Republic* 399a (Perseus).
  - Cicero, *De divinatione* 2.96 (Latin Library).
  - Dowland's translation of Ornithoparchus (EEBO-TCP A08534).
- **The "Psellus" trap.** In Hiller and in von Jan only the theorists' own text was read. Apparatus lines mentioning "Psellus" were filtered out before reading and were not consulted. The Greek text of the work, translations of it and web searches for its phrases were not used.
- **Arithmetic.** Every number was recomputed:
  - tone 203.91 cents; limma 256:243 = 90.22 cents, less than half a tone (101.96 cents);
  - 2½ tones − 4:3 = 11.73 cents;
  - six tones − 2:1 = 531441:524288 = 23.46 cents;
  - 2:1 × 4:3 = 8:3;
  - 16 = 2 × 6 + 4;
  - note counts 11/12/15 and step counts 10/11/14;
  - octave pairs 1–8, 4–11, 5–12, 8–15;
  - ordinal coincidences 4:3, 8:4, 12:4; no integer k for 5:k = 3:2, 11:k = 8:3, 15:k = 4:1;
  - weights 4:1 and 9:4.

  All are correct.
- **Source fields.** All 55 source fields were rewritten.
  - `[checked]` now means opened and read in this fact-check.
  - `[from memory]` marks a reference not opened.
  - `[not re-checked]` / `[internal, not re-opened]` mark page images and internal cards or rechecks, which are not available or were not reopened.
  - Exact page and line numbers were added wherever the edition was read.
- **Running text.** No running ru/en text was changed. No note showed it to be wrong. All anchors are unchanged and were re-verified as exact substrings.

## Changes, with reasons

### V34, note 2 (corrected: content and source)
- **Was:** "ratio … ad is Vinet's usual construction for the relation of one note to another (V19 …; V22)".
- **Reason:** In V22 the construction relates numbers, not notes (*quomodo novem numerus ad octo habet*). V19 is the only note-to-note instance (*rationem primus sonus ad octavum habere*), so "usual" is not supported.
- **Now:** "the construction Vinet uses for the relation of one term to another: of note to note in V19 (…), of number to number in V22 (…)", with the same change in ru.
- **Source:** L&S s.v. *ratio* corrected from "II.B.1.a" to II.B.1 "relation, reference, respect to a thing". L&S has no explicit sub-letter a.

### V35, note 1 (corrected: source)
- **Was:** L&S s.v. *tamquam* I "as, just as, as it were", not the dictionary's wording.
- **Now:** the exact gloss, "as much as, so as, just as, like as, as if, as it were". The note text was unaffected.

### V36, note 1 (corrected: content and source)
- **Was:** Vinet leaves the two Greek words "untranslated and unexplained".
- **Reason:** V37 explains the difference between the two kinds at length. What Vinet omits is a gloss on the words, which Xylander gives (X31).
- **Now:** "untranslated, without a gloss on the words themselves (the difference between the two kinds he explains in V37)".
- **Also added:** Theon's division is given "reporting Thrasyllus". In Hiller pp. 47.18–48.20 the passage is Thrasyllus' account.
- **Checked:**
  - Theon p. 48.16–20;
  - Gaudentius 8, von Jan p. 338.3–7: παράφωνοι, the tritone from parhypate meson to paramese and the ditone from diatonos meson to paramese, "midway between consonant and dissonant";
  - Problemata XIX.39, 921a7–9, "antiphony is concord in the octave";
  - LSJ s.vv. ἀντίφωνος III and παράφωνος II.

### V36, note 2 (verified; source made exact)
- The claim is confirmed by Boethius, ed. Friedlein:
  - II.27, p. 259.10–15: diatessaron + diapason falls into the superpartient genus and keeps neither multiplicity nor superparticularity;
  - I.6, p. 194.12–17: superpartient ratios are excluded by the Pythagoreans, but "Ptolemaeus tamen etiam hanc proportionem inter consonantias ponit";
  - V.8–9, pp. 358.3–6 and 358.19–359.

### V42, note 1 (corrected: source)
- **Was:** Boethius, *De institutione arithmetica* I.29, p. 60.4–8.
- **Reason:** The passage *cum duae partes … tertii semper vocabulum subauditur … superbipartiens tertias* stands at p. 60.4–8 but belongs to the end of I.28. The heading of XXVIIII *De multiplici superparticulari* follows at p. 60.19–20. Friedlein's running head "I, 29" names the chapter that begins on the page.
- **Now:** I.28 (end of the chapter), p. 60.4–8.
- **Confirmed:** Mus. V.10, p. 360.24–26 (*Habent enim ternarium octo bis duasque eius partes*).
- **Added:** Mus. II.27, p. 259.20–24, which says the same of 8:3.

### V42, note 2 (unverifiable)
- The description of the diagram rests on the page image vinet-p49. The `scans/` folder is not in this workspace, so the image could not be opened.
- The description is internally consistent: pairs divided 4/3, 3/2, 2/1; five numerals 4, 3, 2, 2, 1. It agrees with the `text_issues` of A and C in `packet-g4.json`.
- The note is kept as it stands. The source is relabelled `[not re-checked]` instead of `[checked]`.

### V47, note 1 (corrected: source)
- **Was:** "Lewis & Short, Gaffiot, Georges s.v. torsio, appensio".
- **Reason:** The dictionaries do not say this.
  - *Torsio:* L&S "a wringing or griping"; Georges "Marter, Plage, Grimmen"; Gaffiot "colique".
  - "Twisting" is supported by Georges and Gaffiot s.v. *tortio* ("das Drehen", "action de tourner, torsion"). DMLBS gives *torsio* as the Late Latin spelling of *tortio*.
  - *Appensio* is not in L&S at all. Georges and Gaffiot give only "weighing". "Hanging" is supported by DMLBS s.v. *appensio* 1 "hanging (of bells)".
- **Now:** the source states exactly which dictionary supports which gloss. The note text ("torsio 'twisting' … appensio 'hanging'") stands, since it is supported as stated.
- **Confirmed:** DMLBS *claviculus* "little nail, tacket"; printed "chor-|datum" at 50.4–5.

### V47, note 2 (corrected: content and source)
- **Was:** Theon lists "the same methods … and for wind instruments the pipes and the breath".
- **Reason:** Theon (Hiller pp. 56.9–57.7) lists:
  - length and thickness of strings;
  - tension by turning the pegs;
  - "or more evidently" (γνωριμώτερον) the hanging of weights;
  - for wind instruments, the width of the cavities (εὐρύτης τῶν κοιλιῶν) and the tightening and slackening of the breath;
  - besides these, volumes and weights such as discs and vessels.

  He says cavities, not pipes, and his list is longer. Note 3 already correctly says "width of the cavities".
- **Now:** "almost the same methods", followed by the exact list, in ru and en.
- **Confirmed:**
  - Boethius I.10–11, pp. 196–198 (I.11, p. 198.11–14 *aequa pondera nervis aptans*);
  - L&S *comperio*;
  - the physics (pitch ∝ √tension; weights 4:1 for the octave and 9:4 for the fifth), kept as `[from memory]`.

### V55, note 1 (corrected: content and source)
- **Was:** "In V04 the same word follows an affirmation and means 'moreover'".
- **Reason:** In form, V03 ends with a negative sentence (*Rerum enim naturalium nulla est, quae vacet symmetria*). What distinguishes V04 is that *quinimo* adds a stronger claim, extending from natural things to everything made. That is L&S *quin* II.C.1 (*quin etiam* "yea indeed, nay even"). Also, V04 is rendered «более того» / "indeed" in composed-g3, not "moreover".
- **Now:** "adds a stronger claim to what precedes and means 'indeed, moreover' (like quin etiam, L&S quin II.C.1)", with the same change in ru.
- **Confirmed:** L&S II.C.2 and II.D as cited.

### V62, note 1 (corrected: content added)
- **Reason:** L&S, Georges and Gaffiot all record the noun *modulatus, -ūs* "a modulating, music" (Sen. *Herc. F.* 263). So *modulatu* can equally be the ablative of respect of that noun. The supine analysis (A&G § 510) stands.
- **Now:** one sentence added: the form coincides with that ablative, and the sense is the same.

### V63, note 2 (corrected: content and source)
- **Was:** Theon "therefore Plato adopts it".
- **Reason:** Theon p. 56.5 reads διὸ μᾶλλον τοῦτο παραλαμβάνει Πλάτων. The μᾶλλον ("rather, in preference") had been dropped.
- **Now:** "adopts it in preference (μᾶλλον … παραλαμβάνει)" / «предпочтительно принимает его».
- **Checked:**
  - Theon p. 56.3–5 and pp. 63.25–64.1 (Plato carried the diatonic genus and the system to four octaves, a fifth and a tone; Hiller's marginal reference is Tim. 35 sq.);
  - *Timaeus* 36b (256:243);
  - *Republic* 399a (Dorian and Phrygian);
  - Boethius I.21, p. 212.26 (*aliquanto durius et naturalius*).

### V64, note 1 (corrected: content and source)
- **Was:** "cf. Pliny's moduli Lydii, Dorii, Phrygii".
- **Reason:** The wording is the one L&S use (s.v. *modulus* I.4, citing Plin. 7.204). Pliny's text itself could not be opened in this check.
- **Now:** "cf. moduli Lydii, Dorii, Phrygii, as L&S cite Pliny (7.204)". The source marks Pliny's text as not opened.
- **Confirmed:** L&S I.4 and Gaffiot ¶ 4.

### V64, note 2 (corrected: content and source)
- **Was:** "both are grammatically possible", citing A&G §§ 303–306 generally.
- **Reason:** A&G does not discuss a nearest antecedent. The relevant rule is § 305: the relative agrees with its antecedent in gender and number.
- **Now:** the note states why both readings are possible: *quorum* (gen. pl. masc./neut.) fits both masculine *modulus* and neuter *genus* (*horum … unumquodque*). The source is narrowed to § 305.

### Source-only notes on verified items
- **V64, note 4:** The Pollux passage was read in Bethe's edition, vol. 1, p. 233, § IV.108 (καὶ μέλος δέ τι ἐξόδιον, ὃ ἐξιόντες ᾖδον, in the chorus section). Bekker 1846, p. 168 could not be read: the scan's OCR has no Greek. It is marked `[not re-checked]`. LSJ s.v. ἐξόδιος confirms there is no funeral sense. The hedged remark that a funerary sense "is sometimes supposed" is left as an explicitly uncertain statement.
- **V39, note 1:** confirmed exactly:
  - Sectio canonis props. 14–15, von Jan pp. 160.20–161.16 (octave < 6 tones; fourth < 2½ tones; fifth < 3½ tones);
  - Boethius I.21, p. 213.11–12, *duorum tonorum est ac semitonii, sed non pleni*.
- **V40, note 1:** Boethius *Arith.* I.31, p. 65.12–17 gives exactly Vinet's pair 16:6 as an example of *duplex superbipartiens* (*VIII ad III … et XVI ad VI*). Mus. I.4, p. 192.14–17 confirms *duplex superbipartiens, ut sunt tres ad octo*.
- **V44, note 3:**
  - *Arith.* I.29, p. 61.17–19 (*duplex sesqualter*);
  - Mus. I.4, p. 191.25–27 (*superbipartiens, ut sunt quinque ad tres*);
  - Mus. I.4, p. 192.3–5 (*duplex supersesqualter, ut sunt quinque ad duo*; the form *supersesqualter* is Friedlein's text);
  - added: *Arith.* I.28, p. 59.1–4, on 5:3.
- **V38, n. 1; V52, n. 2; V53, n. 1; V58, n. 2; V59, n. 2; V62, n. 2:** Theon passages confirmed at Hiller 49.3–5, 55.8, 54.12–14, 55.5–7, 55.15–17 and 56.1–3.
- **V52, note 2; V56, note 1; V59, note 2:** Boethius I.21 confirmed at pp. 212.25, 213.4–5 and 213.1–2.
- **V62, note 2:** Cic. *Div.* 2.96 reads *meditatione atque exercitatione*; L&S meditatio II.A is as cited.
- **V65, note 2:** The Dowland quotation is exact (book II, ch. 6, "Of Tact"). The DeFord title is confirmed bibliographically only.

## Table of all notes

| Segment | Note | Verdict | Sources opened |
|---|---|---|---|
| V34 | 1 | verified | Latin V31–V34, X29; composed-g3 note to V31 |
| V34 | 2 | corrected | L&S ratio; Latin V11, V19, V22, V43, X29; composed-g1/g3 renderings |
| V34 | 3 | verified | arithmetic |
| V34 | 4 | verified | LSJ διαπασῶν; composed-g3 note to V33; Latin V34, X29 |
| V35 | 1 | corrected (source) | LSJ διαπασῶν; L&S tamquam; note to V33 |
| V35 | 2 | verified | Latin V35, X30; arithmetic |
| V36 | 1 | corrected | Latin X31, V37; Theon (Hiller) 47–48; Gaudentius (Jan) 337–338; Forster Probl. XIX.39; LSJ ἀντίφωνος, παράφωνος |
| V36 | 2 | verified | Boethius Mus. I.6, II.27, V.8–9 (Friedlein) |
| V37 | 1 | verified | L&S excipio, par/pariter; Latin and rendering of X32 |
| V37 | 2 | verified | Latin V17, V36; arithmetic |
| V37 | 3 | verified | Latin V11, V15; composed-g3 renderings and notes |
| V38 | 1 | verified | Theon (Hiller) 49; Latin V36 |
| V39 | 1 | verified | arithmetic; Latin V39, V55; Sectio canonis (Jan) 160–161; Boethius Mus. I.21 |
| V40 | 1 | verified | Boethius Mus. I.4, Arith. I.31; Latin X36, V22, V40–V44; arithmetic |
| V42 | 1 | corrected (source) | A&G § 135; Boethius Arith. I.28, Mus. V.10, II.27; arithmetic |
| V42 | 2 | unverifiable | packet-g4 text_issues (page image not available) |
| V43 | 1 | verified | L&S intentio, intensio; printed lines 49.9–10, 49.19 |
| V44 | 1 | verified | L&S ratio; Latin V43, V45 |
| V44 | 2 | verified | Latin V44, X38; arithmetic |
| V44 | 3 | verified | Boethius Arith. I.28–29, Mus. I.4; about.md § 4.3 |
| V45 | 1 | verified | L&S intensio; composed-g3 note to V11; Latin V43 |
| V46 | 1 | verified | arithmetic |
| V47 | 1 | corrected (source) | L&S torsio; Georges, Gaffiot tortio, appensio; DMLBS tortio, appensio, claviculus; printed lines 50.4–5; Latin X41 |
| V47 | 2 | corrected | L&S comperio; Theon (Hiller) 56–57; Boethius Mus. I.10–11 |
| V47 | 3 | verified | L&S amplitudo; Theon (Hiller) 57 |
| V47 | 4 | verified | L&S intensio; about.md § 4.5 |
| V49 | 1 | verified | L&S facultas; Latin and rendering of V32 |
| V49 | 2 | verified | Latin V17, V18, X42; composed-g3 notes to V18 |
| V49 | 3 | verified | L&S intensio |
| V49 | 4 | verified | printed lines 51.1–2; Latin V35–V40 |
| V50 | 1 | verified | Latin V47, V50, X43 |
| V52 | 1 | verified | L&S modulatio; Latin V52–V65, X44; composed-g2 rendering of X44 |
| V52 | 2 | verified | about.md § 4.5; Boethius Mus. I.21; Theon (Hiller) 55; Latin V53, V58, V63 |
| V53 | 1 | verified | L&S fere; Latin V54–V59; Theon (Hiller) 54 |
| V55 | 1 | corrected | L&S quin; Latin V03, V04, V54; composed-g3 rendering of V04 |
| V55 | 2 | verified | Latin V39, V53, V56; arithmetic |
| V56 | 1 | verified | Boethius Mus. I.21; Latin V55 |
| V57 | 1 | verified | Latin V31, V32, V34, X49; note to V31; L&S confusio |
| V58 | 1 | verified | L&S tempero; Latin V60 |
| V58 | 2 | verified | Latin X50; Theon (Hiller) 55 |
| V59 | 1 | verified | Latin V22, V57; arithmetic |
| V59 | 2 | verified | A&G § 540; Boethius Mus. I.21; Theon (Hiller) 55 |
| V59 | 3 | verified | Latin V05, V52 |
| V60 | 1 | verified | Latin V58; L&S tempero |
| V62 | 1 | corrected | A&G § 510; L&S modulor, modulatus; Georges, Gaffiot modulatus |
| V62 | 2 | verified | L&S meditatio; Cicero Div. 2.96; Theon (Hiller) 56 |
| V63 | 1 | verified | L&S simplus; Latin V31, V52–V57, X55 |
| V63 | 2 | corrected | Theon (Hiller) 56, 63–64; Plato Tim. 36b, Rep. 399a; Boethius Mus. I.21 |
| V64 | 1 | corrected | L&S modulus; Gaffiot modulus; Latin X56 |
| V64 | 2 | corrected | A&G §§ 303–306 (§ 305 applies); Latin V64 |
| V64 | 3 | verified | LSJ Παιάν; L&S Hymen/Hymenaeus; printed line 53.12; Latin X56 |
| V64 | 4 | verified | L&S exodium; LSJ ἐξόδιος; Pollux IV.108 (Bethe) |
| V65 | 1 | verified | Latin and rendering of X57; L&S pausa, concito |
| V65 | 2 | verified | Dowland/Ornithoparchus (EEBO-TCP A08534) II.6; DeFord (bibliographic); Latin V65 |
| V65 | 3 | verified | L&S temperamentum |

**Totals:** 55 notes checked. 43 verified, 11 corrected (8 in content, 3 in the source only), 0 deleted, 1 unverifiable.
