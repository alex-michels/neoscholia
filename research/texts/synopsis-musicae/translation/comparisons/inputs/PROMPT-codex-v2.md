# Critical comparison of six independent translations against the Greek

**Neoscholia** is a non-commercial open library of first translations of ancient and Byzantine texts into Russian and English. It had one Byzantine text translated six times, independently, into Russian and into English. The text is the music section (a synopsis of harmonics) of the anonymous *Quadrivium* of 1008, an early 11th-century school compendium of the mathematical sciences.

The six translators are anonymous to you: labels **A, B, C, D, E, F**. They all received the same brief and the same package. Your job is to review their work critically against the Greek, for the human editor, who will decide. The editor is a classical philologist and historian.

## Your role

You are a classical philologist and a specialist in ancient and Byzantine Greek and in ancient Greek harmonics:
- you read early 11th-century Byzantine scholarly Greek full of technical vocabulary;
- you know the theorists (Nicomachus, Theon of Smyrna, Cleonides, Aristoxenus, Ptolemy, Aristides Quintilianus, Gaudentius, Bacchius, the *Sectio canonis*);
- you can recompute every ratio and every division;
- you write and judge exact scholarly Russian and English.

## Files (in this folder)

- `translation-brief.md`: the brief the translators received (role, rules, translation principles, output format).
- `about.md`: the text, the witnesses, the sigla, the signs of the edition and how to read the apparatus.
- `greek-units.json`: the whole Greek text in 67 units (U001–U067). `greek_with_lines` gives the same Greek with the Basel line markers |page.line|, to which the apparatus refers.
- `group-1.json` … `group-4.json`: all 67 units in four groups (U001–U025, U026–U036, U037–U045, U046–U067). Each holds:
  - for each unit: the Greek, and for each translator their Russian (`ru`), English (`en`), `doctrine`, `checks`, `notes` and `doubts`. The order of the labels changes from unit to unit on purpose;
  - units marked `context_only`, which belong to the neighbouring group: read them for context, do not judge them there;
  - the apparatus for these sections;
  - each translator's `text_issues` for these units.
- `terms.json`: each translator's term list.

`translation-brief.md` and `about.md` were written for the translators. In them, "PROMPT.md" means the brief, and "greek-text.json" is the text now given in `greek-units.json`, with the `apparatus` lists of the group files. The brief's folder rule and output format do not apply to you; your rules are below. In the translators' notes, references have been cleaned of links and tool names: judge a reference by its bibliographic content. Do not judge spacing or typography in any field other than the `ru` and `en` translations (doctrine, checks, notes, doubts, text issues, terms, references). Judge quality, not quantity: the number or length of notes and doubts is not a merit in itself; fault a translator for a missing note only where the reader needs one. Marking a reference `[from memory]` is not a fault; judge whether the claim is right.

## Rules

1. **Work only in this folder**, the folder that contains this PROMPT.md: `{FOLDER}`.
   - Create working files only in its subfolder `work/`. Keep all temporary files in `work/`, not in a system temp directory.
   - Do not open, list or search any other folder on this computer, not even the parent folder.
   - Do not use git history.
   - Do not open any URL containing alex-michels or neoscholia: github.com, raw.githubusercontent.com, *.github.io, the GitHub API, gists, web archives, any copy or mirror. Do not read search snippets from such URLs. Do not search the web for Neoscholia or for its editor.
2. **Judge each label only by its text.** Do not try to guess who or what produced a translation, and do not mention any such guess.
3. **Decide every disputed point on reference works, not on impression.**
   - Lexica: LSJ, DGE, Lampe, Sophocles, Bailly, Pape, and LBG where open.
   - Grammars: Smyth, Kühner–Gerth, Jannaris.
   - The theorists: Jan's *Musici scriptores Graeci*, Hiller's Theon of Smyrna, Hoche's Nicomachus, Aristides Quintilianus, Ptolemy, Boethius, Meibom.
   - Mark every reference `[checked]` (you opened it and read the place) or `[from memory]`.
   - Never invent a reference, a page or a quotation.
   - If you cannot open a source that a translator cites, mark the claim "not verified", not "false".
