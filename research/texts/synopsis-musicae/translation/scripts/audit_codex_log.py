"""Audit Codex session logs (rollout-*.jsonl) of one run: the sessions' working folders, every command and web action,
paths outside the run folder, web domains and searches, and hits of forbidden terms (other runs' folders, earlier
translations or editions of the text). Reads only the given log files.
Usage: python -I audit_codex_log.py <run folder> <rollout.jsonl> [...]"""
import collections, json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = sys.argv[1].replace('\\', '/').lower().rstrip('/')
FORB = ['heiberg', 'quadrivium', 'anonymi logica', 'mizler', 'xylander', 'vinet', 'alard', 'vincent', 'notices et extraits', 'neoscholia',
        'alex-michels', 'synopsis of music', 'synopsis musicae', 'μουσικῆς σύνοψις', 'gertsman', 'герцман', 'psell', 'pachymer',
        'ws-cmp', 'ws-r7', 'neoscholia-runs', 'sol-comparison', 'claude-comparison', 'translations-2026', 'auth.json']
cmds, searches, urls, outside, cwds, hits = [], [], [], collections.Counter(), set(), collections.Counter()


def strings(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, dict):
        for v in x.values():
            yield from strings(v)
    elif isinstance(x, list):
        for v in x:
            yield from strings(v)


for f in sys.argv[2:]:
    for line in open(f, encoding='utf-8'):
        try:
            e = json.loads(line)
        except Exception:
            continue
        p = e.get('payload') or {}
        if e.get('type') in ('session_meta', 'turn_context') and p.get('cwd'):
            cwds.add(p['cwd'])
        if e.get('type') != 'response_item':
            continue
        t = p.get('type')
        acts = []
        if t in ('function_call', 'custom_tool_call', 'local_shell_call'):
            a = p.get('arguments') or p.get('input') or p.get('action') or ''
            try:
                a = json.loads(a) if isinstance(a, str) else a
            except Exception:
                pass
            acts = list(strings(a))
            cmds.append(' '.join(acts)[:300])
        elif t == 'web_search_call':
            a = p.get('action') or {}
            acts = list(strings(a))
            if a.get('query'):
                searches.append(a['query'])
            for q in a.get('queries') or []:
                searches.append(q)
            if a.get('url'):
                urls.append(a['url'])
        for s in acts:
            urls += re.findall(r'https?://[^\s"\'<>)\]]+', s)
            for m in re.findall(r'[A-Za-z]:[\\/][^\s"\'|;)<>]*', s):
                q = m.replace('\\', '/').lower()
                if not q.startswith(RUN) and not q.startswith(('c:/windows', 'c:/python', 'c:/program files')):
                    outside[m[:120]] += 1
            low = s.lower()
            for k in FORB:
                if k in low:
                    hits[(k, s[:160].replace('\n', ' '))] += 1

print('session folders:', sorted(cwds))
print('commands:', len(cmds), '| web searches:', len(searches), '| urls:', len(urls))
print('\npaths outside the run folder:', outside.most_common(30) or 'none')
print('\nweb domains:', collections.Counter(re.sub(r'^https?://([^/]+).*', r'\1', u) for u in urls).most_common(40))
print('\nweb searches:')
for q in searches:
    print('  -', q)
print('\nforbidden terms:', hits.most_common(40) or 'none')
