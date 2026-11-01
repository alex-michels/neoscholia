# Composing the final translation of the Synopsis of music

Text: the anonymous Τῆς μουσικῆς σύνοψις ἠκριβωμένη, the music section of the Byzantine Quadrivium of 1008.

**What exists:**
- six independent scholarly translations, labelled A–F, each into Russian and into English, made directly from one established Greek text;
- three independent reviews of the six;
- the editor's decisions on 30 disputed points, and verified research on the terms.

**Your task.** Write the final Russian and English translation of your units. This is the version that goes to the site, under the name of the editor, a classical philologist.

## Files

All paths are relative to the folder `compose/` (given in your prompt).

| File | What it is | How to use it |
|---|---|---|
| `DECISIONS.md` | The final decisions | Authoritative. Read it in full first. |
| `cards/<ID>.md` | The editor's decision cards with the verified research | Read the cards named in the header of each of your unit packets. |
| `glossary.md` | The three reviewers' recommended renderings of all terms | Consult it for any term not decided in DECISIONS.md. |
| `units/Uxxx.md` | One packet per unit | See below. |
| `edition/section-N.md` | All of the edition's materials for a section | Read when a packet points to it. |
| `../scripts/show_composed.py` | Prints composed units | `python -I <ws-cmp>/scripts/show_composed.py <ws-cmp> out --notes U001-U014` |
| `../scripts/check_composed.py` | Mechanical checks of composed units | `python -I <ws-cmp>/scripts/check_composed.py <ws-cmp> out` |

Each unit packet contains:
- the Greek;
- the edition's apparatus and decisions touching its lines;
- the six translations with their notes and doubts;
- the three reviews (sense, divergences with verdicts, notes to keep, text issues);
- every error the reviewers found.

## How to compose a unit

1. Read the Greek and understand it yourself: grammar, doctrine, numbers. Use the reviewers' "sense" and divergence verdicts, and the translators' doubts. The translation is made from the Greek; the six versions are your material, not your source.
2. For each language, start from the best rendering of the unit. Use the reviewers' "best" picks, but judge for yourself; the reviewers have family biases. Improve it clause by clause with the best wording found in any of the six. Then apply DECISIONS.md and the cards.
3. Check against the error list. No error listed for any translator may appear in your text, even if it was in the version you started from.
4. Check every clause against the Greek:
   - nothing omitted;
   - nothing added outside [square brackets];
   - every number and ratio as in the Greek;
   - the signs ⟨ ⟩, ⟨⟨ ⟩⟩ and † † exactly as in the Greek.
5. **Russian.** Good, natural scholarly Russian, not a calque of the Greek or of English. **English.** Clear modern scholarly British English. Each language is translated from the Greek and stands on its own. Keep the same construal in both, unless a note says why not.
6. Units sometimes split a sentence. Read the neighbouring units' Greek (their packets) so that your sentence joins its neighbours correctly.

## Notes

Merge the notes of the six translators, the reviewers' "notes to keep", the edition's materials and the research on the cards into a small set of well-founded notes. Prefer fewer, better notes; do not retell the translation.

A note is needed for:
- each term decided in DECISIONS.md: the calque or literal sense, the Greek, the established alternatives. Put the main note at the place named in DECISIONS.md; elsewhere give a short cross-reference;
- doctrine and parallels in the theorists, with exact references;
- the arithmetic behind ratios and divisions;
- departures from the classical theorists and probable errors of the compiler;
- textual problems that change the sense: readings of the apparatus, P-only passages, conjectures, cruces.

**Sources.**
- Use only references that occur in your materials: the translators' notes and doubts, the reviewers' evidence, the edition, the cards.
- Do not invent or reconstruct a reference, a page or a quotation.
- If a reference was marked [checked] by anyone in the materials, set `"verified": "checked"`; otherwise `"from memory"`.
- Do not browse the web: everything needed is in the materials. If a point cannot be settled from them, put it in `open`.

**Cross-references** to a note on another unit are written «см. примеч. к [U035]» / 'see the note on [U035]', with the unit id in square brackets. They will be turned into links.

Follow the style rules for notes in DECISIONS.md § 4.

## Output

For each unit write `out/Uxxx.json` (UTF-8, valid JSON), e.g. `out/U040.json`:

```json
{
  "id": "U040",
  "ru": "the Russian text of the unit",
  "en": "the English text of the unit",
  "notes": [
    {
      "anchor_ru": "an exact substring of ru where the note marker goes (a word or short phrase)",
      "anchor_en": "an exact substring of en",
      "kind": "term | doctrine | arithmetic | text | compiler",
      "ru": "the note in Russian",
      "en": "the note in English",
      "source": "the references, clean (no [checked] marks)",
      "verified": "checked | from memory"
    }
  ],
  "basis": "English, 1-4 sentences: which versions (A-F) the RU and the EN mainly follow and what was taken from others; which listed errors were avoided; any Greek kept in the running text and why",
  "decisions": ["P03", "P04"],
  "open": ["a question for the editor, only if a real doubt remains"]
}
```

When all your units are written:
1. Run `check_composed.py` and fix every problem in your units. Problems in other units are not yours; problems about units missing are expected.
2. Print your units with `show_composed.py` and read them once more as a whole, Russian and then English, for consistency and style.

Your final answer is short: the units written, the open questions, and anything the verifier should look at first.
