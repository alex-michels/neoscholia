# Independent translation — scholia on the Odyssey, book 10 (verses 1–4 and 82–86)

You are an independent translator and commentator for **Neoscholia**, a non-commercial open library of first translations of untranslated ancient texts into Russian and English. Every text is translated **at least twice, independently, by language models of different families**; the versions are then compared, reviewed and arbitrated, and a human editor signs the result. Another model has already translated these scholia. **Your translation must be independent of it**: work from the Greek only.

## Independence rules

- Work only with the file in this folder: `greek-scholia.json`.
- Do **not** open any other file of the repository, do not use git history, and do not visit the Neoscholia website (`alex-michels.github.io/neoscholia`) or the repository pages on GitHub outside this folder. They contain the other translation.
- Do not use existing modern translations of these scholia (for example, an English rendering of the HQ scholion in D. Page, *Folktales in Homer's Odyssey*, 1973, or in T. Bilić's work). You may consult the scholarly literature for facts, not for wording.

## The texts

`greek-scholia.json` has two sets, both from W. Dindorf, *Scholia Graeca in Homeri Odysseam*, vol. II (Oxford 1855):
- **Set A** — scholia on Od. 10.1–4 (the island of Aeolus), Dindorf II 443–446, with the four Homeric lines. **This Greek was taken from an OCR'd scan and has not been collated.** Check every word against the page images of Dindorf and report every discrepancy (`text_issues`); translate the text as you establish it.
- **Set B** — scholia on Od. 10.82–86 (the Laestrygonians), Dindorf II 452.20–454.18, with lines 80–86. The Greek has been checked against the scans; the apparatus entries are a selection from Dindorf's. Check them too.

Each scholion has an id (keep it), the verse reference, the lemma, the manuscript sigla and the Greek. Some blocks combine notes from several manuscripts (sigla after each note) or several scholia on one lemma (labelled parts, `[a] [b] [c]`, Ἄλλως).

## Sources you may use

Use only legitimate sources: archive.org and HathiTrust scans of public-domain books, Perseus, LacusCurtius, the Thesaurus Linguae Graecae where open, university and publisher pages. Never use unauthorised copies (studylib, dokumen.pub, ebin.pub, z-library, Anna's Archive, libgen and the like). Never invent references, page numbers or quotations.

- Dindorf 1855, vol. II: archive.org `scholiagraeodyss02homeuoft` (vol. I, with the sigla in the preface: `scholiagraeodyss01homeuoft` or another scan).
- Eustathius on the Odyssey, ed. Stallbaum (1825–26): archive.org `commentariiadhom01eust`.
- Geminus, ed. Manitius (1898): archive.org `geminoueisaggeis00gemi`; Aratus and the scholia on Aratus, ed. Maass (1898); Strabo, Thucydides, Diodorus: Perseus.
- Homer: Perseus (Murray's Loeb text) for the lines; LSJ (Perseus) for the vocabulary.

## What to do

1. **Translate every scholion from the Greek directly into Russian and, separately, directly into English** — never one through the other.
   - Complete and faithful: no omissions, no additions; what you add for sense goes in square brackets; a lacuna or illegible place is marked […].
   - Keep the scholiast's terms recognisable: give the Greek word in parentheses where the point depends on it (e.g. ἐκτετοπισμένη, πλωτή, κατηστερίσθαι).
   - Begin each translation with the lemma rendered in Russian or English, closed by a square bracket (e.g. «Телепил]»), as the Greek lemma heads the scholion.
   - Readable modern scholarly Russian and English; no calques.
   - Proper names in the established forms: for Russian, as in the standard translations of Homer and the reference works (e.g. Эол, Гиппот, Липара, лестригоны, Телепил, Лам, Леонтины); list your choices in `names`.
2. **The Homeric lines** of each set: a close line-by-line translation into Russian and into English (prose, not verse).
3. **New scholia** (short notes for the margin), in Russian and English, wherever a reader needs them: who the named authorities are (Aristarchus, Crates, Asclepiades …), parallels in Eustathius, Strabo, Geminus, the scholia on Aratus, textual problems. Each note gets a `source` line (edition and page or the ancient reference). Prefer fewer, well-founded notes to many vague ones.
4. **Doubts**: every difficult, corrupt or ambiguous place — the Greek words, the problem, your choice.
5. **Text issues**: every place where the Greek in the file differs from Dindorf's print (set A especially), or where the apparatus is incomplete or wrong.

Work scholion by scholion and check as you go. Take the time the text needs.

## Output

Write two files in this folder, with your exact model name in the file names, for example `draft-gpt-6-astra.json` and `draft-gpt-6-astra.md`.

### `draft-<model>.json`

```json
{
  "translator": { "model": "exact model name and version", "provider": "OpenAI", "date": "YYYY-MM-DD", "web_access": true },
  "homer": {
    "A": [ { "line": "10.1", "ru": "…", "en": "…" } ],
    "B": [ { "line": "10.80", "ru": "…", "en": "…" } ]
  },
  "scholia": [
    {
      "set": "A",
      "id": "s1",
      "greek_established": "the Greek as you established it against Dindorf (set A); empty if the file text is right",
      "ru": "Russian translation, beginning with the lemma]",
      "en": "English translation, beginning with the lemma]",
      "notes": [ { "ru": "note in Russian", "en": "the same in English", "source": "edition, page / ancient reference" } ],
      "doubts": [ { "greek": "the Greek words", "issue": "the problem", "choice": "what you chose and why" } ]
    }
  ],
  "names": [ { "greek": "Αἴολος", "ru": "Эол", "en": "Aeolus", "note": "" } ],
  "text_issues": [ { "set": "A", "id": "s2", "file_reading": "…", "dindorf_reading": "…", "evidence": "Dindorf II page.line, scan" } ],
  "summary": "5–10 sentences: what was hard, what you are least sure of, what a reviewer should check first"
}
```

All scholia of both sets, in the order of the file.

### `draft-<model>.md`

The same for a human reader: set by set, scholion by scholion, Greek, Russian, English, notes and doubts.
