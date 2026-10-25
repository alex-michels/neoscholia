"""Build the data of the page «Схолии к «Одиссее» X» (src/_data/scholia/odyssey-10.json).

Source: v02-arbitration.json in this folder. It holds three outputs of version 0.2:
  textA  the Greek of scholia 10.1–4 checked against the scans of Dindorf II 443–446;
  setA   one translation (RU, EN) on that Greek, arbitrated between the published draft 0.1
         and the independent translation by GPT-6 Astra (independent/), with notes and divergences;
  setB   the same for the scholia to 10.82–86 in the appendix of the Crates article (applied there).
This script adds the editorial layer for the site: Russian labels, notes lettered in reading order,
the apparatus with Russian glosses, and the review log in Russian.

Usage (from the project root):  python -I research/texts/odyssey-scholia/page.py
"""
import html
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = ROOT / "src" / "_data" / "scholia" / "odyssey-10.json"

VERSION = "0.2"

src = json.loads((HERE / "v02-arbitration.json").read_text(encoding="utf-8"))
textA = {s["id"]: s for s in src["textA"]["established"]}
setA = {s["id"]: s for s in src["setA"]["scholia"]}

# Notes are lettered in reading order on the page. The arbitration lettered them by the old page,
# so s1 and s4 are relettered: old mark -> new mark.
RELETTER = {"s1": {"δ": "α", "γ": "β", "β": "γ", "α": "δ"}, "s4": {"π": "ο", "ο": "π"}}
LATIN = "abcdefghij"

# ---------- Russian layer ----------
HEAD = {
    "s1": {"ref": "Σ Од. 10.1", "dindorf": "II 443.26–444.7", "scan": "n46",
           "chips": ["география странствий"], "late": ""},
    "s2": {"ref": "Σ Од. 10.2", "dindorf": "II 444.8–445.23", "scan": "n47",
           "chips": ["мифография", "звёзды и ветры", "магия"], "late": "поздний слой: P, Цец"},
    "s3": {"ref": "Σ Од. 10.3", "dindorf": "II 445.24–446.14", "scan": "n48",
           "chips": ["Аристарх", "толкование слова"], "late": ""},
    "s4": {"ref": "Σ Од. 10.4", "dindorf": "II 446.15–19", "scan": "n49",
           "chips": ["грамматика", "рационализация"], "late": ""},
}
LABELS = {
    "s1": [("Q", "отдельная схолия к той же лемме · 443.26–28"),
           ("B Q V", "основная схолия · 443.29–444.4"),
           ("V", "продолжение только в V · 444.4–7")],
    "s2": [("Q", "начало длинной схолии · 444.8–17"),
           ("Q", "три Эола · 444.17–21"),
           ("V", "отдельная схолия: два Эола · 444.21–22"),
           ("P, поздняя рука", "приписка из комментария Цеца к Ликофрону, 738 · 444.23–445.16"),
           ("P", "конец приписки, по Буттману — из другого источника · 445.16–23")],
    "s3": [("H M Q T V", "основная схолия · 445.24–446.7"),
           ("Q", "другая схолия (ἄλλως) · 446.7–10"),
           ("T", "отдельная схолия к слову πλωτῇ · 446.11–14")],
    "s4": [("V", "к слову χάλκεον · 446.15–16"),
           ("B Q", "к словам χάλκεον ἄρρηκτον · 446.17–18"),
           ("T", "к словам λισσὴ δὲ πέτρη · 446.19")],
}
# In Dindorf the first note of s1, s2, s3 opens with the lemma; the arbitrated Greek leaves it out.
GREEK_LEMMA = {"s1": "Αἰολίην δ’ ἐς νῆσον", "s2": "Αἴολος Ἱπποτάδης", "s3": "πλωτῇ ἐνὶ νήσῳ"}

APPARATUS = {
    "s1": [
        "443.26 (к схолии Q) Cf. p. 444, 4. 449, 3. et schol. Apoll. Rh. 3, 42. BUTTM.",
        "443.29 Cf. schol. ad v. 20.",
        "444.1 οἱ δὲ] τινὲς δὲ P., omisso λέγοντες. (Схолия есть и в P.)",
        "444.6 Φοινικοῦσσαν] Non bene hic inserta legebantur hæc: τινὲς δὲ ἀλληγοροῦντες — προστασσόμενοι, quæ vid. infra ad v. 6. BUTTM.",
        "Рядом, не переведено: 443.22–25 — схолия Q к 9.564, перенесённая сюда Буттманом (см. примеч. γ).",
    ],
    "s3": None,  # filled from the data with the glosses below
    "s4": ["У Диндорфа аппарата к 446.15–19 нет."],
}
GLOSS = {  # English glosses of the arbitration -> Russian
    "444.9 οἱ addidi. (Dindorf)": "444.9 οἱ addidi.",
    " (The antecedent of τρεῖς γὰρ is Buttmann's correction.)": " (На эту исправленную фразу и отсылает γάρ в τρεῖς γὰρ.)",
    " (V note)": " (схолия V)",
    " (H and Q read 'some …, others …')": " (В H Q: «одни…, другие…».)",
    "445.26 (printed on p. 446)": "445.26 (в аппарате на с. 446)",
    " (old number; fr. 33d Snell–Maehler)": " (старая нумерация; ныне фр. 33d Snell–Maehler)",
}

