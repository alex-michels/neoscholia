# Adversarial verification and application, U001–U028 and bibliography (1.11.2026)

Input: 79 findings (fact-check of the notes, reading for accuracy, language reading, bibliography check).
Findings are numbered 1–79 in the order of the task list (1–47: units and general; 48–79: bibliography entries,
Aleksandrova 2025 = 48 … Vinc. = 79, in the order of the bibliography).
Each finding was first tested against the Greek, the note, DECISIONS.md, the unit packet and, for references,
the source itself. Edited: `compose/final/U001–U028.json` (16 units) and `compose/final/bibliography.json`.
Every edited unit has a line «Adversarial check 1.11.2026: …» appended to its `verify` list.
`check_composed.py … final` after editing: **no problems found, 67 units checked, 0 problems**
(one intermediate hit, «засвидетельствовано» in U020 note 1, caught by the «свидетель» rule, replaced by «встречается»).

## Sources read for this pass

- Hiller 1878 (Theon), archive.org OCR, local copy of the same file from earlier research
  (`inputs/work/g1/dl_theon/theon_djvu.txt`): pp. 12, 17, 19–20, 47–48, 49–50, 64, 69–73; praefatio (codex A
  "membranaceus, saeculi XI. vel XII.").
- Jan 1895, archive.org OCR, local copy (`inputs/work/g3/dl_jan/jan_djvu.txt`): pp. 201 (Cleonides 14), 242–243
  (Nicomachus 4), 261 (Nicomachus 12).
- Düring 1930 (Ptolemy), archive.org djvu text read in the built-in browser (nothing saved): Book III κεφάλαια
  (p. 82, line 2: Πῶς ἂν ἡ δι’ ὅλου χρῆσίς τε καὶ ἀνάκρισις γίνοιτο τῶν λόγων διὰ πεντεκαιδεκαχόρδου κανόνος),
  chapter III 1 opening (p. 83.5–9: εἰ δέ τις ἐκ περιουσίας βούλοιτο συμπληροῦν τῷ κανόνι τὸ δὶς διὰ πασῶν σύστημα …
  τοὺς ἐν τῇ λύρᾳ δεκαπέντε τοῦ δὶς διὰ πασῶν μεγέθους); index «πεντεκαιδεκάχορδος (κανών) 82,2». Page 83 inferred
  from the running heads (80/81 before the κεφάλαια page, 84 after the chapter opening).
