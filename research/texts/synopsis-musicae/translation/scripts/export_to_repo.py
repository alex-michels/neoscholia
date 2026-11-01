"""Copy the final translation of the Synopsis of music and the material of its making (six translations, three
comparisons, the editor's decisions, the composition and check logs, the scripts) into the repo, replacing local
paths with placeholders. Refuses to finish if a local path or the Windows user name survives.
Usage: python -I export_to_repo.py <ws-cmp folder> <translations runs folder> <repo text folder>"""
import json, os, re, shutil, sys
sys.stdout.reconfigure(encoding='utf-8')
WS, TR, DEST = (p.replace('\\', '/').rstrip('/') for p in sys.argv[1:4])
OUT = DEST + '/translation'
HOME = re.sub(r'^([A-Za-z]:/Users/[^/]+).*$', r'\1', WS)
USER = HOME.rsplit('/', 1)[1]
RUNS = WS.split('/Neoscholia-runs/')[0] + '/Neoscholia-runs'
REPO = DEST.split('/research/')[0]

# longest first; each also matched with backslashes and escaped backslashes
PREFIXES = [(WS, '<ws-cmp>'), (TR, '<runs>/' + TR.rsplit('/', 1)[1]), (RUNS, '<runs>'), (REPO, '<repo>'),
            (os.environ.get('TEMP', HOME + '/tmp').replace('\\', '/'), '<tmp>'), (HOME + '/.claude', '<claude>'), (HOME + '/Documents', '<documents>'),
            (HOME, '<home>'), ('/c/Users/' + USER, '<home>')]


def variants(p):
    for sep in ('/', '\\', '\\\\'):
        yield p.replace('/', sep)


PAT = []
for p, ph in PREFIXES:
    for v in variants(p):
        PAT.append((re.compile(re.escape(v), re.I), ph))
        if re.match(r'[A-Za-z]:', v):
            PAT.append((re.compile(re.escape(v[0].swapcase() + v[1:]), re.I), ph))


def clean(text):
    for rx, ph in PAT:
        text = rx.sub(ph, text)
    return text


copied = []


def put(src, rel):
    dst = f'{OUT}/{rel}'
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    text = open(src, encoding='utf-8').read()
    out = clean(text)
    if src.endswith('.py'):  # leak checks in the scripts name the user: compute it instead of spelling it
        out = re.sub(rf"(['\"]){re.escape(USER)}\1", "__import__('getpass').getuser()", out)
    if src.endswith('.json'):
        json.loads(out)  # still valid after cleaning
    open(dst, 'w', encoding='utf-8', newline='\n').write(out)
    copied.append(rel)


# the final translation
put(f'{WS}/compose/assembled/translation.json', 'translation.json')
put(f'{WS}/compose/assembled/translation.md', 'translation.md')
# the six independent translations, under their labels and models
KEY = {'A': ('e5', 'sonnet-5.5'), 'B': ('a1', 'gpt-6.1-terra'), 'C': ('f6', 'kimi-k3'), 'D': ('c3', 'gpt-6-astra'),
       'E': ('d4', 'opus-5.5'), 'F': ('b2', 'gpt-6.1-sol')}
for lab, (run, model) in KEY.items():
    for ext in ('json', 'md'):
        put(f'{TR}/ws-{run}/translation.{ext}', f'independent/{lab}-{model}.{ext}')
# the three comparisons and their inputs
put(f'{WS}/claude-comparison/result.json', 'comparisons/claude.json')
for m in ('sol', 'astra'):
    for ext in ('json', 'md'):
        put(f'{WS}/{m}-comparison/comparison.{ext}', f'comparisons/{m}.{ext}')
for f in ('about.md', 'translation-brief.md', 'terms.json', 'greek-units.json'):
    put(f'{WS}/inputs/{f}', f'comparisons/inputs/{f}')
for f in ('PROMPT-codex.md', 'PROMPT-codex-v2.md'):
    put(f'{WS}/scripts/{f}', f'comparisons/inputs/{f}')
put(f'{WS}/astra-vs-decisions.txt', 'comparisons/astra-vs-decisions.txt')
put(f'{WS}/single-major.txt', 'comparisons/single-major-recheck.txt')
# the editor's decisions and the term research
put(f'{WS}/editor-decisions-raw.txt', 'decisions/editor-decisions.txt')
for f in ('DECISIONS.md', 'cards.md', 'glossary.md'):
    put(f'{WS}/compose/{f}', f'decisions/{f}')
put(f'{WS}/terms-research/finals-all.md', 'decisions/term-research.md')
put(f'{WS}/terms-research/consistency-issues.md', 'decisions/term-consistency-issues.md')
# composition, verification, consistency, fact-check
put(f'{WS}/compose/BRIEF.md', 'logs/compose-brief.md')
for f in sorted(os.listdir(f'{WS}/compose/final')):
    if f.endswith('.md'):
        put(f'{WS}/compose/final/{f}', f'logs/{f}')
for f in sorted(os.listdir(f'{WS}/compose/factcheck')):
    if f.endswith('.md'):
        put(f'{WS}/compose/factcheck/{f}', f'logs/factcheck/{f}')
# scripts
for f in sorted(os.listdir(f'{WS}/scripts')):
    if f.endswith('.py'):
        put(f'{WS}/scripts/{f}', f'scripts/{f}')

# nothing local may survive
bad = re.compile(rf'{re.escape(USER)}|[A-Za-z]:[\\/]+Users|AppData|/c/Users|@gmail', re.I)
left = []
for rel in copied:
    for i, line in enumerate(open(f'{OUT}/{rel}', encoding='utf-8'), 1):
        hit = bad.search(line)
        if hit and (not rel.endswith('.py') or hit.group(0).lower() == USER.lower() or '@' in hit.group(0)):
            left.append(f'{rel}:{i}: {hit.group(0)}')
print(len(copied), 'files copied to', OUT.replace(REPO, '<repo>'))
if left:
    print('LOCAL TRACES LEFT:', len(left))
    print('\n'.join(left[:40]))
    sys.exit(1)
print('no local traces')
