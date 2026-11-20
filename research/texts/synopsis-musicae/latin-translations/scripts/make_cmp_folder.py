"""Make one reviewer's folder for the comparison of the four Latin translations: PROMPT.md (PROMPT-codex.md with
{FOLDER} replaced by the folder's own path), the anonymised inputs (comparisons/inputs) and scans/. The folder must be
outside the repository and must not exist yet.
Usage: python -I make_cmp_folder.py <synopsis-musicae folder> <new folder>"""
import os, re, shutil, sys
R, RUN = sys.argv[1], os.path.abspath(sys.argv[2])
assert not os.path.exists(RUN), f'{RUN} exists'
assert 'neoscholia' not in RUN.lower(), 'the folder must be outside the repository'
INP = f'{R}/latin-translations/comparisons/inputs'
os.makedirs(f'{RUN}/scans')
os.makedirs(f'{RUN}/work')
p = open(f'{INP}/PROMPT-codex.md', encoding='utf-8').read()
assert p.count('{FOLDER}') == 1
open(f'{RUN}/PROMPT.md', 'w', encoding='utf-8').write(p.replace('{FOLDER}', RUN))
for f in ('translation-brief.md', 'about.md', 'latin-texts.json', 'terms.json', 'group-1.json', 'group-2.json', 'group-3.json', 'group-4.json'):
    shutil.copyfile(f'{INP}/{f}', f'{RUN}/{f}')
n = 0
for d, pat, name in ((f'{R}/source/basel1556', r'^la-seq\d+-p(\d+)\.jpg$', 'xylander-p{}.jpg'),
                     (f'{R}/source/tournon1591', r'^la-vinet-seq\d+-p(\d+)\.jpg$', 'vinet-p{}.jpg')):
    for f in sorted(os.listdir(d)):
        m = re.match(pat, f)
        if m:
            shutil.copyfile(f'{d}/{f}', f'{RUN}/scans/{name.format(m.group(1))}')
            n += 1
print(f'{RUN}: PROMPT.md and 8 input files, {n} scans')
