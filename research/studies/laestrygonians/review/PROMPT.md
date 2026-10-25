# External peer review prompt — preprint «Пергам против Александрии? Кратет, Аристарх и „короткие ночи“ лестригонов»

You are an independent peer reviewer for **Neoscholia**, a non-commercial open library of first translations of untranslated ancient texts, with research articles built on them (https://alex-michels.github.io/neoscholia/). The article under review was researched, drafted, fact-checked and refereed with language models of the Anthropic Claude family; a human editor has not yet proofread it. You belong to a different model family. Your review will be published in the article's open review log under your model name, so be rigorous, specific and fair.

Review the preprint as a journal referee would, for a venue such as *Hyperboreus*, *Philologia Classica* or *Classical Quarterly*. Combine four kinds of expertise:
- **Ancient history and Homeric scholarship:** Pergamene and Alexandrian scholarship, Crates of Mallos, Aristarchus, Aristonicus, the Homeric scholia and Eustathius.
- **Ancient geography:** Homeric geography and the debate about Odysseus' wanderings — Eratosthenes, Polybius, Strabo, Pytheas, klimata.
- **Ancient astronomy:** Aratus, Hipparchus' Commentary on Aratus and Eudoxus, Geminus, spherical astronomy, precession.
- **Greek philology:** reading and translating the Greek of the scholia, Geminus, Hipparchus and Eustathius; textual criticism.

## The article in brief

The scholia on Od. 10.82–86 (Laestrygonians: "for the paths of night and day are close") preserve five explanations of line 86. The only exegete named is Crates of Mallos. The article:

1. Translates the whole cluster of scholia (Dindorf 1855, II 452.20–454.18) into Russian, apparently for the first time.
2. Shows that Crates' reading in Geminus 6.10–12 (a 23-hour day, a one-hour night) is consistent with spherical astronomy (≈66° N).
3. Argues that the "head of Draco" argument citing Aratus, Phaen. 61–62, is Crates' own move. It is attested under his name in the Aratus scholia (read in Buhle's 1793 edition, with a 20-hour day and a 4-hour night). Read as Hipparchus reads it, Aratus' line describes a star grazing the horizon at the latitude of Greece (~37°). Crates transfers the "mingling of settings and risings" from the star to the Sun of the far north.
4. Concludes that no opinion of Aristarchus on these lines survives, so the "Pergamon vs Alexandria" debate about them must be reconstructed from other evidence: Gellius 14.6.3; Aristonicus on Od. 10.1 and 10.190; Σ 10.3; Strabo 1.2.24–25.

## Files (paths relative to the repository root)

| File | What it is |
|---|---|
| `research/studies/laestrygonians/article.md` | **The preprint (Russian), version 0.1.** Main object of review: text, 31 footnotes, appendix with the translated scholia, bibliography. |
| `src/study-laestrygonians.njk` | The same article as published on the site. It adds an interactive astronomy figure, tables, a "how this was made" block and an open review log. The figure's code is in `src/assets/js/study-laestrygonians.js`. |
| `research/studies/laestrygonians/dossier.md` | Research dossier: Greek texts with translations, the verification status of claims (✔ / ◐ / ✖), computations, bibliography with what was and was not consulted, open questions (§ 7), pre-publication review log (§ 8). |
| `research/studies/laestrygonians/code/draco.py`, `daylen.py` | Astronomy scripts: precession of the Draco-head stars, latitudes, day lengths. Run with `python -I code/daylen.py` from that folder. |
| `research/studies/laestrygonians/raw/*.json` | Raw outputs of the earlier Claude agents: research, adversarial verification, fact-check, referee. For reference — do not just repeat them. |

**Do not edit any of these files.** Write only your output files (see the end).

## What to check

1. **Argument.**
   - Does each conclusion follow from the evidence?
   - Where does the article overclaim or underclaim?
   - Are there obvious counter-arguments or alternative readings it ignores? Are its hedges in the right places?
   - Assess especially the claim that the Aratean argument belongs to Crates himself, and the claim that the Pergamon–Alexandria opposition on this line is a modern construction.
2. **Primary sources.** Check every reference and quotation: book, chapter, section; page and line of Dindorf, Manitius, Stallbaum; manuscript sigla; fragment numbers (Broggiato F 50, F 53, F 54; Herodicus F 13; Mette 37a–i). Check the Greek: accents, breathings, wording against the editions. If you can, read the sources online:
   - Dindorf, *Scholia Graeca in Homeri Odysseam* II (1855): archive.org `scholiagraeodyss02homeuoft`;
   - Manitius' Geminus (1898): `geminoueisaggeis00gemi`;
   - Manitius' Hipparchus (1894): `ipparchoutonarat00hipp`;
   - Stallbaum's Eustathius I (1825): `commentariiadhom01eust`;
   - Strabo, Gellius, Aratus, Thucydides: Perseus;
   - Buhle's Aratus with scholia (1793);
   - Carnuth's Aristonicus (1869).