# Editorial fixes to the wording of the notes (RU and EN)
NOTE_FIX = {
    "Генеалогия близка к Аполлодору (1.7.2–3)": "Генеалогия близка к «Библиотеке» Псевдо-Аполлодора (1.7.2–3)",
    "The genealogy is close to Apollodorus (1.7.2–3)": "The genealogy is close to the Library of Pseudo-Apollodorus (1.7.2–3)",
}

# Notes that answer a divergence between the two translations
DIVERGENCE_NOTE = "расхождение переводов"

# ---------- review log (Russian) ----------
DRAFT = ("Черновик", "Claude Opus 5.5 · Anthropic",
         "Версия 0.1: перевод и новые схолии для макета страницы. Греческий текст набран по распознанному скану Диндорфа и с изданием не сверялся.")
INDEP = "Независимый перевод", "GPT-6 Astra · OpenAI (Codex)"
COLLATE = "Сверка текста", "Claude Opus 5.5 · Anthropic"
ARBITER = "Арбитраж", "Claude Opus 5.5 · Anthropic"
EDITOR = ("Редактор", "Александр Михельс, PhD", None)

INDEP_TEXT = {
    "s1": "Перевод только с греческого, без доступа к опубликованному. Попутно сверил текст с изданием: 3 замечания (сиглы, аппарат), все подтвердились.",
    "s2": "Перевод только с греческого, без доступа к опубликованному. Попутно сверил текст с изданием: 11 замечаний; все подтвердились, в одном описка при выписывании аппарата (ἔσται вместо ἔσεται).",
    "s3": "Перевод только с греческого, без доступа к опубликованному. Попутно сверил текст с изданием: 9 замечаний; все подтвердились, в двух описки при выписывании аппарата (ἔνιστε, αἰλός).",
    "s4": "Перевод только с греческого, без доступа к опубликованному. Попутно сверил текст с изданием: 2 замечания (ошибочное περιβόλου, порядок частей), оба подтвердились.",
}
COLLATE_TEXT = {
    "s1": "Проверено по сканам Диндорфа, с. 443–444. Сиглы разделены: B Q V — до слова Λεοντίνους, дальше только V. Добавлена отдельная схолия Q (443.26–28), к которой относится лемма: на странице её не было. В аппарат внесены чтение P и замечание Буттмана о вставке после Φοινικοῦσσαν.",
    "s2": "Проверено по сканам, с. 444–445. Сигла — Q, а не «H Q». Напечатано начало схолии Q (444.8–17), прежде сокращённое с […], и отдельная схолия V (444.21–22). Приписка P дана целиком (444.23–445.23): на странице она без пометы обрывалась на словах δεσπότην ἀνέμων. В тексте P, как в издании, строчные ταύρῳ, κυνός и нет запятой после πλεύσειαν. В «Одиссее» 10.2 — θεοῖσιν (у Мюррея с ν).",
    "s3": "Проверено по сканам, с. 445–446. ῥιπαῖς вместо ῥιπαῖσιν: так у Диндорфа, ῥιπαῖσιν — форма современного текста Пиндара. Возвращена первая фраза схолии Q (Ἄλλως…), выпущенная на странице без пометы, и добавлена отдельная схолия T к πλωτῇ (446.11–14).",
    "s4": "Проверено по скану, с. 446. περιβολῆς вместо περιβόλου: ошибка перешла из соседней схолии T. Части даны в порядке издания — сначала V, потом B Q; ἰσχυρόν с точкой, как в издании. Добавлена схолия T к λισσὴ δὲ πέτρη (446.19).",
}
# Divergences between the published draft and the independent translation, and how they were settled
ARBITRATION = {
    "s1": [
        ("οὐ τὰς Αἰόλου νήσους", "было «островами Эоловыми» / ‘Aeolian’, у независимого — «островами Эола»",
         "принят независимый: Αἰόλου — родительный падеж имени, а не прилагательное, как у Гомера (Αἰολίην); с прилагательным фраза читается так, будто «Эолийский остров — не из Эолийских островов»"),
        ("ἐκτετοπισμένην", "было «лежащем в стороне», у независимого — «расположенном вдали»",
         "по смыслу принят независимый: «удалённом» / ‘far-removed’ — термин александрийских толкователей (примеч. γ)"),
        ("Ἱκεσίαν", "было «Гикесию», у независимого — «Икесию»",
         "оставлено «Гикесия»: придыхание передаётся последовательно, как в «Гиера»"),
        ("Αἰολίην δ’ ἐς νῆσον (Гомер 10.1)", "было «на остров Эолию», у независимого — «на Эолийский остров»",
         "принят независимый: Αἰολίην — прилагательное при νῆσον; так остров Гомера отличается от «островов Эола» в схолии"),
    ],
    "s2": [
        ("φυλάσσει δὲ Ὅμηρος τὸ εἰπεῖν ἐξ Ἱππότου", "было «строго держится того, чтобы называть его сыном Гиппота», у независимого — «избегает говорить „от Гиппота“»",
         "оставлен смысл опубликованного перевода (примеч. ζ): Гомер дважды называет Эола Гиппотадом (10.2, 10.36); формулировка уточнена — «говорить „от Гиппота“»"),
        ("ἐφρόντισε μᾶλλον εἰδέναι", "было «старался прежде всего знать», у независимого — «старался ещё лучше изучить»",
         "оставлен смысл опубликованного: μᾶλλον — «предпочтительно», εἰδέναι — «знать», а не «изучать»; уточнено: «больше всего заботился о том, чтобы знать»"),
        ("τὸν πόδα τῆς νηὸς ἔχων", "части [b] на странице не было; независимый переводит «шкот» и замечает, что это не гомеровское слово",
         "перевод «шкот» принят, замечание отклонено: у Гомера в 10.32 стоит πόδα νηὸς ἐνώμων (примеч. κ)"),
        ("Αἴολος Ἱπποτάδης (Гомер 10.2)", "было «Эол Гиппотад», у независимого — «Эол, сын Гиппота»",
         "оставлено «Гиппотад»: схолия обсуждает именно отчество"),
    ],
    "s3": [
        ("ἐν δὲ ἄλλῳ", "было «в другом [толковании]», у независимого — «в другом [источнике]»",
         "ἐν ἄλλῳ отсылает к другому списку или комментарию; русский выровнен с английским: «в другом [комментарии]»"),
        ("οὐκ ἂν οὐδὲ ἐκ δευτέρου", "у независимого в английском ‘a second time either’",
         "отклонено: ‘either’ подразумевает, что и в первый раз остров не нашли; русское «и во второй раз» упрощено до «во второй раз»"),
    ],
    "s4": [
        ("διὰ τὴν περὶ αὐτὸ λειότητα", "было «из-за гладкости вокруг неё», у независимого — «из-за гладкости своей поверхности со всех сторон»",
         "оставлен буквальный перевод, он допускает оба понимания; второе — в примечании ο"),
        ("ἀπρόσβατον", "у независимого в английском ‘cannot be attacked’",
         "отклонено: ἀπρόσβατος — «к которому не подойти, на который не взойти», без военного смысла"),
        ("περιβολῆς τάξιν ἐπέχουσα", "опубликованный перевод был сделан по ошибочному περιβόλου («занимая место городской стены»), у независимого — «выполняя роль ограды»",
         "по сути принят независимый: «занимая место ограды»; слова «городской» в греческом нет"),
        ("πᾶσαν δέ τέ μιν πέρι τεῖχος (Гомер 10.3–4)", "оба перевода вставляли глагол: «обегает», «окружает»",
         "принят перевод без глагола: «весь его кругом — стена»; схолия B Q как раз отмечает, что глагола нет"),
        ("λισσή (Гомер 10.4)", "в английском было ‘sheer’, у независимого — ‘smooth’",
         "принят независимый: на слове «гладкая» держатся схолии V и T"),
    ],
}