- LSJ 9th ed., Perseus XML (local copy, `inputs/work/terms/dl/lsj/`): μέλος (musical senses under **B**, B.2, B.3),
  νευρά (2 "harpstring, Poll. 4.62", single citation), πεντεκαιδεκάχορδος ("Adrast. ap. Theon. Sm. p.64 H., Ptol. Harm.
  3.1 tit., Porph. in Harm. p.168 D."), συμφθείρω (II "Pass., of colours, … Plu. 2.436b; of sounds, D.H. Dem. 48; … Id.
  Comp. 14"), ὑποτέμνω.
- Strunk at attalus.org: "trihemitone" in §§ 3, 5, 7, 12; "trisemitone" nowhere; the διάγραμμα definition of
  Cleonides 14 absent (consistent with Jan's brackets).
- DGE coverage: printed vol. VIII (2019) ends at ἐπισκήνωσις; DGE en línea α–ἔξαυος (CSIC catalogue, web search).
- Bibliography spot checks: nv.mosconsv.ru/node/470 (Tsypin 2014), vestnik.nsglinka.ru issue 13.4 (Aleksandrova 2025),
  CEEOL 33621, 63002, 129818 (Shchetnikov 2009, 2008a; Myakin, Aleksandrova 2009), artcenter.ru listing
  (Gertsman 2024), sblhs2.com (Smyth 1920 vs 1916).

## 1. Changes applied

### U001
- **note 2 (RU, EN, source)** — finding 11 (fact, question: U001 n.2). Not an editor's decision, so applied as a factual precision.
  - RU before: «Таков порядок математических наук у Теона Смирнского: после арифметики должна следовать «музыка в числах» (ἡ ἐν ἀριθμοῖς μουσική; с. 16.24–17.15 Hiller).»
  - RU after: «Таков у Теона Смирнского порядок изучения: «для нашего рассмотрения» он ставит после арифметики «музыку в числах» (ἡ ἐν ἀριθμοῖς μουσική), хотя «по природе» пятое место, после астрономии, принадлежит музыке как учению о гармонии космоса (с. 16.24–17.25 Hiller).»
  - EN before: “This is the order of the mathematical sciences in Theon of Smyrna: after arithmetic comes “music in numbers” (…; pp. 16.24–17.15 Hiller).”
  - EN after: “This is Theon of Smyrna’s order of study: “for our study” he places “music in numbers” (ἡ ἐν ἀριθμοῖς μουσική) after arithmetic, although “by nature” the fifth place, after astronomy, belongs to music as the study of the harmony of the cosmos (pp. 16.24–17.25 Hiller).”
  - source: pp. 16.24–17.15 → pp. 16.24–17.25.
  - Why: Hiller 17.8–14 (ἡμῖν δ’ ἀναγκαῖον δευτέραν αὐτὴν τάττειν … πρὸς τὴν τῆς ἡμετέρας θεωρίας εὐμάρειαν), 17.14–25 (natural order; ὡς δὲ πρὸς τὴν φύσιν πέμπτη ἡ τῆς τοῦ κόσμου ἁρμονίας θεωρητικὴ μουσική). The old wording made Theon's study order his order of the sciences.

### U002
- **note 1 (RU, EN, source)** — finding 1. «(с. 12.10–13.1 Hiller)» → «(с. 12.10–21 Hiller)»; “(pp. 12.10–13.1 Hiller)” → “(p. 12.10–21 Hiller)”; source “pp. 12.10–13.1” → “p. 12.10–21”. Why: read in Hiller: 12.10 καὶ οἱ Πυθαγορικοὶ δέ; 12.14–15 τέλος γὰρ αὐτῆς τὸ ἑνοῦν; 12.19–21 ἐν κόσμῳ μὲν ἁρμονία … σωφροσύνη γίνεσθαι πέφυκε; 12.26 begins the Republic paragraph.

### U005
- **text RU** — finding 22. «гармонией как самого себя, так и вселенной» → «гармонией как его самого, так и вселенной». Why: «себя» binds to the subject «кто-нибудь»; ἑαυτοῦ refers to τὸ θεῖον.
- **text RU** — finding 23 (style). «предстаёт в добром и наилучшем состоянии» → «предстаёт в хорошем, более того, в наилучшем состоянии». Why: the copy-editor's own fallback, parallel to the EN “in a good, indeed the best possible, state”; keeps «состояние» for ἔχον rather than adding «устроенной».
- **text EN** — findings 19 and 24 (same point). “of the universe, in which [the Divine] the universe, being fitted” → “of the universe: in it the universe, being fitted”. Why: the bracket read as an apposition to “the universe”; RU has «: в нём …» without a bracket; note 1 explains the antecedent of ἐν ᾧ (the English “it” is as open as the Greek, and the note decides).

### U008
- **note 1 (RU, EN, source)** — findings 2 and 12.
  - «φθόγγος ἐστὶ φωνῆς ἐναρμονίου τάσις … (с. 47.18–19 Hiller)» → «φθόγγον … εἶναι φωνῆς ἐναρμονίου τάσιν … (с. 47.18–20 Hiller)»; EN likewise. Why: Hiller 47.18–20 has indirect speech (Θράσυλλος … φθόγγον φησὶν εἶναι φωνῆς ἐναρμονίου | τάσιν; τάσιν opens line 20); the nominative was a reconstruction printed as a quotation.
  - «ср. у Никомаха: τάσις … φθόγγου ἀδιαστάτου («Руководство», 4, Jan, с. 242–243).» → «ср. у Никомаха: τάσιν … φθόγγου ἀδιαστάτου («Руководство», 4, Jan, с. 242–243; у Яна в квадратных скобках) и определение, приписанное «некоторым»: ἦχος ἀπλατὴς κατὰ τόπον ἀδιάστατος («Руководство», 12, Jan, с. 261).» EN: “cf. Nicomachus’ τάσιν … φθόγγου ἀδιαστάτου (Manual 4, Jan pp. 242–243, bracketed by Jan) and the definition ascribed to “some”, ἦχος ἀπλατὴς κατὰ τόπον ἀδιάστατος (Manual 12, Jan p. 261).” Why: Jan pp. 242.21–243.5 prints the whole block [φθόγγον δὲ … σύνθεσιν.] in brackets; the text there has τάσιν (acc.), so the same correction of case as for Theon; Jan p. 261 (unbracketed): ὡς δ’ ἔνιοι, ἦχος ἀπλατὴς κατὰ τόπον ἀδιάστατος.
  - source: “Theon of Smyrna, p. 47.18–19 Hiller; Nicomachus, Manual 4 (Jan pp. 242–243);” → “Theon of Smyrna, p. 47.18–20 Hiller; Nicomachus, Manual 4 (Jan pp. 242–243, bracketed), 12 (Jan p. 261);”.
- **open** (new) — finding 41: the RU note order (callouts 1, 3, 2, 4) recorded as an open point for the build/editor. No reordering (any order distorts one language).

### U009
- **note 1 (RU, EN)** — finding 25. RU «неодинаковыми по высоте и низости» → «неодинаковыми по высоте (ὀξύτητι καὶ βαρύτητι)»; EN “unlike in highness and lowness” → “unlike in highness and lowness (ὀξύτητι καὶ βαρύτητι)”. Why: «низость» = baseness; «неодинаковыми» kept for ἀνομοίων; Cleonides' Greek pair (Jan p. 179) added in both languages to keep them parallel.

### U013
- **notes order** — finding 26. [нестройный, изданным иначе, Ведь] → [Ведь, нестройный, изданным иначе]. Why: the note on γάρ sits on the first word in both languages; callouts now run 1, 2, 3.
- **note on «изданным иначе» (RU, EN, source)** — finding 3.
  - RU «…(с. 47.18–48.8 Hiller); немелодичные шумы (ψόφοι) … (с. 50.14–16 Hiller).» → «…(с. 47.18–48.8 Hiller). Ср. также пифагорейское учение в изложении Адраста у Теона: немелодичные шумы (ψόφοι) … (с. 50.4–16 Hiller).» EN in parallel (“Cf. also the Pythagorean doctrine as reported by Adrastus in Theon: … (p. 50.4–16 Hiller).”).
  - source: “pp. 47.18–48.8, 50.14–16 Hiller” → “pp. 47.18–48.8 (Thrasyllus), 50.4–16 (Adrastus) Hiller”.
  - Why: read in Hiller: 49.6 ὁ δὲ περιπατητικὸς Ἄδραστος … φησί; 50.4 φησὶ δὲ καὶ τοὺς Πυθαγορικοὺς περὶ αὐτῶν οὕτω τεχνολογεῖν; 50.14–16 ψόφοι, οὓς οὐδὲ φθόγγους χρὴ καλεῖν κυρίως. The old note put p. 50 under “Cf. Thrasyllus”.

### U014
- **note 3 (RU, EN)** — finding 27: «Hiller, с. [206]» → «с. [206] Hiller»; “Hiller p. [206]” → “p. [206] Hiller” (DECISIONS § 4). Finding 30: «в смешанных списках Никомаха» → «в смешанных перечнях названий у Никомаха» (in this series «список» = manuscript copy).
- **note 5 (RU, EN, source)** — finding 27: «(Hiller, с. [206])» → «(с. [206] Hiller)»; “(Hiller p. [206])” → “(p. [206] Hiller)”. Same reason as finding 30: «разделяет с этим списком» → «разделяет с этим перечнем» (the note compares the list with a codex, so «список» was ambiguous). Finding 13: «кодекс моложе 1008 г.» → «кодекс датируется XI или XII в. (Hiller, praef.), и направление зависимости неизвестно.»; “the codex is later than 1008.” → “the codex is of the 11th or 12th century (Hiller, praef.), and the direction of dependence is unknown.”; source + “Hiller, praef. (date of codex A);”. Why: Hiller, praef.: “Codex A membranaceus, saeculi XI. vel XII.” — s. XI does not exclude 1001–1008; the edition's own resolved doubt says “the direction of dependence is unknown”.

### U015
- **note 1 (RU, EN, source)** — finding 7. Added after the Theon sentence: RU «В двухоктавном смысле слово употребляет Птолемей: πεντεκαιδεκάχορδος κανών — пятнадцатиструнный канон, на котором можно выстроить всю систему в две октавы (τὸ δὶς διὰ πασῶν σύστημα; «Гармоника» III 1, заглавие и начало главы; LSJ s.v. πεντεκαιδεκάχορδος).» EN “In the two-octave sense the word is Ptolemy’s: the πεντεκαιδεκάχορδος κανών, a fifteen-stringed canon on which the whole two-octave system (τὸ δὶς διὰ πασῶν σύστημα) can be set out (Harmonics III 1, title and opening; LSJ s.v. πεντεκαιδεκάχορδος).” Source + “Ptolemy, Harmonics III 1 (title and opening)”. Why: LSJ's second citation; Düring p. 82.2 (κεφάλαια) and 83.5–9 (chapter text) read. The Düring page is left out of the note so as not to add a new bibliography key (Ptolemy is cited by book and chapter, as Plato and Euclid are).

### U018
- **note 1 (RU)** — finding 31. «аристоксеновы величины» → «аристоксеновские величины» (as «аристоксеновская» in the same note).
- **note 2 (RU, EN, source)** — finding 14. «в словарях (LSJ, DGE, Bailly, Pape) это слово не отмечено.» → «в словарях (LSJ, Bailly, Pape) это слово не отмечено (DGE до η ещё не дошёл).»; EN “not recorded in LSJ, DGE, Bailly or Pape.” → “not recorded in LSJ, Bailly or Pape (DGE has not yet reached η).”; source “LSJ, DGE, Bailly, Pape: no entry …” → “LSJ, Bailly, Pape: no entry for ἡμιεπόγδοος (DGE not yet at η)”. Why: DGE printed to ἐπισκήνωσις (vol. VIII, 2019); its silence for an η-word says nothing. The DECISIONS sentence that lists DGE goes to the editor.
- **note 3 (RU, EN, source)** — finding 8.
  - RU before: «(√(9/8) = √72/8 ≈ 1,0607; ср. Теон Смирнский, с. 69 Hiller: полутон — ἐφεκκαιδέκατον, 17:16; οὐδὲ γὰρ … «ведь сверхосминное [отношение] не может принять деления»).»
  - RU after: «(√(9/8) = √72/8 ≈ 1,0607). Теон Смирнский допускает то же деление избытка пополам лишь как рабочую меру: доказывая, что лимма 256:243 меньше полутона, он при тоне 9:8 принимает полутон за δὶς ἐπόγδοον, τουτέστιν ἐφεκκαιδέκατον, то есть 17:16, и тут же добавляет: οὐδὲ γὰρ οἷόν τε τὸ ἐπόγδοον διαίρεσιν ἐπιδέξασθαι, «ведь сверхосминное [отношение] не может принять деления», хотя так полагают те, кто судит об этом не разумом, а слухом (с. 69.12–70.1 Hiller).» EN in parallel.
  - source: “p. 69.13–17 Hiller” → “pp. 69.12–70.1 Hiller”.
  - Why: Hiller 69.12–18, 70.1 read (ὅτι δὲ τοῦτο τὸ διάστημα … ἔλαττόν ἐστιν ἡμιτονίου … τὸ ἡμιτόνιον δὶς ἐπόγδοον ἔσται, τουτέστιν ἐφεκκαιδέκατον … οὐδὲ γὰρ οἷόν τε … εἰ καὶ οἱ μὴ λόγῳ ἀλλὰ τῇ ἀκοῇ ταῦτα κρίνοντες νομίζουσιν); the old wording presented 17:16 as Theon's semitone. DECISIONS' “(cf. Теон, с. 69 Hiller)” is kept in substance.
- **open** (new) — finding 32 («двойной полутон»), for the editor.

### U019
- **note 1 (RU, EN, source, verified)** — findings 4 and 9. Rewritten; the old content kept, with:
  - range «с. 19.20–20.3 Hiller» → «с. 19.18–20.4 Hiller» (Hiller 19.18–19 καὶ μονὰς τοίνυν … ἄτομος; 20.2–4 … εἰς ἄπειρον τμητόν; line count checked against the apparatus “19 ἥ] ἢ A”, “21 inscr.”);
  - added: Theon's verbatim formula τῶν θ' πρὸς τὰ η' ἡ μονὰς οὐ τέμνεται (70.1–3) and the argument that the tone cannot be halved because the difference is the indivisible unit (70.14–19, apparatus “14 inscr. ὅτι ὁ τόνος δίχα οὐ τέμνεται”); the attribution to Adrastus given as probable only (named at 64.1 and 73.19, not at the sentence); Theon's conclusion, the reverse of the compiler's (71.1–4, 72.2–4, 72.19–20: ὁ δὲ νοήσει ληπτὸς τόνος δύναται νοεῖσθαι καὶ εἰς ἴσα διαιρούμενος), pp. 70.19–72.20.
  - source: “Theon of Smyrna, pp. 19.20–20.3 Hiller” → “Theon of Smyrna, pp. 19.18–20.4, 70.1–3, 70.14–19, 70.19–72.20 Hiller (Adrastus named at 64.1, 73.19)”.
- **open** — the item on “Theon p. 66 (Adrastus)” removed: settled by a verified fact (p. 66 has nothing on the unit; the passage is p. 70, now in the note, as the item itself asked).

### U020
- **note 1 (RU, EN)** — finding 33: «(буквы ο и ι неуверенны)» → «(буквы ο и ι читаются неуверенно)». Finding 15: «νευρά в значении «струна» — обычное слово позднего греческого языка (LSJ s.v. νευρά 2); оно стоит…» → «νευρά в значении «струна [инструмента]» встречается в позднем греческом (LSJ s.v. νευρά 2: «струна арфы», у Поллукса); это слово стоит…»; EN “is usual in later Greek (LSJ s.v. νευρά 2)” → “is attested in later Greek (LSJ s.v. νευρά 2: “harpstring”, in Pollux)”. Why: LSJ gives one citation (Poll. 4.62); “usual” is not supported. Pape and Bailly (seen by the fact-checker) were not added, since I did not see them.
- **note 2 (RU, EN)** — finding 43: «LSJ: «подрезать…»» → «LSJ s.v. ὑποτέμνω: «подрезать…»»; “LSJ gives” → “LSJ s.v. ὑποτέμνω gives” (DECISIONS § 4; lemma ὑποτεμεῖν ≠ headword).
- **note 3 (RU, EN, source)** — findings 10, 34 and 14, merged.
  - RU before: «ἡμιεπόγδοον — калька: «полусверхосминное»; в словарях это слово не отмечено. Автор сам поясняет его: «то есть полутон». По числам U018 … (см. примеч. к [U018] и к [U025]).»
  - RU after: «ἡμιεπόγδοον — калька: «полусверхосминное»; в словарях это слово не отмечено (см. примеч. к [U018]). По числам U018 это отношение с избытком в половину восьмой: 8½:8 = 17:16, так что пополам делится избыток, а не отношение 9:8 (см. примеч. к [U025]). Ср. у Теона Смирнского полутон как δὶς ἐπόγδοον, τουτέστιν ἐφεκκαιδέκατον, то есть 17:16 (с. 69.14–15 Hiller).» EN in parallel.
  - source: “LSJ, DGE, Bailly, Pape (no entry for ἡμιεπόγδοος); U018; U025” → “LSJ, Bailly, Pape (no entry for ἡμιεπόγδοος); U018; U025; Theon of Smyrna, p. 69.14–15 Hiller”.
  - Why: the retelling (“the author glosses it himself”) dropped; a one-clause lexicon statement kept, since the reader meets the word here; DGE dropped (η); Theon 69.14–15 read.

### U024
- **note 1 (verified)** — not a listed finding; from the fact-check log (U024): Meno 82b–85b read in Burnet's text by the fact-checker, construction confirmed. “from memory” → “checked”.

### U025
- **text EN** — finding 18. “the epogdoic ratio [9:8] of the tone is divided” → “the epogdoic ratio [9:8] of the tone, too, is divided”. Why: ταύτῃ τοι καὶ ὁ ἐπόγδοος …; RU «и» already renders καί. The U029 harmonisation is not in my units (for the editor).
- **note 1 (RU, EN)** — finding 35. «√72 ≈ 8,485 против 8,» → «√72 ≈ 8,485 (между 8 и 9),»; “√72 ≈ 8.485 against 8,” → “√72 ≈ 8.485 (between 8 and 9),”.

### U026
- **note 1 (RU)** — finding 36. «3 тона. τριδίεσις в словарях…» → «3 тона. Слово τριδίεσις в словарях…».
- **note 2 (EN)** — findings 5 and 45. “The usual English term is “trihemitone”; “trisemitone” (Strunk) is a minority form.” → “The usual English term is “trihemitone” (so Strunk).” Why: attalus.org (Strunk 1950, the edition the bibliography describes) has “trihemitone” only.

### U027
- **note 1 (RU)** — finding 39. «между соседними звуками рода, составны — между несоседними» → «между смежными звуками рода, составны — между несмежными» (DECISIONS P09: ἑξῆς = «смежные»; «соседние» reserved for ἐγγὺς φθόγγοι).
- **note 2 (RU, EN, source)** — finding 16. «LSJ s.v. μέλος II» → «LSJ s.v. μέλος B» (three places). Why: LSJ 9th ed. (Perseus XML read): A limb; B “musical member, phrase: hence, song, strain”, B.2 “tune”, B.3 “melody of an instrument”; no section II.
- **note 3 (RU, EN, source)** — finding 6. RU «глагол συμφθείρω сказан о красках и звуках, которые «сливаются» (Дионисий Галикарнасский)» → «страдательное συμφθείρομαι сказано о красках, которые «сливаются» друг с другом (Плутарх), и о звуках (Дионисий Галикарнасский)»; EN “the verb συμφθείρω is used of colours and sounds that “melt into each other” (Dionysius of Halicarnassus)” → “the passive of συμφθείρω is used of colours that “melt into each other” (Plutarch) and of sounds (Dionysius of Halicarnassus)”; source “s.v. συμφθείρω (D.H. Dem. 48; Comp. 14)” → “s.v. συμφθείρω II (Plu. Def. orac. 436b; D.H. Dem. 48; Comp. 14)”. Why: LSJ συμφθείρω II read (Plu. 2.436b = De defectu oraculorum).
- **note 4 (RU, EN, source)** — findings 43 and 17. «(LSJ: «функция, значение»)» → «(LSJ s.v. δύναμις: «функция, значение»)»; EN likewise. «Ср. Клеонид, гл. 14: διάγραμμα» → «Ср. Клеонид, гл. 14 (заключительные определения, у Яна в квадратных скобках, Jan, с. 201): διάγραμμα»; EN “Cf. Cleonides ch. 14 (the closing definitions, bracketed by Jan, p. 201): διάγραμμα”; source “Cleonides chs. 2, 14;” → “Cleonides chs. 2, 14 (Jan p. 201, bracketed);”. Why: Jan p. 201 read: [Διάγραμμα δὲ σχῆμα ἐπίπεδον τὰς τῶν μελῳδουμένων περιέχον δυνάμεις … ὑποθέσεως.]; Strunk's translation omits the block. The DECISIONS P10 content is unchanged.

### U028
- **text RU** — finding 40. «отсюда оказывается возможным и существование слияния» → «тем самым оказывается возможным и слияние». Why: removes the Russian break after «в напевах … —» and the wordy «существование»; «тем самым» = EN “thereby”; καί kept («и слияние»). The possibility reading and note 3's anchor «оказывается возможным» are untouched, so the open question is not prejudged.
- **note 2 (source)** — finding 16. “LSJ s.v. μέλος II” → “LSJ s.v. μέλος B”.

## 2. Findings not applied (with reasons)

- **Finding 20, U004 τὸ πᾶν (question).** An open question for the editor; the recommendation (keep the adverbial «всецело» / “wholly so”) goes to for_editor. The `open` item stays.
- **Finding 21, U028 ἐγγίνεται (question).** Open question; recommendation (keep possibility; LSJ s.v. ἐγγίγνομαι III “impers., it is allowed or possible, c. inf.”, confirmed by the fact-checker) to for_editor. The `open` item stays.
- **Finding 28, U014 «по продвижению» → «по следованию» (style).** «продвижение» is the agreed glossary rendering of πρόοδος (glossary.md, line 243), and the change is not clearly better («по продвижению … от низкого к высокому» is clear in context). Passed to the editor as optional.
- **Finding 29, U014 note 2 «переданную форму» → «эту форму» (style).** «переданная форма» (the transmitted form) is ordinary Russian philological usage and carries the point that the edition does not normalise; not clearly better.
- **Finding 32, U018 «двойной полутон» (question).** DECISIONS (ratio section) explicitly keeps «содержащий двойной полутон»; to for_editor and recorded in U018 `open`.
- **Finding 37, U026 note 2: delete «В хроматическом роде этот интервал несоставной (см. примеч. к [U058])» (style).** The sentence is P11's pointer to U058, where the consistency pass moved Theon p. 55.2–6 (the reference DECISIONS P11 wants in this note); deleting it would cut that link. The overlap with note 1 is one clause.
- **Finding 38, U026 note 3 «букв. «ритм»» → «ритм» (gloss).** «букв.» marks that the running text keeps the literal sense while the note argues for “order, proportion”; it does work here.
- **Finding 41, U008 RU note order (question).** No list order fits both word orders; recorded in U008 `open` and for_editor (per-language numbering in the build).
- **Finding 42, sigla without commas (U043–U052).** Outside U001–U028; U001–U028 already use commas (checked). To for_editor.
- **Finding 43, LSJ s.v. — U066 note 2 part.** Outside my units; to for_editor (U020 and U027 parts applied).
- **Finding 44, EN spaced em dashes → en dashes (U004, U032, U042).** A series-wide house-style choice not fixed by DECISIONS § 4; changing U004 alone would make it inconsistent with U032 and U042. To for_editor.
- **Finding 46, key «Александрова, Мякин 2009» (question).** The key is prescribed by DECISIONS § 4; kept. Published order (Мякин first) confirmed on CEEOL 129818 and is already in the entry. To for_editor.
- **Finding 47, Gertsman 2000 (question).** Not a bibliography entry of any cited work; to for_editor.
- **Finding 76, Synodal translation (question).** Entry accepted (first complete Synodal Bible, 1876; NT 1862); the printing actually used is unknown; to for_editor.

Partly applied (see § 1): finding 15 (Pape not cited, as I did not see it); finding 34 (the lexicon clause kept, the retelling dropped); finding 7 (Düring page not in the note, to avoid a new bibliography key); finding 9 (shortened; Adrastus given as probable).

## 3. Bibliography (`final/bibliography.json`)

`factcheck/bibliography-proposed.json` checked entry by entry against `factcheck/bibliography.md`; same 33 keys in the
same order, same fields (key_ru, key_en, ru, en); every author–year key and every plain key cited in the notes and
source fields of U001–U067 is present (scan: Barker 1989, Bellermann 1841, Gertsman 2010/2024, Macran 1902,
Shchetnikov 2008a/2008b/2009/2012, Tsypin 2013/2014, Aleksandrova 2025, Aleksandrova, Myakin 2009, and the plain keys
Hiller, Jan, LSJ, DGE, Bailly, Pape, Lampe, Meibom, Friedlein, Pistelli, Smyth, Strunk, Kühner–Gerth, Dvoretsky,
Sophocles, Lexicon, Vinc., Bas., Par.). No new key was needed by this pass.

Spot checks on the web (all agree with the proposed entries):
- Tsypin 2014: nv.mosconsv.ru/node/470 — «Клеонид. Введение в гармонику»; Лебедев (предисловие), Цыпин (перевод, научные комментарии); т. 5, вып. 3, 2014, с. 168–186, DOI 10.26176/mosconsv.2014.18.3.09.
- Aleksandrova 2025: vestnik.nsglinka.ru, issue 13.4 — title as in the entry, pp. 9–21, DOI 10.63219/2308-1031-2025-4-9-21.
- Shchetnikov 2009: CEEOL 33621 — ΣΧΟΛΗ III/2009, no. 2, pp. 466–558.
- Shchetnikov 2008a: CEEOL 63002 — ΣΧΟΛΗ II/2008, no. 1, pp. 75–89.
- Myakin, Aleksandrova 2009: CEEOL 129818 — authors in the order Myakin, Alexandrova; ΣΧΟΛΗ III/2009, no. 1, pp. 161–205.
- Gertsman 2024: artcenter.ru publications list — СПб.: РИИИ, 2024, 60 с. (the 2023 Herzen University book of the same main title is a different work, as the log says).
- Smyth: the SBL handbook blog confirms that the Perseus Smyth is A Greek Grammar for Colleges (1920), distinct from the shorter 1916 book — the correction of the entry is right.
- Strunk: attalus.org states “taken from O. Strunk, Source Readings in Music History, pp. 34–46”, and has “trihemitone” only.

Accepted from the log without a further check of my own (the checker gives catalogue links): Bas., Par., Vinc., Hiller,
Jan, Friedlein, Bellermann, Meibom, Pistelli, Kühner–Gerth, LSJ, Barker, Tsypin 2013, Shchetnikov 2008b, 2012; standard
imprints (Dvoretsky 1958, Macran 1902, Lampe 1961–1968, Pape 1880, DGE 1980–, Bailly 1895 / Abrégé 1901, Sophocles
1914 memorial edition) agree with what I know of them. Not verified by anyone: Lampe p. 131 (from the edition's
apparatus); the printing of the Synodal Bible used.

Findings 48–75 and 77–79 (entry completions; 73 = Smyth, wrong book, an error): accepted as proposed. Finding 76
(Synodal): accepted, with the question to the editor.

Written: `final/bibliography.json` = the proposed file, unchanged in content (CRLF, indent 2, as before).

## 4. For the editor (also returned in for_editor)

See the structured output: U004 and U028 open questions with recommendations; U018 «двойной полутон»; U008 note order;
DECISIONS § 4 example «LSJ s.v. μέλος II» → «B»; DECISIONS § 1 “not recorded in LSJ, DGE, Bailly or Pape” (DGE not at η);
U029 harmonisation with U025; U066 LSJ s.v.; sigla commas U043–U052; EN dashes; the key «Александрова, Мякин 2009»;
the Synodal printing; Gertsman 2000; U014 «продвижение» (optional); Barker 1989 page references unchecked online.
