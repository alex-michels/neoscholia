# Check of composed group 1 (X01–X29, Xylander)

Checked against packet-g1.json, common.json and about.md, one segment at a time. For every segment I compared the composed text with the Latin and the printed lines, with A–D and with the three reviews. I also checked the place cards, the general cards, the agreed points, the corroborated major error (X28 B), the rechecks R01–R04, the brackets and the anchors.

Backups of the state before the check are in `work/chk1/` (`composed-g1.before-check.json`, `segs_*.before.py`). The script that made the changes is `work/chk1/fix_g1.py`.

**Rebuild.** Every change was also made in `segs_a.py`, `segs_b.py` and `segs_c.py`. Running `build.py` again reproduces the checked `composed-g1.json`; I confirmed that the two are identical.

**Sources checked by me.**
- **Theon of Smyrna**, ed. Hiller (1878), the archive.org text, pp. 18–19, 47–49, 64, 70–71.
- **Boethius**, De inst. mus. I (Latin Wikisource): I.6, I.8, I.10, I.16, I.21, I.23.
- **Lewis & Short** (alatius.com): certus, tempero, congruentia, beatitas, commensuratio, coapto.
- **LSJ** (lsj.gr): μόνος.

## Running text: 1 segment changed

- **X27 EN.** "or from several tones, containing in potency…" became "or from several tones, **[a tune]** containing in potency…".
  - *Reason:* without the noun, the participle reads as if it belonged to "tones". In the Latin, continens agrees with cantilena; the Russian «он содержит» is unambiguous.
  - *Consequence:* the anchor_en of the cantilena note changed from "tune" (now twice in the text) to "single tune" (once, verbatim).

## Notes: 11 segments changed

1. **X11, the Theon / Vinet note. Factual error.** "Ниже (X45–X47)" / "Below (X45–X47)" became **X44**, with the Latin quoted (Harmoniae proprium est, ut ea systemata construat atque concinnet).
   - *Reason:* the cited place, Xyl. 47.21–48.1, is X44. X45–X47 deal with the genera, not with the construction of systems.
   - The English "fitting together" became "framing", as G03 requires for concinnare.
2. **X10, the certus note. Wrong source.** The note cited L&S certus II.A.1.b for "definite, fixed, not 'a certain'". II.A.1.b is the indefinite sense ("like quidam, … certain"); "established, settled, fixed" is II.A.1 (checked on L&S).
   - The note now gives II.A.1 as the sense chosen and says that the indefinite sense exists (II.A.1.b) but is less natural in a definition.
3. **X08, the second note. Misquotation of a theorist.** "Thrasyllus in Theon: the note is the tension of a voice partaking of harmony" became "'the tension of an attuned voice' (φωνῆς ἐναρμονίου τάσις), that is, of a voice fit for harmony" (RU «напряжение гармоничного голоса»).
   - *Reason:* Theon p. 47.18–20 Hiller has φθόγγον … φωνῆς ἐναρμονίου τάσιν. There is no "partaking" there, and the old wording made the parallel to harmoniae particeps look closer than it is.
   - The line reference 47.18–24 became 47.18–20, and the source is marked as verified. The open item "Theon not verified" is resolved and removed.
4. **X28, the main note. False cross-reference.** The note said that "in X29–X30 and X35 the Greek names are given literally". In X29 the composed text, following G21 (a), gives the established term with the literal sense in brackets («кварта [«через четыре»]»).
   - The note now says: literal Greek names in X28, X30 and X35; in X29, the term plus the literal sense in square brackets. Card G21 was added to the source.
   - «передаются» became «передавались бы» (a counterfactual, because here the rule is not followed).
5. **X02, the proportio note.** The note duplicated the X25 note on the numerical sense of proportio, with the Boethius I.10 reference. The agreed point asks for one note on that sense, at X25. The range "X35–X38" also included X36, which has no proportio.
   - The note is cut down to the distinction of words (proportio / ratio / proportionalitas), with the list X25, X35, X37, X38, X41 and "see the note to X25". The Boethius reference stays at X25.
6. **X26, the compositae note.** I removed the Boethius I.23 sentence (chromatic incomposite against diatonic composite trihemitone) and its source. The same point and the same source stand in the X27 note on the next segment. In its place: "cf. … the note to X27".
7. **X05, the concinnare / coaptare note.**
   - "постоянная пара" / "standing pair" became "постоянные слова" / "standing words". The two verbs occur together only here.
   - "The first is rendered 'to frame' throughout" was not true of the adverb concinne (X32), which G03 renders «слаженно» / "harmoniously". The note now says so and adds coaptatio «прилаживание» / "fitting together", as in G03.
   - Source: coapto "(eccl. Lat.)" rechecked on L&S.