# ---------- helpers ----------
def esc(s):
    return html.escape(s, quote=False)


def mark_map(sid, notes):
    """old mark -> (new mark, id)"""
    rel = RELETTER.get(sid, {})
    marks = [n["ru"].split(".", 1)[0].strip() for n in notes]
    new = {m: rel.get(m, m) for m in marks}
    order = sorted(new.values(), key="αβγδεϛζηθικλμνξοπ".index)
    num = sid[1:]
    return {m: (nm, f"n{num}{LATIN[order.index(nm)]}") for m, nm in new.items()}


def lemma_span(s):
    m = re.match(r"^([^\[\]]{1,40})\]\s*", s)
    return f'<span class="lm">{m.group(1)}]</span> {s[m.end():]}' if m else s


def anchors(s, marks, lang):
    def sub(m):
        nm, nid = marks[m.group(1)]
        return f'<sup class="n"><a href="#{nid}{"-en" if lang == "en" else ""}">{nm}</a></sup>'
    return re.sub(r"\{(.)\}", sub, s)


def fix_refs(s, sid):
    for old, new in NOTE_FIX.items():
        s = s.replace(old, new)
    rel = RELETTER.get("s1", {})
    if sid == "s3":  # note ξ points to the old note β of s1
        s = re.sub(r"(примеч\.|note) β", lambda m: f"{m.group(1)} {rel['β']}", s)
    return s


