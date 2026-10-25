"""Static parts of the site page for the Zacher Epitome, Book I (src/_data/texts/zacher-1.json).
The chapters, notes and review logs are written by arbitration.py; this script adds the title,
the introduction, the process block and the footer texts. Run after arbitration.py:
  python -I page.py
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
HERE = Path(__file__).resolve().parent
SITE_DATA = HERE.parents[2] / "src" / "_data" / "texts" / "zacher-1.json"
REPO = "https://github.com/alex-michels/neoscholia/blob/main/research/texts/zacher-epitome/"

INTRO_RU = """
<p>Перед вами анонимное латинское сокращение «Деяний Александра Македонского» (<i lang="la">Res gestae Alexandri Macedonis</i>) Юлия Валерия Александра Полемия. Это латинский перевод греческого «Романа об Александре» Псевдо-Каллисфена (древнейшая редакция α), выполненный в начале IV в. Сокращение принято называть «эпитомой Цахера» по имени первого и пока единственного издателя, германиста Юлиуса Цахера (Галле, 1867).</p>
<p>Время и место создания эпитомы неизвестны. Древнейшие рукописи относятся к началу IX в.: Гаага, Королевская библиотека, 74 J 9, и Лейден, Voss. lat. Q 20. Поэтому привычная датировка VIII–IX вв. даёт лишь нижнюю границу, и текст может быть старше. Предположение о его италийском происхождении оспаривается.</p>
<p>Значение памятника определила его судьба. Полный Юлий Валерий дошёл в немногих неполных свидетелях, а эпитома — примерно в восьмидесяти рукописях; она фактически вытеснила оригинал. Для начальных глав романа она, вместе со своей расширенной оксфордской переработкой, остаётся единственным источником латинского текста. Через эпитому сюжет вошёл в «Историческое зерцало» Винсента из Бове и в хронику Элинана из Фруамона. К ней или к полному Юлию Валерию восходит «Александр» Альберика из Писансона, а через него — немецкая «Песнь об Александре» Лампрехта. По мнению ряда исследователей, эпитомой пользовался и Томас Кентский.</p>
<p>Эпитоматор сократил текст примерно до трети, причём первая книга сохранена полнее остальных. Он держится слов Юлия Валерия, но упрощает лексику и синтаксис. Он опускает подробности сражений, языческие обряды и оракулы, большую часть упоминаний Аммона и всё, что бросает тень на Александра. По выражению Г. Зимонайта, получилась «безобидная редакция» романа. Иногда сокращение меняет смысл. Оскорбительная шутка Лисия на свадьбе Филиппа заменена общей фразой (гл. 21). В рассказе о Павсании Олимпиада, отвергшая его у Юлия Валерия, вдруг оказывается «согласной» (гл. 24); сходная порча есть и в одной из рукописей полного Валерия.</p>
<p>Первая книга охватывает «рождение» Александра в широком смысле:</p>
<ul>
<li>египетская магия Нектанеба и его бегство в Македонию;</li>
<li>обольщение Олимпиады под видом бога Аммона, знамения и рождение Александра;</li>
<li>его воспитание, гибель Нектанеба от руки сына, укрощение Буцефала, состязание в Олимпии;</li>
<li>разлад и примирение родителей, убийство Филиппа Павсанием и воцарение Александра;</li>
<li>поход в Италию, Ливию и Египет, взятие Тира, обмен посланиями с Дарием и первая победа над ним.</li>
</ul>
<p>Завершается книга разрушением Фив и сценой с кулачным бойцом Клитомахом в Коринфе.</p>
<p>Перевод выполнен по изданию Цахера в TEI-транскрипции Г. Зимонайта (лицензия CC0), сверенной с печатным изданием. Нумерация глав принадлежит Цахеру: он разметил текст по главам издания К. Мюллера (1846), общим для Псевдо-Каллисфена и Юлия Валерия. Поэтому номера идут с пропусками (нет глав 16, 27–28, 31–33, 43–45): это главы, которых в эпитоме нет; глав 27–28 нет и у Юлия Валерия. Зато номер главы сразу указывает на соответствующее место Юлия Валерия и греческой редакции α в издании В. Кролля. Эти параллели отмечены над каждой главой.</p>
<p>Необходимы оговорки. Современного критического издания эпитомы нет. Цахер использовал лишь семь из примерно восьмидесяти рукописей, хотя и древнейшие, готовил книгу в спешке и почти не вносил исправлений. Расширенные версии эпитомы (оксфордско-монпельевская, лигницкая) здесь не учитываются. Насколько нам удалось установить, на современные языки эпитома прежде не переводилась. Перевод подготовлен с помощью ИИ и ещё не проверен редактором.</p>
<p>— Александр Михельс, PhD</p>
"""

INTRO_EN = """
<p>This is an anonymous Latin abridgement of the <i lang="la">Res gestae Alexandri Macedonis</i> of Julius Valerius Alexander Polemius, the early fourth-century Latin translation of the Greek <i>Alexander Romance</i> of Pseudo-Callisthenes (its oldest recension, α). It is known as the “Zacher Epitome” after its first and so far only editor, the Germanist Julius Zacher (Halle, 1867).</p>
<p>When and where the Epitome was made is unknown. The oldest manuscripts date from the early ninth century: The Hague, Koninklijke Bibliotheek, 74 J 9, and Leiden, Voss. lat. Q 20. The usual dating to the eighth or ninth century is therefore only a lower limit, and the text may be older. An Italian origin has been proposed and disputed.</p>
<p>The text matters because of what happened to it. The full Julius Valerius survives in a few incomplete witnesses; the Epitome survives in about eighty manuscripts and in practice replaced the original. For the opening chapters of the Romance it remains, together with its expanded Oxford reworking, the only source of the Latin text. Through the Epitome the story reached Vincent of Beauvais’ <i>Speculum historiale</i> and the chronicle of Helinand of Froidmont. Alberic of Pisançon’s <i>Alexandre</i> goes back to it or to the full Julius Valerius, and through Alberic so does Lamprecht’s German <i>Alexanderlied</i>. Several scholars think Thomas of Kent used it as well.</p>
<p>The epitomator cut the text to about a third, keeping the first book more fully than the others. He stays close to Julius Valerius’ wording but simplifies the vocabulary and syntax. He leaves out battle details, pagan rites and oracles, most mentions of Ammon, and anything that casts a shadow on Alexander. G. Siemoneit calls the result a “harmless version” (<i lang="de">Harmlos-Fassung</i>) of the Romance. Sometimes the cuts change the meaning. Lysias’ insulting joke at Philip’s wedding is replaced by a general phrase (ch. 21). In the Pausanias story Olympias, who rejects him in Julius Valerius, suddenly “consents” (ch. 24); a similar corruption occurs in one manuscript of the full Valerius.</p>
<p>Book I covers Alexander’s “birth” in the broad sense:</p>
<ul>
<li>Nectanebo’s Egyptian magic and his flight to Macedonia;</li>
<li>the seduction of Olympias in the guise of the god Ammon, the portents, and Alexander’s birth;</li>
<li>his education, Nectanebo’s death at his son’s hands, the taming of Bucephalus, the contest at Olympia;</li>
<li>the quarrel and reconciliation of his parents, Philip’s murder by Pausanias, and Alexander’s accession;</li>
<li>the campaign to Italy, Libya and Egypt, the capture of Tyre, the exchange of letters with Darius, and the first victory over him.</li>
</ul>
<p>The book ends with the destruction of Thebes and the scene with the boxer Clitomachus at Corinth.</p>
<p>The translation follows Zacher’s edition in G. Siemoneit’s TEI transcription (CC0), checked against the printed edition. The chapter numbers are Zacher’s: he divided the text by the chapters of K. Müller’s edition (1846), which Pseudo-Callisthenes and Julius Valerius share. Hence the gaps (there are no chapters 16, 27–28, 31–33, 43–45): these chapters are absent from the Epitome, and 27–28 are absent from Julius Valerius as well. In return, a chapter number points straight to the matching place in Julius Valerius and in W. Kroll’s edition of the Greek recension α. These parallels are shown above each chapter.</p>
<p>Some caveats. There is no modern critical edition of the Epitome. Zacher used only seven of the roughly eighty manuscripts, although the oldest ones; he prepared the book in haste and made few corrections. The expanded versions of the Epitome (Oxford–Montpellier, Liegnitz) are not considered here. As far as we could establish, the Epitome has not been translated into a modern language before. The translation was prepared with the help of AI and has not yet been checked by an editor.</p>
<p>— Alexander Michels, PhD</p>
"""

PROCESS = f"""
<p>Латинский текст взят из TEI-транскрипции и сверен с изображениями страниц издания Цахера: найдено шесть расхождений, четыре из них влияют на смысл или на чтение и исправлены (гл. 10, 18, 36, 38; в гл. 2 восстановлено написание печати). Для каждой главы собраны параллели у Юлия Валерия (изд. Кюблера, 1888) и в греческой редакции α (изд. Кролля, 1926) и составлен глоссарий имён и терминов.</p>
<p>Черновик перевода на русский и английский и новые схолии написала модель Claude Opus 5.5, отдельно для двух половин книги. Каждую половину проверили две модели: Claude Sonnet 5.5 — точность перевода фраза за фразой, Claude Fable 5.1 — язык и факты в примечаниях. Их замечания свела Claude Opus 5.5: каждое принято, принято частично или отклонено с объяснением. Журнал рецензии открывается под каждой главой; полный список решений — в <a href="{REPO}arbitration-log.md">журнале арбитража</a>, пакет для внешней рецензии — в <a href="{REPO}review/book1-for-review.md">book1-for-review.md</a>.</p>
<p>Версию 0.1 проверила модель другого семейства — GPT-6 Astra (OpenAI, через Codex): 22 замечания к 14 местам, все, кроме девяти мелких правок перевода, — к примечаниям. Самое серьёзное: в схолии 53 Валерию приписывалась игра слов «са-Тирос», которая на деле принадлежит Плутарху. Перед решением каждое спорное место сверено с изданиями Кюблера, Цахера, Кролля, Плутарха и Прайзенданца по изображениям страниц. Принято 20 замечаний, 13 из них с уточнениями; 2 отклонены (гл. 41: «currus» у Валерия — одна колесница Дария). При сверке нашлось ещё шесть ошибок, которых не заметил ни один рецензент, в том числе две в правках версии 0.1; они тоже исправлены и отмечены в журнале.</p>
<p>Перевод прошёл проверку моделями двух семейств, Claude (Anthropic) и GPT (OpenAI). Следующая ступень — проверка редактором.</p>
"""

OPEN = [
    "Гл. 14: «Qui dum sedulo huius artis peritia frueretur» отнесено к Александру. Рецензент Claude Sonnet 5.5 предлагал Нектанеба; GPT-6 Astra и сверка с Валерием (1,14: «non una sedulitas discenti puero cum magistro») поддерживают Александра. Окончательное решение — за редактором.",
    "Гл. 13, схолия 24: армянская версия прочитана моделью по изображению страницы издания 1842 г. Чтение «из Ламоментеа» и его связь с Лаомедонтом нужно сверить с переводом A. M. Wolohojian (1969) или с греческой ретроверсией R. Raabe (1896).",
    "Статья Г. Зимонайта (2023) прочитана через сторонний сайт: издательский сайт требовал проверки «вы не робот». Ссылки на неё нужно сверить с официальным PDF (<a href=\"https://doi.org/10.1515/9783111091679-012\">DOI 10.1515/9783111091679-012</a>).",
    "Французский перевод Юлия Валерия (J.-P. Callu, 2010) и итальянский (G. Berengo, 1851–1852) могут включать начальные главы эпитомы, которыми издатели восполняют утраченное начало Валерия. Мы их не видели, поэтому «первый перевод» — с оговоркой.",
    "Чтения Миланской рукописи Юлия Валерия Цахер знал только по печати Маи, и местами они расходятся с коллацией Кюблера (гл. 20, 38).",
    "Использование эпитомы Томасом Кентским указано по вторичным справкам (G. Cary, 1956) и не проверено.",
    "Тождество рукописи H Цахера («Гаага, № 830») и Den Haag, KB 74 J 9 не проверено.",
]

VERSIONS = [
    {"version": "0.2", "date": "25.10.2026", "text": f"Рецензия GPT-6 Astra (OpenAI): 22 замечания, 20 принято, 2 отклонено. Исправлены схолии 5, 8, 10, 11, 19, 24, 46, 51, 53, 59, 64 и 66 и перевод гл. 6, 11, 22 и 46; ещё шесть ошибок найдено при сверке с изданиями. <a href=\"{REPO}review/external/gpt-6-astra.md\">Рецензия</a> · <a href=\"{REPO}arbitration-log.md\">решения</a>."},
    {"version": "0.1", "date": "25.10.2026", "text": "Первая публикация: черновик Claude Opus 5.5, рецензии Claude Sonnet 5.5 и Claude Fable 5.1, арбитраж 42 замечаний; латинский текст сверен с печатным изданием."},
]


def main():
    site = json.loads(SITE_DATA.read_text(encoding="utf-8"))
    st = site["stats"]
    site.update({
        "title": "Эпитома Юлия Валерия. Книга I",
        "subtitle": "«Эпитома Цахера»: от Нектанеба до разрушения Фив и Коринфа (38 глав)",
        "crumbs": [{"label": "Библиотека", "href": "index.html"}, {"label": "Роман об Александре", "href": "alexander.html"},
                   {"label": "Эпитома Юлия Валерия"}, {"label": "Книга I"}],
        "source": "J. Zacher, Julii Valerii epitome, Halle 1867, с. 1–38; TEI-транскрипция G. Siemoneit, сверенная с печатью",
        "first": "Первый перевод на современные языки — насколько нам удалось установить",
        "refPrefix": "I.",
        "origLang": "la",
        "intro_ru": INTRO_RU.strip(),
        "intro_en": INTRO_EN.strip(),
        "process": {
            "text": PROCESS.strip(),
            "stats": [
                {"value": str(st["chapters"]), "label": "глав, 4771 слово латыни"},
                {"value": str(st["notes"]), "label": "новая схолия на полях"},
                {"value": str(st["issues"]), "label": f"замечания трёх рецензентов: {st['issues_v01']} к версии 0.1, {st['issues_v02']} к версии 0.2"},
                {"value": str(st["accepted"]), "label": f"принято, {st['partly']} — частично, {st['rejected']} отклонено"},
            ],
            "open": OPEN,
        },
        "cite": "Эпитома Юлия Валерия («эпитома Цахера»). Книга I / пер. с лат. и комм.: Александр Михельс. Версия {version}. Neoscholia, 2026. https://alex-michels.github.io/neoscholia/zacher-1.html",
        "licenses": f"<p>Латинский текст: J. Zacher (ed.), <i>Julii Valerii epitome</i>, Halle 1867 — общественное достояние; TEI-транскрипция G. Siemoneit — CC0. Исправления транскрипции по печатному изданию перечислены в <a href=\"{REPO}arbitration-log.md\">журнале арбитража</a>.</p><p>Перевод и новые схолии — CC BY-NC-SA 4.0. Журнал рецензии — CC0.</p>",
        "ai": "<p>Черновик перевода и новые схолии подготовила модель Claude Opus 5.5. Рецензии: Claude Sonnet 5.5 (точность) и Claude Fable 5.1 (язык и примечания) — к версии 0.1; GPT-6 Astra (OpenAI) — к версии 0.2. Арбитраж замечаний и сверку с изданиями провела Claude Opus 5.5 с агентами-проверщиками. Системы ИИ не являются авторами; за текст отвечает редактор, Александр Михельс, PhD.</p>",
        "versions": VERSIONS,
    })
    order = ["title", "subtitle", "crumbs", "source", "first", "refPrefix", "origLang", "intro_ru", "intro_en",
             "process", "versions", "cite", "licenses", "ai", "stats", "chapters"]
    site = {k: site[k] for k in order}
    SITE_DATA.write_text(json.dumps(site, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print("written", SITE_DATA)


main()
