"""Arbitration of the model reviews of the Zacher Epitome, Book I.

Version 0.1: drafts by Claude Opus 5.5, reviews by Claude Sonnet 5.5 and Claude Fable 5.1 (reviews/).
Version 0.2: review by a model of another family, GPT-6 Astra (review/external/).
Version 0.3: the independent translation by GPT-6 Astra (independent/), compared and arbitrated (raw/v03-compare.json).
Each issue gets a decision and a reason; accepted fixes are applied to the drafts in that order.
Inputs (this folder): source/book1.la.json, drafts/draft-{A,B}.json, reviews/review-*.json,
review/external/*.json, context.json, raw/text-check.json.
Outputs:
  translation/book1.json          — the current version (Latin, RU, EN, notes, review log)
  review/book1-for-review.md      — the same for an external reviewer (Codex / GPT)
  ../../../src/_data/texts/zacher-1.json — data for the site page
  arbitration-log.md              — every review issue with the decision and the reason
Run: python -I arbitration.py
"""
import html
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", newline="\n")
HERE = Path(__file__).resolve().parent
SITE_DATA = HERE.parents[2] / "src" / "_data" / "texts" / "zacher-1.json"
VERSION, DATE = "0.3", "25.10.2026"
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


# Links to unauthorised copies are not republished (the project cites legitimate sources only).
UNAUTHORISED = ("studylib.net", "dokumen.pub", "ebin.pub")


def show(t):
    """Escape a reviewer's text for the page; URLs become short links."""
    def link(m):
        url, tail = m.group(1).rstrip(".,;)"), m.group(1)[len(m.group(1).rstrip(".,;)")):]
        if any(d in url for d in UNAUTHORISED):
            return "[ссылка на неавторизованную копию не воспроизводится]" + tail
        return f'<a href="{url}">источник</a>{tail}'
    return re.sub(r"(https?://\S+)", link, esc(t))


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
        s["doubts"][field[1]][field[2] if len(field) > 2 else "issue"] = new
    elif field[0] == "doubt_add":
        s["doubts"].append(new)


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

# ---------- 2b. Version 0.2: review by a model of another family (review/external/) ----------
# Issues are numbered from 1, as in the reviewer's own report. Notes are addressed by their number on the page.
EXTERNAL = {"gpt-6-astra": "GPT-6 Astra · OpenAI"}
NOTE_AT = {}
for ch in sorted(segs):
    for i in range(len(segs[ch]["notes"])):
        NOTE_AT[len(NOTE_AT) + 1] = (ch, i)


def note(n, lang):
    ch, i = NOTE_AT[n]
    return ch, ("note", i, lang)


D2 = {}
def dec2(rev, i, decision, reason, *edits):
    D2[(rev, i)] = (decision, reason, list(edits))

# Each disputed point was checked against Kübler, Zacher, Kroll, Plutarch and Preisendanz before the decision
# (raw/v02-verify.json).
A = "gpt-6-astra"
dec2(A, 1, "принято с изменением", "Текст Валерия здесь утрачен, и Кюблер печатает эпитому (Kübler, conspectus; p. 2 app. к 2,9), так что «om. Val.» у Кролля не свидетельство. Добавлено, что Валерий знает этот оракул: надпись на статуе Нектанеба в 1,34.",
     (*note(5, "ru"), "У Валерия этого оракула здесь нет (Кролль: «om. Val.»).",
      "В эпитоме этого оракула нет. Помета Кролля «om. Val.» (с. 3, к строкам 10–18) здесь не независимое свидетельство: текст Валерия в этом месте утрачен, и Кюблер печатает вместо него эпитому (см. схолию 1). Был ли этот оракул здесь у Валерия, неизвестно; но в 1,34 Валерий приводит его как надпись под статуей Нектанеба (царь вернётся «не старше, а моложе»), и Александру объясняют, что этот оракул был дан египтянам, когда они искали своего царя."),
     (*note(5, "source"), None, "; Kübler 1888, p. 2 app.; Iul. Val. 1,34 (Kübler 1888, p. 44)"))
dec2(A, 2, "принято с изменением", "См. предыдущее.",
     (*note(5, "en"), "This oracle is absent here in Valerius (Kroll: ‘om. Val.’).",
      "The oracle is absent from the Epitome. Kroll’s ‘om. Val.’ (p. 3, on lines 10–18) is not independent evidence here: Valerius’ text is lost at this point, and Kübler prints the Epitome in its place (see note 1). Whether Valerius had the oracle here cannot be known; but in 1,34 he gives it as the inscription beneath Nectanebo’s statue (the king will return ‘not older, but younger’), and Alexander is told that this oracle was given to the Egyptians when they were seeking their king."))
