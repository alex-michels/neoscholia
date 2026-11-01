# Consistency log, final reading of U001–U067 (1.11.2026)

The final reader's pass over `compose/final/`. I read DECISIONS.md and BRIEF.md first, then the whole text with
`show_composed.py` (texts, then notes), the three verifier logs, the glossary and, where a point needed it, the unit
packets, the cards and `edition/`. Every change below was made in place in `final/Uxxx.json`; the verifiers' `verify`
fields are left as their record. 165 changes in 52 units: 14 in the running text and
its anchors, 28 to remove repeated notes, 37 to citation forms inside the notes, 86 to source fields.

Result: `python -I scripts/check_composed.py <ws-cmp> final` reports no problems (67 units, 0 problems), after the two
corrections to the checker in section 5.

## 1. Running text: one rendering for one Greek construction

| Unit | Lang. | Where | Before | After | Why |
|---|---|---|---|---|---|
| U023 | RU | text | ни удвоить данный: ведь число шестнадцать, будучи квадратом, нельзя | ни удвоить данный [квадрат]: ведь число шестнадцать, являющееся квадратом, нельзя | Same Greek as U030 (τὸ δεδομένον; τετράγωνον ὄντα): one rendering; the gerund «будучи» referred to the object of an impersonal infinitive construction (flagged by the U029–U042 verifier, corrected there in U030 only) |
| U023 | EN | text | arithmetic cannot cut a given square into [two] equal squares, or double the given one: | arithmetic cannot cut the given square into [two] equal squares or double the given [square]: | Same Greek as U030 (τὸ δοθὲν τετράγωνον … τὸ δεδομένον): same rendering as U030 |
| U021 | EN | text | For geometry both subtracts, in every way, a smaller straight line from the greater and adds | For geometry both subtracts a smaller straight line from the greater in every way and adds | Same Greek as U029, whose word order the verifier corrected (“subtracts a smaller straight line from the greater in every way”) |
| U031 | EN | text | makes half the given square, | makes half of the given square, | Same Greek (ἥμισυ τοῦ δοθέντος τετραγώνου) as U024 “makes half of the given square” |
| U034 | RU | text | а по упорядоченному числу промежуточных звуков | а по упорядоченному количеству промежуточных звуков | ποσότης is «количество» / “quantity” (agreed glossary; so in U046 «в количестве звуков» / “quantity of notes”); «число» / “number” is kept for ἀριθμός (U045, U047), with which the author contrasts it; the note on U034 already says «количества (ποσότης)» |
| U034 | EN | text | but from the ordered number of the notes in between | but from the ordered quantity of the notes in between | ποσότης is «количество» / “quantity” (agreed glossary; so in U046 «в количестве звуков» / “quantity of notes”); «число» / “number” is kept for ἀριθμός (U045, U047), with which the author contrasts it; the note on U034 already says «количества (ποσότης)» |
| U034 | EN | text | by the ratio of the sounding from the first note to the last | by the ratio of the sound from the first note to the last | ἠχή: one English word in U034 and U045; U045 has “the raising of the sound” by card P08 (main_en), which outranks the glossary’s “sounding”; RU «звучание» in both already |
| U034 | EN | note 2 | judged by the raising of the sounding from the low to the high | judged by the raising of the sound from the low to the high | ἠχή: one English word in U034 and U045; U045 has “the raising of the sound” by card P08 (main_en), which outranks the glossary’s “sounding”; RU «звучание» in both already (the note quotes U045) |
| U044 | RU | text | а единицы не делятся, | а единицы не рассекаются, | τέμνω is «рассекать» / “cut” everywhere else (U019 μονὰς οὐ τέμνεται «единица не рассекается» / “the unit is not cut”; U023, U030 τεμεῖν, τέμνειν «рассечь» / “cut”), while «делить» / “divide” renders διαιρέω; U044 restates U019 |
| U044 | EN | text | and units are not divided, | and units are not cut, | τέμνω is «рассекать» / “cut” everywhere else (U019 μονὰς οὐ τέμνεται «единица не рассекается» / “the unit is not cut”; U023, U030 τεμεῖν, τέμνειν «рассечь» / “cut”), while «делить» / “divide” renders διαιρέω; U044 restates U019 |
| U044 | RU | note 4, anchor | единицы не делятся | единицы не рассекаются | Anchor follows the text change |
| U044 | EN | note 4, anchor | units are not divided | units are not cut | Anchor follows the text change |
| U044 | RU | note 4 | в числах единица не делится, деление возможно | в числах единица не рассекается, деление возможно | The note follows the text («рассекается», as in U019) |
| U044 | EN | note 4 | in numbers the unit is not divided; division is possible | in numbers the unit is not cut; division is possible | The note follows the text (“cut”, as in U019) |

## 2. Notes repeated in several units

The main note stays at the place DECISIONS.md names (or, where it names none, at the first occurrence); elsewhere a
short cross-reference.

