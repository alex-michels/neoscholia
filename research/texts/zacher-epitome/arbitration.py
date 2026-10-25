"""Arbitration of the model reviews of the Zacher Epitome, Book I (version 0.1).

Inputs (this folder): source/book1.la.json, drafts/draft-{A,B}.json, reviews/review-*.json,
context.json, raw/text-check.json.
Outputs:
  translation/book1.json          — the reviewed version 0.1 (Latin, RU, EN, notes, review log)
  review/book1-for-review.md      — the same for an external reviewer (Codex / GPT)
  ../../../src/_data/texts/zacher-1.json — data for the site page
  arbitration-log.md              — every review issue with the decision and the reason
Run: python -I arbitration.py
"""
import html
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", newline="\n")
HERE = Path(__file__).resolve().parent
SITE_DATA = HERE.parents[2] / "src" / "_data" / "texts" / "zacher-1.json"
VERSION, DATE = "0.1", "25.10.2026"
MODELS = {"draft": "Claude Opus 5.5", "r1": "Claude Sonnet 5.5", "r2": "Claude Fable 5.1", "arb": "Claude Opus 5.5"}


def load(p):
    return json.loads((HERE / p).read_text(encoding="utf-8"))


latin = {c["chapter"]: c for c in load("source/book1.la.json")}
segs = {}
for h in "AB":
    for s in load(f"drafts/draft-{h}.json")["segments"]:
        segs[s["chapter"]] = s
context = load("context.json")
textcheck = {c["chapter"]: c for c in load("raw/text-check.json")["chapters"]}
parallels = {p["chapter"]: p for p in context["parallels"]}

# ---------- 1. Base text: corrections from the check against the printed edition (Zacher 1867) ----------
LATIN_FIXES = [
    (2, "quaecumque", "quaecunque", "print spelling (TEI normalised it)"),
    (18, "Nam: „Ave, inquit,", "Nam: „Ave,“ inquit,", "closing quotation mark missing in the TEI"),
    (10, "in sinum mulieris extendit", "in sinum mulieris [clementius] extendit", "Zacher prints the word in square brackets as spurious; the TEI dropped it"),
    (36, "lusitatio tunc congruat", "lusitatio tuae congruat", "transcription error: the print has 'tuae'"),
    (38, "quam vis tu", "quamvis tu", "the print has one word"),
]
for ch, old, new, why in LATIN_FIXES:
    t = latin[ch]["latin"]
    assert old in t, (ch, old)
    latin[ch]["latin"] = t.replace(old, new, 1)

# ---------- 2. Decisions on the review issues ----------
# key: (review file tag, issue index) -> (decision, reason, [(chapter, field, old, new), ...])
# field: "ru" | "en" | ("note", i, "ru"|"en"|"source") | ("doubt", i)
D = {}
def dec(tag, i, decision, reason, *edits):
    D[(tag, i)] = (decision, reason, list(edits))

dec("A-r1", 0, "частично", "Отклонено отождествление с Нектанебом: «Qui» естественно относится к только что названному Alexandro, а слова «iamque se in hisce doctum perpenderet» («уже считал себя в этом сведущим») описывают ученика после урока, не мастера-астролога; «Alexander» в главном предложении названо заново ради противопоставления «hominem». Принято снять добавленное притяжательное «его». Место вынесено на внешнюю рецензию.",
    (14, "ru", "И пока тот прилежно пользовался его знанием этого искусства и уже считал себя в нём учёным", "И пока тот [Александр] усердно пользовался знанием этого искусства и уже считал себя в нём сведущим"))
dec("A-r1", 1, "частично", "См. предыдущее: подлежащее — Александр; притяжательное снято.",
    (14, "en", "And while [Alexander] was eagerly enjoying his expertise in this art", "And while [Alexander] was eagerly enjoying the expertise of this art"))
dec("A-r1", 2, "принято", "virginal — наружные половые органы, не матка; в RU «лоно» допустимо.",
    (8, "en", "cover the woman’s womb with papyrus and seal it with a gold ring", "cover the woman’s private parts with papyrus and seal them with a gold ring"),
    (8, "en", "For your seeing the woman’s womb sealed", "For your seeing the woman’s private parts sealed"))