dec2(A, 3, "принято", "Согласование (ошибка внесена при арбитраже версии 0.1).",
     (*note(8, "ru"), "(suam constellationem) остался без объяснения", "(suam constellationem) осталось без объяснения"))
dec2(A, 4, "принято с изменением", "По изданию Прайзенданца (PGM I, 1928, с. 82–89): в рецепте две фигурки из воска (глина — дополнение издателя), имя пишется на груди женской фигурки; ложа, светильников и сока нет. Обобщение о «стандартном наборе» снято.",
     (*note(10, "ru"), "*", "Восковой фигурке с надписанным именем есть параллель в греко-египетских магических папирусах: в любовном привороте PGM IV 296–466 велено вылепить из воска две фигурки, мужскую и женскую, написать на груди женской фигурки имя той, кого привораживают, вместе с именем её матери, и произнести заклинание. Ложа, светильников и травяного сока в этом рецепте нет."),
     (*note(10, "source"), "PGM IV 296–466", "PGM IV 296–466 (Preisendanz 1928, I, pp. 82–89)"))
dec2(A, 5, "принято с изменением", "См. предыдущее.",
     (*note(10, "en"), "*", "A wax figure inscribed with a name has a parallel in the Graeco-Egyptian magical papyri: the erotic binding spell PGM IV 296–466 prescribes modelling two wax figures, a man and a woman, writing on the woman’s breast the name of the woman to be bound, together with her mother’s name, and reciting a spell. The little bed, the lamps and the herbal juice have no counterpart in this recipe."))
dec2(A, 6, "принято", "Смешение времён в английском.",
     (6, "en", "she calls the man to her and told him the vision of the dream.", "she calls the man to her and tells him the vision of the dream."))
dec2(A, 7, "принято с изменением", "Направление отношения верное у рецензента; «due» добавляет оттенок долга, которого нет в adfectus. Непроверенная ссылка на Стоунмена–Гарджуло заменена ссылкой на Кролля.",
     (*note(11, "en"), "but a father’s regard", "but regard for him as a father"),
     (*note(11, "source"), "Kroll 1926, p. 7 app. (β); Stoneman–Gargiulo 2007, comm. ad 1.6", "Ps.-Call. α 1.6 (Kroll 1926, p. 7 with app.)"))
dec2(A, 8, "принято с изменением", "У Плутарха (Alex. 3.1–2) потеря глаза — предсказание дельфийского оракула, о его исполнении Плутарх не говорит. Фраза уточнена целиком.",
     (*note(19, "ru"), "Ср. у Плутарха (Alex. 2.6; 3.2): змей рядом со спящей Олимпиадой охладил к ней Филиппа, и тот будто бы лишился глаза, которым подглядел бога в облике змея.",
      "Ср. у Плутарха (Alex. 2.6; 3.1–2): змей, которого однажды видели рядом со спящей Олимпиадой, охладил к ней Филиппа; после этого видения дельфийский оракул велел Филиппу приносить жертвы Аммону и чтить его больше всех богов и предсказал, что он лишится того глаза, которым подсмотрел в щель двери бога в облике змея на ложе своей жены."),
     (*note(19, "source"), "Plut. Alex. 2.6; 3.2", "Plut. Alex. 2.6; 3.1–2"))
dec2(A, 9, "принято с изменением", "См. предыдущее.",
     (*note(19, "en"), "Compare Plutarch (Alex. 2.6; 3.2): a serpent seen beside the sleeping Olympias cooled Philip towards her, and he is said to have lost the eye with which he spied on the god in serpent form.",
      "Compare Plutarch (Alex. 2.6; 3.1–2): a serpent once seen lying beside the sleeping Olympias cooled Philip towards her; after this apparition the Delphic oracle told Philip to sacrifice to Ammon and revere him above all gods, and foretold that he would lose the eye with which he had spied through the chink of the door on the god, in serpent form, lying with his wife."))
dec2(A, 10, "принято", "visus est — «был виден» (у Валерия egredi visitur, Kübler p. 10); событие подано как увиденное.",
     (11, "ru", "показалось, что из неё вышел змеёныш", "было видно, как из неё вышел змеёныш"))
dec2(A, 11, "принято", "considere с аблативом места — «сесть на» (Verg. Aen. 4.573 considite transtris); «у ложа» передавало adsidensque lectulo Валерия. Добавлено в список трудных мест.",
     (22, "ru", "сев у ложа", "сев на ложе"),
     (22, ("doubt_add",), None, {"latin": "considensque lectulo", "issue": "Valerius has ‘adsidensque lectulo’ (sitting by the sickbed, the usual sense of ‘adsidere’ + dative); the Epitome changed the verb. ‘considere’ with a bare ablative means ‘to sit down on’ (Verg. Aen. 4.573 ‘considite transtris’; cf. ch. 11 ‘considensque’).", "choice": "«сев на ложе» / ‘sitting down on the couch’ (changed in version 0.2 after the GPT-6 Astra review)."}))