def apparatus(sid):
    if APPARATUS.get(sid):
        return APPARATUS[sid]
    out = []
    for line in setA[sid]["apparatus"]:
        for en, ru in GLOSS.items():
            line = line.replace(en, ru)
        out.append(line)
    return out


# ---------- build ----------
scholia = []
for sid in ("s1", "s2", "s3", "s4"):
    a, t, h = setA[sid], textA[sid], HEAD[sid]
    marks = mark_map(sid, a["notes"])
    parts = []
    for i, (p, (sigla, label)) in enumerate(zip(a["parts"], LABELS[sid])):
        grc = p["greek"]
        ru, en = p["ru"], p["en"]
        if sid == "s2" and i == 1:  # the opening of the Q scholion is printed, so the cut mark goes
            grc, ru, en = (x.removeprefix("[…] ") for x in (grc, ru, en))
        if i == 0 and sid in GREEK_LEMMA:
            grc = f"{GREEK_LEMMA[sid]}] {grc}"
        parts.append({
            "sigla": sigla, "label": label,
            "grc": lemma_span(esc(grc)),
            "ru": anchors(lemma_span(esc(ru)), marks, "ru"),
            "en": anchors(lemma_span(esc(en)), marks, "en"),
        })
    notes = []
    for n in a["notes"]:
        old = n["ru"].split(".", 1)[0].strip()
        nm, nid = marks[old]
        strip = lambda s: re.sub(r"^.\.\s*", "", s, count=1)
        notes.append({
            "id": nid, "mark": nm,
            "ru": esc(fix_refs(strip(n["ru"]), sid)),
            "en": esc(fix_refs(strip(n["en"]), sid)),
            "tag": DIVERGENCE_NOTE if n.get("origin") == "divergence" else "",
            "source": n.get("source", ""),
        })
    notes.sort(key=lambda n: n["id"])
    log = [
        {"step": DRAFT[0], "who": DRAFT[1], "text": DRAFT[2]},
        {"step": INDEP[0], "who": INDEP[1], "text": INDEP_TEXT[sid]},
        {"step": COLLATE[0], "who": COLLATE[1], "text": COLLATE_TEXT[sid]},
        {"step": ARBITER[0], "who": ARBITER[1],
         "text": "Опубликованный черновик и независимый перевод сведены в один. Расхождения:",
         "items": [{"grc": g, "was": w, "verdict": v} for g, w, v in ARBITRATION[sid]]},
        {"step": EDITOR[0], "who": EDITOR[1], "text": "", "pending": "Ожидает проверки."},
    ]
    scholia.append({
        "id": sid, "ref": h["ref"], "lemma": t["lemma"], "dindorf": h["dindorf"],
        "scan": f"https://archive.org/details/scholiagraeodyss02homeuoft/page/{h['scan']}/mode/1up",
        "chips": h["chips"], "late": h["late"],
        "parts": parts, "apparatus": [esc(x) for x in apparatus(sid)], "notes": notes, "log": log,
    })

LEMMA_LINK = {"10.1": ("s1", "Αἰολίην δ’ ἐς νῆσον"), "10.2": ("s2", "Αἴολος Ἱπποτάδης"),
              "10.3": ("s3", "πλωτῇ ἐνὶ νήσῳ"), "10.4": ("s4", "χάλκεον ἄρρηκτον")}
homer = []
tr = {x["line"]: x for x in src["setA"]["homer"]}
for x in src["textA"]["homer"]:
    sid, lemma = LEMMA_LINK[x["line"]]
    rest = x["greek"][len(lemma):]
    assert x["greek"].startswith(lemma), x
    homer.append({"line": x["line"], "grc": f'<a class="lemma-link" href="#{sid}">{lemma}</a>{esc(rest)}',
                  "ru": esc(tr[x["line"]]["ru"]), "en": esc(tr[x["line"]]["en"])})

data = {"version": VERSION, "homer": homer, "scholia": scholia,
        "notes": sum(len(s["notes"]) for s in scholia), "parts": sum(len(s["parts"]) for s in scholia)}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(f"{OUT.relative_to(ROOT)}: {len(scholia)} scholia, {data['parts']} parts, {data['notes']} notes")
for s in scholia:
    for p in s["parts"]:
        for lang in ("ru", "en"):
            assert "{" not in p[lang], (s["id"], p[lang][:80])