| Unit | Lang. | Where | Before | After | Why |
|---|---|---|---|---|---|
| U009 | RU | note 1 | φθόγγων τὴν πρὸς ἀλλήλους ποιὰν σχέσιν; σύστημα δὲ διαστημάτων ποιὰν περιοχήν; ἁρμονία δέ ἐστι συστημάτων σύνταξις. Примеры | φθόγγων τὴν πρὸς ἀλλήλους ποιὰν σχέσιν (об определениях системы и гармонии см. примеч. к [U010] и к [U011]). Примеры | Thrasyllus’ definitions of the system and of harmony were quoted twice, here and in the notes on U010 and U011; each is kept at its own unit, a cross-reference here |
| U009 | EN | note 1 | φθόγγων τὴν πρὸς ἀλλήλους ποιὰν σχέσιν; σύστημα δὲ διαστημάτων ποιὰν περιοχήν; ἁρμονία δέ ἐστι συστημάτων σύνταξις. Thrasyllus’ | φθόγγων τὴν πρὸς ἀλλήλους ποιὰν σχέσιν (on the definitions of the system and of harmony see the notes on [U010] and [U011]). Thrasyllus’ | Same |
| U020 | RU | note 3 | в словарях это слово не отмечено (см. примеч. к [U018]). Автор | в словарях это слово не отмечено. Автор | Repeated the arithmetic of the main notes: Theon’s ἐφεκκαιδέκατον (note on U018) and the mean proportional √72 (note on U025); kept there, cross-references here (one reference to U018 at the end) |
| U020 | RU | note 3 | так что пополам делится избыток, а не отношение 9:8 (ср. Теон Смирнский, с. 69 Hiller: ἐφεκκαιδέκατον, 17:16). Равная по величине половина тона потребовала бы среднего пропорционального между 9 и 8, √72 ≈ 8,485, — иррациональной точки (см. примеч. к [U025]). | так что пополам делится избыток, а не отношение 9:8 (см. примеч. к [U018] и к [U025]). | Repeated the arithmetic of the main notes: Theon’s ἐφεκκαιδέκατον (note on U018) and the mean proportional √72 (note on U025); kept there, cross-references here |
| U020 | EN | note 3 | the word is not recorded in the lexica (see the note on [U018]). The author | the word is not recorded in the lexica. The author | Repeated the arithmetic of the main notes: Theon’s ἐφεκκαιδέκατον (note on U018) and the mean proportional √72 (note on U025); kept there, cross-references here (one reference to U018 at the end) |
| U020 | EN | note 3 | so that the excess is halved, not the ratio 9:8 (cf. Theon of Smyrna, p. 69 Hiller: ἐφεκκαιδέκατον, 17:16). A half of the tone equal in size would require the mean proportional between 9 and 8, √72 ≈ 8.485, an irrational point (see the note on [U025]). | so that the excess is halved, not the ratio 9:8 (see the notes on [U018] and [U025]). | Repeated the arithmetic of the main notes: Theon’s ἐφεκκαιδέκατον (note on U018) and the mean proportional √72 (note on U025); kept there, cross-references here |
| U020 | RU, EN | note 3, source | LSJ, DGE, Bailly, Pape (no entry for ἡμιεπόγδοος); Theon of Smyrna p. 69.13–17 Hiller; direct calculation | LSJ, DGE, Bailly, Pape (no entry for ἡμιεπόγδοος); U018; U025 | Source follows the shortened note |
| U026 | RU | note 1 | У Клеонида (гл. 5; Jan, с. 187–189) несоставны интервалы между соседними звуками: трёхполутон несоставной только в хроматике, дитон — только в энармонике, а всё, что больше дитона, составное; тритон в перечне автора с этим расходится. Об авторском понимании несоставного см. примеч. к [U027]. | У Клеонида (гл. 5, Jan, с. 187–189) трёхполутон несоставной только в хроматике, дитон — только в энармонике, а всё, что больше дитона, составное; тритон в перечне автора с этим расходится. О понятии несоставного у Клеонида и у автора см. примеч. к [U027]. | Cleonides’ definition of the incomposite (intervals between successive notes) was given twice, here and in the note on U027, the main place; here only what concerns the author’s list |
| U026 | EN | note 1 | For Cleonides (ch. 5, Jan pp. 187–189) the incomposite intervals are those between successive notes: the trihemitone is incomposite only in the chromatic, the ditone only in the enharmonic, and everything larger than the ditone is composite; the tritone in the author’s list departs from this. On the author’s own notion of the incomposite see the note on [U027]. | In Cleonides (ch. 5, Jan pp. 187–189) the trihemitone is incomposite only in the chromatic, the ditone only in the enharmonic, and everything larger than the ditone is composite; the tritone in the author’s list departs from this. On the notion of the incomposite in Cleonides and in the author see the note on [U027]. | Cleonides’ definition of the incomposite (intervals between successive notes) was given twice, here and in the note on U027, the main place; here only what concerns the author’s list |
| U026 | RU | note 2 | В хроматическом роде этот интервал несоставной (U058; Теон Смирнский, с. 55.2–6 Hiller: ἡμιτόνιον καὶ ἡμιτόνιον καὶ τριημιτόνιον ἀσύνθετον; так же у Никомаха). | В хроматическом роде этот интервал несоставной (см. примеч. к [U058]). | Theon’s chromatic tetrachord (τριημιτόνιον ἀσύνθετον, p. 55.2–6 Hiller) was quoted twice, here and in the note on U058, where the author describes that tetrachord; kept there |
| U026 | EN | note 2 | In the chromatic genus it is incomposite (U058; Theon of Smyrna, p. 55.2–6 Hiller: ἡμιτόνιον καὶ ἡμιτόνιον καὶ τριημιτόνιον ἀσύνθετον; likewise Nicomachus, Manual). | In the chromatic genus it is incomposite (see the note on [U058]). | Theon’s chromatic tetrachord (τριημιτόνιον ἀσύνθετον, p. 55.2–6 Hiller) was quoted twice, here and in the note on U058, where the author describes that tetrachord; kept there |
| U058 | RU | note 1 | «несоставной трёхполутон»: букв. «три полутона», интервал в полтора тона, приблизительно малая терция (в зависимости от строя); о термине см. | «несоставной трёхполутон»; о термине см. | The note repeated the definition of the trihemitone from the main P11 note (U026); it keeps the cross-reference, and receives Theon’s line reference and the Nicomachus remark moved from U026 |
| U058 | RU | note 1 | (с. 55 Hiller): κατὰ ἡμιτόνιον καὶ ἡμιτόνιον καὶ τριημιτόνιον ἀσύνθετον. Схема | (с. 55.2–6 Hiller): κατὰ ἡμιτόνιον καὶ ἡμιτόνιον καὶ τριημιτόνιον ἀσύνθετον; так же у Никомаха. Схема | The note repeated the definition of the trihemitone from the main P11 note (U026); it keeps the cross-reference, and receives Theon’s line reference and the Nicomachus remark moved from U026 |
| U058 | EN | note 1 | “incomposite trihemitone”: lit. “three semitones”, an interval of a tone and a half, approximately a minor third depending on the tuning; on the term see | “incomposite trihemitone”; on the term see | The note repeated the definition of the trihemitone from the main P11 note (U026); it keeps the cross-reference, and receives Theon’s line reference and the Nicomachus remark moved from U026 |
| U058 | EN | note 1 | (p. 55 Hiller): κατὰ ἡμιτόνιον καὶ ἡμιτόνιον καὶ τριημιτόνιον ἀσύνθετον. In tones | (p. 55.2–6 Hiller): κατὰ ἡμιτόνιον καὶ ἡμιτόνιον καὶ τριημιτόνιον ἀσύνθετον; likewise Nicomachus, Manual. In tones | The note repeated the definition of the trihemitone from the main P11 note (U026); it keeps the cross-reference, and receives Theon’s line reference and the Nicomachus remark moved from U026 |
| U058 | RU, EN | note 1, source | Theon of Smyrna p. 55 Hiller; LSJ s.v. τριημιτόνιον | Theon of Smyrna, p. 55.2–6 Hiller; U026; U027 | Source follows the note |
| U042 | RU | note 6 | потому что эти интервалы в них сливаются. σύμφθαρσις — «одновременное уничтожение» составных частей смеси, «слияние» (LSJ s.v. σύμφθαρσις). См. примеч. к [U027]. | потому что эти интервалы в них сливаются (о слиянии, σύμφθαρσις, см. примеч. к [U027]). | The LSJ gloss of σύμφθαρσις repeated the main note on U027; cross-reference only |
| U042 | EN | note 6 | because these fuse in them. σύμφθαρσις is the “simultaneous destruction” of the components of a mixture, their “melting into one another” (LSJ s.v. σύμφθαρσις). See the note on [U027]. | because these fuse in them (on fusion, σύμφθαρσις, see the note on [U027]). | The LSJ gloss of σύμφθαρσις repeated the main note on U027; cross-reference only |
| U042 | RU, EN | note 6, source | U026; U027; LSJ s.v. σύμφθαρσις | U026; U027 | Source follows the note |
| U043 | RU | note 1 | — термины логики: ἄμεσος говорится о посылке без среднего термина (Аристотель, «Первая аналитика» 68b30; «Вторая аналитика» 72b19), ἔμμεσος значит «имеющий средний термин» (у поздних комментаторов — Симпликия, Олимпиодора); по-русски в логике — «непосредственные / опосредованные». Интервал | — термины логики: ἄμεσος говорится о посылке без среднего термина, ἔμμεσος — о посылке со средним термином. Интервал | Repeated the main P09 note (U034: Aristotle’s loci, the late commentators, «непосредственные / опосредованные»); DECISIONS puts the main note at U034 and asks U043 only to explain the logical sense of the pair, which the note still does |
| U043 | EN | note 1 | are terms of logic: ἄμεσος is said of a premise without a middle term (Aristotle, Prior Analytics 68b30; Posterior Analytics 72b19), and ἔμμεσος means “having a middle term” (in the late commentators, Simplicius and Olympiodorus); in English logic, “immediate / mediate”. An interval | are terms of logic: ἄμεσος is said of a premise without a middle term, ἔμμεσος of one with a middle term. An interval | Repeated the main P09 note (U034: Aristotle’s loci, the late commentators, «непосредственные / опосредованные»); DECISIONS puts the main note at U034 and asks U043 only to explain the logical sense of the pair, which the note still does |
| U043 | RU, EN | note 1, source | Aristotle, Prior Analytics 68b30; Posterior Analytics 72b19; LSJ s.vv. ἄμεσος, ἔμμεσος; DGE s.v. ἔμμεσος | U034 | Source follows the note (the references stand in the note on U034) |
| U051 | RU | note 3 | и о параллели у Клеонида (гл. 14: διάγραμμα … τὰς τῶν μελῳδουμένων περιέχον δυνάμεις, ср. здесь ἐμπεριέχον δυνάμεις) см. примеч. к [U027]. | и о параллели у Клеонида (гл. 14) см. примеч. к [U027]. | The Cleonides ch. 14 quotation repeated the main P10 note (U027); cross-reference only |
| U051 | EN | note 3 | and on the parallel in Cleonides (ch. 14: διάγραμμα … τὰς τῶν μελῳδουμένων περιέχον δυνάμεις, cf. ἐμπεριέχον δυνάμεις here), see the note on [U027]. | and on the parallel in Cleonides (ch. 14), see the note on [U027]. | The Cleonides ch. 14 quotation repeated the main P10 note (U027); cross-reference only |
| U045 | EN | note 2 | (Cleonides ch. 2); the handbook English is “tension / relaxation”. “Intensification” | (Cleonides ch. 2). “Intensification” | Repeated the main P08 note (U037), which the note cites; the RU note has no counterpart |
| U030 | RU | note 1 | «[два]» добавлено по смыслу, как в U023: невозможно лишь деление пополам (половина 16, 8, и его удвоение, 32, не квадратные числа), а на четыре равных квадрата по 4 число 16 делится. τετραγωνισθῆναι — «стать квадратным числом», а не «быть возведённым в квадрат». Подробнее см. примеч. к [U023]; геометрическое | «[два]» добавлено по смыслу, как в U023. О числах 16, 8 и 32 и о значении τετραγωνισθῆναι см. примеч. к [U023]; геометрическое | Repeated the note on U023 (the same sentence of the main text, repeated in the P passage); cross-reference only |
| U030 | EN | note 1 | “[two]” is added for the sense, as in U023: only bisection is impossible (the half of 16, 8, and its double, 32, are not square numbers), while 16 can be divided into four equal squares of 4. τετραγωνισθῆναι means “to become a square number”, not “to be squared”. See the note on [U023]; the geometrical | “[two]” is added for the sense, as in U023. On the numbers 16, 8 and 32 and the sense of τετραγωνισθῆναι see the note on [U023]; the geometrical | Same |
| U030 | RU, EN | note 1, source | calculation; U023; U031 | U023; U031 | Source follows the shortened note |