dec2(A, 12, "принято", "См. предыдущее.",
     (22, "en", "sitting down by the couch", "sitting down on the couch"))
dec2(A, 13, "принято с изменением", "По изображению страницы Цахера (с. 27–28, аппарат): словами — «octo» в L и «octingentos» в A и B (не в E: OCR читает ABVb как AEYb); Vb — рукопись Валерия, а не эпитомы.",
     (*note(46, "ru"), "В рукописях эпитомы числа записаны римскими цифрами; словами их передал Цахер.",
      "В рукописях эпитомы эти числа записаны большей частью римскими цифрами (словами лишь изредка, например «octo» в L, «octingentos» в A и B); Цахер печатает все числа словами."))
dec2(A, 14, "принято с изменением", "См. предыдущее.",
     (*note(46, "en"), "The Epitome manuscripts give the figures in Roman numerals; Zacher writes them out in words.",
      "The Epitome manuscripts mostly give these figures in Roman numerals (only occasionally in words, e.g. ‘octo’ in L, ‘octingentos’ in A and B); Zacher prints them all in words."))
dec2(A, 15, "принято с изменением", "У Валерия (Kübler p. 47,4–9) во втором сне сатир протягивает сыр (tyrum), Александр его растаптывает, а толкователи предсказывают, что Тир будет попран. Игра «са-Тирос» — у Плутарха (Alex. 24.8–9), в α от неё остался след (Kroll p. 40 app.). Дано толкование сна и происхождение игры слов.",
     (*note(53, "ru"), "Опущены также сон о сатире («са-Тирос») и основание Триполиса из трёх деревень.",
      "Опущены также второй сон Александра и основание Триполиса из трёх деревень. Во сне сатир протягивает Александру сыр (tyrum, греч. τυρός), Александр бросает его и растаптывает, а толкователи объясняют: Тир (Tyrum) скоро будет попран ногами царя. Игра «са-Тирос» (σάτυρος → σὰ Τύρος, «Тир твой») — у Плутарха (Alex. 24, 8–9); в α от неё остался лишь след (Kroll, p. 40, app. к стр. 8)."),
     (*note(53, "source"), "Iul. Val. 1,35 (Kübler 1888, pp. 45–47)", "Iul. Val. 1,35 (Kübler 1888, cap. 35–36, pp. 45–47); Ps.-Call. α 1.35 (Kroll 1926, p. 40 with app.); Plut. Alex. 24.8–9"))
dec2(A, 16, "принято с изменением", "См. предыдущее.",
     (*note(53, "en"), "Also omitted are the dream of the satyr (‘sa-Tyros’) and the founding of Tripolis from three villages.",
      "Also omitted are Alexander’s second dream and the founding of Tripolis from three villages. In the dream a satyr holds out a cheese to him (tyrum, Greek τυρός); Alexander throws it down and tramples it, and the interpreters explain that Tyre (Tyrum) will soon be trampled under the king’s feet. The ‘sa-Tyros’ pun (σάτυρος → σὰ Τύρος, ‘Tyre is yours’) is Plutarch’s (Alex. 24.8–9); α keeps only a trace of it (Kroll, p. 40, app. to l. 8)."))
dec2(A, 17, "принято с изменением", "«При стольких силах» передаёт consitum эпитомы, а не confisum. Попутно смягчена догадка об «ошибке Маи»: consitum стоит во всех рукописях эпитомы (с IX в.), независимых от Маи, так что это старое чтение.",
     (*note(59, "ru"), "Перевод («при стольких силах») подходит к обоим чтениям.",
      "Перевод («при стольких силах») следует чтению эпитомы «consitum»; чтение «confisum» означало бы «полагающийся на такие силы»."),
     (*note(59, "ru"), "так что «consitum», возможно, ошибка Маи.",
      "так что неясно, ошибся ли Маи или Кюблер не отметил разночтения; эпитома во всяком случае показывает, что «consitum» — старое чтение."),
     (38, ("doubt", 0, "choice"), None, "Rendered after the Epitome’s ‘consitum’: ‘furnished with such forces’ / «при стольких силах»; see the note."))
dec2(A, 18, "принято с изменением", "См. предыдущее.",
     (*note(59, "en"), "The translation (‘furnished with such forces’) suits both readings.",
      "The translation (‘furnished with such forces’) follows the Epitome’s reading ‘consitum’; ‘confisum’ would mean ‘relying on such forces’."),
     (*note(59, "en"), "so ‘consitum’ may be Mai’s error.",
      "so it is unclear whether Mai erred or Kübler failed to record the variant; the Epitome at least shows that ‘consitum’ is an old reading."))
