"""Build the anonymised inputs for the comparison of the six translations: four groups with neighbouring context units,
the label order rotating from unit to unit, the Greek with line markers, the translators' brief without any real path.
Usage: python -I build_cmp_inputs.py <out folder> <label key json>"""
import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
OUT, KEYF = sys.argv[1], sys.argv[2]
KEY = json.load(open(KEYF, encoding='utf-8'))
LAB = list(KEY)
g = json.load(open('<runs>/synopsis-musicae-translations-2026-10-31/ws-a1/greek-text.json', encoding='utf-8'))
T = {L: json.load(open(f'<runs>/synopsis-musicae-translations-2026-10-31/ws-{f}/translation.json', encoding='utf-8')) for L, f in KEY.items()}
U = {L: {u['id']: u for u in T[L]['units']} for L in KEY}
order = [u['id'] for u in g['units']]
GROUPS = {1: ('U001', 'U025', [], ['U026']), 2: ('U026', 'U036', ['U025'], ['U037']),
          3: ('U037', 'U045', ['U036'], ['U046']), 4: ('U046', 'U067', ['U045'], [])}


TRACE = [  # working-environment traces in the translators' notes and sources (not in their ru/en translations)
    (r'\[checked:\s*[\w.-]+\.(?:com|org|edu|net|gr|de)/[^\]]*\]', '[checked]'),
    (r'\s*\(https?://[^)\s]+\)', ''),
    (r'Logeion XML greatscott\d+\.xml:\s*', 'Logeion '),
    (r'greatscott\d+\.xml', 'LSJ'),
    (r'https?://[^\s;)\]]+', ''),
    (r'official Logeion/Perseus XML', 'Logeion'),
    (r'\[checked by delegated [^\]]*\]', '[checked]'),
    (r';?\s*entry read in the delegated lexicon audit', ''),
    (r'\s*by the delegated lexicon search', ''),
    (r'\s*\(?delegated (lexicon|music|arithmetic|parallels?)( and \w+)? (audit|search|review)\)?', ''),
    (r'in the inspected LSJ auto- compound file', 'in LSJ'),
    (r'\b[Ss]upplied (?=(apparatus|critical text|definition|Greek|greek-text|about\.md|U\d|edition description))', ''),
    (r'\[checked: archive\.org OCR\]', '[checked]'),
    (r'First1KGreek:\s*\(', 'First1KGreek ('),          # debris left where a link was removed
    (r',?\s*main Greek text:\s*(?=[.;,\]]|$)', ''),
    (r':\s+(?=[.;])', ''),
    (r'\s+;', ';'),
    (r'\[checked\]:\s*;', '[checked];'),
    (r'\s{2,}', ' '),
]
NTRACE = {'n': 0}


def clean(x, top=True):
    """Remove traces from every string, except a unit's own ru/en translation (top level)."""
    if isinstance(x, str):
        y = x
        for a, b in TRACE:
            y = re.sub(a, b, y)
        if y != x:
            NTRACE['n'] += 1
        return y.strip()
    if isinstance(x, list):
        return [clean(v, False) for v in x]
    if isinstance(x, dict):
        return {k: (v if top and k in ('ru', 'en') else clean(v, False)) for k, v in x.items()}
    return x


def unit_entry(u, k, context):
    rot = LAB[k % 6:] + LAB[:k % 6]
    e = {x: u[x] for x in ('id', 'section', 'bas', 'p_only', 'paragraph_start', 'greek', 'greek_with_lines') if x in u}
    if 'p_fragment' in u:
        e['p_fragment'] = u['p_fragment']
    if context:
        e['context_only'] = 'Context only: this unit belongs to the neighbouring group. Read it; do not judge it.'
    e['translations'] = {L: clean({f: U[L][u['id']].get(f) for f in ('ru', 'en', 'doctrine', 'checks', 'notes', 'doubts')}) for L in rot}
    return e


for gi, (a, b, before, after) in GROUPS.items():
    i, j = order.index(a), order.index(b)
    core = g['units'][i:j + 1]
    ids = {u['id'] for u in core}
    secs = sorted({u['section'] for u in core})
    units = ([unit_entry(u, order.index(u['id']), True) for u in g['units'] if u['id'] in before]
             + [unit_entry(u, order.index(u['id']), False) for u in core]
             + [unit_entry(u, order.index(u['id']), True) for u in g['units'] if u['id'] in after])
    out = {'group': gi, 'units_to_judge': f'{a}-{b}', 'sections': secs, 'units': units,
           'apparatus': [x for x in g['apparatus'] if x['section'] in secs],
           'text_issues': {L: clean([x for x in (T[L].get('text_issues') or []) if str(x.get('unit')) in ids], False) for L in LAB}}
    json.dump(out, open(f'{OUT}/group-{gi}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('group', gi, a, '-', b, '+ context', before + after)

json.dump({'units': [{x: u[x] for x in ('id', 'section', 'bas', 'p_only', 'greek', 'greek_with_lines') if x in u}
                     | ({'p_fragment': u['p_fragment']} if 'p_fragment' in u else {}) for u in g['units']]},
          open(f'{OUT}/greek-units.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({L: clean(T[L].get('terms') or [], False) for L in LAB}, open(f'{OUT}/terms.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('strings cleaned of traces:', NTRACE['n'])

p = open('<runs>/synopsis-musicae-translations-2026-10-31/ws-a1/PROMPT.md', encoding='utf-8').read()
p = re.sub(r'`[A-Za-z]:\\[^`]*`', "`(each translator's own folder)`", p)
p = p.replace('## Independence rules', "## Independence rules\n\n*This is the translators' brief. Its folder rules applied to them, not to you.*", 1)
assert __import__('getpass').getuser() not in p and 'Documents' not in p
open(f'{OUT}/translation-brief.md', 'w', encoding='utf-8').write(p)

blob = ''.join(open(f'{OUT}/{f}', encoding='utf-8').read() for f in
               ['group-1.json', 'group-2.json', 'group-3.json', 'group-4.json', 'terms.json', 'greek-units.json', 'translation-brief.md', 'about.md'])
for k in ['Claude', 'Opus', 'Sonnet', 'GPT', 'Kimi', 'Moonshot', 'OpenAI', 'Anthropic', 'Terra', 'Astra', 'Codex', 'Copilot', __import__('getpass').getuser(), 'ws-',
          r'https?://', 'raw\\.github', 'greatscott', r'\bXML\b', 'delegat', r'[Ss]upplied (apparatus|U\d|Greek|greek-text|critical|definition|about)']:
    n = len(re.findall(k, blob))
    if n:
        print('MENTION', k, n, [blob[max(0, m.start() - 60): m.end() + 40] for m in list(re.finditer(k, blob))[:2]])
print('rebuilt')
