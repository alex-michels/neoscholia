"""Check one independent translation: completeness of translation.json, and from the run log: tokens, web use, URLs by domain,
paths outside the translator's folder, and hits of forbidden sources. Usage: python -I check_tr.py <folder> [<log>]"""
import collections, json, re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
D = Path(sys.argv[1]); LOG = Path(sys.argv[2]) if len(sys.argv) > 2 else None
g = json.load(open(D / 'greek-text.json', encoding='utf-8'))
ids = [u['id'] for u in g['units']]
try:
    t = json.load(open(D / 'translation.json', encoding='utf-8'))
except Exception as e:
    print('JSON ERROR:', e); t = None
if t:
    us = t.get('units', [])
    print('translator:', json.dumps(t.get('translator'), ensure_ascii=False))
    print('units', len(us), '| ids in order:', [u.get('id') for u in us] == ids,
          '| empty ru/en:', [u.get('id') for u in us if not (u.get('ru') or '').strip() or not (u.get('en') or '').strip()])
    print('notes', sum(len(u.get('notes') or []) for u in us), '| doubts', sum(len(u.get('doubts') or []) for u in us),
          '| terms', len(t.get('terms') or []), '| text_issues', len(t.get('text_issues') or []))
    refs = json.dumps(t, ensure_ascii=False)
    print('[checked]', refs.count('[checked]'), '| [from memory]', refs.count('[from memory]'))
    print('contamination:', json.dumps(t.get('contamination'), ensure_ascii=False)[:600])
    print('summary:', (t.get('summary') or '')[:500])
if LOG and LOG.exists():
    L = LOG.read_text(encoding='utf-8', errors='replace')
    m = re.findall(r'tokens used\s*\n?\s*([\d.,]+)', L)
    print('tokens used:', m[-1] if m else '?')
    urls = re.findall(r'https?://([^/\s"\'<>)\]]+)', L)
    print('URL domains:', collections.Counter(urls).most_common(14))
    outside = [p for p in re.findall(r'[A-Za-z]:[\\/][^\s"\'<>|]*', L) if D.name.lower() not in p.lower() and 'powershell' not in p.lower()
               and 'system32' not in p.lower()]
    print('paths outside the folder:', collections.Counter(outside).most_common(8))
    FORB = ['heiberg', 'anonymi logica', 'quadrivium of 1008', 'mizler', 'xylander', 'vinet', 'alard', 'gertsman', 'герцман', 'di mambro',
            'katsiampoura', 'benakis', 'bryennius', 'pachymeres', 'zonaras', 'italicus', 'rhakendytes', 'notices et extraits', 'neoscholia',
            'alex-michels', 'psellus', 'psellos']
    low = L.lower()
    print('forbidden-term hits in log:', {k: low.count(k) for k in FORB if low.count(k)})
