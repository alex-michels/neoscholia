"""Audit a Claude agent transcript (jsonl): every tool call with its target. Flags file paths outside the translator's folder,
web URLs and search queries, and hits of forbidden sources. Usage: python -I audit_agent_log.py <agent.jsonl> <folder>"""
import collections, json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
LOG, FOLDER = sys.argv[1], sys.argv[2].replace('\\', '/').lower()
calls = []
for line in open(LOG, encoding='utf-8'):
    try:
        e = json.loads(line)
    except Exception:
        continue
    msg = e.get('message') or {}
    for c in (msg.get('content') or []) if isinstance(msg.get('content'), list) else []:
        if c.get('type') == 'tool_use':
            calls.append((c.get('name'), c.get('input') or {}))
print('tool calls:', len(calls), collections.Counter(n for n, _ in calls).most_common())
PATHKEYS = ('file_path', 'path', 'notebook_path')
outside, urls, queries, cmds = [], [], [], []
for n, i in calls:
    for k in PATHKEYS:
        p = str(i.get(k) or '').replace('\\', '/')
        if p and not p.lower().startswith(FOLDER):
            outside.append((n, p))
    if n in ('Bash', 'PowerShell'):
        c = i.get('command', '')
        cmds.append(c)
        for p in re.findall(r'[A-Za-z]:[\\/][^\s"\'|;)]*|/[a-z]/[^\s"\'|;)]*', c):
            q = p.replace('\\', '/').lower()
            if FOLDER not in q and not q.startswith(('c:/windows', '/c/windows')) and 'python' not in q:
                outside.append((n, p))
        urls += re.findall(r'https?://[^\s"\'<>)]+', c)
    if n == 'WebFetch':
        urls.append(i.get('url', ''))
    if n == 'WebSearch':
        queries.append(i.get('query', ''))
    if n == 'Agent' or n == 'Task':
        print('SUBAGENT prompt head:', str(i.get('prompt', ''))[:200])
print('\npaths outside the folder:', collections.Counter(outside).most_common(20) or 'none')
dom = collections.Counter(re.sub(r'^https?://([^/]+).*', r'\1', u) for u in urls)
print('\nweb domains:', dom.most_common(25))
print('\nweb searches (%d):' % len(queries))
for q in queries:
    print('  -', q)
FORB = ['heiberg', 'anonymi logica', 'quadrivium', 'mizler', 'xylander', 'vinet', 'alard', 'gertsman', 'герцман', 'mambro',
        'katsiampoura', 'benakis', 'bryenn', 'pachymer', 'zonara', 'italic', 'rhakendyt', 'notices et extraits', 'neoscholia',
        'alex-michels', 'psell', 'synopsis of music', 'aneponym']
hits = collections.Counter()
for u in urls + queries:
    for k in FORB:
        if k in u.lower():
            hits[(k, u[:160])] += 1
print('\nforbidden terms in URLs/queries:', hits.most_common() or 'none')
