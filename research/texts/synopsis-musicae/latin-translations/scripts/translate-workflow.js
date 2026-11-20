export const meta = {
  name: 'latin-translate',
  description: 'Independent RU/EN translation of the two Latin versions (Xylander, Vinet) in an isolated folder',
  phases: [
    { title: 'Translate', detail: 'one translator per Latin version' },
    { title: 'Revise', detail: 'critical and stylistic revision of each version' },
    { title: 'Assemble', detail: 'translation.json and translation.md, terms, final check' },
  ],
}
// args: { folder: '<run folder outside the repository>', model: 'fable' | null, label: 'Opus 5.5' }
const F = args.folder
const MODEL = args.model || undefined
const RULES = `You are part of a team making an independent scholarly translation. The full task is in ${F}/PROMPT.md; read it first, then ${F}/about.md and ${F}/latin-texts.json. Follow PROMPT.md exactly, above all its Independence rules:
- work only in the folder ${F}; write working files only in ${F}/work/;
- do not open, list or search any other folder on this computer (not the parent folder, not any project or repository), and no git history;
- do not consult the Greek text of the work, any other translation of it, or studies of it; do not search the web for the work or its phrases;
- the internet is allowed and expected for dictionaries, lexica, grammars, reference works and the theorists' texts; mark every reference [checked] or [from memory].
Record any forbidden material you meet by accident in a contamination list.`

const VERSIONS = [
  { key: 'xylander', name: "Xylander's version" },
  { key: 'vinet', name: "Vinet's version" },
]
const done = await pipeline(VERSIONS,
  (v) => agent(`${RULES}

Your part: translate ${v.name} (latin-texts.json, key "${v.key}") into Russian and into English, every segment in order, following PROMPT.md (How to work, passes 1–6; Translation principles; Notes) and the conventions in about.md.
Write your result to ${F}/work/${v.key}-draft.json in the "segments" format of PROMPT.md (Output), plus a "terms" list and a "text_issues" list for this version and a "contamination" list. Write the file as you go, section by section.
Return a short report: how many segments, the hardest places, anything you could not resolve.`, { label: `translate:${v.key}`, phase: 'Translate', model: MODEL }),
  (rep, v) => agent(`${RULES}

Your part: revise the draft translation of ${v.name} in ${F}/work/${v.key}-draft.json against the Latin (latin-texts.json, key "${v.key}"), as PROMPT.md, passes 5–6, describes:
- critical revision, segment by segment: nothing omitted or added, additions in [square brackets], every number and ratio recomputed, terms as in about.md and consistent, notes correct and their references checked;
- stylistic revision, separately for Russian (good scholarly Russian, no calques or anglicisms) and English.
Check doubtful dictionary meanings yourself. Write the revised version to ${F}/work/${v.key}-revised.json (same format) and a list of what you changed and why to ${F}/work/${v.key}-revision-log.md.
The translator's report: ${typeof rep === 'string' ? rep.slice(0, 3000) : ''}
Return a short report of the main changes.`, { label: `revise:${v.key}`, phase: 'Revise', model: MODEL }))

const final = await agent(`${RULES}

Your part: assemble the final result from ${F}/work/xylander-revised.json and ${F}/work/vinet-revised.json.
- Write ${F}/translation.json exactly in the format of PROMPT.md (Output): translator (model: your exact model name and version; provider; date; web_access; subagents: "a team of agents: a translator and a reviser for each version, and an assembler"), versions.xylander.segments and versions.vinet.segments (every segment of latin-texts.json once, in order, with its id), terms (merged, with version = xylander, vinet or both), text_issues, contamination, summary.
- Check that the same Latin term is rendered the same way within each version, and that both versions follow about.md; fix inconsistencies and say so in the summary.
- One more full comparison of each translation with the Latin.
- Write ${F}/translation.md for a human reader, as PROMPT.md describes.
Revision reports: ${JSON.stringify((done || []).map((d) => (typeof d === 'string' ? d.slice(0, 2000) : d)))}
Return: the number of segments in each version, the model name you recorded, and the summary.`, { label: 'assemble', phase: 'Assemble', model: MODEL })
return { label: args.label, final }
