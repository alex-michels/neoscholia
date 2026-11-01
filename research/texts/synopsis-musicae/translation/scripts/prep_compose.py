"""Packets for composing the final Russian and English translation from the six independent ones.
Writes into <ws-cmp>/compose/:
  units/Uxxx.md   one file per unit: Greek, the edition's materials for its lines, the six translations,
                  the three reviews and the merged list of errors;
  cards.md        the editor's decision cards: question, options offered, the editor's choice and comment;
  term-finals.md  the verified term research (renderings of the six reopened cards marked superseded);
  glossary.md     every term of the three reviewers' glossaries with their recommendations.
Usage: python -I prep_compose.py <ws-cmp folder> <constituted text.json>"""
import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
O, TEXT = sys.argv[1], sys.argv[2]
C = f'{O}/compose'
os.makedirs(f'{C}/units', exist_ok=True)

def fmt(v):
    return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)


# --- decision cards, as on the editor's page ---
src = open(f'{O}/scripts/build_decisions.py', encoding='utf-8').read()
src = src[:src.index('used_div, used_term = set(), set()')]
ns = {'__name__': 'cards'}
argv = sys.argv
sys.argv = ['x', O, 'unused.html']
exec(compile(src, 'build_decisions.py', 'exec'), ns)
sys.argv = argv
CARDS = ns['POLICIES'] + ns['PLACES']

dec = {}
for line in open(f'{O}/editor-decisions-raw.txt', encoding='utf-8'):
    m = re.match(r'([PL]\d\d)( — комментарий)?: (.*)', line.strip())
    if m:
        dec.setdefault(m.group(1), {})['comment' if m.group(2) else 'choice'] = m.group(3)
REOPENED = {'P02': 'b', 'P03': 'a', 'P06': 'b', 'P09': 'b', 'P10': 'a', 'P11': 'a'}

out = ['# The editor\'s decision cards (31.10.2026)\n',
       'Each card: the question, the options offered, the editor\'s choice and comment. For P02, P03, P06, P09, P10 and P11 the editor '
       'chose again after the term research; the second choice refers to the options of the research, set out in DECISIONS.md, '
       'and it overrides the first.\n']
for c in CARDS:
    d = dec.get(c['id'], {})
    out.append(f"## {c['id']}. {c['title']}\n")
    out.append(f"**Question:** {c['q']}\n")
    for k, v in c['opts']:
        out.append(f"- option {k}: {v}")
    if c.get('note'):
        out.append(f"\n**Note on the page:** {c['note']}")
    out.append(f"\n**Editor's choice:** {d.get('choice', '-')}")
    if d.get('comment'):
        out.append(f"\n**Editor's comment:** {d['comment']}")
    if c['id'] in REOPENED:
        out.append(f"\n**Editor's second choice, after the term research:** {REOPENED[c['id']]} (see DECISIONS.md). It overrides the first.")
    out.append('\n')
open(f'{C}/cards.md', 'w', encoding='utf-8').write('\n'.join(out))

# --- verified term research ---
r = json.load(open(f'{O}/terms-research/workflow-output.txt', encoding='utf-8'))['result']
out = ['# Verified term research (31.10.2026)\n',
       'The finals of the research and verification agents, card by card. For P02, P03, P06, P09, P10 and P11 the editor chose again '
       '(DECISIONS.md): their main_ru / main_en below are SUPERSEDED, and their notes are material only, to be rewritten for the '
       'chosen renderings. The consistency review that follows was written before the editor\'s second choice.\n']
for g in r['groups']:
    for chk in g['verify']['checks']:
        f = chk['final']
        sup = chk['id'] in REOPENED
        out.append(f"## {chk['id']}{' — RENDERINGS SUPERSEDED, see DECISIONS.md' if sup else ''}\n")
        for k in ('main_ru', 'main_en', 'note_ru', 'note_en', 'units', 'alternatives', 'conflict_with_editor', 'open_points'):
            v = f.get(k)
            if v:
                lab = f'{k} (superseded)' if sup and k.startswith('main') else k
                out.append(f"**{lab}:** {v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)}\n")
        out.append(f"**verifier's corrections:** {chk['problems']}\n")