dec("A-r1", 3, "принято с изменением", "Разведены horoscopus (знак асцендента) и constellatio (расположение светил при рождении); вместо «натальной карты» выбрано «расположение светил».",
    (4, "ru", "И Нектанеб тотчас обращается к своему собственному гороскопу", "И Нектанеб тотчас обращается к собственному расположению светил"),
    (4, "en", "And at once Nectanebo brings in his own horoscope", "And at once Nectanebo brings in his own nativity"),
    (4, "ru", "семь светил и гороскоп,", "семь светил и гороскоп [знак асцендента],"),
    (4, "en", "and likewise the horoscope,", "and likewise the horoscope [the marker of the ascendant],"),
    (4, ("note", 1, "ru"), "«свой гороскоп» (suam constellationem)", "«собственное расположение светил» (suam constellationem)"),
    (4, ("note", 1, "en"), "‘his own horoscope’ (suam constellationem)", "‘his own nativity’ (suam constellationem)"))
dec("A-r1", 4, "принято", "longe celebratior — сравнительная степень.",
    (4, "ru", "был уже весьма знаменит", "был уже гораздо более известен"))
dec("A-r1", 5, "принято", "metalli species — «материал», а не «камень».",
    (4, "ru", "и у каждого из них был свой особый камень", "и у каждого из них был свой особый материал"),
    (4, "en", "each of which had its own kind of stone", "each of which had its own kind of material"))
dec("A-r1", 6, "принято", "pretiosae opes — ценное имущество вообще.",
    (3, "ru", "собрав все драгоценности, какие у него были", "собрав всё ценное имущество, какое у него было"))
dec("A-r1", 7, "принято", "«perhaps» не имеет соответствия в латыни.",
    (10, "en", "Jupiter perhaps, from the eagle, or Ammon, from the serpent.", "either Jupiter, judging from the eagle, or Ammon, judging from the serpent."))
dec("A-r1", 8, "принято", "regalius, competentius — сравнительные степени.",
    (13, "ru", "После этого его растили по-царски и как подобало.", "После этого его воспитывали уже более по-царски и более подобающим образом."))
dec("A-r1", 9, "принято", "erat — прошедшее время упрёка; noveras — плюсквамперфект.",
    (14, "en", "It is the art which you knew that you ought to complain of.", "You ought to have complained about the art that you had known."))

dec("A-r2", 0, "принято", "Замечание Цахера относится только к Лаомедонту; Пегас есть в β и в армянской версии (Stoneman–Gargiulo 2007).",
    (13, ("note", 0, "ru"), "У Валерия коня приводят конюхи самого Филиппа, а сравнения с Пегасом и конями Лаомедонта и «звериный порок» — латинские добавления (Цахер: «эта фраза отсутствует в греческих текстах»).",
     "У Валерия коня приводят конюхи самого Филиппа. Сравнений с Пегасом и конями Лаомедонта в A нет, но Пегас есть в β (L B C: κάλλει διαφέροντα τοῦ Πηγάσου), а Пегас и кобылицы Лаомедонта — в армянской версии, так что оба сравнения восходят к греческому источнику; замечание Цахера «вся эта фраза отсутствует в греческих текстах ALBC» касается лишь придаточного о конях Лаомедонта. Греческого соответствия не имеет только «звериный порок» (vitium beluile): в α конь просто «людоед» (ἀνθρωποφάγον)."),
    (13, ("note", 0, "source"), None, "; Stoneman–Gargiulo 2007, comm. ad 1.13"))
