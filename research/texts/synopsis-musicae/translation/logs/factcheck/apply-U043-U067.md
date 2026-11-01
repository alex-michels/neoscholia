# Applying the factcheck findings, U043–U067 (adversarial verifier, 1.11.2026)

Input: 34 findings for U043–U067 from the four checks (fact-check of the notes, accuracy reading, language reading, bibliography). They are numbered F1–F34 in the order they were handed over:

- F1–F9: fact-check, `notes-U043-U067.md`.
- F10–F12: accuracy reading, `reading-accuracy.md`.
- F13–F34: language reading, `reading-language.md`.

I tried to refute every finding before applying it. For each one I re-read the Greek, the note, DECISIONS.md, the glossary, the unit packet or edition material and, where the finding is about a source, the source itself.

Sources I read myself:
- Hiller's Theon: the local OCR `inputs/work/g1/dl_theon/theon_djvu.txt`, pp. 55–61 and 65–66, with the apparatus.
- Jan, *Musici scriptores Graeci*: the local OCR `inputs/work/g3/dl_jan/jan_djvu.txt`.
  - Nicomachus, pp. 261–263, located by the running heads.
  - Bacchius, pp. 298–299.
  - Gaudentius, p. 331.
- Logeion API (LSJ, DGE, Bailly 2024, Pape) for γοερός, γενναῖος, ἀφορότης, διάτασις and διάστασις. Perseus returned HTTP 403.
- Vincent 1847 on archive.org (third Psellus fragment; WebFetch, in summary only). It confirms that the first paragraph is printed from the edition and that the footnote gives P's variant for the wind-instrument clause only.
- Edition material: `edition/section-5.md` and `edition/section-7.md` (Par. lineation at U066).

Backup of the state before this pass: the session scratchpad, `final-backup-before-apply-U043-U067/` (not in the workspace).

Result: 19 unit files changed (U043–U046, U049–U056, U058, U059, U062, U064–U067). Each changed unit's `verify` list has a "factcheck pass: …" line, and U045 `open` has a new item. `check_composed.py … final`: "no problems found, 67 units checked". A scan of U043–U067 confirms that every anchor is a unique substring and that the notes run in anchor order in both languages.

## 1. Changes applied

