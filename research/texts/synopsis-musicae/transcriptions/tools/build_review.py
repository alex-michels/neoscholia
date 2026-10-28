"""Build the editor's local review page: for each place the checkers left open, a zoom of the word, the line with its neighbours,
the page with the line marked, both readings anonymised, the checkers' notes and a decision form.
Usage: python -P -E build_review.py <out dir> [debug]"""
import difflib, html, json, re, sys, unicodedata
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw, ImageStat
sys.stdout.reconfigure(encoding='utf-8')
SP = Path(__file__).parent
OUT = Path(sys.argv[1])
DEBUG = len(sys.argv) > 2
(OUT / 'img').mkdir(parents=True, exist_ok=True)
SRC = Path('C:/Users/user/Documents/Projects/Neoscholia/research/texts/synopsis-musicae/source')

sys.path.insert(0, str(SP))
from review_spec import SPEC  # list of places: id, src (wf dir), band or y, tok, line (optional), questions

def load_items():
    items = {}
    for wf in sorted({s['src'] for s in SPEC}):
        for it in json.load(open(SP / wf / 'decisions.json', encoding='utf-8')):
            items[(wf, it['id'])] = it
    return items

def bands(g):
    """Text-line cores by horizontal projection (as locate_lines.py), on a greyscale image at full size."""
    W, H = g.size
    s = 1400 / W
    gs = g.resize((1400, int(H * s)))
    st = ImageStat.Stat(gs)
    thr = st.mean[0] - 1.2 * st.stddev[0]
    dark = gs.crop((int(1400 * .12), 0, int(1400 * .88), gs.size[1])).point(lambda v: 255 if v < thr else 0)
    prof = [v / 255 * dark.size[0] for v in dark.resize((1, dark.size[1]), Image.BOX).getdata()]
    prof = [sum(prof[max(0, i - 1):i + 2]) / len(prof[max(0, i - 1):i + 2]) for i in range(len(prof))]
    mx = max(prof)
    on = [v > max(2.0, 0.08 * mx) for v in prof]
    out, y = [], 0
    while y < len(on):
        if on[y]:
            y0 = y
            while y < len(on) and on[y]:
                y += 1
            if (y - y0) / len(on) >= 0.004:
                out.append((int(y0 / s), int(y / s)))
        y += 1
    return out, thr

def col_profile(g, thr, x0, y0, x1, y1):
    d = g.crop((x0, y0, x1, y1)).point(lambda v: 255 if v < thr else 0)
    return [v / 255 * d.size[1] for v in d.resize((d.size[0], 1), Image.BOX).getdata()]

def segments(prof, gapmin):
    on = [v > 0.6 for v in prof]
    segs, x = [], 0
    while x < len(on):
        if on[x]:
            x0 = x
            while x < len(on) and on[x]:
                x += 1
            segs.append([x0, x])
        x += 1
    merged = []
    for s in segs:
        if merged and s[0] - merged[-1][1] < gapmin:
            merged[-1][1] = s[1]
        else:
            merged.append(s)
    return [s for s in merged if s[1] - s[0] > 2]

def written(tok):
    """Letters actually on the page: drop supplied letters in round brackets, [?] and combining marks."""
    t = re.sub(r'\([^)]*\)|\[\?\]', '', tok)
    t = unicodedata.normalize('NFD', t)
    return ''.join(c for c in t if not unicodedata.combining(c) and c.isalpha())

def tokens(line):
    return [t for t in line.split() if written(t)]

def esc(s):
    return html.escape(s or '', quote=True)

def mark_diff(a, b):
    ta, tb = a.split(), b.split()
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    oa, ob = [], []
    for t, i1, i2, j1, j2 in sm.get_opcodes():
        sa, sb = ' '.join(ta[i1:i2]), ' '.join(tb[j1:j2])
        if t == 'equal':
            oa.append(esc(sa)); ob.append(esc(sb))
        else:
            if sa: oa.append(f'<mark>{esc(sa)}</mark>')
            if sb: ob.append(f'<mark>{esc(sb)}</mark>')
    return ' '.join(oa), ' '.join(ob)

