# Language reading of the final composed translation, U001–U067 (1.11.2026)

Copy-editor's pass (Russian and English) over `compose/final/`. Read first: `DECISIONS.md` (all sections), the glossary
entries for the terms in doubt, `final/consistency-log.md`, the verify logs where a point needed them, and the unit
packets U005, U035, U039, U042 for the renderings the translators and reviewers proposed. Then the whole text with
`show_composed.py … final --notes U001-U067` (running text, then every note, RU and EN), and two scratch scans (not
kept in the workspace) for anchor order, quotation marks, dashes, ё, -ise/-ize, sigla and citation forms.
`check_composed.py … final`: no problems (67 units). No file other than this log was changed.

Severity: **error** = grammar, orthography, typography, a term inconsistent with DECISIONS or across units, a
misnumbered note; **improvement** = style, idiom, repetition; **question** = a point fixed by DECISIONS or the
glossary that I would put to the editor.

## 1. Errors

| Unit | Where | Current | Proposed | Why |
|---|---|---|---|---|
| U005 | text-ru | гармонией как самого себя, так и вселенной | гармонией как его самого, так и вселенной | «себя» binds to the subject of the clause, «кто-нибудь»: as printed, someone calls the Divine the harmony of *himself*. Three of the six translations already have «его самого» (packet U005). |
| U009 | note 1 (ru) | двумя звуками, неодинаковыми по высоте и низости | двумя звуками, различными по высоте (ὀξύτητι καὶ βαρύτητι) | «низость» means baseness, meanness; the pitch sense is «низкость» (so U037 note 2 for βάρος). The pair is simply «по высоте» in Russian. |
| U013 | notes (order) | 1 нестройный · 2 изданным иначе · 3 Ведь | order 3, 1, 2 | Notes are numbered in list order; note 3 sits on the first word in both languages, so the callouts would run 3, 1, 2. |
| U014 | notes 3, 5 (ru, en) | Hiller, с. [206] / Hiller p. [206] | с. [206] Hiller / p. [206] Hiller | DECISIONS § 4 form «с. N Hiller» / 'p. N Hiller', as everywhere else. |
| U018 | note 1 (ru) | Составитель берёт аристоксеновы величины | Составитель берёт аристоксеновские величины | A possessive adjective in -ов from a personal name is capitalised (cf. «Аристоксеново определение», U008, U009); the note itself has «аристоксеновская» a line above. |
| U027 | note 1 (ru) | несоставны интервалы между соседними звуками рода, составны — между несоседними | несоставны интервалы между смежными звуками рода, составны — между несмежными | Cleonides' ἑξῆς / μὴ ἑξῆς is Tsypin's «смежные / несмежные» (DECISIONS P09; U027 note 2, U034 note 1); «соседние» is reserved for ἐγγὺς φθόγγοι (DECISIONS, U042, U044). |
| U037 | note 1 (en) | magadized | magadised | House spelling is -ise ("Christianises" U005, "summarises" U050). |
| U040 | notes (order) | 1 двукратное сверхчастное · 2 октавы с квартой · 3 трёхкратное | order 2, 1, 3 | Note 2's anchor precedes note 1's in both languages. |
| U043 | notes (order) | 1 между смежными · 2 в силлогизмах · 3 а между несмежными | order 1, 3, 2 | Same, both languages. |
| U046 | notes (order) | 1 пятикратным [5:1] · 2 [пятый звук] | order 2, 1 | Same, both languages. |
| U050 | notes (order) | 1 Следует знать · 2 †и то и другое† · 3 бо́льшая тяжесть · 4 протяжённости отверстий | order 1, 3, 4, 2 | Same, both languages. |
| U054 | notes (order) | 1 потому и называется · 2 по большей части · 3 держится скорее · 4 напев | order 2, 1, 3, 4 | Same, both languages. |
| U055 | notes (order) | 1 да это и невозможно · 2 ни целиком через полутоны | order 2, 1 | Same, both languages. |
| U056 | notes (order) | 1 из трёх … · 2 остаток … · 3 разделена | order 1, 3, 2 | Same, both languages. |
| U065 | text-ru (+ note 2 anchor) | и складывается напев то лидийский, то фригийский, то дорийский, причём | и складывается то лидийский, то фригийский, то дорийский напев, причём (note 2 anchor «напев») | RU callouts run 2, 1, 3, EN 1, 2, 3; the RU word order that follows the Greek (and the EN) fixes it with one list. |
| U066 | note 1 (ru) | наборщик перескочил с одного конца строки на другой | наборщик перескочил с конца одной строки на конец следующей | As printed it says "from one end of the line to the other" (one line); the EN and the evidence (Par., adjacent line ends) mean a skip between lines. |