dec("A-r2", 1, "принято", "То же для английского примечания.",
    (13, ("note", 0, "en"), "In Valerius the horse is brought by Philip’s own grooms, and the comparisons with Pegasus and Laomedon’s horses and the ‘beastly vice’ are Latin additions (Zacher: ‘this phrase is absent from the Greek texts’).",
     "In Valerius the horse is brought by Philip’s own grooms. The comparisons with Pegasus and Laomedon’s horses are missing in A, but β (L B C) has Pegasus (κάλλει διαφέροντα τοῦ Πηγάσου) and the Armenian version has both Pegasus and Laomedon’s mares, so both go back to the Greek source; Zacher’s remark that ‘this whole phrase is absent from the Greek texts ALBC’ concerns only the clause about Laomedon’s horses. Only the wording ‘beastly vice’ (vitium beluile) has no Greek counterpart: in α the horse is simply ‘man-eating’ (ἀνθρωποφάγον)."))
dec("A-r2", 2, "принято", "Слова «как отцу ребёнка» есть уже в α 1.6; β отличается только глаголом.",
    (6, ("note", 0, "ru"), "(«patris adfectum»; в β, по аппарату Кролля, — «как к отцу ребёнка»)",
     "(«patris adfectum»; уже в греческом α 1.6 Олимпиада обещает «хвалиться тобой как отцом ребёнка» — καυχήσομαι δέ σε ὡς καὶ πατέρα τοῦ παιδός, в β — χρήσομαι, «обращаться с тобой как с отцом ребёнка»)"),
    (6, ("note", 0, "source"), None, "; Stoneman–Gargiulo 2007, comm. ad 1.6"))
dec("A-r2", 3, "принято", "То же для английского примечания.",
    (6, ("note", 0, "en"), "(‘patris adfectum’; in β, according to Kroll’s apparatus, ‘as the father of the child’)",
     "(‘patris adfectum’; already in the Greek α 1.6 Olympias promises to ‘boast of you as the father of the child’, καυχήσομαι δέ σε ὡς καὶ πατέρα τοῦ παιδός; β has χρήσομαι, ‘treat you as the father of the child’)"))
dec("A-r2", 4, "принято", "L — главная рукопись β, а не α.",
    (2, ("note", 1, "ru"), "рукописи A и L греческого α дают ζαλβοί", "рукопись A (α) и лейденская рукопись L (β) дают ζαλβοί"),
    (2, ("note", 1, "en"), "manuscripts A and L of the Greek α have ζαλβοί", "manuscript A (α) and the β manuscript L have ζαλβοί"))
dec("A-r2", 5, "принято", "В α 1.2 докладывает лазутчик (κατάσκοπος), лишь затем названный στρατάρχης.",
    (2, ("note", 0, "ru"), "о нашествии докладывает военачальник,", "о нашествии докладывает лазутчик (κατάσκοπος, «которого римляне называют эксплоратором»; далее он назван στρατάρχης),"),
    (2, ("note", 0, "en"), "the invasion is reported by a commander,", "the invasion is reported by a scout (κατάσκοπος, ‘whom the Romans call explorator’; he is then called στρατάρχης),"))
dec("A-r2", 6, "принято", "«Ночь» перенесена из более поздней фразы Валерия; добавлена только насмешка.",
    (14, ("note", 0, "ru"), "Добавлены «однажды ночью» и насмешка «теперь, лёжа навзничь».",
     "Слова «однажды ночью» перенесены сюда из более поздней фразы Валерия («Nam et nox erat et secreta, quo venerant»); насмешка «теперь, лёжа навзничь» — добавление эпитомы (Кюблер в аппарате: «nunc resupinus iacens rimare Epit.»)."),
    (14, ("note", 0, "en"), "Added are ‘one night’ and the taunt ‘now, lying on your back’.",
     "The words ‘one night’ are brought forward from a later sentence of Valerius (‘Nam et nox erat et secreta, quo venerant’); the taunt ‘now, lying on your back’ is an addition of the epitome (Kübler’s apparatus: ‘nunc resupinus iacens rimare Epit.’)."))