dec2(A, 19, "отклонено", "Форма currus — действительно множественное число, но фраза взята у Валерия, где это одна колесница Дария: двумя строками выше «currum quidem … abdendum mandat» (Kübler p. 54), а вся фраза передаёт греческое «τὸ μὲν ἅρμα αὐτοῦ καὶ τὰ τόξα» (α 1.41, Kroll p. 47); ср. Арриан 2.11.6 и Плутарх, Alex. 20.10. Поэтическое множественное, как Verg. Aen. 6.485. Перевод сохранён; в схолию 64 и в список трудных мест добавлено объяснение.",
     (*note(64, "ru"), "в эпитоме он колесницу «потерял».",
      "в эпитоме он колесницу «потерял». Слово «currus», которым названа захваченная затем колесница, — форма множественного числа; она взята у Валерия, который так передаёт греческое «τὸ μὲν ἅρμα αὐτοῦ» («его колесницу», α 1.41)."),
     (*note(64, "en"), "in the Epitome he has ‘lost’ it.",
      "in the Epitome he has ‘lost’ it. The word for the chariot Alexander then captures, ‘currus’, is plural in form; it comes from Valerius, who uses it to render the Greek ‘τὸ μὲν ἅρμα αὐτοῦ’ (‘his chariot’, α 1.41)."),
     (*note(64, "source"), None, "; Ps.-Call. α 1.41 (Kroll 1926, p. 47)"),
     (41, ("doubt", 3, "issue"), None, "‘currus’ is formally accusative plural (all manuscripts; Zacher p. 34 app.). It is copied from Valerius, where it is Darius’ own chariot: just before, Darius orders ‘currum quidem … abdendum’ (Kübler p. 54), and Valerius is rendering α ‘τὸ μὲν ἅρμα αὐτοῦ καὶ τὰ τόξα’ (‘his chariot and his bow’, Kroll p. 47). A poetic plural for one chariot, as in Verg. Aen. 6.485 ‘currus … arma tenentem’."))
dec2(A, 20, "отклонено", "См. предыдущее.")
dec2(A, 21, "принято", "Аппарат о Scamandrum — на с. 35, к строке 2.",
     (*note(66, "source"), "Zacher 1867, p. 34, apparatus", "Zacher 1867, p. 35, apparatus"))
dec2(A, 22, "принято", "fere при числах и сроках — «примерно».",
     (46, "ru", "И так, почти на третий день,", "И так, примерно на третий день,"))

# Found while checking the review (not raised by the reviewer).
FIXES = []
def fix(ch, severity, category, lang, problem, *edits):
    FIXES.append((ch, {"severity": severity, "category": category, "lang": lang, "problem": problem}, list(edits)))

fix(10, "major", "note-fact", "note", "Схолия 19: у Валерия «ne quid omnino coniugali fidei deesset apud eum maritum, cui talis visio proderetur» — fides здесь «достоверность» для мужа, которому явлено зрелище (ср. «quo fidem faceret divino commercio»; в α — τεκμήριον στοργῆς … πρὸς τοὺς θεωμένους); «супружеской верности» передавало обратный смысл. Змей не «касается» Олимпиады, а тянется её поцеловать (osculum adfectat); Филипп отступает «в страхе и изумлении» (Kübler p. 9).",
    (*note(19, "ru"), "У Валерия (1,10) змей ещё ложится Олимпиаде на колени и касается её раздвоенным языком, «чтобы супружеской верности ничего не недоставало», а Филипп отступает в страхе; эпитоматор это выпустил.",
     "У Валерия (1,10) змей ещё усаживается Олимпиаде на колени и, трепеща раздвоенным языком, тянется её поцеловать, «чтобы в глазах мужа, которому явлено такое зрелище, достоверности этого супружества ничего не недоставало» (ne quid omnino coniugali fidei deesset apud eum maritum, cui talis visio proderetur), а Филипп отступает в страхе и изумлении; эпитоматор это выпустил."),
    (*note(19, "en"), "In Valerius (1,10) the serpent also settles on Olympias’ knees and touches her with its forked tongue, ‘so that nothing should be lacking to conjugal fidelity’, while Philip draws back in fear; the epitomator omitted this.",
     "In Valerius (1,10) the serpent also settles on Olympias’ knees and, flickering its forked tongue, tries to kiss her, ‘so that, in the eyes of the husband to whom such a sight was shown, nothing should be lacking to the credibility of the union’ (ne quid omnino coniugali fidei deesset apud eum maritum, cui talis visio proderetur), while Philip draws back in fear and amazement; the epitomator omitted this."))
