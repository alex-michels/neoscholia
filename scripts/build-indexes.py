"""Build the site indexes (authors, works and passages, places, names and myths).

The gazetteer lives in research/indexes/ (one JSON file per index, made with model help and reviewed):
  names.json, places.json, authors.json — entries with name forms, glosses, Wikidata/Pleiades ids and
  regular-expression patterns for every form of the name;
  works.json — works with their author and the passages cited (loci), each with the place where it is cited.
This script finds every mention of every entry in the texts of the library, checks that the cited anchors
exist, and writes src/_data/indexes.json for the page indexes.html. Run it again after a text changes:
  python scripts/build-indexes.py            # build
  python scripts/build-indexes.py --check-ids  # also compare Wikidata labels and Pleiades titles (network)
"""
import html
import json
import re
import sys
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
GAZ = ROOT / "research" / "indexes"
OUT = ROOT / "src" / "_data" / "indexes.json"

TEXTS = {  # page → short name used in the index
    "zacher-1": "Эпитома Цахера, кн. I",
    "odyssey-10": "Схолии к «Одиссее» X",
    "study-laestrygonians": "«Пергам против Александрии?»",
}


def strip(s):
    return html.unescape(re.sub(r"<[^>]+>", " ", s))


# ---------- text units: (page, anchor, label, [strings]) ----------
def units():
    out = []
    z = json.loads((ROOT / "src/_data/texts/zacher-1.json").read_text(encoding="utf-8"))
    for c in z["chapters"]:
        out.append(("zacher-1", f"c{c['chapter']}", f"I.{c['chapter']}", [c["latin"], c["ru"], c["en"]]))
        for n in c["notes"]:
            out.append(("zacher-1", f"n{n['n']}", f"прим. {n['n']}", [n["ru"], n["en"]]))

    o = (ROOT / "src/odyssey-10.njk").read_text(encoding="utf-8")
    homer = o[o.index('id="homer-h"'):o.index('id="sch-h"')]
    out.append(("odyssey-10", "homer-h", "Од. 10.1–4", [strip(homer)]))
    for m in re.finditer(r'<article class="seg" id="(s\d+)">(.*?)</article>', o, re.S):
        sid, body = m.groups()
        notes = re.findall(r'<p class="note" id="(n\d+[a-z])" data-lang="ru"><span class="mark">([^<]+)</span>(.*?)</p>\s*<p class="note" id="\1-en" data-lang="en">(.*?)</p>', body, re.S)
        main = re.sub(r'<p class="note".*?</p>', "", body, flags=re.S)
        verse = re.search(r'<span class="ref">([^<]+)</span>', main)
        out.append(("odyssey-10", sid, verse.group(1).strip() if verse else sid, [strip(main)]))
        for nid, mark, ru, en in notes:
            out.append(("odyssey-10", nid, f"прим. {mark}", [strip(ru), strip(en)]))

    a = (ROOT / "research/studies/laestrygonians/article.md").read_text(encoding="utf-8")
    notes = dict(re.findall(r"^\[\^(\d+)\]:\s*(.+)$", a, re.M))
    body = re.sub(r"^\[\^\d+\]:.*$", "", a, flags=re.M)
    secs = {}
    for part in re.split(r"^## ", body, flags=re.M)[1:]:
        title, _, text = part.partition("\n")
        secs[title.strip()] = text
    out.append(("study-laestrygonians", "abstract", "аннотация",
                [v for k, v in secs.items() if k.startswith(("Аннотация", "Abstract"))]))
    for k, v in secs.items():
        m = re.match(r"(\d+)\.\s", k)
        if m:
            out.append(("study-laestrygonians", f"s{m.group(1)}", f"§ {m.group(1)}", [k, v]))
        elif k.startswith("Приложение"):
            for i, block in enumerate(re.split(r"^### ", v, flags=re.M)[1:], 1):
                parts = block.split("\n", 1)[0].split(" · ")
                greek_lemma = len(parts) > 1 and re.search(r"[Ͱ-Ͽἀ-῿]", parts[1])
                head = parts[0] + (" " + parts[1] if greek_lemma else "")
                out.append(("study-laestrygonians", f"appx-{i}", f"приложение, {head}", [block]))
    for n, t in notes.items():
        out.append(("study-laestrygonians", f"n{n}", f"прим. {n}", [t]))
    return out


def compile_entry(e):
    pats = [p for lang in ("ru", "en", "la", "grc") for p in e.get("patterns", {}).get(lang, []) if p]
    rx = [re.compile(r"(?<![\w])(?:" + p + ")") for p in pats]
    ex = [re.compile(p) for p in e.get("exclude", []) if p]
    return rx, ex


def find_refs(e, unit_list):
    rx, ex = compile_entry(e)
    refs = []
    for page, anchor, label, strings in unit_list:
        text = " \n ".join(strings)
        hit = False
        for r in rx:
            for m in r.finditer(text):
                around = text[max(0, m.start() - 40): m.end() + 40]
                if not any(x.search(around) for x in ex):
                    hit = True
                    break
            if hit:
                break
        if hit:
            refs.append({"page": page, "anchor": anchor, "label": label})
    return refs


def group(refs):
    """refs → [{text, links:[{href,label}]}] in the order of TEXTS."""
    out = []
    for page, name in TEXTS.items():
        links = [{"href": f"{r['page']}.html#{r['anchor']}", "label": r["label"]} for r in refs if r["page"] == page]
        if links:
            out.append({"text": name, "links": links})
    return out