dec("A-r2", 7, "принято", "Добавлены предыдущая фраза Валерия и параллель α 1.6.",
    (6, ("note", 1, "ru"), "это может быть и порча «dei mox», и переосмысление.",
     "это может быть и порча «dei mox», и стяжение с предыдущей фразой Валерия («Aderit tamen ipse etiam ad te deus»); заметим, что в греческом α 1.6 сам бог «приходит к тебе сначала в виде змея» (γίνεται πρῶτον δράκων), так что чтение эпитомы ближе к греческому."),
    (6, ("note", 1, "en"), "this may be a corruption of ‘dei mox’ or a deliberate reinterpretation.",
     "this may be a corruption of ‘dei mox’ or a conflation with Valerius’ preceding sentence (‘Aderit tamen ipse etiam ad te deus’); note that in the Greek α 1.6 the god himself ‘comes to you first as a serpent’ (γίνεται πρῶτον δράκων), so the epitome’s wording is actually closer to the Greek."))
dec("A-r2", 8, "принято", "Слово валериевское (1,6), а не глосса.",
    (10, ("note", 0, "ru"), "вероятно, это глосса, предвосхищающая «mansuetius», и мы переводим без него.",
     "слово есть у Валерия в 1,6 («draco clementius reptabundus», Кюблер, с. 5), откуда оно, вероятно, и попало сюда; мы переводим без него."),
    (10, ("note", 0, "en"), "it is probably a gloss anticipating ‘mansuetius’, and we translate without it.",
     "the word occurs in Valerius 1,6 (‘draco clementius reptabundus’, Kübler p. 5), from where it probably intruded here; we translate without it."))
dec("A-r2", 9, "принято", "ex admiratione — причинное значение.",
    (10, "en", "Then Philip, cheered out of his amazement, said:", "Then Philip, gladdened by his amazement, said:"))
dec("A-r2", 10, "принято", "Согласование времён в английском.",
    (7, "en", "He laid aside the sceptre, climbed onto the bed and consummates the marriage.", "He lays aside the sceptre, climbs onto the bed and consummates the marriage."))
dec("A-r2", 11, "принято", "Неудачная калька.",
    (7, "en", "and at once gave herself to the bed", "and at once took to the bed"))
dec("A-r2", 12, "принято", "ex hoste — «из похода», а не «от врага».",
    (4, "en", "when he comes back from the enemy", "when he comes back from the war"))
dec("A-r2", 13, "принято", "Смешение времён в русском.",
    (6, "ru", "зовёт этого человека к себе и рассказала ему видение сна", "зовёт этого человека к себе и рассказывает ему видение сна"))
dec("A-r2", 14, "принято", "По глоссарию: «горный хрусталь».",
    (4, "ru", "Солнце — хрусталём", "Солнце — горным хрусталём"))
dec("A-r2", 15, "принято", "Кавычки отмечают ложный этноним, как в глоссарии.",
    (13, "ru", "тот самый Аристотель Милетский", "тот самый Аристотель „Милетский“"),
    (13, "en", "the famous Aristotle of Miletus", "the famous Aristotle ‘of Miletus’"))

dec("B-r1", 0, "принято", "В английском местоимение двусмысленно.",
    (18, "en", "And he did not return the greeting.", "And Alexander did not return the greeting."))
dec("B-r1", 1, "принято", "eius — статуя Филиппа (у Валерия paternae statuae).",
    (25, "en", "climbing onto his statue", "climbing onto Philip’s statue"),
    (25, "ru", "его статую", "статую Филиппа"))
dec("B-r1", 2, "принято", "praescivisset — знал заранее; monitu — предостережение.",
    (34, "ru", "узнав по внушению богов о крушении своего счастья", "заранее узнав по предостережению богов о крушении своего счастья"))
dec("B-r1", 3, "принято", "primates — знать, вельможи.",
    (35, "ru", "тирийские старейшины", "тирийские вельможи"))
dec("B-r1", 4, "принято", "inter eos — «среди них».",
    (38, "ru", "долго и тяжко служил у них некоему", "среди них долго и тяжко служил некоему"))
dec("B-r1", 5, "принято", "o viri — «мужи».",
    (17, "ru", "Друзья, ржание ли поразило мой слух", "Мужи, ржание ли поразило мой слух"))