## 2. The first reader's points

- **U018 «тон, который содержит двойной полутон».** Yes, ambiguous. In a text where «двойная октава», «двойная кварта», «двойная квинта» are interval names (U035, U036 ff.), «двойной полутон» reads like another named interval, not "the semitone twice". The EN already has 'contains the semitone twice'. But DECISIONS (ratio section, last paragraph) names «содержащий двойной полутон» as ordinary «двойной» that stays, so this is a **question**: recommend «затем тон, который содержит полутон дважды, образуя сверхосминное отношение [9:8]…».
- **U035, U039 «восполняются / восполняется» (συμπληρόω).** Not right. «Восполнить» is to make good a deficit (восполнить пробел, недостачу); «кварта восполняется двумя тонами» suggests that the tones make up for a lack in the fourth. LSJ συμπληρόω is "fill up, complete; make up (a number)". One verb fits both places: «слагаться (из)». U039: «Кварта же слагается из двух тонов и полутона да ещё некой малой величины сверх того, …; квинта — из трёх [тонов] и полутона; октава — из шести [тонов]; октава с квартой — из восьми [тонов] и полутона; октава с квинтой — из девяти [тонов] и полутона; двойная октава — из двенадцати [тонов]» (ἐκ and διά both go into «из»). U035: «так как в октахорде слагаются все интервалы и оттуда вновь повторяются». «Слагается из» is offered in the U039 packet by translators A and D and by two reviewers; «складывается из» is the plainer alternative. «Составляется» is excluded: DECISIONS reserves it for ἀπαρτίζω. The quotation in U034 note 3 and U035 note 1 follows. Not fixed by DECISIONS, so **improvement**.
- **U042 «относят свои отношения к звуку просламбаномену»; «имеют определённое расположение своих отношений относительно соседних звуков».** The first is an unforced jingle (отношения / относят) and not prescribed: «отсчитывают свои отношения от звука просламбаномена» (what note 5 says: «берутся от первого звука системы»); note 5's anchor becomes «от звука просламбаномена». The second (отношений относительно) is prescribed verbatim by DECISIONS P14, so a **question**: «имеют определённое расположение своих отношений к соседним звукам перед ними», where «к» carries the "ratio to" sense and the jingle goes.
- **U005 «предстаёт в добром и наилучшем состоянии».** Clumsy: a positive and a superlative joined by «и» read as two states, and «в добром состоянии» is colloquial. εὖ τε καὶ ὡς ἄριστα is an intensifying pair, Russian «хорошо и как нельзя лучше». Proposed: «в нём вселенная, слаживаемая и сплачиваемая, со всей ясностью предстаёт устроенной хорошо и как нельзя лучше». (Several translators in the packet have «устроенным/устроенной хорошо и наилучшим образом».) If «состояние» must stay: «предстаёт в хорошем, более того, в наилучшем состоянии», which matches the EN.
- **U045, U049, U056 «интервальное расстояние» / 'intervallic span' (διάστασις).** English: acceptable ("intervallic" is standard in music theory), though 'span' alone, as in U051, would do. Russian: understandable but pleonastic, since an interval is a distance; it reads as a coinage, and nowhere does a note tell the reader that it renders διάστασις as against διάστημα. The rendering is the glossary's and the composer's (basis of U045, U049, U056), so a **question**: either keep it and add a short note at U045 (see 3, U045), or use «расстояние» / 'span' throughout, as U051 already does («отношения расстояний», «найдены же такие отношения расстояний», «составлена из трёх расстояний»). Note also that U035–U036 render the same word «интервалы», so the distinction is not kept consistently in any case.

## 3. Improvements