fix(13, "major", "note-fact", "note", "Схолия 24 (правка версии 0.1): «кобылиц Лаомедонта» в армянской версии нет. По изданию 1842 г. (§ 31) конь превосходит «красотой и быстротой» Пегаса и Ариона и приведён «из Ламоментеа» — вероятно, искажённое имя Лаомедонта; это согласуется с аппаратом Кролля (с. 14: καὶ τάχει, τοῦ Ἀρίονος Arm.). Непроверенная ссылка на Стоунмена–Гарджуло заменена проверенными источниками.",
    (*note(24, "ru"), "Сравнений с Пегасом и конями Лаомедонта в A нет, но Пегас есть в β (L B C: κάλλει διαφέροντα τοῦ Πηγάσου), а Пегас и кобылицы Лаомедонта — в армянской версии, так что оба сравнения восходят к греческому источнику; замечание Цахера «вся эта фраза отсутствует в греческих текстах ALBC» касается лишь придаточного о конях Лаомедонта.",
     "Сравнений с Пегасом и конями Лаомедонта в A нет. Пегас есть в β (L B C: κάλλει διαφέροντα τοῦ Πηγάσου) и в армянской версии: там конь превосходит «красотой и быстротой» Пегаса и Ариона, а привели его, по словам приведших, «из Ламоментеа» — вероятно, это искажённое имя Лаомедонта. Значит, сравнение с Пегасом восходит к греческому источнику, а упоминание Лаомедонта, по-видимому, тоже; замечание Цахера «вся эта фраза отсутствует в греческих текстах ALBC» касается лишь придаточного о конях Лаомедонта."),
    (*note(24, "en"), "The comparisons with Pegasus and Laomedon’s horses are missing in A, but β (L B C) has Pegasus (κάλλει διαφέροντα τοῦ Πηγάσου) and the Armenian version has both Pegasus and Laomedon’s mares, so both go back to the Greek source; Zacher’s remark that ‘this whole phrase is absent from the Greek texts ALBC’ concerns only the clause about Laomedon’s horses.",
     "The comparisons with Pegasus and Laomedon’s horses are missing in A. Pegasus is in β (L B C: κάλλει διαφέροντα τοῦ Πηγάσου) and in the Armenian version, where the horse surpasses Pegasus and Arion ‘in beauty and speed’ and is said to have been brought ‘from Lamomentea’, probably a garbled form of Laomedon’s name. So the Pegasus comparison goes back to the Greek source, and the mention of Laomedon probably does too; Zacher’s remark that ‘this whole phrase is absent from the Greek texts ALBC’ concerns only the clause about Laomedon’s horses."),
    (*note(24, "source"), "Ps.-Call. α 1.13 (Kroll 1926, p. 14); Iul. Val. 1,13 (Kübler 1888, pp. 12–14); Zacher 1867, p. 17 app.; Stoneman–Gargiulo 2007, comm. ad 1.13",
     "Ps.-Call. α 1.13 (Kroll 1926, p. 14 with app.); β: Müller 1846, Ps.-Call. p. 13; Armenian text, Venice 1842, p. 16 (§ 31); Iul. Val. 1,13 (Kübler 1888, pp. 12–14); Zacher 1867, p. 17 app."))
fix(34, "minor", "note-fact", "note", "Схолия 51 предполагала, что у Валерия оракул был в гл. 3; там Валерий утрачен (см. замечание к схолии 5).",
    (*note(51, "ru"), "(как и оракул о возвращении в гл. 3)", "(в гл. 3 эпитомы этого оракула тоже нет)"),
    (*note(51, "en"), "(as he dropped the oracle of the return in ch. 3)", "(the Epitome has no oracle of the return in ch. 3 either)"))
fix(6, "minor", "mistranslation", "en", "«superveniet draco reptabundus» — змей приползёт к ней, а не «по ней» (‘crawling upon you’); ср. русское «к тебе приползёт змей».",
    (6, "en", "a serpent will come crawling upon you", "a serpent will come crawling up to you"))
fix(11, "minor", "mistranslation", "ru", "«Ex quo cum draco erupisse videatur»: «как видно» читается как «по-видимому» и повторяет в малом проблему «показалось» (замечание 10 рецензента).",
    (11, "ru", "И поскольку змей, как видно, вырвался из него,", "И поскольку видели, как змей вырвался из него,"))
fix(14, "minor", "presentation", "note", "Список трудных мест к гл. 14 цитировал перевод до правок версии 0.1.",
    (14, ("doubt", 2, "choice"), None, "Taken as Alexander: «И пока тот [Александр] усердно пользовался знанием этого искусства…» / ‘And while [Alexander] was eagerly enjoying the expertise of this art…’. Both the external reviewer and the check against Valerius 1,14 (‘non una sedulitas discenti puero cum magistro’, Kübler p. 15) support this reading."),
    (14, ("doubt", 4, "choice"), None, "«Тебе следовало пенять на искусство, которое ты знал» / ‘You ought to have complained about the art that you had known’."))

fix_rows = []
for ch, x, edits in FIXES:
    for e in edits:
        apply(*e)
    fix_rows.append((ch, x))