## 3. Citation forms inside the notes (DECISIONS.md § 4)

| Unit | Lang. | Where | Before | After | Why |
|---|---|---|---|---|---|
| U014 | RU | note 2 | «диатон» (Щетников 2008; Александрова, Мякин 2009) или «диатоника» (Щетников 2008) | «диатон» (Щетников 2008а; Александрова, Мякин 2009) или «диатоника» (Щетников 2008а) | Two different works of Shchetnikov are dated 2008 (the U001–U028 verifier’s flag): the Nicomachus translation (ΣΧΟΛΗ 2.1) is 2008а / 2008a, «Алгоритм…» (ΣΧΟΛΗ 2.1, source of «сверхдвухчастное», «двукратное-и-половинное»; card P03) is 2008б / 2008b |
| U018 | RU | note 2 | откуда «двукратное с половиной»; Щетников 2008) | откуда «двукратное с половиной»; Щетников 2008б) | Two different works of Shchetnikov are dated 2008 (the U001–U028 verifier’s flag): the Nicomachus translation (ΣΧΟΛΗ 2.1) is 2008а / 2008a, «Алгоритм…» (ΣΧΟΛΗ 2.1, source of «сверхдвухчастное», «двукратное-и-половинное»; card P03) is 2008б / 2008b |
| U026 | RU | note 2 | «трёхполутон» (Щетников 2008; | «трёхполутон» (Щетников 2008а; | Two different works of Shchetnikov are dated 2008 (the U001–U028 verifier’s flag): the Nicomachus translation (ΣΧΟΛΗ 2.1) is 2008а / 2008a, «Алгоритм…» (ΣΧΟΛΗ 2.1, source of «сверхдвухчастное», «двукратное-и-половинное»; card P03) is 2008б / 2008b |
| U027 | RU | note 2 | «мелос» (Герцман 2024; Щетников 2008) | «мелос» (Герцман 2024; Щетников 2008а) | Two different works of Shchetnikov are dated 2008 (the U001–U028 verifier’s flag): the Nicomachus translation (ΣΧΟΛΗ 2.1) is 2008а / 2008a, «Алгоритм…» (ΣΧΟΛΗ 2.1, source of «сверхдвухчастное», «двукратное-и-половинное»; card P03) is 2008б / 2008b |
| U040 | RU | note 1 | У Щетникова (Щетников 2008) | У Щетникова (Щетников 2008а) | Two different works of Shchetnikov are dated 2008 (the U001–U028 verifier’s flag): the Nicomachus translation (ΣΧΟΛΗ 2.1) is 2008а / 2008a, «Алгоритм…» (ΣΧΟΛΗ 2.1, source of «сверхдвухчастное», «двукратное-и-половинное»; card P03) is 2008б / 2008b (the U040 packet: Shchetnikov’s Nicomachus has ἐπιμόριον «сверхчастное», ἐπιμερές «сверхмногочастное») |
| U036 | RU | note 1 | (с. 48 Hiller; пер.: Щетников 2009) | (с. 48 Hiller; Щетников 2009) | One citation form for Щетников 2009 (as at U010, U015): author–year, without the label «пер.:» |
| U037 | RU | note 1 | «извлечённые вместе», пер.: Щетников 2009) | «извлечённые вместе», Щетников 2009) | One citation form for Щетников 2009 (as at U010, U015): author–year, without the label «пер.:» |
| U037 | RU | note 4 | καὶ ἀνέσεως τοῦ πνεύματος, пер.: Щетников 2009) | καὶ ἀνέσεως τοῦ πνεύματος, «по усилению и ослаблению дыхания», Щетников 2009) | One citation form for Щетников 2009 (as at U010, U015): author–year, without the label «пер.:»; the quotation of Shchetnikov’s Theon that the label stood for is given (card P08) |
| U018 | RU | note 1 | (гл. 5; Jan, с. 187) | (гл. 5, Jan, с. 187) | One form for Jan’s pages: RU «гл. N, Jan, с. X», EN “ch. N, Jan p. X” (as at U008–U016) |
| U018 | RU | note 1 | «Деление канона», 16; Jan, с. 161) | «Деление канона», 16, Jan, с. 161) | One form for Jan’s pages: RU «гл. N, Jan, с. X», EN “ch. N, Jan p. X” (as at U008–U016) |
| U025 | RU | note 1 | «Деление канона», 3 и 16; Jan, с. 152–153, 161; | «Деление канона», 3 и 16, Jan, с. 152–153, 161; | One form for Jan’s pages: RU «гл. N, Jan, с. X», EN “ch. N, Jan p. X” (as at U008–U016) |
| U027 | RU | note 1 | (гл. 5; Jan, с. 188) | (гл. 5, Jan, с. 188) | One form for Jan’s pages: RU «гл. N, Jan, с. X», EN “ch. N, Jan p. X” (as at U008–U016) |
| U027 | RU | note 1 | «Гармоническое введение», 4; Jan, с. 330–331) | «Гармоническое введение», 4, Jan, с. 330–331) | One form for Jan’s pages: RU «гл. N, Jan, с. X», EN “ch. N, Jan p. X” (as at U008–U016) |
| U053 | RU | note 1 | «Гармоническое введение», 5, с. 331 Jan) | «Гармоническое введение», 5, Jan, с. 331) | One form for Jan’s pages: RU «гл. N, Jan, с. X», EN “ch. N, Jan p. X” (as at U008–U016) |
| U053 | EN | note 1 | (Harmonic Introduction 5, p. 331 Jan) | (Harmonic Introduction 5, Jan p. 331) | One form for Jan’s pages: RU «гл. N, Jan, с. X», EN “ch. N, Jan p. X” (as at U008–U016) |
| U035 | EN | note 2 | (Theon of Smyrna pp. 52, 56 Hiller; | (Theon of Smyrna, pp. 52, 56 Hiller; | DECISIONS § 4: “Theon of Smyrna, p. N Hiller”, with the comma |
| U037 | EN | note 1 | cf. Theon of Smyrna p. 51 Hiller: | cf. Theon of Smyrna, p. 51 Hiller: | DECISIONS § 4: “Theon of Smyrna, p. N Hiller”, with the comma |
| U037 | EN | note 2 | (cf. Theon of Smyrna p. 48 Hiller: | (cf. Theon of Smyrna, p. 48 Hiller: | DECISIONS § 4: “Theon of Smyrna, p. N Hiller”, with the comma |
| U037 | EN | note 4 | almost verbatim with Theon of Smyrna p. 57 Hiller: | almost verbatim with Theon of Smyrna, p. 57 Hiller: | DECISIONS § 4: “Theon of Smyrna, p. N Hiller”, with the comma |
| U061 | RU | note 1 | (так у Клеонида и, по Теону, у Аристоксена; | (так у Клеонида и, по Теону Смирнскому, у Аристоксена; | DECISIONS § 4: the first mention of Theon in a note is «Теон Смирнский» |
| U061 | EN | note 1 | (so in Cleonides and, according to Theon, in Aristoxenus; | (so in Cleonides and, according to Theon of Smyrna, in Aristoxenus; | DECISIONS § 4: the first mention of Theon in a note is “Theon of Smyrna” |
| U027 | EN | note 2 | by consecutive notes” (tr. Strunk). | by consecutive notes” (Strunk). | One form for Strunk’s Cleonides translation: “Strunk” (no year in the materials; see the bibliography) |
| U037 | EN | note 4 | (Macran 1902; Strunk’s Cleonides) | (Macran 1902; Strunk) | One form for Strunk’s Cleonides translation: “Strunk” (no year in the materials; see the bibliography) |
| U066 | EN | note 2 | “a progression of the melody by consecutive notes”, ch. 14) | “a progression of the melody by consecutive notes”, ch. 14, Strunk) | The quotation is Strunk’s translation (card L15), unattributed here; the RU note attributes its own quotation to Цыпин 2014 |
| U044 | EN | note 1 | Smyth §958) | Smyth § 958) | One form for the grammars: “Kühner–Gerth” (en dash) and “§ N” with a space, as in U058 and RU U044 |
| U044 | RU | note 3 | (Kühner-Gerth II.1 § 359.4–5; | (Kühner–Gerth II.1 § 359.4–5; | One form for the grammars: “Kühner–Gerth” (en dash) and “§ N” with a space, as in U058 and RU U044 |
| U044 | EN | note 3 | (Kühner-Gerth II.1 §359.4–5; Smyth §1014) | (Kühner–Gerth II.1 § 359.4–5; Smyth § 1014) | One form for the grammars: “Kühner–Gerth” (en dash) and “§ N” with a space, as in U058 and RU U044 |
| U014 | EN | note 3 | De institutione musica I.22: | De institutione musica I 22: | Book and chapter of Boethius as at U025 (“III 1”) and in the RU note («I 22») |
| U039 | RU | note 2 | Ксиландр на полях Базельского издания предлагает удалить δίς | Ксиландр на полях Bas. предлагал удалить δίς | One siglum for the Basel edition, “Bas.”, as in all other notes (e.g. U035, U036 «на полях Bas.»); tense as at U035 («предлагал») |
| U039 | EN | note 2 | Xylander, in the margin of the Basel edition, would delete δίς | Xylander, in the margin of Bas., proposed deleting δίς | One siglum for the Basel edition, “Bas.”, as in all other notes (e.g. U035, U036 «на полях Bas.»); wording as at U035 (“proposed”) |
| U040 | RU | note 2 | но его нет в Базельском издании и в Par.; | но его нет в Bas. и в Par.; | One siglum for the Basel edition, “Bas.”, as in all other notes (e.g. U035, U036 «на полях Bas.») |
| U040 | RU | note 2 | но его нет в Базельском издании (видимо, | но его нет в Bas. (видимо, | One siglum for the Basel edition, “Bas.”, as in all other notes (e.g. U035, U036 «на полях Bas.») |
| U040 | EN | note 2 | but not in the Basel edition or Par.; | but not in Bas. or Par.; | One siglum for the Basel edition, “Bas.”, as in all other notes (e.g. U035, U036 «на полях Bas.») |
| U040 | EN | note 2 | but not in the Basel edition (probably | but not in Bas. (probably | One siglum for the Basel edition, “Bas.”, as in all other notes (e.g. U035, U036 «на полях Bas.») |
| U042 | RU | note 1 | (Венсан, с. 340.7–342.4); в Базельском издании, H, Par. и V его нет | (Vinc. 340.7–342.4); в Bas., H, Par. и V его нет | One siglum for the Basel edition, “Bas.”, as in all other notes (e.g. U035, U036 «на полях Bas.»); Vincent’s pages cited as “Vinc. N” as everywhere else |
| U042 | EN | note 1 | (Vincent pp. 340.7–342.4); it is absent from the Basel edition, H, Par. and V | (Vinc. 340.7–342.4); it is absent from Bas., H, Par. and V | One siglum for the Basel edition, “Bas.”, as in all other notes (e.g. U035, U036 «на полях Bas.»); Vincent’s pages cited as “Vinc. N” as everywhere else |
| U044 | RU | note 2 | см. примеч. к [U034] и [U043] | см. примеч. к [U034] и к [U043] | Form of a double cross-reference as elsewhere («к [U018] и к [U040]») |

## 4. Source fields

Why, for every row: one form for each source (DECISIONS.md § 4). Theon as “Theon of Smyrna, p. N Hiller” (with the
comma); modern scholars by the English keys of the bibliography (Tsypin, Shchetnikov 2008a / 2008b, Gertsman,
Aleksandrova, Myakin), since the source field serves both languages and was mixed Cyrillic and Latin; “Strunk”;
“Kühner–Gerth … § N”; “Cleonides chs. 2, 14”; Boethius “I 22”; “Sophocles, Lexicon”; the edition as “Edition,
<part> at Bas. N” or “at P (Vinc. N)” (it was cited six ways); “calculation” (was also “direct calculation”,
“computation”); unit numbers without “of this text” or “Note on”.

| Unit | Lang. | Where | Before | After |
|---|---|---|---|---|
| U001 | RU, EN | note 1, source | LSJ s.vv. σύνοψις, ἀκριβόω; apparatus to Bas. 23.2 | LSJ s.vv. σύνοψις, ἀκριβόω; Edition, apparatus at Bas. 23.2 |
| U004 | RU, EN | note 2, source | Edition, alternatives for translation at Bas. 24.1–3; the author's usage at U055 | Edition, alternatives for translation at Bas. 24.1–3; U055 |
| U013 | RU, EN | note 3, source | Apparatus and alternatives for translation at Bas. 24.23 | Edition, apparatus and alternatives for translation at Bas. 24.23 |
| U014 | RU, EN | note 2, source | Nicomachus, Manual 11, 12; Cleonides ch. 4 (Jan p. 182); Gaudentius, Harmonic Introduction 6 (Jan p. 332); Shchetnikov 2008; Aleksandrova, Myakin 2009; Tsypin 2014; Barker 1989 | Nicomachus, Manual 11, 12; Cleonides ch. 4 (Jan p. 182); Gaudentius, Harmonic Introduction 6 (Jan p. 332); Shchetnikov 2008a; Aleksandrova, Myakin 2009; Tsypin 2014; Barker 1989 |
| U014 | RU, EN | note 3, source | Edition, apparatus and departures at Bas. 25.7; Gaudentius, Harmonic Introduction 6 (Jan p. 333); Boethius, De institutione musica I.22; Euclid, Sectio canonis 20 (Jan p. 165); Theon of Smyrna, p. [206], p. 92.11–12 Hiller; Nicomachus, Manual 12 (Jan p. 264) | Edition, apparatus and departures at Bas. 25.7; Gaudentius, Harmonic Introduction 6 (Jan p. 333); Boethius, De institutione musica I 22; Euclid, Sectio canonis 20 (Jan p. 165); Theon of Smyrna, p. [206], p. 92.11–12 Hiller; Nicomachus, Manual 12 (Jan p. 264) |
| U015 | RU, EN | note 1, source | LSJ s.vv. ὀκτάχορδος, πεντεκαιδεκάχορδος (no entry for ἑκκαιδεκάχορδος); DGE (no entry); Theon of Smyrna p. 64 Hiller; Barker 1989, pp. 212, 220 n. 50, 264–265, 361; Щетников 2009 (Теон Смирнский); Александрова 2025 | LSJ s.vv. ὀκτάχορδος, πεντεκαιδεκάχορδος (no entry for ἑκκαιδεκάχορδος); DGE (no entry); Theon of Smyrna, p. 64 Hiller; Barker 1989, pp. 212, 220 n. 50, 264–265, 361; Shchetnikov 2009; Aleksandrova 2025 |
| U016 | RU, EN | note 1, source | U014 and the edition's apparatus and departures to Bas. 25.7; Nicomachus, Manual 11 (Jan p. 258) | U014; Edition, apparatus and departures at Bas. 25.7; Nicomachus, Manual 11 (Jan p. 258) |
| U018 | RU, EN | note 1, source | Theon of Smyrna pp. 53.8–16, 55.11–13 Hiller; Cleonides ch. 5 (Jan p. 187); Euclid, Sectio canonis 16 (Jan p. 161) | Theon of Smyrna, pp. 53.8–16, 55.11–13 Hiller; Cleonides ch. 5 (Jan p. 187); Euclid, Sectio canonis 16 (Jan p. 161) |
| U018 | RU, EN | note 2, source | Цыпин 2013; Щетников 2008; Герцман 2010; Александрова, Мякин 2009; Barker 1989; LSJ s.vv. ἐπόγδοος, ἐπιτέταρτος, ἐπιδιμερής, διπλασιημιόλιος; LSJ, DGE, Bailly, Pape: no entry for ἡμιεπόγδοος | Tsypin 2013; Shchetnikov 2008b; Gertsman 2010; Aleksandrova, Myakin 2009; Barker 1989; LSJ s.vv. ἐπόγδοος, ἐπιτέταρτος, ἐπιδιμερής, διπλασιημιόλιος; LSJ, DGE, Bailly, Pape: no entry for ἡμιεπόγδοος |
| U018 | RU, EN | note 3, source | Edition, apparatus and alternatives to Bas. 25.24–25; Theon of Smyrna p. 69.13–17 Hiller; direct calculation | Edition, apparatus and alternatives for translation at Bas. 25.24–25; Theon of Smyrna, p. 69.13–17 Hiller; calculation |
| U019 | RU, EN | note 1, source | Theon of Smyrna pp. 19.20–20.3 Hiller | Theon of Smyrna, pp. 19.20–20.3 Hiller |
| U020 | RU, EN | note 1, source | Edition, apparatus, alternatives and resolved doubts to Bas. 26.4; LSJ s.v. νευρά 2 | Edition, apparatus, alternatives for translation and resolved doubts at Bas. 26.4; LSJ s.v. νευρά 2 |
| U023 | RU, EN | note 1, source | Edition, description of the witnesses; direct calculation | Edition, description of the witnesses; calculation |
| U024 | RU, EN | note 1, source | Plato, Meno 82b–85b; direct calculation | Plato, Meno 82b–85b; calculation |
| U025 | RU, EN | note 1, source | Euclid, Sectio canonis 3, 16 (Jan pp. 152–153, 161); Boethius, De institutione musica III 1 (chapter heading, ed. Friedlein); direct calculation | Euclid, Sectio canonis 3, 16 (Jan pp. 152–153, 161); Boethius, De institutione musica III 1 (chapter heading, ed. Friedlein); calculation |
| U026 | RU, EN | note 2, source | LSJ s.v. τριημιτόνιον; Pape; Щетников 2008; Александрова, Мякин 2009; Герцман 2010; Цыпин 2014; Цыпин 2013; Theon of Smyrna p. 55.2–6 Hiller; Strunk | LSJ s.v. τριημιτόνιον; Pape; Shchetnikov 2008a; Aleksandrova, Myakin 2009; Gertsman 2010; Tsypin 2014; Tsypin 2013; Strunk; U058 |
| U027 | RU, EN | note 1, source | Cleonides ch. 5 (Jan p. 188); Theon of Smyrna p. 54 Hiller; Gaudentius, Harmonic Introduction 4 (Jan pp. 330–331) | Cleonides ch. 5 (Jan p. 188); Theon of Smyrna, p. 54 Hiller; Gaudentius, Harmonic Introduction 4 (Jan pp. 330–331) |
| U027 | RU, EN | note 2, source | LSJ s.v. μέλος II; Dvoretsky s.v. μέλος; Cleonides ch. 14; Цыпин 2014; Strunk; Герцман 2024; Щетников 2008 | LSJ s.v. μέλος II; Dvoretsky s.v. μέλος; Cleonides ch. 14; Tsypin 2014; Strunk; Gertsman 2024; Shchetnikov 2008a |
| U027 | RU, EN | note 4, source | LSJ s.vv. δύναμις, ἰσχύς; Cleonides ch. 2, 14; Цыпин 2014; Barker 1989, pp. 233, 287, 314, 406 | LSJ s.vv. δύναμις, ἰσχύς; Cleonides chs. 2, 14; Tsypin 2014; Barker 1989, pp. 233, 287, 314, 406 |
| U028 | RU, EN | note 1, source | Edition, apparatus, departures and resolved doubts to P (Vinc. 338.4–7) and Bas. 27.14; LSJ s.vv. σύμφθαρσις, σύμφρασις | Edition, apparatus, departures and resolved doubts at P (Vinc. 338.4–7) and Bas. 27.14; LSJ s.vv. σύμφθαρσις, σύμφρασις |
| U028 | RU, EN | note 3, source | LSJ s.v. ἐγγίγνομαι (impers. c. inf.); edition, apparatus to P (Vinc. 338.7); direct calculation | LSJ s.v. ἐγγίγνομαι (impers. c. inf.); Edition, apparatus at P (Vinc. 338.7); calculation |
| U029 | RU, EN | note 2, source | apparatus and resolved doubts, P (Vinc. 338.11, 338.14); Lampe p. 131; LSJ, DGE s.v. ἀνεγχώρητος; U022; U031 | Edition, apparatus and resolved doubts at P (Vinc. 338.11, 338.14); Lampe p. 131; LSJ, DGE s.v. ἀνεγχώρητος; U022; U031 |
| U030 | RU, EN | note 1, source | direct calculation; U023; U031 | calculation; U023; U031 |
| U030 | RU, EN | note 2, source | apparatus and resolved doubts, P (Vinc. 338.16, 338.17); LSJ s.v. ἑξκαιδέκατος; U018; U023 | Edition, apparatus and resolved doubts at P (Vinc. 338.16, 338.17); LSJ s.v. ἑξκαιδέκατος; U018; U023 |
| U032 | RU, EN | note 1, source | apparatus, P (Vinc. 340.2) and Bas. 27.14; edition, treatment of the P passages | Edition, apparatus at P (Vinc. 340.2) and Bas. 27.14, treatment of the P passages |
| U033 | RU, EN | note 1, source | apparatus, Bas. 27.14; Vinc. 340.3 | Edition, apparatus at Bas. 27.14; Vinc. 340.3 |
| U033 | RU, EN | note 2, source | Theon of Smyrna p. 51.4–20 Hiller; Tsypin 2013; Tsypin 2014; Shchetnikov 2012; U034, U035, U040 | Theon of Smyrna, p. 51.4–20 Hiller; Tsypin 2013; Tsypin 2014; Shchetnikov 2012; U034, U035, U040 |
| U034 | RU, EN | note 1, source | LSJ, DGE s.vv. ἄμεσος, ἔμμεσος; Aristotle, Prior Analytics 68b30; Posterior Analytics 72b19; Anonymus Bellermanni §§ 4–6 (Bellermann 1841); Cleonides ch. 5; Tsypin 2014; Strunk’s Cleonides | LSJ, DGE s.vv. ἄμεσος, ἔμμεσος; Aristotle, Prior Analytics 68b30; Posterior Analytics 72b19; Anonymus Bellermanni §§ 4–6 (Bellermann 1841); Cleonides ch. 5; Tsypin 2014; Strunk |
| U034 | RU, EN | note 2, source | Theon of Smyrna p. 51.4–20 Hiller; U045–U047 | Theon of Smyrna, p. 51.4–20 Hiller; U045–U047 |
| U034 | RU, EN | note 3, source | apparatus and departures, Bas. 28.1; LSJ s.v. περαίνω | Edition, apparatus and departures at Bas. 28.1; LSJ s.v. περαίνω |
| U035 | RU, EN | note 1, source | Theon of Smyrna p. 51.4–20 Hiller; LSJ s.v. φερωνυμία | Theon of Smyrna, p. 51.4–20 Hiller; LSJ s.v. φερωνυμία |
| U035 | RU, EN | note 2, source | Euclid, Sectio canonis 11; [Aristotle], Problems XIX 41; Theon of Smyrna pp. 52, 56 Hiller; Cleonides ch. 8; Tsypin 2013; Tsypin 2014; Shchetnikov 2012; apparatus, departures and alternatives for translation, Bas. 28.4, 28.11, 29.8–9; LSJ s.v. ἐπαναδιπλόω | Euclid, Sectio canonis 11; [Aristotle], Problems XIX 41; Theon of Smyrna, pp. 52, 56 Hiller; Cleonides ch. 8; Tsypin 2013; Tsypin 2014; Shchetnikov 2012; Edition, apparatus, departures and alternatives for translation at Bas. 28.4, 28.11, 29.8–9; LSJ s.v. ἐπαναδιπλόω |
| U036 | RU, EN | note 1, source | Theon of Smyrna p. 48 Hiller; Shchetnikov 2009; [Aristotle], Problems XIX 39 (Jan p. 100); LSJ s.v. ἀντίφωνος III; Gaudentius, Harmonic Introduction 8 (Jan pp. 337–338) | Theon of Smyrna, p. 48 Hiller; Shchetnikov 2009; [Aristotle], Problems XIX 39 (Jan p. 100); LSJ s.v. ἀντίφωνος III; Gaudentius, Harmonic Introduction 8 (Jan pp. 337–338) |
| U036 | RU, EN | note 2, source | apparatus and alternatives for translation, Bas. 28.11–12 | Edition, apparatus and alternatives for translation at Bas. 28.11–12 |
| U037 | RU, EN | note 1, source | LSJ s.vv. ἀνισόχρονος, ἰσόχρονος, αὐτός IV.4; Theon of Smyrna pp. 48.16–49.2, 51 Hiller; Shchetnikov 2009; [Aristotle], Problems XIX 18, 39 (Jan pp. 88, 100–101) | LSJ s.vv. ἀνισόχρονος, ἰσόχρονος, αὐτός IV.4; Theon of Smyrna, pp. 48.16–49.2, 51 Hiller; Shchetnikov 2009; [Aristotle], Problems XIX 18, 39 (Jan pp. 88, 100–101) |
| U037 | RU, EN | note 2, source | apparatus and departures, Bas. 28.15, 28.17, 28.18 | Edition, apparatus and departures at Bas. 28.15, 28.17, 28.18 |
| U037 | RU, EN | note 3, source | U014; U035–U036; direct calculation | U014; U035–U036; calculation |
| U037 | RU, EN | note 4, source | Plato, Republic 349e; LSJ s.vv. ἐπίτασις, ἄνεσις; Cleonides ch. 2; Tsypin 2014; Macran 1902; Strunk’s Cleonides; Theon of Smyrna p. 57 Hiller; Shchetnikov 2009 | Plato, Republic 349e; LSJ s.vv. ἐπίτασις, ἄνεσις; Cleonides ch. 2; Tsypin 2014; Macran 1902; Strunk; Theon of Smyrna, p. 57 Hiller; Shchetnikov 2009 |
| U039 | RU, EN | note 1, source | Cleonides ch. 8 (Jan p. 194); Euclid, Sectio canonis 14–15 (Jan pp. 160–161); Theon of Smyrna pp. 66–67 Hiller; U018; computation | Cleonides ch. 8 (Jan p. 194); Euclid, Sectio canonis 14–15 (Jan pp. 160–161); Theon of Smyrna, pp. 66–67 Hiller; U018; calculation |
| U039 | RU, EN | note 2, source | apparatus, Bas. 29.8–9 (Xylander’s marginal note) and the alternatives for translation at Bas. 29.8–15; U035; U040–U041 | Edition, apparatus at Bas. 29.8–9 (Xylander’s marginal note) and alternatives for translation at Bas. 29.8–15; U035; U040–U041 |
| U040 | RU, EN | note 1, source | Theon of Smyrna p. 56.12–17 Hiller; Nicomachus, Introduction to Arithmetic I 23; Tsypin 2013; Shchetnikov 2008; LSJ s.v. ἐπιμερής | Theon of Smyrna, p. 56.12–17 Hiller; Nicomachus, Introduction to Arithmetic I 23; Tsypin 2013; Shchetnikov 2008a; LSJ s.v. ἐπιμερής |
| U040 | RU, EN | note 2, source | apparatus and departures, Bas. 29.14–15 | Edition, apparatus and departures at Bas. 29.14–15 |
| U040 | RU, EN | note 3, source | apparatus and resolved doubts, Bas. 29.16; Theon of Smyrna pp. 56, 63 Hiller; Gaudentius, Harmonic Introduction 10 (Jan pp. 339–340); Euclid, Sectio canonis 12 (Jan p. 160) | Edition, apparatus and resolved doubts at Bas. 29.16; Theon of Smyrna, pp. 56, 63 Hiller; Gaudentius, Harmonic Introduction 10 (Jan pp. 339–340); Euclid, Sectio canonis 12 (Jan p. 160) |
| U041 | RU, EN | note 1, source | U018; U023; computation | U018; U023; calculation |
| U041 | RU, EN | note 2, source | Theon of Smyrna pp. 62–64 Hiller; Nicomachus, Manual 6 (Jan p. 248) | Theon of Smyrna, pp. 62–64 Hiller; Nicomachus, Manual 6 (Jan p. 248) |
| U042 | RU, EN | note 1, source | edition: apparatus to P (Vinc. 340.7–342.4), departures at Bas. 29.23, treatment of the P passages | Edition, apparatus at P (Vinc. 340.7–342.4), departures at Bas. 29.23, treatment of the P passages |
| U042 | RU, EN | note 3, source | apparatus to P (Vinc. 340.8); U027; U034; U036–U037 | Edition, apparatus at P (Vinc. 340.8); U027; U034; U036–U037 |
| U042 | RU, EN | note 4, source | U035; U041; edition, treatment of the P passages | U035; U041; Edition, treatment of the P passages |
| U042 | RU, EN | note 5, source | Cleonides ch. 8 (Jan p. 194.5–16); U041; computation | Cleonides ch. 8 (Jan p. 194.5–16); U041; calculation |
| U043 | RU, EN | note 2, source | LSJ s.vv. ὑπερβατόν, ὑπερβατός; U041 of this text; direct calculation | LSJ s.vv. ὑπερβατόν, ὑπερβατός; U041; calculation |
| U043 | RU, EN | note 3, source | Apparatus, P (Vinc. 340.20); Bas. 31.10 | Edition, apparatus at P (Vinc. 340.20) and Bas. 31.10 |
| U044 | RU, EN | note 1, source | LSJ s.v. περί C.I.5; Herodotus 2.93; LSJ s.v. οὕτως; Smyth §958 | LSJ s.v. περί C.I.5; Herodotus 2.93; LSJ s.v. οὕτως; Smyth § 958 |
| U044 | RU, EN | note 2, source | U034, U042, U043 of this text | U034, U042, U043 |
| U044 | RU, EN | note 3, source | Apparatus, P (Vinc. 342.1–4); Kühner-Gerth II.1 §359.4–5; Smyth §1014 | Edition, apparatus at P (Vinc. 342.1–4); Kühner–Gerth II.1 § 359.4–5; Smyth § 1014 |
| U044 | RU, EN | note 4, source | U018, U019, U028, U041 of this text | U018, U019, U028, U041 |
| U045 | RU, EN | note 1, source | Apparatus, Bas. 29.23–24 (Vinc. 342.5–6) | Edition, apparatus at Bas. 29.23–24 (Vinc. 342.5–6) |
| U045 | RU, EN | note 2, source | Cleonides ch. 2; U037 of this text | Cleonides ch. 2; U037 |
| U046 | RU, EN | note 2, source | U034 of this text; apparatus, Bas. 30.3, 30.5; direct calculation | U034; Edition, apparatus at Bas. 30.3, 30.5; calculation |
| U048 | RU, EN | note 1, source | direct calculation | calculation |
| U049 | RU, EN | note 3, source | direct calculation (ideal-string formula) | calculation (ideal-string formula) |
| U049 | RU, EN | note 4, source | Apparatus, Bas. 30.15, 30.21–23 (Vinc. 342 n. 5); Theon of Smyrna, pp. 56–57 Hiller | Edition, apparatus at Bas. 30.15, 30.21–23 (Vinc. 342 n. 5); Theon of Smyrna, pp. 56–57 Hiller |
| U050 | RU, EN | note 1, source | Apparatus, Bas. 30.23 (P passage; Vinc. 342 nn. 6–7); Theon of Smyrna, pp. 57, 65.10–66.11 Hiller | Edition, apparatus at Bas. 30.23 (P passage; Vinc. 342 nn. 6–7); Theon of Smyrna, pp. 57, 65.10–66.11 Hiller |
| U050 | RU, EN | note 2, source | Apparatus, Bas. 30.23 (P passage); Theon of Smyrna, pp. 65.10–66.11 Hiller | Edition, apparatus at Bas. 30.23 (P passage); Theon of Smyrna, pp. 65.10–66.11 Hiller |
| U051 | RU, EN | note 1, source | Apparatus, Bas. 30.23 (Vinc. 342.25–26); Theon of Smyrna, pp. 48, 49 Hiller | Edition, apparatus at Bas. 30.23 (Vinc. 342.25–26); Theon of Smyrna, pp. 48, 49 Hiller |
| U051 | RU, EN | note 2, source | Apparatus, Bas. 31.1 | Edition, apparatus at Bas. 31.1 |
| U051 | RU, EN | note 3, source | Apparatus, Bas. 31.2; Cleonides ch. 14 | Edition, apparatus at Bas. 31.2; U027 |
| U051 | RU, EN | note 4, source | U015, U016 of this text; edition, resolved doubt at Bas. 31.4; apparatus, Bas. 31.5 | U015, U016; Edition, resolved doubts at Bas. 31.4, apparatus at Bas. 31.5 |
| U051 | RU, EN | note 5, source | U035, U037, U039–U041 of this text | U035, U037, U039–U041 |
| U052 | RU, EN | note 1, source | Edition, apparatus and resolved doubt at P (Vinc. 340.20); section 5, departure at Bas. 30.23; U010; U042–U044 | Edition, apparatus and resolved doubts at P (Vinc. 340.20), departures at Bas. 30.23; U010; U042–U044 |
| U053 | RU, EN | note 1, source | Theon of Smyrna pp. 55.8, 56.8 Hiller; Gaudentius, Harmonic Introduction 5 (p. 331 Jan); Cleonides ch. 3 | Theon of Smyrna, pp. 55.8, 56.8 Hiller; Gaudentius, Harmonic Introduction 5 (Jan p. 331); Cleonides ch. 3 |
| U054 | RU, EN | note 1, source | Theon of Smyrna p. 54.12–15 Hiller; Theon of Smyrna pp. 54–56 Hiller (the parallel section) | Theon of Smyrna, p. 54.12–15 Hiller; Theon of Smyrna, pp. 54–56 Hiller (the parallel section) |
| U054 | RU, EN | note 3, source | Edition, apparatus and departure at Bas. 31.23 | Edition, apparatus and departures at Bas. 31.23 |
| U054 | RU, EN | note 4, source | Notes on U027 and U053 | U027; U053 |
| U056 | RU, EN | note 1, source | Theon of Smyrna p. 54.6–9 Hiller; LSJ s.v. τονιαῖος | Theon of Smyrna, p. 54.6–9 Hiller; LSJ s.v. τονιαῖος |
| U057 | RU, EN | note 1, source | Theon of Smyrna p. 54.6–9 Hiller; calculation | Theon of Smyrna, p. 54.6–9 Hiller; calculation |
| U058 | RU, EN | note 2, source | Edition, resolved doubt at Bas. 32.11–13; Kühner–Gerth II.2 § 532 Anm.; Smyth § 2837 | Edition, resolved doubts at Bas. 32.11–13; Kühner–Gerth II.2 § 532 Anm.; Smyth § 2837 |
| U059 | RU, EN | note 1, source | Theon of Smyrna p. 55.4–7 Hiller; LSJ s.vv. γοερός, παθητικός; edition, apparatus and departure at Bas. 32.15 | Theon of Smyrna, p. 55.4–7 Hiller; LSJ s.vv. γοερός, παθητικός; Edition, apparatus and departures at Bas. 32.15 |
| U060 | RU, EN | note 1, source | Theon of Smyrna pp. 54.6–56.1 Hiller; calculation | Theon of Smyrna, pp. 54.6–56.1 Hiller; calculation |
| U060 | RU, EN | note 2, source | Theon of Smyrna pp. 55.15–56.1 Hiller; LSJ s.v. κοινός V; LSJ s.v. ἀποφέρω B | Theon of Smyrna, pp. 55.15–56.1 Hiller; LSJ s.v. κοινός V; LSJ s.v. ἀποφέρω B |
| U062 | RU, EN | note 1, source | LSJ s.v. συντακτικός; edition, apparatus and departure at Bas. 32.23; U051 | LSJ s.v. συντακτικός; Edition, apparatus and departures at Bas. 32.23; U051 |
| U063 | RU, EN | note 1, source | Theon of Smyrna p. 56.1–3 Hiller; LSJ s.v. δυσμελῴδητος; Aristoxenus, Elementa harmonica I, p. 19 Meibom | Theon of Smyrna, p. 56.1–3 Hiller; LSJ s.v. δυσμελῴδητος; Aristoxenus, Elementa harmonica I, p. 19 Meibom |
| U064 | RU, EN | note 1, source | Theon of Smyrna pp. 54.14, 56.3–5 Hiller; Aristoxenus, Elementa harmonica I, p. 19 Meibom; Plato, Timaeus 35b–36b; LSJ s.v. γενναῖος | Theon of Smyrna, pp. 54.14, 56.3–5 Hiller; Aristoxenus, Elementa harmonica I, p. 19 Meibom; Plato, Timaeus 35b–36b; LSJ s.v. γενναῖος |
| U065 | RU, EN | note 1, source | Theon of Smyrna p. 48.12–13 Hiller | Theon of Smyrna, p. 48.12–13 Hiller |
| U065 | RU, EN | note 2, source | Note on U027 | U027 |
| U065 | RU, EN | note 3, source | LSJ s.v. ἐξόδιος; Pape s.v. ἐξόδιος (Pollux 4.108); Sophocles, Greek Lexicon of the Roman and Byzantine Periods s.v. ἐξόδιος; edition, apparatus and departure at Bas. 33.12 | LSJ s.v. ἐξόδιος; Pape s.v. ἐξόδιος (Pollux 4.108); Sophocles, Lexicon s.v. ἐξόδιος; Edition, apparatus and departures at Bas. 33.12 |
| U066 | RU, EN | note 2, source | LSJ s.vv. διαμονή, ῥοή; Cleonides chs. 2, 14 (Tsypin 2014); Pindar, Nemean 7.12 | LSJ s.vv. διαμονή, ῥοή; Cleonides chs. 2, 14; Tsypin 2014; Strunk; Pindar, Nemean 7.12 |

## 5. The checker (`scripts/check_composed.py`)

The last three problems it reported were not errors in the text, so the checker was corrected, not the text.

| Where | Before | After | Why |
|---|---|---|---|
| `RATIO_RU` | `r'(двукратн\|…)\w*'` | `r'(?<!полу)(двукратн\|…)\w*'` | It matched «сверхосминного» inside «полусверхосминного» (U020), so the exemption for «полусверх-» never applied. DECISIONS (ratio table, L03) prescribes «полусверхосминного» without a bracket. The U001–U028 verifier proposed the same fix. Real ratio names are still caught (tested on «сверхосминное отношение тона» and «полуторным»). |
| `GREEK_OK` | `{'U033', 'U035'}` | `{'U033', 'U035', 'U054'}` (with a comment) | DECISIONS § 2 allows Greek in the text “anywhere else the author's argument turns on the word itself, i.e. he explains or derives a name”. U054 derives διάτονον from διὰ τόνων, which the translation cannot show; U054's basis lists it, the U043–U067 verifier kept it, and the composer's question to the editor stays open in U054. In U012, U053 and U060 the derivation shows in the translation, so no Greek there; the treatment is therefore consistent. |

## 6. Bibliography

`final/bibliography.json`: 33 entries `{key_ru, key_en, ru, en}`, sorted by `key_en`, for every modern work, edition
and lexicon cited in the notes or their sources. Details are taken only from the cards, the unit packets and
`edition/`; nothing was supplied from memory. My own are only the transliterations and English glosses of the Russian
titles and the language of each lexicon (as its glosses in the materials show). Checked mechanically: every author–year key in the RU notes, the EN notes
and the source fields has an entry, and every entry is cited.

- «Щетников 2008» covered two works (the U001–U028 verifier's flag). Now «Щетников 2008а» / “Shchetnikov 2008a”, the
  translation of Nicomachus (U014, U026, U027, U040), and «Щетников 2008б» / “Shchetnikov 2008b”, «Алгоритм…» (U018;
  card P03: the source of «сверхдвухчастное», «двукратное-и-половинное»). U040 is assigned to 2008a because its packet
  says that Shchetnikov's Nicomachus has ἐπιμόριον «сверхчастное», ἐπιμερές «сверхмногочастное».
- The witnesses that are printed books (Bas., Par.), Vincent's edition of P (Vinc.) and the edition itself (издание /
  Edition) have entries; the manuscripts H, V, P and Marc. gr. Z. 307 do not, since they are not modern works.
- Details missing from the materials, so missing from the entries:
  - LSJ, DGE, Bailly, Pape, Дворецкий / Dvoretsky: full titles, editions and years. Only the platforms are known
    (Perseus LSJ XML, Logeion, lsj.gr; “Bailly 2024”).
  - Lampe, Kühner–Gerth, Meibom, Pistelli: titles and years.
  - Sophocles, Lexicon: year.
  - Strunk: the book and the year. The notes cite “Strunk” without a year.
  - Barker 1989: only “GMW II”; full title and publisher missing.
  - Friedlein (1867): the year comes from a translator's source marked “from memory” (U007 packet).
  - Vinc.: Vincent's initials, the title of his article, the full title of the series (only “Notices et extraits 16.2”).
  - Bas.: title and printer. Par.: place and date of the reprint (known only as the reprint of the Venice editio
    princeps of 1532).
  - Edition: editor, title and date.
  - Щетников 2008б: the full title («Алгоритм…»). Щетников 2009: the exact title of the Theon translation.
    Щетников 2008а, 2009, 2012, Александрова, Мякин 2009: page ranges.
  - Герцман 2010: place and publisher. Герцман 2024: place (“РИИИ” as given).
  - Александрова 2025: initials and title.
  - Александрова, Мякин 2009: the order of the names on the publication (the cards give both orders; the key follows
    DECISIONS.md).
  - Synodal translation: the edition.

## 7. Checked, no change needed

- **Unit boundaries.** U014/U015, U028/U029, U037/U038, U042/U043, U051/U052, and every other pair: no sentence is split
  between units; each unit ends and the next begins as the Greek does, in both languages (διὰ τούτων «Ими» / 'By these';
  γάρ «Ведь» / 'For' at U043; the ⟨⟨ ⟩⟩ of the P passages at U028–U032, U042–U044, U050).
- **Cross-references.** All 62 cross-references «см. примеч. к [Uxxx]» / 'see the note on [Uxxx]' point to a unit that
  has the note in question (topic checked one by one); the RU and EN notes carry the same references. No reference
  stands in the running text.
- **DECISIONS.md terms** across the whole text: ratio names with brackets (U018–U047), P01, P02 b (U035 only with the
  author's names), P05, P06 b, P07 ('(μέλος)' at U027, U028, U054, U065), P08, P09 b, P10 a, P11 a, P12, P13, P14,
  P15, ἀπαρτίζω, L01–L15; note names; signs of the edition.
- **Same Greek, same rendering** (beyond section 1): σύμφθαρσις, ἀσύνθετος, παραύξησις, διάστασις («интервальное
  расстояние» in U045, U049, U056; «интервалы» in U035, as DECISIONS prescribes, and in U036, which continues it; «расстояние» in U051), ἐγγὺς φθόγγοι,
  κατὰ σειράν / καθ’ ὑπερβατόν, συντάττω / σύνταξις, συμφωνέω, μέλος / μελῳδία, the parallel sentences U021/U029,
  U023/U030, U024/U031.
- **Typography.** «ёлочки» with no nesting problems, curly quotes in English, no straight quotes, ё, no «свидетель»,
  no Cyrillic in English notes, no English glosses in Russian notes except Barker's renderings that DECISIONS (P06)
  asks for at U015.

## 8. Left for the editor

- The composers' open questions stay in their units (U004, U012, U019, U028, U029, U033, U034, U037, U050, U051, U052,
  U054, U061); none was settled here.
- The verifiers' `verify` notes are left as written. U034's quotes the earlier «по упорядоченному числу» / 'ordered
  number', now «количеству» / 'quantity' (section 1).
