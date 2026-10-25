# External review prompt — Zacher Epitome, Book I (RU + EN translation)

You are an independent reviewer for **Neoscholia**, a non-commercial open library of first translations of untranslated ancient and medieval texts (https://alex-michels.github.io/neoscholia/). Every translation is drafted and cross-reviewed by language models; the review log is published next to the text. Your review will be published there under your model name. You belong to a different model family than the models that drafted and reviewed this translation (Anthropic Claude). Your job is to find what they missed.

## The text

*Iulii Valerii Epitome* (the "Zacher Epitome"): an anonymous Carolingian (8th–9th c.) abridgement of Julius Valerius' Latin Alexander Romance. Book I runs from Nectanebo's flight to Macedonia up to Alexander's accession. Base text: J. Zacher, *Julii Valerii epitome* (Halle 1867), via the CC0 TEI transcription by G. Siemoneit (2023). Chapter numbers follow Zacher, who numbers by the corresponding chapters of Julius Valerius Book I; that is why some numbers are skipped. No translation into any modern language existed before this one.

## Files (paths relative to the repository root)

| File | What it is |
|---|---|
| `research/texts/zacher-epitome/review/book1-for-review.md` | **Read this first.** Chapter by chapter: Latin, Russian, English, margin notes. This is the version under review. |
| `research/texts/zacher-epitome/translation/book1.json` | The same content as data (`chapters[]`: `chapter`, `latin`, `ru`, `en`, `notes[]`). |
| `research/texts/zacher-epitome/source/book1.la.json` | The Latin by chapter, extracted from the TEI. |
| `research/texts/zacher-epitome/source/epitome.tei.xml` | The full TEI transcription of Zacher 1867 (CC0). |
| `research/texts/zacher-epitome/glossary.json` | Agreed Russian and English forms of names and terms. |
| `research/texts/zacher-epitome/context.json` | Parallels with Julius Valerius and Ps.-Callisthenes α, notes on the text, bibliography. |
| `research/texts/zacher-epitome/reviews/` | Earlier model reviews (Claude), for reference only. Do not simply repeat them; if you agree with an issue that is still present, you may report it again. |

**Do not edit any of these files.** Write only your output files (see the end).

## What to do

Work chapter by chapter, comparing every sentence of the Russian and of the English with the Latin. Check the two languages separately: an error may be in one and not the other.

1. **Accuracy**
   - mistranslations;
   - omissions and additions;
   - misread Latin: cases, voice, tense and mood, participles and ablative absolutes, reference of pronouns, late and medieval Latin usage;
   - wrong or inconsistent names.
2. **Sense of the passage.** Does the translation make sense of the narrative where the Latin does? Flag places where the translation smooths over a real difficulty or corruption in the Latin instead of marking it.
3. **Language**
   - natural, correct modern Russian and English in a scholarly register;
   - no calques, no anachronistic or slangy words;
   - consistent terminology;
   - names as in `glossary.json` (or argue against the glossary if it is wrong).
4. **Margin notes («новые схолии»)**
   - fact-check every claim, especially claims about Julius Valerius and Ps.-Callisthenes;
   - flag anything unsupported, wrong or overstated.

   If you have web access, you may check against Julius Valerius (ed. B. Kübler, Leipzig 1888, on archive.org) and Ps.-Callisthenes α (ed. W. Kroll, 1926). If you cannot verify a claim, say "unverifiable" rather than guessing.
5. **Text problems.** Places where the Latin itself looks corrupt or where Zacher's text may be wrong. Mark these as suggestions, not errors of the translation.

Do not report pure matters of taste. Do not rewrite chapters wholesale; give targeted fixes.

## Severity (MQM-style)

| Severity | Meaning |
|---|---|
| `critical` | Changes the meaning of the passage, invents content, or a note states something false |
| `major` | An error a specialist would object to: wrong construction, wrong name, misleading term, a real omission |
| `minor` | Small inaccuracy, awkward or unidiomatic phrasing, inconsistency |

Categories: `mistranslation`, `omission`, `addition`, `latin-grammar`, `names-terms`, `fluency`, `style`, `note-fact`, `source-text`.

## Output

Write two files in `research/texts/zacher-epitome/review/external/`. Use your model name in the file names, for example `gpt-6.1-sol.json` and `gpt-6.1-sol.md`.

### 1. `<model>.json` — machine-readable, exactly this shape

```json
{
  "reviewer": { "model": "exact model name and version", "provider": "OpenAI", "date": "YYYY-MM-DD", "web_access": true },
  "issues": [
    {
      "chapter": 4,
      "lang": "ru",
      "severity": "major",
      "category": "latin-grammar",
      "latin": "the Latin words concerned",
      "quote": "exact text from the translation or note, copied verbatim",
      "problem": "what is wrong and why, with reference to the Latin",
      "fix": "ready-to-paste replacement for the quoted text",
      "confidence": "high"
    }
  ],
  "chapters": [
    { "chapter": 1, "ru": "ok", "en": "minor issues", "comment": "one line, optional" }
  ],
  "summary": "5–10 sentences: overall quality of RU and EN, recurring problems, what a human editor must look at first"
}
```

- `lang` is one of `ru`, `en`, `both`, `note`, `latin`.
- `confidence` is one of `high`, `medium`, `low`.
- `chapters` covers every chapter, including those without issues.
- `quote` must match the text in `book1-for-review.md` exactly, so that the fix can be applied automatically.

### 2. `<model>.md` — the same review for a human

A short summary, then the issues grouped by chapter. Write it in Russian if you can do so fluently, otherwise in English.