items = load_items()
cards = []
for sp in SPEC:
    it = items[(sp['src'], sp['id'])]
    slug = re.sub(r'[^A-Za-z0-9]+', '-', sp['id']).strip('-').lower()
    img_path = Path(it['image'])
    tif = img_path.with_suffix('.tif')
    with Image.open(tif if tif.exists() else img_path) as im:
        rgb = im.convert('RGB')
    g = rgb.convert('L')
    W, H = g.size
    bs, thr = bands(g)
    pitches = [b2[0] - b1[0] for b1, b2 in zip(bs, bs[1:]) if 0 < b2[0] - b1[0] < H / 12]
    pitch = sorted(pitches)[len(pitches) // 2] if pitches else 60
    if 'y' in sp:
        c = sp['y']
        core = (c - pitch * .2, c + pitch * .2)
    else:
        y0, y1 = bs[sp['band'] - 1]
        c, core = (y0 + y1) / 2, (y0, y1)
    # horizontal extent of the line and its words, from the ink in the x-height core
    xa, xb = int(W * .04), int(W * .96)
    prof = col_profile(g, thr, xa, int(core[0]), xb, int(core[1]))
    segs = [[s[0] + xa, s[1] + xa] for s in segments(prof, gapmin=max(6, pitch * sp.get('gap', .16)))]
    segs = [s for s in segs if s[1] - s[0] > pitch * .15] or segs
    lx0, lx1 = segs[0][0], segs[-1][1]
    line_text = sp.get('line') or it['reading_1']
    toks = tokens(line_text)
    qs = []
    for qi, q in enumerate(sp['questions']):
        if 'xr' in q:
            wx0, wx1 = q['xr']
            how = 'manual'
        elif len(segs) == len(toks):
            wx0, wx1 = segs[q['tok'][0]][0], segs[q['tok'][1]][1]
            how = 'segments'
        else:
            lens = [len(written(t)) + 1 for t in toks]
            tot = sum(lens)
            a = sum(lens[:q['tok'][0]]) / tot
            b = sum(lens[:q['tok'][1] + 1]) / tot
            wx0, wx1 = lx0 + a * (lx1 - lx0), lx0 + b * (lx1 - lx0)
            how = f'proportional ({len(segs)} segments, {len(toks)} words)'
        qs.append((wx0, wx1, how))
        if DEBUG:
            print(sp['id'], qi + 1, how, int(wx0), int(wx1), 'pitch', pitch)
    # line view: the line with its neighbours, target line tinted, words tinted stronger
    top, bot = int(max(0, c - pitch * 1.7)), int(min(H, c + pitch * 1.55))
    left, right = int(max(0, lx0 - pitch * .6)), int(min(W, lx1 + pitch * .6))
    tint = Image.new('RGB', (W, H), (255, 255, 255))
    d = ImageDraw.Draw(tint)
    d.rectangle([left, c - pitch * .62, right, c + pitch * .48], fill=(255, 246, 196))
    for wx0, wx1, _ in qs:
        d.rectangle([wx0 - pitch * .25, c - pitch * .62, wx1 + pitch * .25, c + pitch * .48], fill=(255, 212, 150))
    lined = ImageChops.multiply(rgb, tint)
    lv = lined.crop((left, top, right, bot))
    if lv.size[0] > 1500:
        lv = lv.resize((1500, int(lv.size[1] * 1500 / lv.size[0])), Image.LANCZOS)
    lv.save(OUT / 'img' / f'{slug}-line.jpg', quality=90)
    # word zooms
    zooms = []
    for qi, (wx0, wx1, _) in enumerate(qs):
        pad = (wx1 - wx0) * .3 + pitch * .7
        z = rgb.crop((int(max(0, wx0 - pad)), int(max(0, c - pitch * .85)), int(min(W, wx1 + pad)), int(min(H, c + pitch * .7))))
        f = min(900 / z.size[0], 300 / z.size[1], 5)
        z = z.resize((int(z.size[0] * f), int(z.size[1] * f)), Image.LANCZOS)
        name = f'{slug}-q{qi + 1}.jpg'
        z.save(OUT / 'img' / name, quality=92)
        zooms.append(name)
    # page view with the line marked
    pg = rgb.copy()
    d = ImageDraw.Draw(pg)
    d.rectangle([left, c - pitch * .7, right, c + pitch * .55], outline=(220, 0, 0), width=max(3, W // 300))
    pg.thumbnail((700, 1000))
    pg.save(OUT / 'img' / f'{slug}-page.jpg', quality=85)
    cards.append((sp, it, slug, zooms))

# ---------- HTML ----------
CH = {'1': 'чтение 1', '2': 'чтение 2', 'other': 'другое', 'unclear': 'не разобрать', 'convention': 'вопрос конвенции'}
CONF = {'high': 'уверен', 'medium': 'вероятно', 'low': 'догадка'}
rel_src = lambda p: '../source/' + Path(p).relative_to(SRC).as_posix()
parts, n_q = [], 0
for sp, it, slug, zooms in cards:
    r1, r2 = mark_diff(it['reading_1'], it['reading_2'])
    decided = [r for r in it['rows'] if r['status'] == 'decided']
    dec_html = ''
    if decided:
        lis = ''.join(f'<li>{esc(r["difference"])} → {CH.get(r["choice"], r["choice"])}</li>' for r in decided)
        dec_html = f'<div class="decided"><b>Уже решено (оба проверяющих согласны):</b><ul>{lis}</ul></div>'
    qhtml = []
    for qi, q in enumerate(sp['questions']):
        n_q += 1
        qid = f'{sp["id"]}#{qi + 1}'
        notes = []
        others = []
        for di in q['diffs']:
            row = it['rows'][di - 1]
            for who, lab in (('A', 'Проверяющий A'), ('B', 'Проверяющий Б')):
                x = row[who] or {}
                oth = f' «{esc(x.get("other"))}»' if x.get('other') else ''
                if x.get('other'):
                    others.append(x['other'])
                notes.append(f'<div class="note"><span class="who">{lab}</span> <span class="tag">{esc(row["difference"])}</span> '
                             f'<b>{CH.get(x.get("choice"), x.get("choice"))}{oth}</b> <i>({CONF.get(x.get("confidence"), "")})</i><br>{esc(x.get("seen"))}</div>')
        others += q.get('extra', [])
        opts = [('1', q['l1']), ('2', q['l2'])] + [(f'o:{o}', o) for o in dict.fromkeys(others) if o not in (q['l1'], q['l2'])]
        radios = ''.join(f'<label class="opt"><input type="radio" name="{esc(qid)}" value="{esc(v)}"> '
                         f'<span class="ch">{"1" if v == "1" else "2" if v == "2" else "≈"}</span> <span class="gr">{esc(t)}</span>'
                         f'{" <span class=src>(предложил проверяющий)</span>" if v.startswith("o:") else ""}</label>' for v, t in opts)
        radios += (f'<label class="opt"><input type="radio" name="{esc(qid)}" value="own"> своё чтение: '
                   f'<input type="text" class="own gr" data-q="{esc(qid)}" placeholder="как написано"></label>'
                   f'<label class="opt"><input type="radio" name="{esc(qid)}" value="unclear"> не разобрать</label>')
        qhtml.append(f'''<div class="q" data-q="{esc(qid)}" data-l1="{esc(q['l1'])}" data-l2="{esc(q['l2'])}">
<h3>Вопрос {qi + 1}. {esc(q['ask'])}</h3>
<a href="img/{zooms[qi]}" target="_blank"><img class="zoom" src="img/{zooms[qi]}" alt="увеличение слова"></a>
<div class="opts">{radios}</div>
<details><summary>Что увидели проверяющие (англ.)</summary>{''.join(notes)}</details>
</div>''')
    ctx = f'<p class="ctx">{esc(sp.get("ctx_ru") or "")}</p>' if sp.get('ctx_ru') else ''
    parts.append(f'''<section class="card" id="{slug}">
<h2>{esc(it['ref'])}</h2>{ctx}
<div class="views">
<a href="img/{slug}-line.jpg" target="_blank"><img class="line" src="img/{slug}-line.jpg" alt="строка со скана"></a>
<a class="pagelink" href="{esc(rel_src(it['image']))}" target="_blank" title="открыть страницу в полном разрешении"><img class="page" src="img/{slug}-page.jpg" alt="страница"></a>
</div>
<div class="readings"><div><span class="rl">1</span> <span class="gr">{r1}</span></div><div><span class="rl">2</span> <span class="gr">{r2}</span></div></div>
{dec_html}
{''.join(qhtml)}
<label class="comment">Комментарий к месту: <input type="text" class="cmt" data-p="{esc(sp['id'])}"></label>
</section>''')

page = f'''<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Спорные чтения</title>
<style>
:root {{ --bg:#f6f4ef; --card:#fff; --ink:#1d1c1a; --muted:#6b675f; --line:#ddd8cc; --accent:#9a3412; --mark:#ffe1b0; --btn-ink:#fff; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg:#1b1a18; --card:#262421; --ink:#ece8df; --muted:#a8a294; --line:#3b3833; --accent:#f0a46b; --mark:#6b4a1c; --btn-ink:#1b1a18; }} }}
* {{ box-sizing:border-box }}
body {{ margin:0; background:var(--bg); color:var(--ink); font:16px/1.5 system-ui, "Segoe UI", sans-serif; }}
main {{ max-width:1080px; margin:0 auto; padding:16px 16px 140px; }}
h1 {{ font-size:1.5rem; margin:.5rem 0 }}
.intro {{ color:var(--muted); max-width:70ch }}
.gr {{ font-family:"Palatino Linotype","Gentium Plus","Noto Serif",serif; font-size:1.12em }}
.card {{ background:var(--card); border:1px solid var(--line); border-radius:10px; padding:16px; margin:22px 0; }}
.card h2 {{ margin:0 0 8px; font-size:1.2rem }}
.ctx {{ color:var(--muted); margin:0 0 8px }}
.views {{ display:flex; gap:12px; align-items:flex-start; flex-wrap:wrap }}
.views img {{ display:block; border:1px solid var(--line); border-radius:4px; background:#fff }}
img.line {{ max-width:100%; width:780px }}
img.page {{ width:150px }}
.views a:first-child {{ flex:1 1 520px; min-width:0 }}
.readings {{ margin:12px 0; display:grid; gap:4px }}
.rl {{ display:inline-block; width:1.6em; text-align:center; font-weight:700; color:var(--accent) }}
mark {{ background:var(--mark); color:inherit; border-radius:3px; padding:0 2px }}
.decided {{ font-size:.92em; color:var(--muted) }}
.decided ul {{ margin:4px 0 }}
.q {{ border-top:1px dashed var(--line); margin-top:12px; padding-top:10px }}
.q h3 {{ font-size:1.02rem; margin:0 0 8px }}
img.zoom {{ display:block; max-width:100%; border:1px solid var(--line); border-radius:4px; background:#fff; margin-bottom:8px }}
.opts {{ display:flex; flex-wrap:wrap; gap:6px 16px }}
.opt {{ display:inline-flex; align-items:center; gap:6px; padding:4px 8px; border:1px solid var(--line); border-radius:6px; cursor:pointer }}
.opt:has(input:checked) {{ border-color:var(--accent); box-shadow:0 0 0 1px var(--accent) }}
.ch {{ font-weight:700; color:var(--accent) }}
.src {{ color:var(--muted); font-size:.85em }}
input.own, input.cmt {{ font:inherit; padding:2px 6px; border:1px solid var(--line); border-radius:4px; background:var(--bg); color:var(--ink); min-width:14em }}
details {{ margin-top:8px }} summary {{ cursor:pointer; color:var(--muted) }}
.note {{ font-size:.9em; margin:6px 0; padding-left:10px; border-left:3px solid var(--line) }}
.who {{ font-weight:600 }} .tag {{ color:var(--muted) }}
.comment {{ display:block; margin-top:12px; color:var(--muted) }}
.comment input {{ width:100%; margin-top:4px }}
.bar {{ position:fixed; left:0; right:0; bottom:0; background:var(--card); border-top:1px solid var(--line); padding:10px 16px; }}
.bar .in {{ max-width:1080px; margin:0 auto; display:flex; gap:12px; align-items:center; flex-wrap:wrap }}
button {{ font:inherit; padding:8px 16px; border-radius:6px; border:0; background:var(--accent); color:var(--btn-ink); font-weight:600; cursor:pointer }}
#out {{ width:100%; height:8em; display:none; font:13px/1.4 ui-monospace,Consolas,monospace }}
</style></head><body><main>
<h1>Спорные чтения: «Синопсис музыки»</h1>
<p class="intro">Здесь места, где два проверяющих не сошлись или не были уверены. Чтения 1 и 2 анонимны, их порядок случаен.
Сверху крупно слово, ниже вся строка с соседними (нужное место подсвечено; подсветка поставлена автоматически, она приблизительная),
справа страница: по клику откроется скан в полном разрешении. Выбор сохраняется в этом браузере. Когда закончите, нажмите
«Скопировать решения» внизу и вставьте текст в чат. Ваше решение окончательно.</p>
{''.join(parts)}
</main>
<div class="bar"><div class="in"><span id="prog"></span><button id="copy">Скопировать решения</button><span id="msg"></span>
<textarea id="out" readonly></textarea></div></div>
<script>
const KEY = 'neoscholia-review-synopsis';
const N = {n_q};
let st = {{}};
try {{ st = JSON.parse(localStorage.getItem(KEY) || '{{}}') }} catch (e) {{}}
const save = () => {{ try {{ localStorage.setItem(KEY, JSON.stringify(st)) }} catch (e) {{}} }};
document.querySelectorAll('input[type=radio]').forEach(r => {{
  if (st[r.name] && st[r.name].v === r.value) r.checked = true;
  r.addEventListener('change', () => {{ st[r.name] = Object.assign(st[r.name] || {{}}, {{ v: r.value }}); save(); prog() }});
}});
document.querySelectorAll('input.own').forEach(t => {{
  const q = t.dataset.q; if (st[q] && st[q].own) t.value = st[q].own;
  t.addEventListener('input', () => {{ st[q] = Object.assign(st[q] || {{}}, {{ own: t.value }});
    if (t.value) {{ const r = document.querySelector(`input[type=radio][name="${{CSS.escape(q)}}"][value=own]`); r.checked = true; st[q].v = 'own' }}
    save(); prog() }});
}});
document.querySelectorAll('input.cmt').forEach(t => {{
  const k = 'cmt:' + t.dataset.p; if (st[k]) t.value = st[k].c || '';
  t.addEventListener('input', () => {{ st[k] = {{ c: t.value }}; save() }});
}});
function prog() {{
  const done = [...document.querySelectorAll('.q')].filter(q => st[q.dataset.q] && st[q.dataset.q].v).length;
  document.getElementById('prog').textContent = `Решено ${{done}} из ${{N}}`;
}}
prog();
document.getElementById('copy').addEventListener('click', async () => {{
  const lines = ['Решения по спорным чтениям («Синопсис музыки»):'];
  document.querySelectorAll('.card').forEach(card => {{
    const ref = card.querySelector('h2').textContent;
    card.querySelectorAll('.q').forEach((q, i) => {{
      const s = st[q.dataset.q] || {{}};
      let a = '— (не решено)';
      if (s.v === '1') a = '1 = ' + q.dataset.l1;
      else if (s.v === '2') a = '2 = ' + q.dataset.l2;
      else if (s.v === 'own') a = 'своё: ' + (s.own || '');
      else if (s.v === 'unclear') a = 'не разобрать';
      else if (s.v && s.v.startsWith('o:')) a = 'вариант проверяющего: ' + s.v.slice(2);
      lines.push(`${{q.dataset.q}}: ${{a}}`);
    }});
    const c = card.querySelector('input.cmt');
    if (c && c.value) lines.push(`${{ref}} — комментарий: ${{c.value}}`);
  }});
  const text = lines.join('\\n');
  const out = document.getElementById('out'); out.value = text; out.style.display = 'block';
  try {{ await navigator.clipboard.writeText(text); document.getElementById('msg').textContent = 'Скопировано. Вставьте в чат.' }}
  catch (e) {{ out.select(); document.getElementById('msg').textContent = 'Выделите текст ниже и скопируйте (Ctrl+C).' }}
}});
</script></body></html>'''
(OUT / 'index.html').write_text(page, encoding='utf-8')
print('places', len(cards), 'questions', n_q, '->', OUT / 'index.html')