4. **Use legitimate sources only.** For example:
   - public-domain scans (archive.org, HathiTrust, Gallica, MDZ, e-rara);
   - Perseus, Scaife, First1KGreek and its files, Logeion;
   - the online DGE and LBG;
   - the TLG where open;
   - university and publisher pages.

   A translator's use of such a source is not a fault. Never use unauthorised copies (studylib, dokumen.pub, ebin.pub, Z-Library, Anna's Archive, Library Genesis and the like). Consult works in copyright (e.g. Barker) only where they are legitimately available; otherwise mark them `[from memory]`.
5. **Do not consult any existing translation of this text**, in whole or in part, including any machine translation. This covers:
   - the Latin of Vinet, Xylander or Alard;
   - Mizler's German;
   - A. J. H. Vincent, *Notices et extraits* 16.2 (1847): do not open this volume at all. Every reading of P you need is in the apparatus. His French translation faces the Greek on pp. 339, 341 and 343;
   - any modern translation;
   - the old printed books of this text, even for the Greek: Basel [1556] (with Xylander's Latin and *Annotationes*), Alard 1636, Leiden 1647, Mizler 1746.
6. **Other forbidden material.**
   - J. L. Heiberg's edition (*Anonymi Logica et Quadrivium*, 1929). If a corpus holds this work (the TLG or any other), do not open its passages. In any corpus or word search (TLG, LBG, Logeion, Perseus/Scaife, Diorisis), skip hits from this work and from the later authors below, and record any you saw in `contamination`.
   - Any study of this text, for example:
     - E. V. Gertsman 2022 (ch. 4) and his articles (*Византийский временник* 51, 1990; 54, 1993; *Палестинский сборник* 32, 1993);
     - S. Di Mambro 2020;
     - L. Benakis 2018;
     - G. Katsiampoura 2004 and 2010.
   - In any handbook (West, Mathiesen and others), skip the pages on this text.
   - The later Byzantine authors who reuse this text: Michael Italicus, Zonaras, Bryennius, Pachymeres, Joseph Rhakendytes.
   - Wallis' *Opera* III also prints Bryennius: open only Ptolemy and Porphyry there.
   - A lexicon entry (LSJ, DGE, Sophocles, Lampe, LBG, Bailly, Pape, Montanari or any other) may cite this text as Psellus, Anon. Heib., *Anonymi Logica et Quadrivium* or Gregorius Aneponymus. You may read the entry, but do not count that citation as evidence; say so in `evidence`.
   - **Known trap.** Jan's notes and apparatus in *Musici scriptores Graeci* quote this text as "Psellus" and cite Bryennius and Pachymeres. This happens especially around Gaudentius c. 8–10 and Bacchius, on παράφωνος and ἀντίφωνος. Hiller's apparatus to Theon does the same. The same applies to the editorial matter of any edition you open (prefaces, notes, testimonia, indices: Jan, Hiller, Meibom, Wallis, Düring, Hoche, Macran, Friedlein, Jahn, Winnington-Ingram). Read the theorists' own text, or a diagram itself; if you meet such a citation, stop reading it and record it in `contamination`.
7. **Do not search the web for this text.** This covers:
   - its phrases and its rare words;
   - its titles and the names under which it circulates: *Quadrivium of 1008*, *Anonymi Logica et Quadrivium*, Anonymus Heiberg, (Pseudo-)Psellus on music or on the four mathematical sciences, *Synopsis of Music*, Gregory the monk / Gregorius Aneponymus.

   Do not search the web for any wording of the translations or of their notes, in Russian or English, or for the Greek of this text in any form. Use web search only for other authors' texts, lexicon entries and bibliographic data.
8. **If you meet forbidden material by accident**, stop reading it, do not use it, and record it in `contamination`.
9. You may use subagents. Give each one these rules and the folder path verbatim.

## Task

### A. Compare, unit by unit (all 67 units)

1. **Read the Greek first.** Read the Greek and the apparatus yourself and state its sense (`sense`) before you weigh the translations.
2. **Divergences.** Find where the translators construe or understand the Greek differently: syntax, a word's meaning here, a term, a number, the reference of a pronoun, the scope of a phrase.
   - Group the translators by reading. Every label A–F appears in exactly one reading of each divergence. If a translator leaves the phrase out, its construal is "omits".
   - Decide which reading is right and why, with evidence from the reference works.
   - Give a recommended rendering of that phrase in Russian and in English.
   - Mark `to_editor` where the evidence does not settle it, or where the choice is the editor's.
3. **Errors.** List real faults of individual translators, in `ru`, in `en` or in their notes:
   - omission, addition, mistranslation, wrong construal;
   - translating a reading other than the printed one (that belongs in their doubts or text issues);
   - a wrong number or ratio;
   - a wrong or missing edition sign (⟨ ⟩, ⟨⟨ ⟩⟩, † †, [ ]);
   - an inconsistent term;
   - poor Russian or English that misleads or is plainly unidiomatic;
   - false claims in notes, doctrine, checks or doubts, including references marked `[checked]` that are wrong. Verify the ones that matter.

   Severity: **major** if it changes or loses the sense, or states a false fact; **minor** otherwise. Do not count mere stylistic preferences or legitimate alternatives as errors. "First occurrence" of a term (where the brief asks for the Greek in parentheses) means in the whole text, not in a group.
4. **Best versions.** `best_ru` and `best_en`: which translator's version is the best base for this unit in each language, and why, in one line. If two are equally good, name both ("X = Y"); if none is usable as a base, say "none".
5. **Notes to keep.** `notes_to_keep`: the notes worth keeping in the published commentary, with the gist and the translator.
6. **Text proposals and doubts.** For each proposal in a translator's `text_issues`, and for each doubt whose alternative changes the sense, judge it against the apparatus and the sources: sound, unsound or open. Record both in `text_issues_review`; for a doubt, put the translator's alternative reading or rendering in `proposal`.
7. **Questions for the editor.** `editor_questions`: what the editor must decide in this unit.

### B. Check your own findings adversarially (second pass)

After A, go through every divergence verdict, every error and every text-proposal verdict again, as a skeptic. Use a subagent that did not write them, if you can.
- Re-read the Greek and the quoted translation.
- Open the sources that decide the point.
- Keep a finding only if the text and the sources support it.
- Correct or drop the rest.
- Then read every unit once more against every translation, looking for major errors you missed.

Record the result in each finding's `second_pass` field:
- `confirmed`: the finding stands as written;
- `modified`: you corrected it;
- `added`: you found it in this pass.

Drop the findings you rejected.

### C. Terms

Merge the six term lists into one concordance of the technical terms and names: note names, intervals, ratio names and recurring formulas. Add any term the lists miss that matters.
- For each term, give the six Russian and English renderings side by side, with the units where it occurs.
- Recommend one Russian and one English rendering, consistent across the text, with the reason and the evidence.
  - English: the standard terminology of the field (A. Barker, *Greek Musical Writings* II).
  - Russian: weigh the published Russian translations of other theorists. V. G. Tsypin's forms and the partly different forms of L. V. Aleksandrova and T. G. Myakin are both named in `about.md` § 5; add any other published translation you can check legitimately. Neither school is the default: give the reason for each choice.
- Mark `to_editor` where the choice is genuinely open. Following either school consistently is not an error.
- Record `term_inconsistencies`: where a translator renders the same term differently in different units without reason.

### D. Overall

For each translator A–F: their strengths and their weaknesses. Then a summary. Then any forbidden material you met (`contamination`; "none" if none).

## Procedure

The input is large (about 1.1 MB), so work in parts:
1. Work group by group (group-1 … group-4). Read one unit at a time with a small script. Do not print whole group files.
2. After each group, save its finished units to `work/units-g1.json` … `work/units-g4.json`. Then rebuild `comparison.json` and `comparison.md` from all finished parts.
3. If `comparison.json` or `work/units-g*.json` already exist when you start, continue from the first unit that is missing. If findings in a finished group lack `second_pass`, run part B for that group first.
4. Do part B group by group as well, and write the results back into the same files.
5. Build the term concordance last, in `work/terms.json`. Then merge it into `comparison.json` as `terms` and `term_inconsistencies`, and write `overall`.
6. At the end, validate with a script:
   - valid JSON;
   - U001–U067 present once each, in order;
   - every required key present;
   - every divergence covers A–F, and every translator in a reading has a quote;
   - every finding has `second_pass`.

   Generate `comparison.md` from `comparison.json`.

## Output

Write **`comparison.json`** and **`comparison.md`** in this folder.

### `comparison.json`

```json
{
  "reviewer": { "model": "your exact model name", "provider": "your provider", "date": "YYYY-MM-DD", "web_access": true, "subagents": "how you used them" },
  "units": [
    {
      "id": "U000",
      "sense": "what the Greek says, in English",
      "divergences": [
        {
          "greek": "the Greek words",
          "issue": "the question",
          "readings": [
            {
              "translators": ["X", "Y"],
              "construal": "how they read it",
              "quotes": [ { "translator": "X", "ru": "their Russian", "en": "their English" } ]
            }
          ],
          "verdict": "which reading is right and why",
          "recommended_ru": "…",
          "recommended_en": "…",
          "evidence": ["source, place [checked] or [from memory]"],
          "confidence": "high, medium or low",
          "to_editor": false,
          "second_pass": "confirmed, modified or added"
        }
      ],
      "errors": [
        {
          "translator": "X",
          "lang": "ru, en, both, or notes (incl. doctrine, checks, doubts)",
          "type": "omission, addition, mistranslation, construal, other-reading, number, term, sign, consistency, language or note-claim",
          "severity": "major or minor",
          "quote": "the faulty words",
          "problem": "what is wrong",
          "fix": "the correction",
          "second_pass": "confirmed, modified or added"
        }
      ],
      "text_issues_review": [
        {
          "kind": "text_issue or doubt",
          "translator": "X",
          "printed": "…",
          "proposal": "…",
          "verdict": "sound, unsound or open",
          "why": "…",
          "evidence": ["…"],
          "to_editor": false,
          "second_pass": "confirmed, modified or added"
        }
      ],
      "best_ru": { "translator": "X", "why": "…" },
      "best_en": { "translator": "X", "why": "…" },
      "notes_to_keep": [ { "translator": "X", "gist": "…" } ],
      "editor_questions": ["…"]
    }
  ],
  "terms": [
    {
      "greek": "…",
      "units": "U000, U000",
      "renderings": [ { "translator": "X", "ru": "…", "en": "…" } ],
      "recommended_ru": "…",
      "recommended_en": "…",
      "why": "…",
      "evidence": ["…"],
      "to_editor": false
    }
  ],
  "term_inconsistencies": [ { "translator": "X", "term": "…", "problem": "…" } ],
  "overall": {
    "by_translator": [ { "translator": "X", "strengths": "…", "weaknesses": "…" } ],
    "summary": "…",
    "contamination": "none, or what you met"
  }
}
```

The example values are placeholders. `web_access` and `to_editor` are JSON booleans (true or false).
- **Every unit U001–U067 must appear once, in order.**
- `quotes`: one entry for every translator listed in `translators` (for "omits", `ru` and `en` are empty strings).
- Empty lists are fine where there is nothing to say.
- Write all fields in English, except the Russian renderings.

### `comparison.md`

The same, for a human reader, unit by unit. At the end come the terms and the overall assessment.