8. **X07, the congruentia note.**
   - The gloss «согласие, соответствие» / 'agreement, correspondence' became «согласие, стройность, соразмерность» / 'agreement, harmony, congruity'. That is L&S's definition: "agreement, harmony, congruity, symmetry". 'Correspondence' is not in L&S.
   - The source changed from [from memory] to [checked].
   - In the temperare note of the same segment, the source changed from L&S tempero [from memory] to L&S tempero I, 'to divide or proportion duly' [checked]. The note's gloss «приводить в должную меру» agrees with it.
9. **X09, the respectus note.**
   - The Russian said only «и от „соотношения“». It now says that «соотношение» is the rendering of Vinet's habitudo (V12), as in G08 and composed V12.
   - The English note lacked the rendering; "rendered 'relation'" is added.
   - Theon reference: p. 48.8–10 became 48.8–9, verified.
10. **X16, the octave note.** «восходящий множитель высоты в каждой равен 2, на всю двойную октаву — 4» was poor Russian. It became «при движении вверх частота в каждой удваивается, а на всю двойную октаву — учетверяется». The English was changed to match ("going up, the frequency doubles…"). The content is unchanged.
11. **X19, the Theon note.** The note itself was right; the source was not verified. I verified it on the Hiller text:
    - pp. 18.15–19.7: the unit is indivisible as number, the one in sensible things is divisible;
    - pp. 70.14–71.10: the tone cannot be halved, not even on the canon, because of the width of the bridge.

    The source is marked as verified and the open item is removed.
- **X10, X11.** Theon references (p. 48.10–11 σύστημα … ποιὰν περιοχήν; p. 48.12–13 ἁρμονία … συστημάτων σύνταξις) are marked as verified; in X10 the line range 48.10–12 became 48.10–11.

## Checked and left unchanged (main points)

- **Decisions applied as decided:**
  - place cards X01-omnino (a), X02-consideratur (a), X03-propositum-dupli (c);
  - general cards G01–G23 where their words occur: G03 frame / fit together; G04 congruence; G05 «соразмерять» / proportion; G06, G07 «высота, или выдерживаемый тон»; G08 «соотнесённость»; G09; G10–G13 «меса монос», геккайдекахорд; G11 «наименования» / «названия»; G14 species / kind; G15; G16 «прямая»; G17 printed Numerorum, propositum dupli, compositae; G18 «приращение»; G19; G20 (a); G21 (a); G22 (e); G23 sound.
  - All agreed points for X01–X29 are applied (vocabulary, brackets, X15 construal, X18 note, X23 «число шестнадцать», X26 compositae, X27 potentia sive facultas, etc.).
- **Errors.** R01 (X07), R02 and R03 (X14), R04 (X15) and the corroborated major error at X28 (B's English) are corrected in the composed text. All confirmed minor errors are either fixed or not inherited.
- **Numbers recomputed:** √(9/8) ≈ 1.0607; (9/8)^¼ ≈ 1.0299; √72 ≈ 8.485; √288 ≈ 16.97; 17:16 and 33:32 (Vinet V22, checked); 81:64; 729:512; 8 + 8 − 1 = 15; √8; √32; s²/2 and 2s².
- **Brackets.** Every ratio name has its bracket except semisesquioctava (as agreed). The ordinary «вдвое» / "double" (X18 dupla accessio, X23 duplum) has none, as about.md §4.3 says.
- **Theorist claims verified:**
  - Boethius: I.8 sonus definition, I.10 sesquioctava … tonum, I.16 16 : 17 : 18, I.21 "diesis autem est semitonii dimidium", I.23 incomposite triemitonium, I.6 unit and line;
  - Theon: p. 48.8–9 ποιὰ σχέσις, p. 64 πεντεκαιδεκάχορδον (Adrastus);
  - L&S beatitas: Cicero ND 1.95, Quintilian 8.3.32, Macrobius, Apuleius, Augustine;
  - L&S commensuratio: "symmetry", Boethius;
  - LSJ μόνος, η, ον: so masculine monos beside mese is indeed anomalous.
- **Vinet cross-references:** all checked against packets g3 and g4 (V03, V05, V08, V09, V11–V17, V22–V25, V27, V29–V32).
- **Xylander cross-references to group 2:** checked against packet-g2 (X30–X57). The only error found is X11 (above).
- **Anchors.** All 66 anchors still occur exactly once, verbatim.

## Still for the editor (unchanged from the composer)

- **X18.** The agreed comma after sesquioctavae (42.14) must be entered in the reading text and in corrections.
- **X24.** If the conjecture propositi duplum is accepted into the reading text, the last clause becomes option (a) of card X03.
