# Verification log, U043–U067

I went over `out/U043–U067.json`, and the corrected versions are in `final/`. I checked every unit against:

- its Greek and the edition entries in its packet (with `edition/section-4` to `section-7` where an entry was cut short);
- the reviews and error lists;
- DECISIONS.md;
- the cards it names: P01–P04, P06–P12, L10–L15.

None of the listed errors in the six translations survives in the composed text. Every number and ratio was recomputed:

- 256:243:216:192;
- 5:1 to 5:4;
- 4:1 to 8:7;
- 256/243 ≈ 90.2 cents against 102.0;
- 1 – 256/243 – 32/27 – 4/3;
- the three tetrachord divisions in tones.

All of them are right. The signs ⟨⟨ ⟩⟩ (U044, U050), † † (U050) and ⟨ ⟩ (U051) match the Greek.

Result of `check_composed.py … final`: **67 units checked, 3 problems**.
- U020 is outside this range.
- The two U054 lines are a deliberate exception. They are explained below.

## Changes

| Unit | Lang. | Where | Before | After | Why |
|---|---|---|---|---|---|
| U043 | RU, EN | note 3 | «а «лежащими посередине» (μεταξὺ τούτων κείμενα, U042)» / “describes as “lying between” (μεταξὺ τούτων κείμενα, U042)” | «лежащими посреди них» / “as those “which lie in the midst of these”” | The quotation now matches the U042 rendering it quotes («лежащие посреди них» / 'which lie in the midst of these'). |
| U043 | RU, EN | note 3 | «… Принято судьями 4:1.» / “… Adopted by the judges 4:1.” | deleted | This is an internal process remark that the reader cannot interpret. The note already says that ἐμμέσων is the edition's conjecture. No composed note in U001–U042 cites the judges. |
| U044 | RU, EN | note 4 | «Поэтому пример U041 берёт за основу число 6, и все члены … выходят целыми» / “Hence the example of U041 takes 6 as its base, so that all the terms … are whole numbers” | «Этому отвечает пример U041: при основании 6 все члены … — целые числа» / “The example of U041 accords with this: on the base 6 all the terms … are whole numbers” | The text nowhere says why 6 was chosen. The causal claim was the composer's inference. |
| U045 | RU, EN | note 1 | «Σκοπητέον δὲ ὡς и без οὐ» / “Σκοπητέον δὲ ὡς and without οὐ” | «и, по-видимому, без οὐ» / “and, it seems, without οὐ” | The edition says that the absence of οὐ is “most probably” P's reading as Vincent read it (apparatus, Bas. 29.23–24). It does not say this is certain. |
| U045 | RU, EN | note 2 | «ἐπίτασις, букв. «натягивание» (о струнах); … Об этой паре…» / “ἐπίτασις, lit. “tightening” (of strings); … On the pair…” | adds «противоположность — ἄνεσις, «ослабление»» / “its opposite is ἄνεσις, “slackening”” | The note referred to “the pair” without naming its second member. |
| U046 | RU, EN | note 1 | «у LSJ s.v. ἐπιτέταρτος опечатка: «4:3»» / “LSJ s.v. ἐπιτέταρτος prints “4:3” by a slip” | «в электронном тексте LSJ на Perseus … описка» / “the Perseus text of LSJ … prints “4:3” by a slip” | The slip was verified in the Perseus text (translator A; Claude reviewer). Nobody checked the printed LSJ. |
| U046 | RU, EN | note 2 | opened «Автор считает звуки включительно (U034): квинта охватывает…» / “The author counts…” | opens with the lemma ἣν ἔχει πρὸς τοὺς πρὸ αὐτοῦ συγκρινόμενος | DECISIONS § 4: a note opens with the Greek lemma. The same practice is used in the final U029–U042. |
| U048 | RU | text | «То же самое мы будем понимать и об остальных отношениях.» | «… и относительно остальных отношений.» | «понимать … об» is not idiomatic Russian (B and F have «относительно»). The anchor was adjusted to «остальных отношений». |
| U048 | RU, EN | note 1 | «Обобщение верно лишь отчасти. … Довод автора (U046) держится лишь в том, что…» / “The generalisation holds only in part. … The author’s argument (U046) holds only in that…” | «περὶ τοὺς λοιποὺς τῶν λόγων: само правило (судить об отношении по высоте, а не по числу звуков) верно для всех отношений, но проверка счётом, проведённая для квинты в U046, переносится на другие интервалы лишь отчасти. … Неизменно верно лишь то, что…» / “… the rule itself … holds for all ratios, but the test by counting carried out for the fifth at U046 carries over to the other intervals only in part. … What always holds is that…” | The note said the author's generalisation was only partly true. In fact his rule (pitch, not count) is true for every ratio. Only the counting test does not carry over: it gives 4:3 and 2:1 between non-extreme notes. The arithmetic is unchanged and correct. The note now opens with the lemma. |
| U049 | RU, EN | note 4 | «слова ἀφορότης в словарях нет» / “ἀφορότης is in no lexicon” | «нет в LSJ, Венсан толкует его как «délimitation»» / “is not in LSJ, and Vincent glosses it “délimitation”” | The apparatus checked LSJ only (Bas. 30.21–22). |
| U049 | RU, EN | notes 1, 3, 4 | opened «Фраза почти дословно…», «Длина струны…», «Текст: вместо …» / “The sentence…”, “Length and tension…”, “Text: for …” | open with the lemmas ἐξεύρηνται δὲ οἱ τοιοῦτοι τῶν διαστάσεων λόγοι …; ἀπὸ τῆς ἐξαρτήσεως τῶν βαρῶν; ἢ ἀπὸ τῆς εὐρύτητος τῶν κοιλιῶν | DECISIONS § 4. |
| U050 | EN | text | “constitutes a †both† kind of melody.” | “constitutes †both† kind of melody.” | L13 a gives EN '†both†'. 'A †both† kind' is the English of option b (Sol; D, F), which the editor rejected. The Russian «образует †и то и другое† вид мелодии» already followed option a. |
| U050 | RU, EN | note 1 | opened «Абзац есть только в P…» / “This paragraph is found only in P…” | opens with the lemma Ἰστέον δὲ ὡς … | DECISIONS § 4. |
| U050 | RU, EN | note 2 | «Предлагались θάτερον …, ἀμβλύτερον (ближе всего по буквам); ни одно не надёжно, и издание сохраняет кресты (решение 4:1).» / “… have been proposed; … (decided 4:1).” | «В аппарате издания приведены конъектуры θάτερον («другой»), βαρύτερον («более низкий») и ἀμβλύτερον («более глухой»; ближе всего по буквам); ни одна не надёжна, и издание сохраняет кресты.» / EN likewise, with “duller” | The conjectures are the edition's own (apparatus, Bas. 30.23). The passive "have been proposed" suggested earlier scholars. ἀμβλύτερον had no gloss (translator E: 'the duller'). The vote count was removed, as at U043. |
| U050 | RU, EN | note 4 | «или как их удалённость вдоль трубки» / “or their distance along the pipe” | «или как протяжённость [трубки] до отверстий» / “or the extent [of the pipe] up to the holes” | The same note says, rightly, that διάτασις has no sense of "distance". That sense belongs to διάστασις (LSJ, DGE, Bailly, Pape). The second reading is the Claude reviewer's 'extension (length to the hole)'. |
| U051 | RU, EN | note 1 | «… Принято судьями 5:0.» / “… Adopted by the judges 5:0.” | deleted | Same reason as at U043. |
| U052 | RU, EN | note 1 | «рукопись H читает здесь ἐμμέσω; в византийском произношении ἐν μέσῳ и ἐμμέσῳ почти не различаются. В аппарате к этому месту вариант не отмечен; напечатано ἐν μέσῳ.» / EN likewise | «H читает здесь ἐμμέσω, Bas. Par. V — ἐν μέσῳ; … эти формы почти не различаются. Напечатано ἐν μέσῳ.» / EN likewise | The other witnesses' reading has been added. The remark about an inconsistency inside the edition is a matter for the editor, not the reader, so it stays only in `open`, where the composer already put it. |
| U056 | RU, EN | note 2 | «… Ср. Евклид, «Деление канона», 15: кварта меньше двух тонов с половиной.» / “Cf. Euclid, Sectio canonis 15: …” | deleted. Source changed from “U039; Euclid, Sectio canonis 15; calculation” to “U039; calculation” | No packet, card or edition entry gives this proposition or reference (BRIEF: "Do not invent or reconstruct a reference"). The arithmetic 4/3 ÷ (9/8)² = 256/243 makes the point without it. The note now opens with the lemma τὸ λοιπὸν τελεῖν ἡμιτόνιον. |
| U061 | RU, EN | note 1; open | «Издание допускает, что ἡ ἁρμονία здесь — старое название энармонического рода …, но глагол … говорят скорее о гармонии вообще» / “The edition suggests that ἡ ἁρμονία may here be…” | «Издание считает весьма вероятным, что ἡ ἁρμονία здесь — старое название самого энармонического рода …, на что наводит предшествующее рассуждение о производном названии (U060). Но глагол «упорядочивает» и связь с U053, где гармония упорядочивает системы для всех трёх родов, говорят скорее о гармонии вообще; перевод «гармония» допускает оба понимания.» / EN likewise | The edition (section 7, alternatives for translation at Bas. 32.21) says “very probably”, which is stronger than “suggests”. The composer's contrary reasoning is sound and is kept. The text «гармония» / 'harmony' needs no change. |
| U063 | RU, EN | note 1 | «превосходная степень слова, которого нет в словарях» / “a word not recorded in the lexica” | «… не отмеченного в LSJ и DGE» / “… not recorded in LSJ or DGE” | Only LSJ and DGE were checked (translators A and E). |
| U066 | RU, EN | note 3 | «ἐπαφή, «касание», в том числе струн лиры» / “including on the strings of the lyre” | «в том числе о касании лиры» / “including the touching of the lyre” | LSJ cites ἐπαφαὶ μουσικαὶ τῆς λύρας ('of the lyre'), not 'the strings of the lyre'. |