cons = r['consistency']
out.append('## Consistency review of all answers\n')
out.append(cons['summary'] + '\n')
for i, x in enumerate(cons['issues'], 1):
    out.append(f"{i}. [{x['ids']}] {x['problem']}\n   FIX: {x['fix']}\n")
open(f'{C}/term-finals.md', 'w', encoding='utf-8').write('\n'.join(out))

# --- glossary of the three reviewers ---
REC = json.load(open(f'{O}/reconcile.json', encoding='utf-8'))
A = json.load(open(f'{O}/astra-comparison/comparison.json', encoding='utf-8'))
out = ['# Glossary: the three reviewers\' recommendations (RU / EN)\n',
       'The editor raised no objection to the agreed glossary. Terms decided by a card follow DECISIONS.md and the cards instead. '
       'The reviewers\' reasons are in the unit packets.\n']
for t in REC['terms']:
    parts = []
    for who in ('claude', 'sol'):
        x = t.get(who)
        if x:
            parts.append(f"{who}: {x.get('recommended_ru')} / {x.get('recommended_en')} [{x.get('units')}]")
    gk = (t.get('claude') or t.get('sol') or {}).get('greek')
    out.append(f"- **{gk}** [{t.get('status')}] " + ' || '.join(parts))
out.append('\n## Astra\'s concordance\n')
for x in A['terms']:
    out.append(f"- **{x['greek']}**: {x.get('recommended_ru')} / {x.get('recommended_en')} [{x.get('units')}]")
open(f'{C}/glossary.md', 'w', encoding='utf-8').write('\n'.join(out))

# one file per card: the card, the verified research on it, and the consistency issues naming it
os.makedirs(f'{C}/cards', exist_ok=True)
FIN = {chk['id']: chk for g in r['groups'] for chk in g['verify']['checks']}
for c in CARDS:
    cid, d = c['id'], dec.get(c['id'], {})
    o = [f"# {cid}. {c['title']}", '', f"**Question:** {c['q']}", '']
    o += [f"- option {k}: {v}" for k, v in c['opts']]
    if c.get('note'):
        o += ['', f"**Note on the page:** {c['note']}"]
    o += ['', f"**Editor's choice:** {d.get('choice', '-')}"]
    if d.get('comment'):
        o.append(f"**Editor's comment:** {d['comment']}")
    if cid in REOPENED:
        o.append(f"**Editor's second choice, after the term research: {REOPENED[cid]}.** It overrides the first; the renderings are in DECISIONS.md.")
    if cid in FIN:
        chk, f = FIN[cid], FIN[cid]['final']
        o += ['', '## Verified term research' + (' (renderings SUPERSEDED by DECISIONS.md; notes are material only)' if cid in REOPENED else ''), '']
        for k in ('main_ru', 'main_en', 'note_ru', 'note_en', 'units', 'alternatives', 'conflict_with_editor', 'open_points'):
            v = f.get(k)
            if v:
                o.append(f"**{k}{' (superseded)' if cid in REOPENED and k.startswith('main') else ''}:** {fmt(v)}\n")
        o.append(f"**Verifier's corrections (already applied in the finals above):** {chk['problems']}\n")
        o.append(f"**Sources the verifier checked:** {fmt(chk.get('sources_checked'))}\n")
    iss = [x for x in cons['issues'] if re.search(rf'\b{cid}\b', x['ids'])]
    if iss:
        o += ['## Consistency issues naming this card (resolved in DECISIONS.md)', '']
        o += [f"- [{x['ids']}] {x['problem']} FIX: {x['fix']}" for x in iss]
    open(f'{C}/cards/{cid}.md', 'w', encoding='utf-8').write('\n'.join(o) + '\n')

# --- per-unit packets ---
T = json.load(open(TEXT, encoding='utf-8'))
SEC = {int(s['section']): s for s in T['sections']}
M = json.load(open(f'{O}/merged3.json', encoding='utf-8'))
UN = {}
for n in (1, 2, 3, 4):
    for u in json.load(open(f'{O}/inputs/group-{n}.json', encoding='utf-8'))['units']:
        UN.setdefault(u['id'], u)


