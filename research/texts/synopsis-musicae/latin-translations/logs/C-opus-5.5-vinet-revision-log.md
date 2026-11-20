# Vinet: revision log (passes 5–6)

Input: `work/vinet-draft.json`. Output: `work/vinet-revised.json` (same format: 66 segments V01–V66 in the order of latin-texts.json, 80 terms, 5 text issues, empty contamination list; 57 notes, 15 doubts). The changes are applied by `work/rev/revise.py`, which asserts every replaced string, so the log below matches the file exactly.

## 1. What was checked

- **Critical revision.** Every segment was compared with the Latin and the printed lines. No omissions or additions were found; all additions are in brackets. Every number and ratio was recomputed, and all are correct: V17 (12 tones = two octaves), V22 (17:16, 33:32, 289:288), V27, V29–V30, V37 (the four octave pairs), V39 (cents, the leimma, the comma), V40–V42, V44, V46, V53–V59. The ratio brackets were checked by script at every ratio name in both languages. The term renderings are consistent across the version (convenientia / conveniens / convenire; intensio and intentio; ratio and proportio; modulatio; sonus; vox; chorda and nervus).
- **Figures.** The three figures were checked on the scans and the draft's crops. The tick positions on p. 44 were measured. The descriptions on pp. 46 and 49 are accurate. The p. 44 description needed a correction (see V22).
- **References.** The references marked [checked] were re-opened, and several [from memory] references were now checked: Theon (Hiller), Boethius (Friedlein), von Jan (Problems XIX, Gaudentius, Sectio canonis), Lewis & Short, Gaffiot and LSJ (through Logeion), Allen and Greenough (Dickinson College Commentaries) and Vitruvius (LacusCurtius). One citation was wrong (Boethius V.9, see V40).
- **Contamination.** I met no forbidden material, so the list stays empty.

## 2. Changes to the translation

### Russian (stylistic)

- **V06, V24, V31, V55.** The generic second person («ты назвал бы», «ты можешь», «как ты пожелаешь», «после того как ты поставишь») is a calque of Latin *dixeris, potes, volueris, imposueris*. It is replaced by impersonal constructions: «можно … назвать», «можно разделить», «как будет угодно», «после того, как поставлены». The alternative in the V31 doubt is adjusted to match.
- **V06.** «что, как видно, находится в … состоянии» becomes «что предстаёт в прекраснейшем и наилучшем состоянии». This renders *conspiciatur* "is seen to be" without the parenthetical «как видно» ("apparently").
- **V16.** «его вообще не следует называть звуком» becomes «его не следует даже называть звуком», to render *ne … quidem*.
- **V20.** «Но о звуках сказанного достаточно» becomes «Итак, о звуках сказано достаточно»: *atque* here closes the topic and is not adversative.
- **V33.** «Кроме того, помимо тех» is redundant and becomes «Впрочем, помимо тех».
- **V34.** «и ими завершается» becomes «и ими ограничивается», closer to *terminetur* "is bounded".
- **V36.** «Интервал кварты и квинта консонируют» becomes «Интервал кварты и [интервал] квинты консонируют»; the draft joined a phrase and a bare noun ungrammatically.
- **V37.** Word order: «как бы мягко и уместно» (*leniter quodammodo et apposite*), «консонирует вместе с низким», «одновременно поднимаются или опускаются».
- **V50.** «Различаются … от» is not idiomatic and becomes «Отличаются … от».

### English (stylistic and accuracy)

- **V04, V16.** The archaic "nay rather" becomes "indeed". In V16 "not even … at all" renders *ne … quidem omnino*. In V04 "it will never have been beautifully made" becomes "it will never prove to have been beautifully made", which keeps the future perfect and reads naturally.
- **V20.** "But so much for the notes" becomes "And so much for the notes".
- **V24.** The object-first order ("For a string that contains … you can divide into …") becomes "For you can divide a string that contains the sesquioctave [9:8] ratio into the semisesquioctave …".
- **V32.** The draft turned the relative clause *quod licet … resonet* into a new main clause. It is restored as a relative clause inside the causal clause: "… a melos which, though it has the force of many intervals, nevertheless sounds through a single interval".
- **V33.** "Besides, there are other intervals apart from those" is redundant and becomes "There are, however, other intervals besides those".
- **V34.**
  - "by reason of the ratio" rendered *ratione* twice; it becomes "with respect to the ratio". The doubt's "choice" is updated to match.
  - "passes through … and ends with them" becomes "proceeds through … and is bounded by them".
- **V36.** "The interval of the fourth and the fifth are consonant" was ungrammatical. It becomes "The interval of the fourth and [that of] the fifth are consonant".
- **V37.** "taking each other up gently, in a way, and fittingly" becomes "taking each other up, as it were, gently and fittingly".
- **V46.** "the same may be observed" dropped *nobis* and the future *licebit*. It becomes "we shall be able to examine the same in the remaining ratios too".

## 3. Changes to notes, checks and references

- **V03.**
  - Vitruvius 1.2.4 checked and quoted, now [checked].
  - *universitas* now cited from Lewis & Short (Cic. N. D. 1.120), [checked]. The note adds Cicero's *universitatem omnia continentem* (N. D. 1.39) as a parallel to *Musica … contineri*.
- **V09 (doubt).** The vague "[from memory]" grammar reference becomes Allen and Greenough § 317 b–c [checked].
- **V11.** Thrasyllus' definition of ἐναρμόνιος was paraphrased loosely. It now follows Theon p. 47: the voice "can be found both higher than a high one and lower than a low one".
- **V17.**
  - Theon reference made precise (p. 88.17–18).
  - The printed accent *solùm* (adverb) added as evidence. Lewis & Short *solum* now [checked].
