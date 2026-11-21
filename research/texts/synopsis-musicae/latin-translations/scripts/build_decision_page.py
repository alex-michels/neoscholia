"""Build the editor's decision page for the translations of the Latin versions from the reviewed cards
(decisions/cards.json): one card per decision, options with the translators (A–D) who chose them and the reviewers who
recommend them, the arguments, the recommendation; the agreed points are listed at the end. The editor's choices are
kept in the browser and copied out as text («Скопировать решения»).
Usage: python -I build_decision_page.py <latin-translations folder>"""
import html, json, sys
sys.stdout.reconfigure(encoding='utf-8')
L = sys.argv[1]
D = json.load(open(f'{L}/decisions/cards.json', encoding='utf-8'))
esc = lambda s: html.escape(str(s or ''), quote=True)
KEY = {'A': 'Claude Fable 5.2', 'B': 'GPT-6.2 Sol', 'C': 'Claude Opus 5.5', 'D': 'GPT-6.2 Astra'}
REV = {'claude': 'Claude', 'sol': 'GPT-6.2 Sol', 'astra': 'GPT-6.2 Astra'}
VER = {'xylander': 'Ксиландр', 'vinet': 'Вине', 'both': 'обе версии'}
cards = D['cards']
groups = [('Общие вопросы: термины и метод', [c for c in cards if c['kind'] == 'general']),
          ('Места у Ксиландра', [c for c in cards if c['kind'] == 'place' and c['version'] == 'xylander']),
          ('Места у Вине', [c for c in cards if c['kind'] == 'place' and c['version'] == 'vinet'])]


def card_html(c):
    opts = []
    for o in c['options']:
        tr = ' '.join(f'<span class="chip">{esc(t)}</span>' for t in o.get('translators') or []) or '<span class="none">никто</span>'
        rv = ', '.join(REV.get(r, r) for r in o.get('recommended_by') or []) or '—'
        opts.append(f'''<label class="opt"><input type="radio" name="{esc(c['id'])}" value="{esc(o['key'])}" data-label="{esc(o['label_ru'])}">
<span class="ob"><b>{esc(o['key'])}) {esc(o['label_ru'])}</b>
<span class="r"><span class="lg">RU</span> {esc(o.get('ru'))}</span>
<span class="r"><span class="lg">EN</span> {esc(o.get('en'))}</span>
<span class="meta">переводы: {tr} · рекомендуют: {esc(rv)}</span></span></label>''')
    return f'''<article class="card" id="{esc(c['id'])}" data-id="{esc(c['id'])}">
<header><span class="cid">{esc(c['id'])}</span><h3>{esc(c['title_ru'])}</h3>
<span class="where">{esc(VER.get(c['version'], c['version']))} · {esc(', '.join(c['segments']))}</span></header>
<p class="lat">{esc(c.get('latin'))}</p>
<p class="q">{esc(c['question_ru'])}</p>
<div class="opts">{''.join(opts)}
<label class="opt"><input type="radio" name="{esc(c['id'])}" value="own"><span class="ob"><b>своё решение</b>
<textarea class="own" placeholder="Ваше решение"></textarea></span></label></div>
<div class="rec"><b>Рекомендация.</b> {esc(c['recommendation_ru'])}
<button type="button" class="take">Принять рекомендацию</button></div>
<details><summary>Доводы</summary><p class="ev">{esc(c['evidence_ru'])}</p></details>
<textarea class="cm" placeholder="Комментарий (необязательно)"></textarea>
</article>'''


body = []
for title, cs in groups:
    body.append(f'<h2>{esc(title)} <small>({len(cs)})</small></h2>')
    body += [card_html(c) for c in cs]
agreed = ''.join(f'<li><span class="where">{esc(", ".join(a.get("segments") or []))}</span> {esc(a.get("point"))}'
                 f'<br><span class="lg">RU</span> {esc(a.get("solution_ru"))} <span class="lg">EN</span> {esc(a.get("solution_en"))}</li>'
                 for a in D['agreed'])