ext_rows, ext_chapters = [], {}
for rev in EXTERNAL:
    r = load(f"review/external/{rev}.json")
    ext_chapters[rev] = {c["chapter"]: c for c in r["chapters"]}
    for i, x in enumerate(r["issues"], 1):
        decision, reason, edits = D2[(rev, i)]
        for e in edits:
            apply(*e)
        ext_rows.append((x["chapter"], rev, i, x, decision, reason))

# ---------- 2c. Version 0.3: the independent translation (independent/draft-*.json) ----------
# GPT-6 Astra translated the Latin in a separate session, without seeing this translation. Five agents
# compared the two chapter by chapter against the Latin, Kübler and Kroll (raw/v03-compare.json); every
# significant divergence got a verdict. One translation is published; a defensible alternative goes into a note.
INDEPENDENT = ("independent/draft-gpt-6-astra-ultra.json", "GPT-6 Astra · OpenAI")
indep = {s["chapter"]: s for s in load(INDEPENDENT[0])["segments"]}
compare = load("raw/v03-compare.json")


def append_note(n, ru, en, source=""):
    ch, i = NOTE_AT[n]
    note_ = segs[ch]["notes"][i]
    note_["ru"] = note_["ru"].rstrip() + " " + ru
    note_["en"] = note_["en"].rstrip() + " " + en
    if source:
        note_["source"] = note_.get("source", "") + "; " + source


def replace_note(n, ru, en, source=""):
    ch, i = NOTE_AT[n]
    note_ = segs[ch]["notes"][i]
    note_["ru"], note_["en"] = ru, en
    if source:
        note_["source"] = source


cmp_rows = []
for r in compare:
    for d in r.get("divergences", []):
        for rp in d["replace"]:
            apply(d["chapter"], rp["lang"], rp["old"], rp["new"])
        if d["action"] in ("note", "replace+note"):
            append_note({41: 64}[d["chapter"]], d["note_ru"], d["note_en"])
        cmp_rows.append(d)
notes_cmp = next(r for r in compare if "additions" in r)
adds = {(a["chapter"], a["target_note_n"]): a for a in notes_cmp["additions"] if a["verdict"] in ("add", "merge")}
# New facts from the independent notes are merged into existing notes, so that the note numbers stay stable.
replace_note(12, adds[(6, 12)]["ru"], adds[(6, 12)]["en"], adds[(6, 12)]["source"])
replace_note(16,
    "В греческом α 1.8 Филипп призывает одного толкователя снов (ὀνειροπόλον), и тот говорит, что папирус растёт «нигде, кроме Египта». У Валерия тоже один толкователь («Tum interpres»), а в эпитоме толкователи (во множественном числе; лишь рукописи L и Vc дают «interpres») говорят «кроме нашей земли», словно сами египтяне. В греческом бог во сне «зашивает» лоно Олимпиады папирусом (καταρράπτειν); отсюда осторожная догадка Цахера в аппарате — «contexere?» («сплести, сшить»). Но рукописи эпитомы и Валерий дают «contegere» («покрыть»), и перевод следует им. Эпитоматор выпустил конец главы Валерия, где объяснено недовольство Филиппа (в тексте Кюблера: он думает, что жена зачала от человека).",
    "In the Greek α 1.8 Philip summons a single dream interpreter (ὀνειροπόλον), who says that papyrus grows ‘nowhere except in Egypt’. Valerius too has one interpreter (‘Tum interpres’), but in the epitome the interpreters (plural; only manuscripts L and Vc read ‘interpres’) say ‘except in our land’, as if they were Egyptians themselves. In the Greek the god in the dream ‘sews up’ Olympias’ womb with papyrus (καταρράπτειν); hence Zacher’s tentative suggestion in his apparatus, ‘contexere?’ (‘to weave, stitch together’). But the epitome manuscripts and Valerius have ‘contegere’ (‘to cover’), and the translation follows them. The epitomator dropped the end of Valerius’ chapter, which explains Philip’s displeasure (in Kübler’s text: he believes his wife conceived by a man).",
    "Ps.-Call. α 1.8 (Kroll 1926, p. 9, ll. 3–4, 7); Iul. Val. 1,8 (Kübler 1888, pp. 7–8 with app.); Zacher 1867, p. 10, app. to l. 14; p. 11, app. to l. 3")