def lines_of(ref):
    """All Bas. (page, line) pairs named in a reference such as 'Bas. 29.8, 29.9', '29.13-14' or '28.13–30.2'."""
    res = set()
    for a, b in re.findall(r'(\d+\.\d+)(?:\s*[-–]\s*(\d+(?:\.\d+)?))?', ref or ''):
        p, l = map(int, a.split('.'))
        if b:
            if '.' in b:
                p2, l2 = map(int, b.split('.'))
            else:
                p2, l2 = p, int(b)
            for pp in range(p, p2 + 1):
                for ll in range(1, 60):
                    if (pp, ll) >= (p, l) and (pp, ll) <= (p2, l2):
                        res.add((pp, ll))
        else:
            res.add((p, l))
    return res


LAB = 'ABCDEF'
# cards by unit: the units each researched card names, the place cards' own unit, P04 with P03, P15 at the title
CARD_UNITS = {}
for g in r['groups']:
    for chk in g['verify']['checks']:
        CARD_UNITS[chk['id']] = set(re.findall(r'U\d{3}', chk['final'].get('units') or ''))
CARD_UNITS['P04'] = CARD_UNITS['P03']
CARD_UNITS['P15'] = {'U001'}
for c in CARDS:
    if c.get('unit'):
        CARD_UNITS.setdefault(c['id'], set()).add(c['unit'])

# the edition's materials, section by section, in full; a unit packet repeats only the short ones touching its lines
os.makedirs(f'{C}/edition', exist_ok=True)
KEYS = ('apparatus', 'departures', 'alternatives_for_translation', 'doubts', 'resolved_doubts')
for n, s in SEC.items():
    o = [f"# The edition, section {n}: {s['title_en']} / {s['title_ru']}", f"{s['ref_bas']}; {s['ref_h']}", '']
    for key in KEYS:
        for e in s.get(key) or []:
            o.append(f"- [{key}] " + '; '.join(f"{k}: {fmt(v)}" for k, v in e.items()))
    if s.get('p_treatment'):
        o.append(f"- [P passage, treatment] {s['p_treatment']}")
    open(f'{C}/edition/section-{n}.md', 'w', encoding='utf-8').write('\n'.join(o) + '\n')