dec("B-r2", 0, "принято", "Чтение Миланской рукописи Цахер знал по печати Маи; Кюблер разночтения не отмечает.",
    (38, ("note", 1, "en"), "*", "‘Consitum’ (‘planted’, here ‘furnished’) stands in all Epitome manuscripts and, according to Zacher (who relied on Mai’s printed text), also in the Milan manuscript of Valerius; but Kübler, who collated that manuscript, prints ‘confisum’ (‘relying on’, Müller’s reading) and records no variant there, so ‘consitum’ may be Mai’s error. The Greek has ‘elated by such power’. The translation (‘furnished with such forces’) suits both readings."))
dec("B-r2", 1, "принято", "То же для русского примечания.",
    (38, ("note", 1, "ru"), "*", "«Consitum» («засаженный», здесь «снабжённый») стоит во всех рукописях эпитомы и, по Цахеру (опиравшемуся на печатный текст Маи), в Миланской рукописи Валерия; но Кюблер, сверявший эту рукопись, печатает «confisum» («полагающийся на силы», чтение Мюллера) и никакого разночтения здесь не отмечает, так что «consitum», возможно, ошибка Маи. В греческом — «превознесённый такой мощью». Перевод («при стольких силах») подходит к обоим чтениям."))
dec("B-r2", 2, "принято", "Страницы Кролля: 54–61.",
    (46, ("note", 1, "source"), "Ps.-Call. α 1.46a (Kroll 1926, pp. 61–62)", "Ps.-Call. α 1.46–46a (Kroll 1926, pp. 54–61)"))
dec("B-r2", 3, "принято", "Чтение Амброзианского кодекса по коллации Кюблера.",
    (20, ("doubt", 0), "*", "‘consortio’ is cited from the Turin palimpsest (Zacher’s Va; Kübler’s T); H L B D E read ‘consilio’ (‘her counsel’), Epitome A ‘connubio’. Zacher also gives ‘connubio’ for the Ambrosianus of Valerius (his Vb, from Mai’s print), but Kübler’s collation has ‘consilio’ there with a marginal ‘vel coniugio’."))
dec("B-r2", 4, "принято", "Объяснение имени коня у Валерия двоякое.",
    (15, ("note", 0, "ru"), "(на бедре у него было случайное клеймо, похожее на бычью голову)", "(не только грозным, словно рогатым, лбом, но и случайным клеймом на бедре, похожим на бычью голову)"),
    (15, ("note", 0, "en"), "(a chance brand on its haunch looked like a bull’s head)", "(not only its fearsome, horn-like brow, but a chance brand on its haunch that looked like a bull’s head)"))
dec("B-r2", 5, "принято", "Сиглы Цахера пояснены.",
    (17, ("note", 1, "ru"), "У Юлия Валерия (Va, Vc) — «evitatis»", "У Юлия Валерия (Туринский палимпсест и Парижская рукопись, у Цахера Va и Vc) — «evitatis»"),
    (17, ("note", 1, "en"), "Julius Valerius (Va, Vc) has ‘evitatis’", "Julius Valerius (the Turin palimpsest and the Paris manuscript, Zacher’s Va and Vc) has ‘evitatis’"))
dec("B-r2", 6, "принято", "«ad comprehendendum» — только в D.",
    (21, ("doubt", 2), "*", "Gerundive without ‘ad’ (D: ‘ad comprehendendum irruerat’; Valerius likewise has ‘ad comprehendendum’)."))
dec("B-r2", 7, "принято", "Совпадает с замечанием B-r1 #5 (уже внесено).")
dec("B-r2", 8, "принято", "apud illos — коринфяне.",
    (47, "en", "a solemn contest was being held among the people", "a solemn contest was being held among them"))
dec("B-r2", 9, "принято", "Неидиоматично по-русски.",
    (42, "ru", "пишет Скамандру, военачальнику своей стороны", "пишет Скамандру, одному из своих военачальников"))


def esc(t):
    return html.escape(t, quote=False)


def apply(ch, field, old, new):
    s = segs[ch]
    if field in ("ru", "en"):
        assert old in s[field], (ch, field, old)
        s[field] = s[field].replace(old, new, 1)
    elif field[0] == "note":
        _, i, lang = field
        n = s["notes"][i]
        if lang == "source":
            n["source"] = (n.get("source", "") + new) if old is None else n["source"].replace(old, new)
        elif old == "*":
            n[lang] = new
        else:
            assert old in n[lang], (ch, field, old)
            n[lang] = n[lang].replace(old, new, 1)
    elif field[0] == "doubt":
        s["doubts"][field[1]]["issue"] = new