| Unit | Where | Current | Proposed | Why |
|---|---|---|---|---|
| U005 | text-en | of the universe, in which [the Divine] the universe, being fitted | of the universe: in it the universe, being fitted | The bracket after "in which" is awkward; note 1 explains the antecedent; RU has «в нём». |
| U014 | text-ru | получают названия по продвижению и порядку | получают названия по следованию и порядку | «Продвижение» suggests promotion or advance; the glossary has it (Sol), so only a style suggestion. |
| U014 | note 2 (ru) | издание сохраняет переданную форму | издание сохраняет эту форму | «переданную» calques "transmitted". |
| U014 | note 3 (ru) | в смешанных списках Никомаха | в смешанных перечнях названий у Никомаха | In this series «список» means a manuscript copy; here lists of names are meant. |
| U020 | note 1 (ru) | (буквы ο и ι неуверенны) | (буквы ο и ι читаются неуверенно) | Letters are not "unsure"; the reading is. |
| U020 | note 3 (ru, en) | ἡμιεπόγδοον — калька: «полусверхосминное»; в словарях это слово не отмечено. Автор сам поясняет его: «то есть полутон». По числам U018 … | ἡμιεπόγδοον — калька: «полусверхосминное»; о слове см. примеч. к [U018]. По числам U018 это 8½:8 = 17:16: пополам делится избыток, а не отношение 9:8 (см. примеч. к [U025]). | Calque and absence from the lexica are already in U018 note 2 (where DECISIONS puts them); "the author glosses it himself" retells the text. EN in parallel. |
| U025 | note 1 (ru, en) | √72 ≈ 8,485 против 8 / √72 ≈ 8.485 against 8 | √72 ≈ 8,485 (между 8 и 9) / √72 ≈ 8.485 (between 8 and 9) | "against 8" is unclear in both languages. |
| U026 | note 1 (ru) | τριδίεσις в словарях (LSJ, Bailly, Pape) не отмечено | Слово τριδίεσις в словарях (LSJ, Bailly, Pape) не отмечено | Neuter agreement needs «слово» (as U004, U063). |
| U026 | note 2 (ru, en) | В хроматическом роде этот интервал несоставной (см. примеч. к [U058]). | delete the sentence | Note 1 of the same unit already says it. |
| U026 | note 3 (ru, en) | ὁ ῥυθμός — букв. «ритм». | ὁ ῥυθμός — «ритм». | "lit." where the literal sense is the rendering. |
| U028 | text-ru | однако в напевах — поскольку …, — отсюда оказывается возможным и существование слияния | однако в напевах — поскольку они низводятся в материю, а в материи усматривается непрерывность, — тем самым оказывается возможным и слияние | «в напевах … отсюда» is an anacoluthon; «существование слияния» is wordy; «тем самым» = EN "thereby". Anchor of note 3 unchanged. |
| U032 | note 1 (ru) | предлагал εἰρήσθω («пусть будет сказано»), не принято. | предлагал εἰρήσθω («пусть будет сказано»); это чтение не принято. | The bare «, не принято» has no subject. |
| U033 | note 2 (ru, en) | Автор считает звуки включительно …; отсюда «через восемь» для октавы. … название διὰ πασῶν объясняется от восьмиструнной лиры | Своё объяснение названий автор даёт в U034–U035 (см. примеч. к [U034]). … название διὰ πασῶν выводится из устройства восьмиструнной лиры | Inclusive counting is the subject of U034 note 2; «объясняется от» is a calque. |
| U034 | text-ru | по отношению звучания от первого звука к последнему они именуются интервалами | по отношению между звучанием первого и последнего звука они именуются интервалами | «по отношению …» is first read as the set phrase «по отношению к» (with regard to). |
| U034 | note 1 (ru) | следует передаче клеонидовских ἑξῆς / μὴ ἑξῆς φθόγγοι у Цыпина | следует тому, как Цыпин передаёт выражения ἑξῆς / μὴ ἑξῆς φθόγγοι у Клеонида | A Russian genitive adjective governs a Greek nominative. |
| U034 | note 3 (ru) | в октахорде «восполняются все интервалы» (U035) | в октахорде «слагаются все интервалы» (U035) | Follows the change in U035 (see 2). |
| U035 | text-ru, note 1 (ru) | восполняются все интервалы / восполняются «все» интервалы | слагаются все интервалы / слагаются «все» интервалы | See 2. |
| U035 | note 2 (ru) | предлагал заменить имена автора этими обычными (U036) …: имена повторяются здесь | предлагал заменить названия автора обычными (U036) …: эти названия повторяются здесь | Names of intervals are «названия» elsewhere in the notes. |
| U036 | note 1 (ru) | ἀντίφωνον как октава — уже в «Проблемах» ([Аристотель], «Проблемы» XIX 39: … | ἀντίφωνον в значении октавы встречается уже у [Аристотеля] («Проблемы» XIX 39: … | «Проблемы» twice in one clause. |
| U036 | note 2 (en) | the key sign of the second note | the reference mark of the second marginal note | "key sign" is not English for a reference mark. |
| U037 | note 1 (ru, en) | (калька: «неизохронно / изохронно») / (calque: “anisochronously / isochronously”) | (заимствованные формы: «анизохронно / изохронно») / (Anglicised: “anisochronously / isochronously”) | These are borrowings, not calques (the calque is the «букв.» form before it); the label comes from card P13. |
| U037 | note 1 (ru) | парафонное — звуки ни одной высоты, ни диссонирующие | парафонное — звуки, не совпадающие по высоте и не диссонирующие | «ни одной высоты» reads "not a single pitch". |
| U037 | note 4 (ru) | (U049, почти дословно совпадающее с Теоном Смирнским, с. 57 Hiller: | (U049; это место почти дословно совпадает с текстом Теона Смирнского, с. 57 Hiller: | Participle with no noun to agree with; «совпадает с Теоном» for «с текстом Теона». |
| U039 | text-ru | Кварта же восполняется двумя тонами и полутоном, да ещё некой малой величиной … двенадцатью [тонами]. | Кварта же слагается из двух тонов и полутона да ещё некой малой величины …; квинта — из трёх [тонов] … двойная октава — из двенадцати [тонов]. (note 1 anchor «да ещё некой малой величины сверх того») | See 2. |
| U039 | note 1 (ru) | если складывать не сами отношения, а их превышения | если не перемножать сами отношения, а складывать их превышения над единицей | Ratios are compounded (multiplied), not added; the EN says so ("instead of compounding"). |
| U039 | note 2 (ru, en) | («октава и кварта / квинта») / (“octave and fourth / fifth”) + repetition of U035 note 2 | («октава с квартой / с квинтой») / (“the octave and a fourth / a fifth”); and shorten to the literal sense, the 11/13-tone point, Xylander's deletion, with «см. примеч. к [U035]» | Notes must use the text's terms; the conflation of the two systems of names and Xylander are already in U035 note 2 (the main note by DECISIONS). |
| U040 | note 1 (ru) | Это общее имя … Видовое имя для 8:3 | Это родовое название … Видовое название для 8:3 | «имя» calques "name"; Russian terminology: «родовое / видовое название». |
| U042 | text-ru (+ note 5 anchor) | относят свои отношения к звуку просламбаномену | отсчитывают свои отношения от звука просламбаномена (anchor «от звука просламбаномена») | See 2. |
| U042 | note 2 (ru, en) | ἔμμεσα / ἄμεσα … — букв. …; это термины логики …, отсюда сравнение … См. примеч. к [U034]. | ἔμμεσα / ἄμεσα (διαστήματα): см. примеч. к [U034] и к [U043]. | Repeats U034 note 1 and U043 note 1. |
| U042 | note 6 (ru, en) | Тридиеса, трёхполутон, дитон и тритон — те же несоставные интервалы, что в U026: они складываются из нескольких интервалов, но звучат как один … | τριημιτόνιον — букв. «три полутона»; см. примеч. к [U026]. О слиянии (σύμφθαρσις) см. примеч. к [U027]. | Retells the translation. |
| U043 | note 2 (ru) | отношения соседних звуков 256:243, 9:8 и 9:8 | отношения смежных звуков 256:243, 9:8 и 9:8 | ἄμεσα context: «смежные»; «соседние» is for ἐγγύς (EN has "adjacent"). |
| U044 | text-ru | при этом приращение от меньших к большим | при этом увеличение от меньших к большим | προσαύξησις, not παραύξησις («приращение», U018, U026, U032); the EN keeps them apart ("increase" / "augmentation"), as does the glossary's concordance. |
| U045 | notes (omission) | no note on «интервальных расстояний» | add at «интервальных расстояний»: «τῶν διαστάσεων — διάστασις, букв. «расстояние»; автор употребляет его наряду с διάστημα «интервал»; в переводе διάστασις — «интервальное расстояние» (U045, U049, U056; «расстояние» в U051, «интервалы» в U035–U036)» / EN parallel | The reader meets a new term without explanation (if the rendering stays; see 2). |
| U046 | text-ru | полуторным [3:2] оказывается не по превышению | полуторным [3:2] предстаёт не по превышению | «оказывается» three times in one sentence for φαίνεται, εὑρίσκεται, δείκνυται; the second and third are prescribed (DECISIONS, L11), the first is free. |
| U046 | note 2 (ru) | — мн. ч. требуют четыре сравнения | — четыре сравнения требуют множественного числа | Indeclinable «мн. ч.» makes subject and object ambiguous. |
| U051 | note 3 (ru) | что рядом с ἰσχύν не строится | что рядом с ἰσχύν синтаксически не связывается | «не строится» calques "does not construe". |
| U052 | note 1 (ru, en) | аппарат к фрагменту P / apparatus to the P fragment | аппарат к отрывку P / apparatus to the P passage | «отрывок P» / "the P passage" everywhere else. |
| U053 | note 1 (ru, en) | … у Теона Смирнского (с. 56.8 Hiller: …), тогда как в тексте Теона — ἐναρμόνιον (с. 55.8 Hiller), и у Гауденция (…) | То же название стоит у Гауденция («Гармоническое введение», 5, Jan, с. 331) и в подписи к диаграмме родов у Теона Смирнского (с. 56.8 Hiller: δίτονον ἁρμονικόν), тогда как в тексте Теона — ἐναρμόνιον (с. 55.8 Hiller). | As printed, Gaudentius seems to have ἐναρμόνιον. EN in parallel. |
| U053 | note 2 (ru, en) | Калька: «паронимически», «паронимия» / Calque: “paronymously”, “paronymy” | Заимствованные формы: «паронимически», «паронимия» / Anglicised: “paronymously”, “paronymy” | Borrowings, not calques (card P12's wording). |
| U058 | note 1 (ru) | ἐκ συμφθάρσεως — «путём слияния» | ἐκ συμφθάρσεως — «образованным слиянием» | The note quotes a rendering not in this unit's text. |
| U062 | note 1 (ru) | Bas., Par. и V дают τό, которое нельзя построить: | Bas., Par. и V дают τό, которое синтаксически ни с чем не связано: | Calque of "cannot be construed". |
| U064 | note 1 (en) | the World Soul | the world soul | As U002 note 2. |
| U067 | text-ru | Конец [раздела о] музыке. | Конец [раздела] музыки. | Without the bracket «Конец музыке» is the idiom "music is finished"; «Конец … музыки» reads correctly both ways. |
| general | notes (ru, en) | Bas. H Par. V; H Par.; Bas. Par. V; H V (U043 n3, U045 n1, U046 n2, U049 n4, U051 n1, n3, n4, U052 n1) | Bas., H, Par., V; H, Par.; Bas., Par., V; H, V | Elsewhere sigla are separated by commas. |
| general | notes (ru) | LSJ without s.v. where the headword differs from the lemma: U020 n2 «LSJ: «подрезать…»», U027 n4 «(LSJ: «функция, значение»)», U066 n2 «(LSJ: «продолжительность»)» | «LSJ s.v. ὑποτέμνω: …», «LSJ s.v. δύναμις: …», «LSJ s.v. διαμονή: …» | DECISIONS § 4: headwords with s.v. |
| general | text-en | spaced em dashes (U004, U032, U042) | spaced en dashes – … – | British house style (Hart's Rules) uses spaced en rules; the EN notes already use en dashes. Only if the series follows that style. |

## 4. Questions (decided points)

- **U008, note order (RU only).** RU callouts run 1, 3, 2, 4 («пригодная для гармонии» before «высота»), EN 1, 2, 3, 4. No single list fits both without distorting a sentence: number the notes per language by anchor position in the build, or accept the RU order.
- **U018** «содержит двойной полутон» → «содержит полутон дважды» (see 2).
- **U042** «относительно соседних звуков» → «к соседним звукам перед ними» (see 2).
- **U045, U049, U056** «интервальное расстояние» (see 2).

## 5. Checked and found right

Running text against DECISIONS: ratio names with brackets (U018–U047, including U020 «полусверхосминного», U025, U046 per L11); P01 (U033, U035; U034 is the known open departure); P02 b (U035 author's names; U036, U039, U040, U042, U051 established names); P05 and the note names (U014); P06 b (U015, U051); P07 (μέλος «напев», μελῳδία «мелодия»; '(μέλος)' at U027, U028, U054, U065; U042 «мелодическая квинта»); P08 (U037, U045, U047, U049, U050); P09 b (U034, U042–U044) and ἐγγὺς φθόγγοι «соседние» (U042, U044); P10 a (U027, U051); P11 a (U026, U042, U058); P12 (U053, U060); P13 (U037); P14 (U009, U010, U042); P15 (U001); ἀπαρτίζω (U015, U027, U054, U056, U057); L01–L15; signs ⟨ ⟩, ⟨⟨ ⟩⟩, † †, [ ]. Typography: «ёлочки» without nesting problems, curly quotes in English, no straight quotes, no hyphen for a dash, ё consistent (всё / все, всём / всем, чём / чем checked in context), decimal comma in RU and point in EN, no «свидетель». Cross-reference forms «см. примеч. к [Uxxx]» / 'see the note on [Uxxx]'. Theon «Теон Смирнский» at the first mention in each note. Gerunds in the running text refer to their subjects (U018 «образуя», U023 «получив», U024 «приняв», U027 «имея … звуча», U060 «получив» per P12).

Counted as confirmed: 41 DECISIONS prescriptions and typographic rules checked across the text.
