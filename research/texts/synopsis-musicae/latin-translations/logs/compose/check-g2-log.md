# Check of composed group 2 (Xylander X30–X58)

Checked against: packet-g2.json (Latin, A–D, reviews, recheck R05–R07, place cards X04–X09, agreed points) and common.json (general cards, agreed points).

For every segment I checked:
- nothing omitted or added against the Latin;
- the construal and the numbers;
- the ratio brackets and the [ ];
- the cards and agreed points;
- the corroborated and rechecked errors;
- the terms;
- the notes and their sources;
- the anchors.

I verified the claims that matter in L&S, LSJ, DMLBS, Georges and Gaffiot (via the Logeion API) and in Boethius, *De institutione musica* (Latin Wikisource: Friedlein's text of book I, Migne's text of book V). A backup of the composed file as received is at work/chkg2/composed-g2.before-check.json.

**Result.** 6 segments were changed: X31, X32, X41, X50, X52, X57. Two changes are in the running English text (X50, X52); the other five corrections are in notes. Nothing needed changing in the other 23 segments.

## Changes

### X31: note 0 (Paraphonum, Antiphonum)
- **Was:** «субстантивированные прилагательные среднего рода» / "neuter adjectives used as nouns".
- **Problem:** in X31 the words are predicative adjectives agreeing with genus (*id genus consonantiae quod Paraphonum Graeci dicunt*). They are used as nouns only in X32 (*Inter paraphonum et antiphonum*).
- **Now:** "neuter adjectives: here they agree with genus (quod … dicunt), in X32 … they are used as nouns".
- **Source added:** the Latin of X31–X32.

### X31: note 1 (Ptolemy's classes in Boethius)
- **Was:** "the octave and the double octave form a class of their own, the octave and a fourth and the octave and a fifth another".
- **Problem:** this implies that the two compounds form a class of their own. They do not. In Boethius's report of Ptolemy the octave and the double octave are *aequisonae*, and the octave and a fourth and the octave and a fifth are *consonae* together with the fourth and the fifth.
- **Checked in:** Migne V.10–11 = Friedlein V.11–12: «aequisonae quidem sunt diapason ac bis diapason … Consonantiae … diapente ac diatessaron, et diapason ac diapente, et diapason ac diatessaron».
- **Done:** rewritten in both languages; the verified reference added to the source.

### X32: note 3 (proportionalitas)
- **Was:** RU «равенство отношений»; EN "likeness of ratios".
- **Problem:** the two languages disagree, and the agreed point on proportionalitas gives Boethius's sense as «сходство отношений».
- **Done:** RU made «сходство отношений»; the agreed point added to the source.

### X41: note 4 (intensio et remissio spiritus)
- **Was:** "the sense ‘strengthening’ is attested for this pair".
- **Problem:** L&S (checked) gives intensio I.B "an intensifying, increase" with one citation, Seneca *NQ* 7.1.3 *intensionibus ac remissionibus*, which is about the sun's heat, not the breath.
- **Now:** "L&S gives the sense ‘intensifying, increase’ for intensio precisely in a pair with remissio (… Seneca, of the sun’s heat)".
- **Source:** marked as checked via Logeion.
- The running text («усиление и ослабление дыхания», per card G30) is unchanged.

### X50: running English text and note 0 (confundetur)
- **Was:** "will be blended the genus of the fourth".
- **Problem:** card G19 (latin field: "X50 confundetur") decided the English for each Latin word: coalitus = coalescence, the confusio family = fusion. "Blending" was astra's option (c), which was not chosen. Confundo is the verb behind Vinet's confusio.
- **Now:** "will be fused the genus of the fourth". The anchor_en is updated.
- **Note now says:** confundo is the word behind Vinet's confusio (V57, V59), hence "fused" in English, as distinct from coalitus in X49 and X51 ("coalescence"); in Russian both are «слияние». This is the note on the Latin difference that G19's evidence asks for.
- The Russian «сольётся» is unchanged.
- Recorded in the segment's fixes.

### X52: running English text (genus)
- **Was:** "the remaining genera of systems".
- **Problem:** *reliqua systematum genera* are kinds of systems, not genera of melody; compare Vinet V60, *caetera quoque systemata*. Card G14 says that non-technical genus is "kind" in English.
- **Now:** "the remaining kinds of systems". The Russian «роды» stays (G14).
- G14 added to the segment's decisions; recorded in fixes.