first_unit = {}
for uid, u in sorted(UN.items()):
    s = SEC[int(u['section'])]
    mine = lines_of(u['bas'])
    cards = sorted(k for k, v in CARD_UNITS.items() if uid in v)
    o = [f"# {uid}  (Bas. {u['bas']}; section {u['section']}: {s['title_en']} / {s['title_ru']})"
         + ('  [P only]' if u.get('p_only') else '') + ('  [paragraph start]' if u.get('paragraph_start') else ''), '',
         f"Decision cards for this unit: {', '.join(cards) or 'none'}", '']
    o += ['## Greek', '', u['greek'], '', 'With Basel line markers: ' + u['greek_with_lines'], '']
    o += [f"## The edition (entries touching the lines of this unit; all of section {u['section']}: edition/section-{u['section']}.md)", '']
    for key in KEYS:
        for i, e in enumerate(s.get(key) or []):
            ref = e.get('ref', '')
            hit = (lines_of(ref) & mine) if 'Bas' in ref or re.match(r'\d', ref) else bool(u.get('p_only'))
            if hit:
                line = f"- [{key}] " + '; '.join(f"{k}: {fmt(v)}" for k, v in e.items())
                k0 = (u['section'], key, i)
                if k0 in first_unit and len(line) > 600:
                    line = f"- [{key}] ref {ref}: long entry, given in full in the packet of {first_unit[k0]}"
                first_unit.setdefault(k0, uid)
                o.append(line)
    if u.get('p_only'):
        o.append(f"- [P passage] treatment of the P passages: edition/section-{u['section']}.md")
    o += ['', '## The six independent translations (labels A-F)', '']
    for L in LAB:
        t = u['translations'].get(L) or {}
        o += [f"### {L}", f"RU: {t.get('ru')}", f"EN: {t.get('en')}"]
        if t.get('doctrine'):
            o.append(f"Doctrine: {t['doctrine']}")
        for nt in t.get('notes') or []:
            o.append(f"- note RU: {nt.get('ru')}\n  note EN: {nt.get('en')}\n  source: {nt.get('source')}")
        for d in t.get('doubts') or []:
            o.append(f"- doubt on {d.get('greek')}: {d.get('issue')} | options: {d.get('options')} | choice: {d.get('choice')} | "
                     f"evidence: {d.get('evidence')}" + (f" | alt RU: {d['alternative_ru']}" if d.get('alternative_ru') else '')
                     + (f" | alt EN: {d['alternative_en']}" if d.get('alternative_en') else ''))
        o.append('')
    m = M[uid]
    o += ['## The three reviews', '']
    for who, name in (('claude', 'Claude workflow'), ('sol', 'GPT-6.1 Sol'), ('astra', 'GPT-6 Astra')):
        x = m.get(who) or {}
        o += [f"### {name}", f"Sense: {x.get('sense')}", f"Best RU: {fmt(x.get('best_ru'))}; best EN: {fmt(x.get('best_en'))}"]
        for d in x.get('divergences') or []:
            rd = '; '.join(f"{','.join(q.get('translators') or [])}: {q.get('construal')}" for q in d.get('readings') or [])
            o.append(f"- divergence on {d.get('greek')}: {d.get('issue')} | readings: {rd} | verdict: {d.get('verdict')}"
                     + (f" | recommended RU: {d['recommended_ru']}" if d.get('recommended_ru') else '')
                     + (f" | recommended EN: {d['recommended_en']}" if d.get('recommended_en') else ''))
        for d in x.get('notes_to_keep') or []:
            o.append(f"- note to keep ({d.get('translator')}): {d.get('gist')}")
        ti = {}
        for d in x.get('text_issues_review') or []:
            k = (d.get('proposal'), d.get('verdict'), d.get('why'))
            ti.setdefault(k, []).append(str(d.get('translator')))
        for (prop, verd, why), who_ in ti.items():
            o.append(f"- text issue ({', '.join(who_)}): proposal {prop} | verdict {verd} | {why}")
        for q in x.get('editor_questions') or []:
            o.append(f"- question for the editor: {fmt(q)}")
        o.append('')
    o += ['## Errors found in the six translations (merged; found_by = which reviewers found it)', '']
    for e in m['errors']:
        txt = []
        for who in ('claude', 'sol', 'astra'):
            x = e.get(who)
            if x and not txt:
                txt.append(f"{who}: «{x.get('quote')}» — {x.get('problem')} FIX: {x.get('fix')}")
            elif x:
                txt.append(f"{who}'s fix: {x.get('fix')}")
        lang = next((e[w].get('lang') for w in ('claude', 'sol', 'astra') if e.get(w)), '')
        typ = next((e[w].get('type') for w in ('claude', 'sol', 'astra') if e.get(w)), '')
        o.append(f"- {e['translator']} {lang} {typ} [{e['severity_max']}; found by {'+'.join(e['found_by'])}]: " + ' || '.join(txt))
    if uid in ('U040', 'U041'):
        o.append("- EDITOR'S CORRECTION: F's «двойное сверхчастное» for διπλασιεπιμερής is NOT an error. It follows Tsypin's usage "
                 "(«сверхчастное» = ἐπιμερής; «сверхчастичное» = ἐπιμόριος), Ptolemy and Porphyry, Moscow 2013. See DECISIONS.md, P03.")
    open(f'{C}/units/{uid}.md', 'w', encoding='utf-8').write('\n'.join(o) + '\n')

sizes = {uid: os.path.getsize(f'{C}/units/{uid}.md') for uid in UN}
print('units', len(sizes), 'total KB', sum(sizes.values()) // 1024, 'max', max(sizes.items(), key=lambda x: x[1]))
for f in ('cards.md', 'term-finals.md', 'glossary.md'):
    print(f, os.path.getsize(f'{C}/{f}') // 1024, 'KB')