U047, U053, U055, U057–U060, U062, U064, U065 and U067 are unchanged.

## Checked and left as composed

- **U054: Greek in the running text, flagged by the checker.** I kept (διὰ τόνων) and (διάτονον). The sentence derives the name: τὸ διάτονον οὕτω καλούμενον right after διὰ τόνων. DECISIONS § 2 allows Greek "anywhere else the author's argument turns on the word itself, i.e. he explains or derives a name". In translation the link between 'through tones' and 'diatonic' cannot be seen without the Greek. U053 and U060 (harmonic ← harmony) need no Greek, because there the link can be seen. The checker's fixed list (U033, U035) does not know this clause. The composer's question to the editor stays in `open`.
- **U046: scope of οὐ.** RU «полуторным [3:2] оказывается не по превышению…» and EN 'does not appear hemiolic [3:2] in respect of the excess…' both render οὐ πρὸς τὴν ὑπεροχὴν … φαίνεται ἡμιόλιος. They say the same thing: by the count of notes the fifth is not 3:2, and U047 says by what it is. L11 b «[пятый звук]» and the DECISIONS wording of the ratio clause are followed exactly.
- **U051: «[интервала] ⟨через⟩ пять [то есть квинты]».** This keeps the sign on the supplied διά only, as all three reviewers recommend. P01 (квинта) is satisfied by the bracketed gloss. The composer's question stays.
- **U058: punctuation and the subject of συγκεκραμένον.** This follows the editor's decision of 31.10.2026 (H and V). The note gives the alternative with the edition's references.
- **U060: Theon's verb.** «получив имя всего слаженного» / 'having taken the name of all that is attuned' uses the same verb as the text, as DECISIONS (P12) requires.
- **U057: «так называемый диатонический род».** Neutral in Russian terminological prose; kept.
- **DECISIONS terms and notes.** I checked all of these:
  - ratio names with brackets at every occurrence (U046, U047);
  - P02 names and the cross-reference at U051;
  - P06 at U051;
  - P09 at U043–U044, with ἐγγὺς φθόγγοι as «соседние звуки»;
  - P10 at U051;
  - P11 at U058;
  - P07 '(μέλος)' at U054 and U065;
  - P08 (U045, U047, U049, U050);
  - P12 (U053, U060);
  - ἀπαρτίζω (U054, U056, U057);
  - L10–L15.