### X57: note 2 (tactus)
- **Was:** "Tactus is the touch of a string (so in Cicero, beside pulsatio, the stroke)".
- **Problem:** Cicero, *de Or.* 3.57.216, the passage L&S cites, has *quae (chordae) ad quemque tactum respondeant*. The nearby word is the participle *pulsae*; pulsatio does not occur there.
- **Now:** "in Cicero strings ‘respond to every touch’: ad quemque tactum respondeant".
- **Source:** "Cic. de Or. 3.57.216 [checked, via Logeion]".

## Checked and left as composed (claims that might look doubtful)

- **X38 note 3, «duplex supersesqualter, ut sunt quinque ad duo».** This is correct for Friedlein's text of I.4 (Latin Wikisource reads «duplex supersesqualter»); Migne reads «duplex sesquialter». No change.
- **X38, qua.** The note's grammar agrees with rechecks R06 and R07 (quam would resume quantitas, quem excessus) and with A&G § 305. The running text follows card X05-qua-habet, option d. The Vinet parallel (V44 *quo numero superat sonos, qui ipsum praecedunt*) and "Vinet calls 5:3 superpartiens" (V44 *tertii, superpartiens*) are both confirmed.
- **X32.** The note on assono and obsono agrees with L&S: assono "to sound to, respond to", Ov. *Met.* 3.507; obsono "to interrupt by a sound", Plaut. *Ps.* 205. Vinet V37 *secundum proportiones et rationes* is confirmed. The note pairing X32's antiphonic examples with the note names of X14 (8–1, 11–4, 12–5, 15–8, all octaves) is correct.
- **X31.** LSJ παράφωνος "sounding beside"; ἀντίφωνος "sounding in answer, concordant, as in the octave", with Pl. *Lg.* 812d. Gaudentius 8 on paraphonic intervals (the tritone) agrees with LSJ.
- **X37, X39.** The renderings follow G06 and G29. L&S intensio II, "the tune", Censorinus 12, is confirmed. DMLBS acuitas sense c, "sharpness (of pitch)", is confirmed.
- **X41.** The Boethius I.11 list (weights, pipes, cups, length and thickness of strings) is correct. DMLBS 3 clavus 1g, "peg", is correct.
- **X45, X49.** L&S coaptatio "a word coined by Augustine for translating the Gr. ἁρμονία" and coalitus "communion, fellowship", Arn. 4, are confirmed.
- **X50, X51, X54.** The Boethius I.21 quotations are confirmed in Friedlein's text: chroma *in mollius decidens*; enarmonium *optime atque apte coniunctum … magis coaptatum*; *per diesin et diesin et ditonum*. I.21 says nothing about the enharmonic being out of use, as the X54 note states.
- **X56.** LSJ ἐξόδιον "finale of a tragedy"; Latin exodium "after-piece". The paean, hymenaeus and "exit song" follow card G36, option b.
- **X57.** LSJ μονή, «μ. τις καὶ στάσις τῆς φωνῆς Aristox. Harm. p. 12 M.», is confirmed. L&S mansio "a staying, remaining" is confirmed.
- **X30.** L&S gemino includes "to repeat" (Ov.), which supports «повторяются» / "repeated".
- **Brackets.** Every ratio name in the running text has its bracket. In X36 the bracket follows card G28, option b. «сверхдвучастное третей» is kept as G28 settles it; sol's objection stays in the composer's open list.
- **Anchors.** All 60 notes have anchors that appear verbatim in their text; I checked this again after the edits.
- **Cards and agreed points.** Every place card for the group (X04–X09) is applied as decided. All general and agreed points for these segments are applied, with the two exceptions corrected above (G19 in X50, G14 in X52).
- **Errors.** Every confirmed, modified or added reviewer error on the wording that was taken over (A, C, and the B/D wording in X30, X37–X41, X51, X56, X58) is fixed. The one rechecked major error (R05, B's «количества») is not taken into the text.

## Minor points left as they are
- **X30.** EN "are repeated again" and RU «вновь повторяются» are slightly pleonastic but render iterum geminantur faithfully. Not changed.
- **X56.** RU «заключительная песнь» against EN "exit song" is exactly the pairing of G36, option b. Not changed.