replace_note(25, adds[(13, 25)]["ru"], adds[(13, 25)]["en"], adds[(13, 25)]["source"])
replace_note(47, adds[(26, 47)]["ru"], adds[(26, 47)]["en"], adds[(26, 47)]["source"])
replace_note(71, adds[(47, 71)]["ru"], adds[(47, 71)]["en"], adds[(47, 71)]["source"])
append_note(30, adds[(17, 0)]["ru"], adds[(17, 0)]["en"], adds[(17, 0)]["source"])
append_note(53, adds[(35, 0)]["ru"], adds[(35, 0)]["en"], adds[(35, 0)]["source"])
append_note(68, adds[(46, 0)]["ru"], adds[(46, 0)]["en"], adds[(46, 0)]["source"])
apply(*note(26, "ru"), "речь Филиппа к двенадцатилетнему сыну", "речь Филиппа к сыну, которому шёл двенадцатый год,")
apply(*note(26, "en"), "Philip’s speech to his twelve-year-old son", "Philip’s speech to his son, then in his twelfth year,")
apply(15, ("doubt", 0, "choice"), None, "‘your [dominions]’ / «твои [владения]»: ‘tuis’ is a substantival plural (changed in version 0.3 after the comparison with the independent translation).")
apply(23, ("doubt", 2, "choice"), None, "‘fiercely’ / «жестоко»: ‘acrius’ is an absolute comparative, there has been no earlier battle (changed in version 0.3).")
NOTE_ADDED = {6: [12], 8: [16], 13: [25], 14: [26], 17: [30], 26: [47], 35: [53], 41: [64], 46: [68], 47: [71]}

# ---------- 3. Review log per chapter, notes numbering ----------
SEV = {"critical": "критическое", "major": "существенное", "minor": "малое"}
CAT = {"mistranslation": "ошибка перевода", "omission": "пропуск", "addition": "добавление", "grammar-of-latin": "латинская грамматика",
       "names-terms": "имена и термины", "fluency": "гладкость", "style": "стиль", "note-fact": "факт в примечании",
       "latin-grammar": "латинская грамматика"}
LANG = {"ru": "RU", "en": "EN", "both": "RU и EN", "note": "примечание"}
DIVCAT = {"meaning": "смысл", "construction": "конструкция", "reference": "к чему относится", "omission": "пропуск", "addition": "добавление",
          "names-terms": "имена и термины", "tense-mood": "время и наклонение", "style": "стиль", "note-fact": "примечание"}
VERDICT = {"ours": "верен опубликованный перевод", "theirs": "принят вариант независимого перевода", "both": "допустимы оба прочтения", "neither": "оба неточны, исправлено"}
ACTION = {"keep": "без изменений", "replace": "текст исправлен", "note": "альтернатива вынесена в примечание", "replace+note": "текст исправлен, альтернатива — в примечании"}
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
        log.append({"role": "Арбитраж, версия 0.1", "who": MODELS["arb"],
                    "text": "<br>".join(f"<b>{no[(t, i)]}.</b> <i>{d}</i>. {esc(why)}" for _, t, i, _, d, why in rows)})
    for rev, who in EXTERNAL.items():
        cc = ext_chapters[rev].get(ch, {})
        mine = [r for r in ext_rows if r[0] == ch and r[1] == rev]
        for r in mine:
            no[(r[1], r[2])] = len(no) + 1
        verdict = " · ".join(f"{lang}: {'без замечаний' if cc.get(lang.lower()) == 'ok' else 'есть замечания'}" for lang in ("RU", "EN"))
        text = f"{verdict}.<br>{show(cc.get('comment', ''))}"
        if mine:
            text += "<br>" + "<br>".join(f"<b>{no[(t, i)]}.</b> {SEV[x['severity']]} · {CAT.get(x['category'], x['category'])} · {LANG[x['lang']]}. {show(x['problem'])}"
                                         for _, t, i, x, _, _ in mine)
        log.append({"role": "Рецензия другой модели", "who": who, "text": text})
        if mine:
            log.append({"role": "Арбитраж, версия 0.2", "who": MODELS["arb"],
                        "text": "<br>".join(f"<b>{no[(t, i)]}.</b> <i>{d}</i>. {esc(why)}" for _, t, i, _, d, why in mine)})
    found = [x for c_, x in fix_rows if c_ == ch]
    if found:
        log.append({"role": "Сверка при арбитраже", "who": f"{MODELS['arb']}, агенты-проверщики",
                    "text": "Не отмечено рецензентами, найдено при сверке с изданиями; <i>исправлено</i>.<br>"
                            + "<br>".join(f"{SEV[x['severity']]} · {CAT.get(x['category'], x['category'])} · {LANG[x['lang']]}. {esc(x['problem'])}" for x in found)})
    ind = indep.get(ch, {})
    log.append({"role": "Независимый перевод", "who": INDEPENDENT[1],
                "text": f"Перевод с латыни на русский и английский в отдельной сессии, только по оригиналу; примечаний: {len(ind.get('notes', []))}; отмеченных трудных мест: {len(ind.get('doubts', []))}."})
    mine3 = [d for d in cmp_rows if d["chapter"] == ch]
    lines = [f"<b>{k}.</b> {DIVCAT[d['category']]} · <i lang=\"la\">{esc(d['latin'][:90])}{'…' if len(d['latin']) > 90 else ''}</i> — <i>{VERDICT[d['verdict']]}; {ACTION[d['action']]}</i>. {esc(d['reason'])}"
             for k, d in enumerate(mine3, 1)]
    if NOTE_ADDED.get(ch):
        lines.append("Примечания " + ", ".join(str(n) for n in NOTE_ADDED[ch]) + " дополнены или исправлены по примечаниям независимого перевода (сведения проверены по изданиям).")
    log.append({"role": "Сопоставление, версия 0.3", "who": f"{MODELS['arb']}, агенты-проверщики",
                "text": "<br>".join(lines) if lines else "Существенных расхождений с независимым переводом нет."})
    log.append({"role": "Редактор", "who": "Александр Михельс, PhD", "text": "Ожидает проверки.", "pending": True})
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
      "Russian and English: drafted by Claude Opus 5.5, reviewed by Claude Sonnet 5.5 and Claude Fable 5.1 (version 0.1) "
      "and by GPT-6 Astra (version 0.2), arbitrated; compared with an independent translation by GPT-6 Astra (version 0.3). "
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