reviews = {}
for p in sorted((HERE / "reviews").glob("review-*.json")):
    tag = p.stem.replace("review-", "")
    reviews[tag] = load(p.relative_to(HERE))
log_rows = []
for tag, r in reviews.items():
    for i, x in enumerate(r["issues"]):
        decision, reason, edits = D[(tag, i)]
        for e in edits:
            apply(*e)
        log_rows.append((x["chapter"], tag, i, x, decision, reason))

# ---------- 3. Review log per chapter, notes numbering ----------
SEV = {"critical": "критическое", "major": "существенное", "minor": "малое"}
CAT = {"mistranslation": "ошибка перевода", "omission": "пропуск", "addition": "добавление", "grammar-of-latin": "латинская грамматика",
       "names-terms": "имена и термины", "fluency": "гладкость", "style": "стиль", "note-fact": "факт в примечании"}
LANG = {"ru": "RU", "en": "EN", "both": "RU и EN", "note": "примечание"}
chapters = []
note_no = 0
for ch in sorted(segs):
    s = segs[ch]
    p = parallels.get(ch, {})
    notes = []
    for n in s["notes"]:
        note_no += 1
        notes.append({"n": note_no, "ru": n["ru"], "en": n["en"], "source": n.get("source", "")})
    log = [{"role": "Черновик", "who": MODELS["draft"], "text": f"Перевод с латыни на русский и английский; примечаний: {len(notes)}; отмеченных трудных мест: {len(s['doubts'])}."}]
    rows = sorted((row for row in log_rows if row[0] == ch), key=lambda r: (r[1][-2:], r[1], r[2]))
    no = {(r[1], r[2]): k for k, r in enumerate(rows, 1)}
    for tag, label, model in (("r1", "Рецензия: точность", MODELS["r1"]), ("r2", "Рецензия: язык и примечания", MODELS["r2"])):
        mine = [r for r in rows if r[1].endswith(tag)]
        text = "<br>".join(f"<b>{no[(t, i)]}.</b> {SEV[x['severity']]} · {CAT.get(x['category'], x['category'])} · {LANG[x['lang']]}. {esc(x['problem'])}"
                           for _, t, i, x, _, _ in mine) or "Замечаний нет."
        log.append({"role": label, "who": model, "text": text})
    if rows:
        log.append({"role": "Арбитраж", "who": MODELS["arb"],
                    "text": "<br>".join(f"<b>{no[(t, i)]}.</b> <i>{d}</i>. {esc(why)}" for _, t, i, _, d, why in rows)})
    log.append({"role": "Внешняя рецензия", "who": "модель другого семейства", "text": "Ожидается (GPT через Codex).", "pending": True})
    log.append({"role": "Редактор", "who": "Редакция Neoscholia", "text": "Ожидает проверки.", "pending": True})
    para = []
    if p.get("jv", "").startswith("No independent"):
        para.append("у Юлия Валерия не сохранилось")
    elif p.get("jv"):
        para.append("Юлий Валерий " + p["jv"].split(" (")[0].replace("Iul. Val. ", ""))
    if p.get("ps_call_alpha"):
        para.append(p["ps_call_alpha"].split(" (")[0].replace("Ps.-Call. ", "Псевдо-Каллисфен "))
    chapters.append({
        "chapter": ch,
        "pages": textcheck.get(ch, {}).get("pages", "").replace("pp. ", "с. ").replace("p. ", "с. ").split(" (")[0].replace("-", "–"),
        "parallels": para,
        "latin": latin[ch]["latin"],
        "ru": s["ru"], "en": s["en"],
        "notes": notes, "doubts": s["doubts"], "log": log,
    })

