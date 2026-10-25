# External peer review prompt — preprint «Пергам против Александрии? Кратет, Аристарх и „короткие ночи“ лестригонов», version 0.2

You are an independent peer reviewer for **Neoscholia**, a non-commercial open library of first translations of untranslated ancient texts, with research articles built on them (https://alex-michels.github.io/neoscholia/). The article under review was researched, drafted, fact-checked and refereed with language models of the Anthropic Claude family (version 0.1). It was then reviewed by GPT-6.1 Sol (OpenAI) and revised (version 0.2). The author, Alexander Michels, PhD, has not yet proofread it. You belong to a different model family from the authoring models. Your review will be published in the article's open review log under your model name, so be rigorous, specific and fair.

Review the preprint as a journal referee would, for a venue such as *Hyperboreus*, *Philologia Classica* or *Classical Quarterly*. Combine four kinds of expertise:
- **Ancient history and Homeric scholarship:** Pergamene and Alexandrian scholarship, Crates of Mallos, Aristarchus, Aristonicus, the Homeric scholia and Eustathius.
- **Ancient geography:** Homeric geography and the debate about Odysseus' wanderings — Eratosthenes, Polybius, Strabo, Pytheas, klimata.
- **Ancient astronomy:** Aratus, Hipparchus' Commentary on Aratus and Eudoxus, Geminus, Ptolemy, spherical astronomy, precession.
- **Greek philology:** reading and translating the Greek of the scholia, Geminus, Hipparchus and Eustathius; textual criticism.

## The article in brief (version 0.2)

The scholia on Od. 10.82–86 (Laestrygonians: "for the paths of night and day are close") preserve five explanations of line 86. The only exegete named is Crates of Mallos. The article:

1. States its contribution narrowly. Much of the material has been discussed by T. Bilić (2012; 2021). What the article claims as its own:
   - a Russian translation of the whole cluster of scholia on Od. 10.82–86 in Dindorf's edition (II 452.20–454.18);
   - a collation of the witnesses to the short redaction of the scholion on Aratus 62, which credits Crates with linking Aratus' line on the head of Draco to Od. 10.86;
   - a reproducible astronomical check that allows for precession (scripts in `code/`).
2. Shows that Crates' reading in Geminus 6.10–12 (a 23-hour day, a one-hour night) agrees with spherical astronomy (about 66° N).
3. On the scholion on Aratus 62: the short redaction (collated in Maass 351.23–28, Buhle 1793, Bekker, Wachsmuth) credits Crates with the comparison and the figures 20 and 4 hours. On the long redaction (known to the authors only from a transcription of Martin's edition, not yet checked against the edition), Crates did not confuse latitudes but drew an analogy: at the latitude of Greece the head of Draco dips below the horizon for a moment, and among the Laestrygonians sunset almost meets sunrise. In the best witnesses the numbers are written in words, so the discrepancy with Geminus (23 and 1) is unlikely to be a one-letter corruption.
4. Argues that no opinion of Aristarchus on line 86 survives. The nearest attested dispute between Aristarchus and Crates in book κ concerns line 190 (did Homer know four cardinal directions; reconstructed by Carnuth and Lehrs from Σ Od. 2.1). The "Pergamon versus Alexandria" debate about the Laestrygonians therefore has to be reconstructed, with Gellius 14.6.3, Strabo 1.2.24–25 and Buonajuto (1996) on the Gellius antithesis.
5. Gives the first Russian translation of the scholia in an appendix (Greek and Russian side by side).

## The previous review

GPT-6.1 Sol reviewed version 0.1 (recommendation: major revision; 5 major and 9 minor issues). Its report: `review/external/gpt-6.md` and `gpt-6.json` (the model named itself "GPT-6 (Codex)" in the file). The authors' verification of that review and the list of changes for version 0.2 are in `dossier.md` § 8.2 and in the review log on the site page (`src/study-laestrygonians.njk`, section "Открытая рецензия"). Some places remain marked as not verified: the long redaction of the Aratus scholion in Martin 1974, page references to Bilić, Mette's conjecture, Page's translation of HQ (p. 43).

Your review has two parts:
- **A. An independent review of version 0.2** as a whole (sections "What to check" below). Do not simply repeat the earlier review; if you agree with a point of it that is still unresolved, you may report it again as your own issue.
- **B. A check of the revision.** For each of the 14 issues of the GPT-6.1 Sol review, say whether version 0.2 resolved it: `resolved`, `partly`, `unresolved`, or `worse` (the revision introduced a new error). Give a one- or two-sentence reason. Judge also whether the authors were right to treat some of Sol's sources as unusable (see "Sources" below).

## Files (paths relative to the repository root)

| File | What it is |
|---|---|
| `research/studies/laestrygonians/article.md` | **The preprint (Russian), version 0.2.** Main object of review: abstract (RU and EN), six sections, 38 footnotes, appendix with the translated scholia, full bibliography. |
| `src/study-laestrygonians.njk` | The same article on the site. The text comes from `article.md` (rendered by `lib/article.js`); the page adds an interactive astronomy figure, tables, a "how this was made" block, the open review log and a table of versions. The figure's code is in `src/assets/js/study-laestrygonians.js`. |
| `research/studies/laestrygonians/dossier.md` | Research dossier: Greek texts with translations, verification status of claims (✔ / ◐ / ✖), computations, bibliography with what was and was not consulted, open questions (§ 7), review logs (§ 8). |
| `research/studies/laestrygonians/code/draco.py`, `daylen.py` | Astronomy scripts: precession of the Draco-head stars, latitudes, day lengths, azimuths. Run with `python -I code/daylen.py` from that folder. |
| `research/studies/laestrygonians/review/external/gpt-6.md`, `gpt-6.json` | The previous external review (GPT-6.1 Sol, of version 0.1). |
| `research/studies/laestrygonians/raw/*.json` | Raw outputs of the Claude agents: research, adversarial verification, fact-check, referee, and the verification of the GPT-6.1 Sol review (`v02_verify_*.json`). For reference only. |

**Do not edit any of these files.** Write only your output files (see the end).

## Sources

Use only legitimate sources: publishers' sites, library and university repositories, archive.org and HathiTrust scans of public-domain books, Perseus, TLG/Packhum where open, JSTOR or DOI pages for bibliographic data. **Do not use or cite unauthorised copies** (studylib, dokumen.pub, ebin.pub, z-library, Anna's Archive, libgen, scribd uploads and the like); the previous reviewer used some and those points had to be marked as unverified. If a work is accessible only that way, say "not accessible legitimately" and treat the point as unverified. Never invent references, page numbers or quotations.

Useful scans:
- Dindorf, *Scholia Graeca in Homeri Odysseam* II (1855): archive.org `scholiagraeodyss02homeuoft`;
- Manitius' Geminus (1898): `geminoueisaggeis00gemi`;
- Manitius' Hipparchus (1894): `ipparchoutonarat00hipp`;
- Maass, *Commentariorum in Aratum reliquiae* (1898), and Buhle's Aratus with scholia (1793);
- Stallbaum's Eustathius I (1825): `commentariiadhom01eust`;
- Carnuth's Aristonicus (1869); Lehrs, *De Aristarchi studiis Homericis*;
- Heiberg's Ptolemy, *Syntaxis* I (1898);
- Strabo, Gellius, Aratus: Perseus.

## What to check (part A)

1. **Argument.**
   - Does each conclusion follow from the evidence? Where does the article overclaim or underclaim? Are the hedges in the right places?
   - Assess especially: the "analogy, not confused latitudes" reading of the Aratus scholion; the claim that the numbers in words make a one-letter corruption unlikely; the reconstruction of the Pergamon–Alexandria opposition from κ 190, Gellius and Strabo.
   - Is the restated novelty fair to Bilić and to earlier scholarship?
2. **Primary sources.** Check every reference and quotation: book, chapter, section; page and line of Dindorf, Maass, Manitius, Stallbaum, Heiberg; manuscript sigla; fragment numbers (Broggiato F 50, F 53, F 54; Herodicus F 13; Mette 37a–i). Check the Greek: accents, breathings, wording against the editions.
3. **The translations.** Check the Russian translations of all Greek and Latin in the article and in the appendix against the originals: mistranslations, omissions, wrong construal. The appendix is the first complete translation of these scholia, so it matters most.
4. **Astronomy.**
   - Verify declinations, grazing latitudes, day lengths, azimuths and obliquity values: run the scripts, recompute independently, or both.
   - Check the reading of Hipparchus 1.4.7–8, Geminus 6.10–12 and 6.20, and Ptolemy, *Almagest* II.6 (the 20-hour parallel through Thule).
   - Does the interactive figure compute and draw correctly (classification by the sign of the Sun's lowest altitude, the presets, the captions)?
5. **Secondary literature.**
   - Are the works cited real, correctly described and correctly cited (including those added in version 0.2: Buonajuto 1996, Podosinov 2015, Luiselli 2015, Bishop 2015, Lightfoot 2017, Broggiato FGrHist 2113)?
   - What important literature is still missing? For each suggestion give full bibliographic data and say how you verified that it exists.
6. **Novelty.** What in version 0.2 is new, and what is already in Bilić (TAPA 142, 2012; *The Land of the Solstices*, 2021), Broggiato (2001, 2014), Mette (1936), Heubeck (1989) or elsewhere? If you can read these works legitimately, say precisely what they already say, with pages.
7. **Open questions.** The dossier lists unresolved checks (§ 7), among them: Martin's edition of the Aratus scholia (the long redaction) — the most important; Pontani's edition vol. V; Broggiato's commentary on F 50; Kidd on Aratus 61; Σ D Il. 5.385; Mette's numbering; the Formiae references. Resolve any you can, with sources.
8. **Presentation.** Structure, clarity for the intended readers (philologists, historians, students, educated public), consistency of terms and citation style. Report only what matters; do not polish the Russian style unless it causes ambiguity.

## Severity

| Severity | Meaning |
|---|---|
| `critical` | A false claim, a wrong reading of a source, or an error that undermines a conclusion |
| `major` | A specialist would object: wrong reference, overclaim, missing key literature or counter-argument, mistranslation |
| `minor` | Small inaccuracy, inconsistency, unclear wording |

Categories: `argument`, `overclaim`, `primary-source`, `greek-text`, `translation`, `fragment-numbering`, `astronomy`, `geography`, `literature-missing`, `literature-error`, `novelty`, `presentation`.

## Output

Write two files in `research/studies/laestrygonians/review/external/`: **`gpt-6-astra.json` and `gpt-6-astra.md`** (or your exact model name, if different). Do not overwrite `gpt-6.json` or `gpt-6.md`.

### 1. `gpt-6-astra.json` — machine-readable, exactly this shape

```json
{
  "reviewer": { "model": "exact model name and version", "provider": "OpenAI", "date": "YYYY-MM-DD", "web_access": true, "version_reviewed": "0.2" },
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
  "previous_review": [
    { "issue": 1, "where": "as in gpt-6.json", "status": "resolved | partly | unresolved | worse", "comment": "one or two sentences" }
  ],
  "literature": [
    { "ref": "full bibliographic reference", "why": "what it adds or which claim it affects", "verified": true, "url": "where you verified it" }
  ],
  "open_checks": [
    { "item": "e.g. Martin 1974, sch. Arat. 61–62", "result": "what you found, or 'not accessible'", "source": "URL / edition" }
  ],
  "novelty": "what is new in version 0.2 and what is already in the literature",
  "summary": "8–15 sentences: overall assessment, strongest and weakest points, what must be fixed before the final version"
}
```

- `issue` in `previous_review` is the 1-based position of the issue in the `issues` array of `gpt-6.json`; give all 14.
- `confidence` is one of `high`, `medium`, `low`.
- `quote` must match `article.md` version 0.2 (or the named file) exactly, so that the fix can be applied automatically. Leave it empty only for issues about something missing.

### 2. `gpt-6-astra.md` — the same review for a human

Write a referee's report in Russian (or in English if you cannot write Russian fluently): summary and recommendation; issues grouped by section; the check of the previous review (a table of the 14 issues with status and comment); suggested literature; the open checks.