rows_md = ["# Арбитраж рецензий: эпитома Цахера, кн. I\n", "## Версия 0.1\n",
           f"Черновик — {MODELS['draft']}; рецензии — {MODELS['r1']} (точность) и {MODELS['r2']} (язык и примечания); арбитраж — {MODELS['arb']}.\n",
           "| Гл. | Рецензия | Серьёзность | Что | Решение | Почему |", "|---|---|---|---|---|---|"]
for ch, tag, i, x, decision, reason in sorted(log_rows, key=lambda r: (r[0], r[1], r[2])):
    prob = x["problem"].replace("|", "/").replace("\n", " ")
    rows_md.append(f"| {ch} | {tag} #{i} | {x['severity']} | {prob[:160]}{'…' if len(prob) > 160 else ''} | {decision} | {reason.replace('|', '/')} |")
rows_md += ["\n## Версия 0.2\n",
            "Рецензия моделью другого семейства: " + ", ".join(f"{w} (`review/external/{r}.json`; номера замечаний — как в рецензии)" for r, w in EXTERNAL.items())
            + f". Арбитраж — {MODELS['arb']}; спорные места перед решением сверены с изданиями Кюблера, Цахера, Кролля и Плутарха (`raw/v02-verify.json`).\n",
            "| Гл. | Рецензия | Серьёзность | Что | Решение | Почему |", "|---|---|---|---|---|---|"]
for ch, rev, i, x, decision, reason in sorted(ext_rows, key=lambda r: (r[0], r[2])):
    prob = x["problem"].replace("|", "/").replace("\n", " ")
    for d in UNAUTHORISED:
        prob = re.sub(r"https?://(www\.)?" + re.escape(d) + r"\S*", "[ссылка на неавторизованную копию]", prob)
    rows_md.append(f"| {ch} | {rev} #{i} | {x['severity']} | {prob[:160]}{'…' if len(prob) > 160 else ''} | {decision} | {reason.replace('|', '/')} |")
rows_md += ["\nНайдено при сверке, рецензентами не отмечено (исправлено):\n", "| Гл. | Серьёзность | Что |", "|---|---|---|"]
rows_md += [f"| {ch} | {x['severity']} | {x['problem'].replace('|', '/')} |" for ch, x in fix_rows]
rows_md.append("\nИсправления латинского текста по печатному изданию: " + "; ".join(f"гл. {c}: «{o}» → «{n}» ({w})" for c, o, n, w in LATIN_FIXES) + ".")
(HERE / "arbitration-log.md").write_text("\n".join(rows_md) + "\n", encoding="utf-8", newline="\n")

SITE_DATA.parent.mkdir(parents=True, exist_ok=True)
site = json.loads(SITE_DATA.read_text(encoding="utf-8")) if SITE_DATA.exists() else {}
site["chapters"] = [{k: c[k] for k in ("chapter", "pages", "parallels", "latin", "ru", "en", "notes", "log")} for c in chapters]
all_rows = log_rows + ext_rows
site["stats"] = {"chapters": len(chapters), "notes": note_no, "issues": len(all_rows),
                 "issues_v01": len(log_rows), "issues_v02": len(ext_rows),
                 "major": sum(1 for r in all_rows if r[3]["severity"] in ("major", "critical")),
                 "accepted": sum(1 for r in all_rows if r[4].startswith("принято")),
                 "partly": sum(1 for r in all_rows if r[4] == "частично"),
                 "rejected": sum(1 for r in all_rows if r[4] == "отклонено")}
SITE_DATA.write_text(json.dumps(site, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
print(f"version {VERSION}", site["stats"])
