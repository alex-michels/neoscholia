"""Merge the three blind comparisons of the four Latin translations (Claude workflow; GPT-6.2 Sol and GPT-6.2 Astra in
Codex) into one per-segment file, count agreement, and list the major errors that only one reviewer found (to be
rechecked). Labels stay anonymous (A–D).
Usage: python -I merge_comparisons.py <latin-translations folder>"""
import collections, json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
L = sys.argv[1]
REV = ['claude', 'sol', 'astra']
C = {r: json.load(open(f'{L}/comparisons/{r}.json', encoding='utf-8')) for r in REV}
SRC = json.load(open(f'{L}/independent/latin-texts.json', encoding='utf-8'))
LAT = {s['id']: (w, s['latin']) for w in ('xylander', 'vinet') for s in SRC[w]['segments']}
IDS = [s['id'] for w in ('xylander', 'vinet') for s in SRC[w]['segments']]


def words(s):
    return set(re.findall(r'\w{3,}', (s or '').lower()))


def labels(x):
    return set(re.findall(r'\b([A-D])\b', x or ''))


merged, singles, corroborated = {}, [], []
best = {r: {'ru': collections.Counter(), 'en': collections.Counter()} for r in REV}
for sid in IDS:
    w, lat = LAT[sid]
    seg = {'version': w, 'latin': lat, 'reviewers': {}}
    for r in REV:
        s = next(x for x in C[r]['segments'] if x['id'] == sid)
        seg['reviewers'][r] = {k: s.get(k) for k in ('sense', 'divergences', 'errors', 'text_issues_review', 'best_ru',
                                                     'best_en', 'notes_to_keep', 'editor_questions')}
        for lang in ('ru', 'en'):
            for lab in labels(s[f'best_{lang}']['translator']):
                best[r][lang][lab] += 1
    merged[sid] = seg
    # major errors: does another reviewer flag the same translator here with overlapping words?
    for r in REV:
        for e in seg['reviewers'][r]['errors']:
            if e.get('severity') != 'major':
                continue
            q = words(e.get('quote')) | words(e.get('problem'))
            others = []
            for r2 in REV:
                if r2 == r:
                    continue
                for e2 in seg['reviewers'][r2]['errors']:
                    if e2['translator'] == e['translator'] and (len(q & (words(e2.get('quote')) | words(e2.get('problem')))) >= 2):
                        others.append({'reviewer': r2, 'severity': e2.get('severity'), 'quote': e2.get('quote')})
            item = {'segment': sid, 'version': w, 'reviewer': r, 'translator': e['translator'], 'lang': e.get('lang'),
                    'type': e.get('type'), 'quote': e.get('quote'), 'problem': e.get('problem'), 'fix': e.get('fix'),
                    'also_flagged_by': others}
            (corroborated if any(o['severity'] == 'major' for o in others) else singles).append(item)
stats = {'best': {r: {lang: dict(best[r][lang].most_common()) for lang in ('ru', 'en')} for r in REV},
         'errors': {r: dict(collections.Counter((e['translator'], e['severity']) for s in C[r]['segments'] for e in s['errors']).most_common())
                    for r in REV},
         'divergences': {r: sum(len(s['divergences']) for s in C[r]['segments']) for r in REV},
         'to_editor': {r: sum(1 for s in C[r]['segments'] for d in s['divergences'] if d.get('to_editor')) for r in REV},
         'editor_questions': {r: sum(len(s.get('editor_questions') or []) for s in C[r]['segments']) for r in REV}}
stats['errors'] = {r: {f'{k[0]} {k[1]}': v for k, v in d.items()} for r, d in stats['errors'].items()}
json.dump({'note': 'three blind comparisons merged by segment; labels A–D anonymous', 'stats': stats, 'segments': merged,
           'major_single': singles, 'major_corroborated': corroborated},
          open(f'{L}/comparisons/merged.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(stats, ensure_ascii=False, indent=1))
print('major errors found by one reviewer only (some also flagged as minor by another):', len(singles),
      collections.Counter((x['reviewer'], x['translator']) for x in singles))
print('major errors corroborated as major:', len(corroborated))