| Unit | Place | Before | After | Why | Finding |
|---|---|---|---|---|---|
| U043 | notes order | 1 между смежными · 2 в силлогизмах · 3 а между несмежными | 1, 3, 2 (now 1 между смежными · 2 а между несмежными · 3 в силлогизмах) | Callouts must follow the anchors; note 3's anchor came before note 2's in RU and EN. Checked by script. | F13 |
| U043 | note «в силлогизмах» (now 3), RU | отношения соседних звуков 256:243, 9:8 и 9:8 | отношения смежных звуков 256:243, 9:8 и 9:8 | The context is ἄμεσα, «смежные» (P09). «Соседние» is reserved for ἐγγύς. The EN already has "adjacent". | F14 |
| U044 | text RU | при этом приращение от меньших к большим | при этом увеличение от меньших к большим | The Greek is προσαύξησις. The agreed glossary concordance has «приращение; увеличение» for παραύξησις; προσαύξησις, and the EN keeps 'augmentation' / 'increase' apart. | F15 |
| U045 | new note 2 at «интервальных расстояний» / 'intervallic spans' | — | RU: «τῶν διαστάσεων — διάστασις, букв. «расстояние»; в музыке — то же, что διάστημα «интервал» (LSJ s.v. διάστασις III …). Автор употребляет оба слова; слово διάστασις передано здесь, в U049 и U056 как «интервальное расстояние», в U051 — как «расстояние», в U035–U036 — как «интервалы».» EN parallel. SRC: LSJ s.v. διάστασις III; U035, U036, U049, U051, U056. | The reader meets an unexplained term (the glossary's rendering). LSJ III "interval … in Music" (Aristoxenus) was seen via Logeion. The renderings in U035, U036 and U051 were checked against the text. Old note 2 is now note 3. | F16 |
| U045 | open | — | New item on «интервальное расстояние» / 'intervallic span' (also U049, U056), with the reader's alternative «расстояние» / 'span' throughout | The rendering is the glossary's, so the change is the editor's decision. The note must be adapted if the rendering changes. | F17 |
| U046 | notes order | 1 пятикратным [5:1] · 2 [пятый звук] | 2, 1 | Callouts follow the anchors in RU and EN. | F18 |
| U046 | text RU | полуторным [3:2] оказывается не по превышению | полуторным [3:2] предстаёт не по превышению | φαίνεται ('appear', as in the EN). This removes the third «оказывается» in one sentence. The other two (εὑρίσκεται, δείκνυται) are prescribed by DECISIONS (L11) and are untouched. | F19 |
| U046 | note «[пятый звук]» (now 1), RU | — мн. ч. требуют четыре сравнения. | — четыре сравнения требуют множественного числа. | Subject and object were ambiguous with the indeclinable abbreviation. | F20 |
| U049 | note 1, RU/EN | (с. 56.9–57.6 Hiller, из Адраста) / pp. 56.9–57.6 Hiller (from Adrastus) | (с. 56.9–57.6 Hiller) / pp. 56.9–57.6 Hiller | Wrong attribution. Theon closes this section at 61.18–19: ταυτὶ μὲν περὶ τῆς εὑρέσεως τῶν συμφωνιῶν· ἐπανέλθωμεν δὲ ἐπὶ τὰ ὑπὸ τοῦ Ἀδράστου παραδεδομένα. Seen in Hiller (local OCR, with the running head "De inventione consonantiarum" on pp. 56–60). | F1 |
| U049 | note 1, RU/EN (addition before the Nicomachus sentence) | — | RU: «Этот раздел об открытии консонансов Теон сам отделяет от изложения Адраста: ταυτὶ μὲν … παραδεδομένα, «вот и всё об открытии консонансов; вернёмся же к тому, что передал Адраст» (с. 61.18–19 Hiller).» EN parallel. SRC: "Theon of Smyrna, pp. 56.9–57.6, 61.18–19 Hiller". | Verified addition. It also keeps the reader from carrying over the Adrastus attribution, which is right in U050 (pp. 65.10–66.11), to this passage. «консонанс» for συμφωνία follows the glossary. | F1 |
| U049 | note 4, RU/EN | слова ἀφορότης нет в LSJ / ἀφορότης is not in LSJ | слова ἀφορότης нет ни в LSJ и DGE, ни у Bailly и Pape / ἀφορότης is in none of LSJ, DGE, Bailly or Pape. SRC + "LSJ, DGE, Bailly, Pape (via Logeion)" | Logeion API for ἀφορότης returns `dicos: []`. DGE is part of Logeion and covers α; the same API returns a DGE entry for διάτασις. Seen myself. | F7 |
| U050 | notes order | 1 Следует знать · 2 †и то и другое† · 3 бо́льшая тяжесть · 4 протяжённости отверстий | 1, 3, 4, 2 | Callouts follow the anchors in RU and EN. | F21 |
| U050 | note 1, RU/EN | за собственной, более краткой редакцией предыдущей фразы / P’s own shorter version | за собственной редакцией предыдущей фразы / P’s own version | Vincent gives P's variant for the wind-instrument clause only (n. 5). That clause is not shorter in P: it lacks καὶ ἀνέσεως but adds τῶν αὐλῶν ἢ τῶν τρημάτων. Nothing shows the rest of P's sentence to be shorter. | F2 |
| U050 | note «протяжённости отверстий» (now 3), RU/EN | «натяжение, расширение, протяжение»; … с. 66 Hiller / … p. 66 Hiller | … «натяжение, расширение, протяжение» (DGE и Bailly также дают «расширение») … с. 66.7–8 Hiller / “tension, dilatation, extension” (DGE and Bailly also give “dilatation”) … p. 66.7–8 Hiller. SRC: Theon p. 66.6–8 Hiller | The finding's fallback for the case where the neutral rendering is kept. DGE II.1 "dilatación" and Bailly "distension, dilatation" were seen via Logeion, and Theon 66.6–8 in Hiller. The rendering and the open item are unchanged (see § 2). | F8 (part) |
| U051 | note 3, RU | что рядом с ἰσχύν не строится | что рядом с ἰσχύν синтаксически не связывается | Calque of "does not construe". Changed together with U062 so that the two notes keep one wording. | F22 |
| U052 | note 1, RU/EN | аппарат к фрагменту P / apparatus to the P fragment | аппарат к отрывку P / apparatus to the P passage | «отрывок P» / 'the P passage' everywhere else (U019–U042, U050). Checked by grep. | F23 |
| U053 | note 1, RU/EN | … в подписи к диаграмме родов у Теона Смирнского (с. 56.8 Hiller: δίτονον ἁρμονικόν), тогда как в тексте Теона — ἐναρμόνιον (с. 55.8 Hiller), и у Гауденция («Гармоническое введение», 5, Jan, с. 331). | «То же название стоит у Гауденция («Гармоническое введение», 5, Jan, с. 331: ἐν μὲν τῷ ἁρμονικῷ) и у Вакхия («Введение в музыкальное искусство», § 22, Jan, с. 298: τὸ οὖν ἁρμονικὸν πῶς μελῳδεῖται;), хотя чуть выше, перечисляя роды, оба называют этот род ἐναρμόνιον. У Теона Смирнского это название стоит в подписи к диаграмме родов (с. 56.8 Hiller: δίτονον ἁρμονικόν; ἁρμονικόν — чтение рукописей A и Z, в апографах — ἐναρμόνιον), тогда как в тексте Теона — ἐναρμόνιον (с. 55.8 Hiller).» EN parallel. SRC + "Bacchius, Introduction to the Art of Music § 22 (Jan p. 298)", "(with Hiller’s apparatus)". | (a) As printed, "and in Gaudentius" followed the "whereas" clause and seemed to give Gaudentius ἐναρμόνιον (F24). (b) Hiller's apparatus to 56.8: "δίτονον ἁρμονικόν] ἁρμονικὸν διατόνιον AZ, δίτονον ἐναρμόνιον apogr." (F6). (c) Bacchius § 22 is on Jan p. 298 (running head "Isagoge § 20–33"; § 21 lists Ἐναρμόνιον, χρῶμα, διάτονον), and Gaudentius 5 is on p. 331 (the genera listed as ἐναρμόνιον, then ἐν μὲν τῷ ἁρμονικῷ). Both seen in Jan (F6). «Вакхий» is the form in the bibliography (entry Meibom). Bacchius' Jan apparatus (ἁρμονικόν MV, ἐναρμόνιον P) is left out, because its siglum P would be confused with our P. | F6, F24 |
| U053 | note 2, RU/EN | Калька: «паронимически», «паронимия» / Calque: “paronymously”, “paronymy” | Заимствованные формы: «паронимически», «паронимия» / Anglicised: “paronymously”, “paronymy” | These are borrowings, not loan translations. The calque proper, «отыменные», follows in the same note. The rendering decided on card P12 (DECISIONS) is untouched; only the label of the note was wrong. | F25 |
| U054 | notes order | 1 потому и называется · 2 по большей части · 3 · 4 | 2, 1, 3, 4 | Callouts follow the anchors in RU and EN. | F26 |
| U055 | notes order | 1 да это и невозможно · 2 ни целиком через полутоны | 2, 1 | Same. | F27 |
| U056 | notes order | 1 из трёх … · 2 остаток … · 3 разделена | 1, 3, 2 | Same. | F28 |
| U058 | note 1, RU/EN | ἐκ συμφθάρσεως — «путём слияния» / “by fusion” | «образованным слиянием» / “formed by fusion” | The note quotes the rendering, and the text has «одним интервалом, образованным слиянием» / 'a single interval formed by fusion'. | F29 |
| U058 | note 1, RU/EN | так же у Никомаха. / likewise Nicomachus, Manual. | так же у Никомаха («Руководство», 12, Jan, с. 262: ἡμιτόνιον, εἶτα ἄλλο ἡμιτόνιον, εἶτα ἐπὶ τούτοις ἀσύνθετον τριημιτόνιον). / likewise Nicomachus, Manual 12 (Jan p. 262: …). SRC + "Nicomachus, Manual 12 (Jan p. 262)" | Locus verified in Jan. Running heads: p. 261 "c. 11.12", p. 263 "c. 12", and the passage stands on the page between them (OCR "202"). The Greek was read in the OCR. | F5 |
| U059 | note 1, RU/EN | (γοερός «скорбный, жалобный», от γόος «плач», LSJ) / (γοερός “mournful, plaintive”, from γόος “wailing”, LSJ) | (γοερός «скорбный, горестный», о людях — «плачущий, причитающий»; от γόος «плач, рыдание», LSJ) / (γοερός “mournful, distressful”, of persons “wailing, lamenting”; from γόος “weeping, wailing”, LSJ) | LSJ (Logeion): "of things, mournful, distressful … II. of persons, wailing, lamenting". "Plaintive" is not LSJ's, and γόος is "weeping, wailing". The rendering «более жалобный» / 'more plaintive' in the text stays. | F3 |
| U062 | note 1, RU | дают τό, которое нельзя построить: | дают τό, которое синтаксически ни с чем не связано: | Calque of "cannot be construed". | F30 |
| U064 | note 1, RU/EN | «подлинный, верный своей природе» (LSJ) / “genuine, true to its kind” (LSJ) | «верный своему происхождению», а о вещах — «хороший в своём роде», «подлинный» (LSJ) / “true to one’s birth or descent” and, of things, “good of their kind”, “genuine” (LSJ) | The quoted wording was a blend, not LSJ's. LSJ (Logeion) has "true to one's birth or descent" (Arist. HA 488b19) and "II. of things, good of their kind, excellent … genuine". «хороший» rather than the finding's «добротный», which is closer to "good". | F4 |
| U064 | note 1, EN | the World Soul | the world soul | As U002 note 2. | F31 |
| U065 | text RU; note 2 anchor_ru | и складывается напев то лидийский, то фригийский, то дорийский, причём; anchor «складывается напев» | и складывается то лидийский, то фригийский, то дорийский напев, причём; anchor «напев» | RU callouts ran 2, 1, 3 while EN ran 1, 2, 3. The new order follows the Greek (… δώριον ἐναρμόζεται μέλος) and the EN, so one list fits both. | F32 |
| U066 | note 1, RU | наборщик перескочил с одного конца строки на другой | наборщик перескочил с конца одной строки на конец следующей | Matches the EN and the edition (section 7: "a compositor's single slip from one line end to the next", Par. 27r.18–20, με-\| … δια-\|). | F33 |
| U067 | text RU | Конец [раздела о] музыке. | Конец [раздела] музыки. | Without the bracket the old text reads as the idiom «конец музыке». The new one reads correctly with or without the bracket. The note 1 anchor «Конец» is unchanged. | F34 |

## 2. Not applied: decisions and open questions for the editor

- **F8 and F10, U050 διάτασις τῶν τρημάτων.** This is the unit's open question. Both checkers recommend «или расширении отверстий» / 'or the widening of the holes'.
  - Theon 66.6–8 Hiller (seen) gives the lower pitch of wind instruments διὰ τὸ μῆκος καὶ τὴν εὐρύτητα τῶν τρημάτων. P's list τοῦ μήκους … τῶν αὐλῶν ἢ τῆς τῶν τρημάτων διατάσεως maps onto it one to one.
  - LSJ, DGE and Bailly give 'dilatation' (seen).
  - The alternative 'extent [of the pipe] up to the holes' has no lexical support and repeats the length already named.
  - Only the lexical facts and the line reference were added to the note. The rendering and the open item are unchanged.
- **F11, U051 ⟨διὰ⟩ πέντε.** Open question. The checker recommends «значения ⟨квинты⟩» / 'the values of the ⟨fifth⟩', with a note that only διά is supplied. Not applied.
- **F12, U061 ἡ ἁρμονία.** Open question.
  - The checker recommends keeping «гармония» / 'harmony'. It also asks for the preferred reading and its grounds to be stated in note 1: the author names the genus only τὸ ἁρμονικὸν γένος (U053, U054, U060, U063); with the article ἡ ἁρμονία produces all three genera (U054, U055); U060 has ἡ κοινὴ ἁρμονία.
  - I confirmed the internal facts against the Greek.
  - Not added, because stating a preference in the note would settle the open point. The open item stays.
- **F17, U045/U049/U056 «интервальное расстояние».** A glossary rendering, so a question. Recorded in U045 `open`. The note added under F16 documents the current rendering.
- **F9, πεντεκαιδεκάχορδον in the edition (resolved doubts at Bas. 31.4).** Not in the translation: U051 note 4 does not repeat the claim. The checker's corrected wording for the edition:
  - the word is used by Adrastus in Theon (p. 64.5–6 Hiller) for the moderns' fifteen-note scheme, whose compass there is three octaves and a tone (Bullialdus: the double octave);
  - Ptolemy uses it for the fifteen-string kanōn of the double octave (Harm. 3.1 tit.; cf. 2.4);
  - "the usual term" overstates (three attestations in LSJ).
  - The Ptolemy part is of moderate confidence: Düring was not seen.

## 3. Rejected findings

None rejected outright. Partial departures from the wording the checkers proposed:
- **F1.** The addition is kept short and placed before the Nicomachus sentence. «консонанс» is used for συμφωνία (glossary).
- **F4.** «хороший в своём роде» instead of «добротный в своём роде».
- **F6.** Bacchius is «Вакхий» (the bibliography's form), with the full title «Введение в музыкальное искусство» / *Introduction to the Art of Music*. The note also says that both Gaudentius and Bacchius list the genus as ἐναρμόνιον just before, which is the nuance the fact-checker noted for Gaudentius and is also true of Bacchius (§ 21). Bacchius' manuscript sigla are left out.
- **F16.** The note also cites LSJ s.v. διάστασις III (the musical sense "interval"), which the finding did not have.

## 4. Outside U043–U067 (for the editor)

- `edition/section-5.md` (apparatus or resolved doubts at Bas. 30.15) calls Theon pp. 56.9–57.6 Hiller "(Adrastus)". This is wrong for the same reason as F1.
- The `bibliography.json` entry "Jan" lists its authors (Клеонид, «Деление канона», Никомах, Гауденций, [Аристотель], «Проблемы»). U053 now also cites Вакхий / Bacchius from Jan, so «Вакхий» / Bacchius should be added there.
- U037 note 1 has the same mislabel as F25 («калька» / "calque" for «анизохронно / изохронно»). It belongs to the U029–U042 pass. If it is changed there, the two notes match; if not, they now differ.