def sort_key(s):
    return s.lower().replace("ё", "е").lstrip("«(„")


def load(name):
    p = GAZ / f"{name}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else []


def main():
    unit_list = units()
    anchors = {(p, a): label for p, a, label, _ in unit_list}
    problems = []
    sections = {}

    for key, title in (("names", "Имена и мифы"), ("places", "Места"), ("authors", "Авторы")):
        entries = []
        for e in load(key):
            refs = find_refs(e, unit_list)
            if not refs and key != "authors":  # an author may be cited without being named; see below
                problems.append(f"{key}: {e['id']} ({e['ru']}) — no mentions found")
                continue
            entries.append({k: e.get(k, "") for k in ("id", "ru", "en", "orig", "kind", "gloss_ru", "wikidata", "pleiades")}
                           | {"refs": group(refs), "n": len(refs)})
        sections[key] = {"title": title, "entries": sorted(entries, key=lambda x: sort_key(x["ru"]))}

    works = load("works")
    authors = {a["id"]: a for a in sections["authors"]["entries"]}
    wentries = []
    for w in works:
        loci = {}
        for l in w.get("loci", []):
            if (l["page"], l["anchor"]) not in anchors:
                problems.append(f"works: {w['id']} {l['locus']} — anchor {l['page']}#{l['anchor']} not found")
                continue
            loci.setdefault(l["locus"], []).append({"page": l["page"], "anchor": l["anchor"], "label": anchors[(l["page"], l["anchor"])]})
        if not loci:
            problems.append(f"works: {w['id']} ({w['ru']}) — no passages")
            continue
        def locus_key(s):
            return [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", s)]
        a = authors.get(w.get("author_id", ""))
        wentries.append({"id": w["id"], "ru": w["ru"], "en": w.get("en", ""), "orig": w.get("orig", ""), "abbr": w.get("abbr", ""),
                         "wikidata": w.get("wikidata", ""), "author": a["ru"] if a else "", "author_id": a["id"] if a else "",
                         "loci": [{"locus": k, "refs": group(v)} for k, v in sorted(loci.items(), key=lambda kv: locus_key(kv[0]))],
                         "n": sum(len(v) for v in loci.values())})
    sections["works"] = {"title": "Произведения", "entries": sorted(wentries, key=lambda x: (sort_key(x["author"] or "яя"), sort_key(x["ru"])))}
    for a in sections["authors"]["entries"]:
        a["works"] = [{"id": w["id"], "ru": w["ru"]} for w in sections["works"]["entries"] if w["author_id"] == a["id"]]
    for a in [a for a in sections["authors"]["entries"] if not a["refs"] and not a["works"]]:
        problems.append(f"authors: {a['id']} ({a['ru']}) — neither mentioned nor cited")
    sections["authors"]["entries"] = [a for a in sections["authors"]["entries"] if a["refs"] or a["works"]]

    order = ["authors", "works", "places", "names"]
    for k in order:
        s = sections[k]
        s["count"] = len(s["entries"])
        top = sorted(s["entries"], key=lambda x: -x["n"])[:3]
        s["sample"] = ", ".join(x["ru"] for x in top) + "…"  # a short teaser for the home page
        letters = []
        for x in s["entries"]:
            ch = sort_key(x["author"] if k == "works" and x["author"] else x["ru"])[:1].upper()
            x["letter"] = ch
            if ch not in letters:
                letters.append(ch)
        s["letters"] = letters
    OUT.write_text(json.dumps({"order": order, "sections": sections}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print({k: sections[k]["count"] for k in order})
    for p in problems:
        print("!", p)

    if "--check-ids" in sys.argv:
        check_ids(sections)


def check_ids(sections):
    """Print Wikidata labels and Pleiades titles next to our names, for a human check."""
    report = []
    qids = [(k, e) for k in ("names", "places", "authors", "works") for e in sections[k]["entries"] if e.get("wikidata")]
    for i in range(0, len(qids), 40):
        chunk = qids[i:i + 40]
        url = "https://www.wikidata.org/w/api.php?action=wbgetentities&format=json&props=labels|descriptions&languages=en|ru&ids=" + "|".join(e["wikidata"] for _, e in chunk)
        req = urllib.request.Request(url, headers={"User-Agent": "Neoscholia index builder (https://github.com/alex-michels/neoscholia)"})
        data = json.loads(urllib.request.urlopen(req, timeout=60).read())["entities"]
        for k, e in chunk:
            ent = data.get(e["wikidata"], {})
            lab = ent.get("labels", {})
            report.append({"index": k, "id": e["id"], "ours": e["ru"], "wikidata": e["wikidata"],
                           "label_en": lab.get("en", {}).get("value", "—"), "label_ru": lab.get("ru", {}).get("value", "—"),
                           "desc": ent.get("descriptions", {}).get("en", {}).get("value", "")})
    for e in sections["places"]["entries"]:
        if e.get("pleiades"):
            req = urllib.request.Request(f"https://pleiades.stoa.org/places/{e['pleiades']}/json", headers={"User-Agent": "Neoscholia index builder"})
            try:
                title = json.loads(urllib.request.urlopen(req, timeout=60).read()).get("title", "—")
            except Exception as ex:  # noqa: BLE001
                title = f"error: {ex}"
            report.append({"index": "places", "id": e["id"], "ours": e["ru"], "pleiades": e["pleiades"], "title": title})
    (GAZ / "ids-check.json").write_text(json.dumps(report, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print(f"ids checked: {len(report)} → research/indexes/ids-check.json")


if __name__ == "__main__":
    main()