# ---------- 4. Write outputs ----------
(HERE / "translation").mkdir(exist_ok=True)
(HERE / "translation" / "book1.json").write_text(json.dumps({"version": VERSION, "date": DATE, "models": MODELS, "latin_fixes": LATIN_FIXES, "chapters": chapters}, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")

md = [f"# Iulii Valerii Epitome (Zacher Epitome), Book I — version {VERSION} for review\n",
      "Latin: J. Zacher (Halle 1867) via the CC0 TEI of G. Siemoneit, corrected against the print where noted. "
      "Russian and English: drafted by Claude Opus 5.5, reviewed by Claude Sonnet 5.5 and Claude Fable 5.1, arbitrated. "
      "Margin notes are numbered across the book. "
      "Corrections of the TEI against the print: " + "; ".join(f"ch. {c}: '{o}' → '{n}'" for c, o, n, _ in LATIN_FIXES) + ". "
      "How each issue of the earlier reviews was decided: ../arbitration-log.md.\n"]
for c in chapters:
    pe = parallels.get(c["chapter"], {})
    jv = "Julius Valerius lost here" if pe.get("jv", "").startswith("No independent") else pe.get("jv", "").split(" (")[0]
    ref = "; ".join(x for x in (jv, pe.get("ps_call_alpha", "").split(" (")[0]) if x)
    md.append(f"\n## Chapter {c['chapter']}  (Zacher pp. {c['pages'].replace('с. ', '')}; {ref})\n")
    md.append(f"**Latin**\n\n{c['latin']}\n")
    md.append(f"**Russian**\n\n{c['ru']}\n")
    md.append(f"**English**\n\n{c['en']}\n")
    if c["notes"]:
        md.append("**Margin notes**\n")
        for n in c["notes"]:
            md.append(f"- [{n['n']}] RU: {n['ru']}\n  EN: {n['en']}\n  (source: {n['source']})")
    if c["doubts"]:
        md.append("\n**Translator's doubts**\n")
        for d_ in c["doubts"]:
            md.append(f"- {d_['latin']} — {d_['issue']} Choice: {d_['choice']}")
(HERE / "review" / "book1-for-review.md").write_text("\n".join(md) + "\n", encoding="utf-8", newline="\n")

rows_md = ["# Арбитраж рецензий: эпитома Цахера, кн. I, версия 0.1\n",
           f"Черновик — {MODELS['draft']}; рецензии — {MODELS['r1']} (точность) и {MODELS['r2']} (язык и примечания); арбитраж — {MODELS['arb']}.\n",
           "| Гл. | Рецензия | Серьёзность | Что | Решение | Почему |", "|---|---|---|---|---|---|"]
for ch, tag, i, x, decision, reason in sorted(log_rows, key=lambda r: (r[0], r[1], r[2])):
    prob = x["problem"].replace("|", "/").replace("\n", " ")
    rows_md.append(f"| {ch} | {tag} #{i} | {x['severity']} | {prob[:160]}{'…' if len(prob) > 160 else ''} | {decision} | {reason.replace('|', '/')} |")
rows_md.append("\nИсправления латинского текста по печатному изданию: " + "; ".join(f"гл. {c}: «{o}» → «{n}» ({w})" for c, o, n, w in LATIN_FIXES) + ".")
(HERE / "arbitration-log.md").write_text("\n".join(rows_md) + "\n", encoding="utf-8", newline="\n")

SITE_DATA.parent.mkdir(parents=True, exist_ok=True)
site = json.loads(SITE_DATA.read_text(encoding="utf-8")) if SITE_DATA.exists() else {}
site["chapters"] = [{k: c[k] for k in ("chapter", "pages", "parallels", "latin", "ru", "en", "notes", "log")} for c in chapters]
site["stats"] = {"chapters": len(chapters), "notes": note_no, "issues": len(log_rows),
                 "major": sum(1 for r in log_rows if r[3]["severity"] == "major"),
                 "accepted": sum(1 for r in log_rows if r[4].startswith("принято")),
                 "partly": sum(1 for r in log_rows if r[4] == "частично")}
SITE_DATA.write_text(json.dumps(site, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
print(f"chapters {len(chapters)}, notes {note_no}, issues {len(log_rows)}", site["stats"])