- **V18.** LSJ πεντεκαιδεκάχορδος checked (Adrastus in Theon p. 64). ἑκκαιδεκάχορδος is not in LSJ, and the note now says so instead of citing it [from memory].
- **V22.**
  - **Figure.** The draft said that the points I and M lie "at about 8¼ and 8½ as measured on the print". Measured on the crop, I lies about 0.34 and M about 0.57 of the L–A unit. The woodcut is inexact, and only the text makes them 8¼ and 8½. The note, the doubt's "choice" and the text issue now say this.
  - **Letter at 2.** It is a poorly printed letter that resembles G, where D is expected. The draft said "D (poorly printed)".
  - **Checks.** Added: four dieses of 33:32 are about 1.13098, larger than 9:8 by about 9.18 cents.
  - Lewis & Short *duplus* checked (*duplo major*).
- **V25 (doubt).** The Lewis & Short *omnimodo* gloss was misquoted. It is replaced by the actual entry ("by all means, in all ways, entirely, altogether, wholly"), now [checked].
- **V32.** LSJ μέλος checked: sense B, "musical member, phrase". The note adds that Xylander has *cantilena* here (X27).
- **V33, V34.**
  - LSJ διαπασῶν checked.
  - The V34 note adds Xylander's *per omnes, hoc est, per octo* (X29), which keeps the two versions' difference visible. It also notes that *ingrediatur termineturque* governs all three members of the list.
- **V37.** Lewis & Short *excipio* ("to follow after, to succeed") and *pariter* (B 1, "at the same time, together") checked.
- **V39.**
  - The Cleonides reference [from memory] is replaced by checked parallels: Theon p. 54.11–12, where the fourth is "of two tones and a semitone", and the Euclidean *Sectio canonis*, props. 14–15 (von Jan pp. 160–161). The *Sectio* proves that the fourth is less than two tones and a semitone and the octave less than six tones.
  - Check added: with Vinet's own arithmetical semitone of V22 (17:16), two tones and a semitone make 1377:1024 (512.78 cents). This is larger still, so the "nameless addition" is wrong on any reading.
- **V40.**
  - **Wrong citation.** "Boethius V.9, p. 359" for *dupla superbipartiens ut octo ad tres* was wrong. The words are in V.10, p. 360.20–26; the Pythagorean and Ptolemaic positions are in V.7–10, pp. 357–360.
  - **Overstatement.** "The Pythagoreans did not count this ratio" is Boethius' account. Theon p. 56.9–15 lists the octave and a fourth in 8:3 among the consonances whose ratios Pythagoras is said to have found first. The note now gives both.
- **V42.**
  - Boethius V.10, p. 360.25–26 added: *habent enim ternarium octo bis duasque eius partes, id est duas unitates*. It confirms that *duas eius partes* means two thirds.
  - Xylander's gloss *nimirum super bipartiens tertias* (X36) added.
- **V43.** Lewis & Short *intensio* (Seneca, Censorinus; "the tune") and *intentio* (*vocis*) checked, now [checked].
- **V44.** Boethius, Mus. I.4, p. 191.25–27 (*superbipartiens, ut sunt quinque ad tres*) added for *superpartiens* = 5:3.
- **V47.**
  - Theon lists one more method, with masses or weights such as discs or vessels; the note no longer calls the lists identical.
  - γνωριμώτερον is rendered "more evidently" («нагляднее») instead of "more clearly".
  - Lewis & Short *comperio* now [checked].
- **V49.**
  - Xylander does use *heccaedecachordum* in X15; the note now specifies that X42 is the place where he describes the system without the Greek word.
  - Lewis & Short *facultas* now [checked].
- **V58.** The source for *temperatum* is now Lewis & Short *tempero* ("to divide or proportion duly, mingle in due proportion"), not *temperamentum*.
- **V59, V62.** Allen and Greenough § 540 and § 510 checked, now [checked].
- **V64.** Gaffiot *modulus* ¶ 4 ("mesure [musique], mode, mélodie") added as evidence for "mode".

## 4. Terms and text issues

- **Terms.** Evidence updated to match the checks above: *universitas*, *symmetria*, *temperare*, *modulus*, *Pentekaedecachordum*, *melos*, *facultas*, *intensio/intentio*, *duplex-superpartiens*, *superpartiens*. No rendering changed.
- **Text issue V64 (*Paeeon*).** The draft proposed *Paeon*. The revision keeps *Paeeon*: it is a regular transliteration of the epic Παιήων (LSJ s.v. Παιάν), and the *é* is the printer's accent, as in *Hypáte*. It is not a misprint.
- **Text issue V22 (figure).** The argument now gives the imprecise placing of the points and the poorly printed letter at 2.

## 5. Kept as in the draft, for the reviewer

- **V22, *octo cum semisse / octo cum quadrante*.** Kept literal, with the arithmetical interpretation (17:16, 33:32) in the notes.
- **V37, the four examples.** All four are octaves (1–8, 4–11, 5–12, 8–15), although V36 lists the compound antiphonic intervals too. Translated as printed.
- **V39, the nameless addition.** Translated as it stands. The note now has the *Sectio canonis* parallel.
- **V47, *intensio spiritus ac remissio*.** The departure from the convention ("tension and slackening of the breath") is kept, with its note.
- **V17 and V18.** The renderings «меса одна» / "mese alone" (V17) and the bracketed «[инструмент] / [система]» (V18) are kept, with their doubts.