cov = D.get('coverage', {})
key = ''.join(f'<li><b>{k}</b> — {esc(v)}</li>' for k, v in KEY.items())
page = f'''<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Решения по латинским переводам</title>
<style>
:root{{--bg:#f7f4ee;--fg:#1f1b16;--muted:#6b6257;--card:#fffdf8;--line:#ddd4c6;--acc:#7a4b1e;--rec:#f1e7d6;--chip:#e9dfcf}}
@media (prefers-color-scheme:dark){{:root{{--bg:#1b1814;--fg:#ece5da;--muted:#a59a8b;--card:#24201b;--line:#3b342c;--acc:#d9a36a;--rec:#2f281f;--chip:#3a3128}}}}
body{{margin:0;background:var(--bg);color:var(--fg);font:16px/1.5 Georgia,'Times New Roman',serif}}
main{{max-width:980px;margin:0 auto;padding:16px 16px 140px}}
h1{{font-size:1.6em;margin:.4em 0}} h2{{margin:1.6em 0 .6em;border-bottom:2px solid var(--line);padding-bottom:.2em}} small{{color:var(--muted);font-weight:normal}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin:14px 0}}
.card.done{{border-color:var(--acc)}} .card header{{display:flex;flex-wrap:wrap;gap:.6em;align-items:baseline}}
.card h3{{margin:0;font-size:1.1em}} .cid{{font-family:monospace;color:var(--acc)}} .where{{color:var(--muted);font-size:.9em}}
.lat{{font-style:italic;margin:.5em 0}} .q{{margin:.5em 0}}
.opt{{display:flex;gap:.6em;padding:.5em;border-radius:8px;cursor:pointer}} .opt:hover{{background:var(--rec)}}
.ob{{display:flex;flex-direction:column;gap:.15em}} .r{{font-size:.95em}} .meta{{color:var(--muted);font-size:.85em}}
.lg{{font:600 .7em sans-serif;color:var(--muted);border:1px solid var(--line);border-radius:4px;padding:0 .3em}}
.chip{{background:var(--chip);border-radius:4px;padding:0 .35em;font:600 .8em sans-serif}} .none{{color:var(--muted)}}
.rec{{background:var(--rec);border-radius:8px;padding:.6em .8em;margin:.6em 0}} .rec button{{margin-left:.6em}}
details{{margin:.4em 0}} .ev{{white-space:pre-wrap;font-size:.92em}}
textarea{{width:100%;box-sizing:border-box;min-height:2.4em;font:inherit;background:var(--bg);color:var(--fg);border:1px solid var(--line);border-radius:6px;padding:.3em .5em}}
button{{font:600 .9em sans-serif;background:var(--acc);color:var(--card);border:0;border-radius:6px;padding:.4em .8em;cursor:pointer}}
.bar{{position:fixed;left:0;right:0;bottom:0;background:var(--card);border-top:1px solid var(--line)}}
.bar .in{{max-width:980px;margin:0 auto;padding:8px 16px;display:flex;flex-wrap:wrap;gap:.6em;align-items:center}}
#out{{display:none}} ul.agreed li{{margin:.4em 0}}
</style></head><body><main>
<h1>Решения по переводам латинских версий «Синопсиса Музыки»</h1>
<p>Ксиландр (1556) и Вине (1591), четыре независимых перевода на русский и английский (A–D), три слепых сравнения (Claude, GPT-6.2 Sol, GPT-6.2 Astra).
Карточек {len(cards)}: общих {len(groups[0][1])}, по местам у Ксиландра {len(groups[1][1])}, у Вине {len(groups[2][1])}.
В них собраны все вопросы, которые сравнивающие вынесли редактору ({cov.get('items_total', '—')}); пункты, в которых все три сравнения и доводы сходятся, перечислены в конце ({len(D['agreed'])}).</p>
<p>Сравнивающий Claude чаще ставил выше переводы A и C, сравнивающие GPT — B и D; рекомендации опираются на доводы, а не на число голосов.
Выберите вариант, своё решение или «Принять рекомендацию». Выбор сохраняется в браузере. В конце нажмите «Скопировать решения» и вставьте текст в чат.</p>
<details><summary>Метки переводов</summary><ul>{key}</ul></details>
{''.join(body)}
<h2>Согласовано без карточек <small>({len(D['agreed'])})</small></h2>
<ul class="agreed">{agreed}</ul>
<textarea id="agreed-cm" placeholder="Замечания к согласованным пунктам (необязательно)"></textarea>
</main>
<div class="bar"><div class="in"><span id="prog"></span>
<button id="all">Принять все рекомендации там, где нет решения</button>
<button id="copy">Скопировать решения</button><span id="msg"></span></div></div>
<textarea id="out" readonly></textarea>
<script>
const KEY = 'neoscholia-latin-decisions-2026-11';
let st = {{}};
try {{ st = JSON.parse(localStorage.getItem(KEY) || '{{}}') }} catch (e) {{}}
const save = () => {{ try {{ localStorage.setItem(KEY, JSON.stringify(st)) }} catch (e) {{}} }};
const cards = [...document.querySelectorAll('.card')];
function paint() {{
  let n = 0;
  for (const c of cards) {{
    const s = st[c.dataset.id] || {{}};
    c.querySelectorAll('input[type=radio]').forEach(r => r.checked = (s.v === r.value));
    c.querySelector('.own').value = s.own || '';
    c.querySelector('.cm').value = s.cm || '';
    const done = !!s.v; c.classList.toggle('done', done); if (done) n++;
    c.querySelector('.take').textContent = s.v === 'rec' ? 'Рекомендация принята' : 'Принять рекомендацию';
  }}
  document.getElementById('agreed-cm').value = st._agreed || '';
  document.getElementById('prog').textContent = `Решено ${{n}} из ${{cards.length}}`;
}}
for (const c of cards) {{
  const id = c.dataset.id;
  c.querySelectorAll('input[type=radio]').forEach(r => r.addEventListener('change', () => {{ st[id] = {{...(st[id] || {{}}), v: r.value}}; save(); paint(); }}));
  c.querySelector('.own').addEventListener('input', e => {{ st[id] = {{...(st[id] || {{}}), v: 'own', own: e.target.value}}; save(); paint(); }});
  c.querySelector('.cm').addEventListener('input', e => {{ st[id] = {{...(st[id] || {{}}), cm: e.target.value}}; save(); }});
  c.querySelector('.take').addEventListener('click', () => {{ st[id] = {{...(st[id] || {{}}), v: 'rec'}}; save(); paint(); }});
}}
document.getElementById('agreed-cm').addEventListener('input', e => {{ st._agreed = e.target.value; save(); }});
document.getElementById('all').addEventListener('click', () => {{ for (const c of cards) {{ const id = c.dataset.id; if (!(st[id] || {{}}).v) st[id] = {{...(st[id] || {{}}), v: 'rec'}}; }} save(); paint(); }});
document.getElementById('copy').addEventListener('click', async () => {{
  const lines = ['Решения по латинским переводам («Синопсис Музыки»):'];
  for (const c of cards) {{
    const id = c.dataset.id, s = st[id] || {{}};
    let a = '— нет решения —';
    if (s.v === 'rec') a = 'рекомендация';
    else if (s.v === 'own') a = 'своё: ' + (s.own || '');
    else if (s.v) {{ const r = c.querySelector(`input[value="${{s.v}}"]`); a = s.v + ' — ' + (r ? r.dataset.label : ''); }}
    lines.push(`${{id}}: ${{a}}`);
    if (s.cm) lines.push(`${{id}} — комментарий: ${{s.cm}}`);
  }}
  if (st._agreed) lines.push('Согласованные пункты — замечания: ' + st._agreed);
  const text = lines.join('\\n');
  const out = document.getElementById('out'); out.value = text;
  try {{ await navigator.clipboard.writeText(text); document.getElementById('msg').textContent = 'Скопировано. Вставьте в чат.' }}
  catch (e) {{ out.style.display = 'block'; out.select(); document.getElementById('msg').textContent = 'Скопируйте текст из поля.' }}
}});
paint();
</script></body></html>'''
open(f'{L}/decisions/decisions.html', 'w', encoding='utf-8').write(page)
print('cards', len(cards), '| agreed', len(D['agreed']), '->', f'{L}/decisions/decisions.html')