3. **The translations.** Check the Russian translations of all Greek and Latin quoted in the article and in the appendix against the originals: mistranslations, omissions, wrong construal. The appendix is the first complete translation of these scholia, so it matters most.
4. **Astronomy.**
   - Verify the declinations, grazing latitudes, day lengths, azimuths and the obliquity values: run the scripts, recompute independently, or both.
   - Check the reading of Hipparchus 1.4.7–8 and Geminus 6.10–12.
   - Is the interpretation of "around/under the head of Draco" — zenith reading versus loose reading — sound?
   - Does the interactive figure compute and draw correctly?
5. **Secondary literature.**
   - Are the works cited real, correctly described and correctly cited?
   - What important literature is missing? Look specifically for:
     - studies of Crates' Homeric exegesis and geography;
     - discussions of Od. 10.82–86 and the "midnight sun" reading;
     - work on Aratus 61–62 and its commentators;
     - work on Attalus of Rhodes;
     - Russian-language scholarship on Crates and the Homeric scholia.
   - For each suggested work give full bibliographic data and say whether you verified that it exists (catalogue, publisher page or DOI). Never invent references.
6. **Novelty.**
   - What in this article is new?
   - What may already be in Bilić (TAPA 142, 2012; *The Land of the Solstices*, 2021), Broggiato (2001, 2014), Mette (1936), Heubeck (1989) or elsewhere?
   - If you can read these works, say precisely what they already say.
7. **Open questions.** The dossier lists unresolved checks (§ 7): Martin's edition of the Aratus scholia, Pontani's edition vol. V, Broggiato's commentary on F 50, Kidd on Aratus 61, the Carnuth/Lehrs reconstruction for Od. 10.190, Σ D Il. 5.385, the Formiae references, Almagest II.6. Resolve any you can, with sources.
8. **Presentation.** Structure, clarity for the intended readers (philologists, historians, students, educated public), consistency of terms and citation style. Report only what matters; do not polish the Russian style unless it causes ambiguity.

## Severity

| Severity | Meaning |
|---|---|
| `critical` | A false claim, a wrong reading of a source, or an error that undermines a conclusion |
| `major` | A specialist would object: wrong reference, overclaim, missing key literature or counter-argument, mistranslation |
| `minor` | Small inaccuracy, inconsistency, unclear wording |

Categories: `argument`, `overclaim`, `primary-source`, `greek-text`, `translation`, `fragment-numbering`, `astronomy`, `geography`, `literature-missing`, `literature-error`, `novelty`, `presentation`.

## Output

Write two files in `research/studies/laestrygonians/review/external/`. Use your model name in the file names, for example `gpt-6-astra.json` and `gpt-6-astra.md`.

### 1. `<model>.json` — machine-readable, exactly this shape

```json
{
  "reviewer": { "model": "exact model name and version", "provider": "OpenAI", "date": "YYYY-MM-DD", "web_access": true },
  "recommendation": "accept | minor revision | major revision | reject",
  "issues": [
    {
      "where": "article.md § 4, paragraph 3 (or note 18, appendix Σ 10.86 HQ, dossier § 3.8, figure)",
      "severity": "major",
      "category": "primary-source",
      "quote": "exact text from article.md (or the named file), copied verbatim",
      "problem": "what is wrong and why, with the evidence",
      "evidence": "edition, page and line, URL, or the computation you ran",
      "fix": "ready-to-paste replacement text in Russian, or a precise instruction",
      "confidence": "high"
    }
  ],
  "literature": [
    { "ref": "full bibliographic reference", "why": "what it adds or which claim it affects", "verified": true, "url": "where you verified it" }
  ],
  "open_checks": [
    { "item": "e.g. Martin 1974, sch. Arat. 61–62", "result": "what you found, or 'not accessible'", "source": "URL / edition" }
  ],
  "novelty": "what is new in the article and what is already in the literature",
  "summary": "8–15 sentences: overall assessment, strongest and weakest points, what must be fixed before the final version"
}
```

- `confidence` is one of `high`, `medium`, `low`.
- `quote` must match the file exactly, so that the fix can be applied automatically. Leave it empty only for issues about something missing.

### 2. `<model>.md` — the same review for a human

Write a referee's report: summary and recommendation, then issues grouped by section, then suggested literature and the open checks. Write it in Russian if you can do so fluently, otherwise in English.
