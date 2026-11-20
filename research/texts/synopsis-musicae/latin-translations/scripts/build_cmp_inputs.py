"""Build the anonymised inputs for the comparison of the four translations of the Latin versions: four groups
(Xylander X01–X29, X30–X58; Vinet V01–V33, V34–V66) with a neighbouring context segment, the label order rotating
from segment to segment, the translators' brief without any real path, and the term lists. Links and traces of the
working environment are removed from notes, checks, doubts, terms and text issues (never from the ru/en translations).
Usage: python -I build_cmp_inputs.py <latin-translations folder> <out folder>"""
import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
L, OUT = sys.argv[1], sys.argv[2]
FILES = {'A': 'A-fable-5.2', 'B': 'B-gpt-6.2-sol', 'C': 'C-opus-5.5', 'D': 'D-gpt-6.2-astra'}
LAB = list(FILES)
T = {k: json.load(open(f'{L}/translations/{v}.json', encoding='utf-8')) for k, v in FILES.items()}
SRC = json.load(open(f'{L}/independent/latin-texts.json', encoding='utf-8'))
S = {k: {w: {s['id']: s for s in T[k]['versions'][w]['segments']} for w in ('xylander', 'vinet')} for k in LAB}
GROUPS = [('xylander', 'X01', 'X29'), ('xylander', 'X30', 'X58'), ('vinet', 'V01', 'V33'), ('vinet', 'V34', 'V66')]

TRACE = [
    (r'\[checked:\s*[^\]]*\]', '[checked]'),
    (r'\[from memory:\s*[^\]]*\]', '[from memory]'),
    (r'\s*\(\s*https?://[^)\s]+\s*\)', ''),
    (r'\s*<https?://[^>\s]+>', ''),
    (r',?\s*https?://[^\s;,)\]"]+[.,]?', ''),
    (r'\b(?:online at|via|at|on|from)\s+(?:[\w-]+\.)+(?:com|org|edu|net|de|fr|gr|io|ru)\b(?:/\S*)?', ''),
    (r'\b(?:[\w-]+\.)+(?:com|org|edu|net|de|fr|gr|io|ru)\b(?:/\S*)?', ''),
    (r'\(\s*\)', ''),
    (r'\s+([;,.])', r'\1'),
    (r'\s{2,}', ' '),
]
NT = {'n': 0}


def clean(x, top=True):
    """Remove links and traces from every string, except a segment's own ru/en translation (top level)."""
    if isinstance(x, str):
        y = x
        for a, b in TRACE:
            y = re.sub(a, b, y)
        if y != x:
            NT['n'] += 1
        return y.strip()
    if isinstance(x, list):
        return [clean(v, False) for v in x]
    if isinstance(x, dict):
        return {k: (v if top and k in ('ru', 'en') else clean(v, False)) for k, v in x.items()}
    return x


def entry(w, seg, k, context):
    rot = LAB[k % 4:] + LAB[:k % 4]
    e = {x: seg[x] for x in ('id', 'starts_paragraph', 'heading', 'ref', 'latin', 'printed') if x in seg}
    if context:
        e['context_only'] = 'Context only: this segment belongs to the neighbouring group. Read it; do not judge it.'
    e['translations'] = {lab: clean({f: S[lab][w][seg['id']].get(f) for f in ('ru', 'en', 'checks', 'notes', 'doubts')}) for lab in rot}
    return e


os.makedirs(OUT, exist_ok=True)
for gi, (w, a, b) in enumerate(GROUPS, 1):
    segs = SRC[w]['segments']
    ids = [s['id'] for s in segs]
    i, j = ids.index(a), ids.index(b)
    core = segs[i:j + 1]
    units = ([entry(w, segs[i - 1], i - 1, True)] if i > 0 else []) + [entry(w, s, ids.index(s['id']), False) for s in core] \
        + ([entry(w, segs[j + 1], j + 1, True)] if j + 1 < len(segs) else [])
    core_ids = {s['id'] for s in core}
    out = {'group': gi, 'version': w, 'segments_to_judge': f'{a}–{b}', 'segments': units,
           'corrections': SRC[w]['corrections'],
           'text_issues': {lab: clean([x for x in (T[lab].get('text_issues') or []) if str(x.get('segment')) in core_ids], False) for lab in LAB}}
    if w == 'vinet':
        out['chapters'] = SRC[w]['chapters']
    json.dump(out, open(f'{OUT}/group-{gi}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('group', gi, w, a, '-', b, len(units), 'segments with context')
json.dump({lab: clean(T[lab].get('terms') or [], False) for lab in LAB}, open(f'{OUT}/terms.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(SRC, open(f'{OUT}/latin-texts.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('strings cleaned of traces:', NT['n'])

p = open(f'{L}/independent/PROMPT.md', encoding='utf-8').read()
p = p.replace('`{FOLDER}`', "`(each translator's own folder)`")
p = p.replace('## Independence rules', "## Independence rules\n\n*This is the translators' brief. Its folder rules applied to them, not to you.*", 1)
open(f'{OUT}/translation-brief.md', 'w', encoding='utf-8').write(p)
a = open(f'{L}/independent/about.md', encoding='utf-8').read()
open(f'{OUT}/about.md', 'w', encoding='utf-8').write(a)

blob = ''.join(open(f'{OUT}/{f}', encoding='utf-8').read() for f in sorted(os.listdir(OUT)) if f.endswith(('.json', '.md')))
bad = 0
for k in ['Claude', 'Opus', 'Fable', 'Sonnet', 'GPT', 'OpenAI', 'Anthropic', 'Astra', 'Codex', __import__('getpass').getuser(),
          r'ws-l\d', r'https?://', r'\.github\.io', r'\bdelegat', r'\bsubagent', 'Neoscholia-runs']:
    n = len(re.findall(k, blob))
    if n:
        bad += 1
        print('MENTION', k, n, [blob[max(0, m.start() - 60): m.end() + 40] for m in list(re.finditer(k, blob))[:2]])
print('no traces' if not bad else 'TRACES LEFT')
