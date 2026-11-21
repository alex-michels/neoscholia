# Terms pass over both versions: log

Files: `composed-g1.json` … `composed-g4.json`, corrected in place. Each segment whose running text changed has a sentence starting "Terms pass:" added to the end of its `basis`. The table is in `terms-final.json`. The originals before this pass are in `work/tf/backup/`.

## Summary

- **Running text.** 57 replacements in 33 segments: 24 replacements in 12 Xylander segments, 33 in 21 Vinet segments. That is 27 Russian and 19 English fields.
- **Notes.** The text of 25 notes changed: 10 Xylander, 15 Vinet. In addition, 7 anchors were updated because the running text under them changed, and 7 source fields were adjusted.
- **Checks.**
  - All 124 segments are present once each, in order: X01–X58 in g1–g2 and V01–V66 in g3–g4.
  - All 234 note anchors are verbatim and occur exactly once in their Russian and English text.
  - Every ratio name in the running text still has its bracket.
  - The table check (`work/tf/verify.py`) finds every rendering of the table in every segment where its Latin word occurs. Each exception is named in the table's comments.

## Method

- **One rendering per word and sense.** I followed card G01 (b): within a version, one rendering for each Latin word in each clearly distinct sense, and the general cards and agreed points exactly as decided.
- **Collisions.** I also separated two different Latin words that had been given one rendering where this was cheap: in the same sentence or segment, or in a passage parallel to the other version. This follows the logic of cards G08 and G11.
- **The same word in parallel passages.** Where both versions use the same Latin word in a parallel passage, the renderings were brought together.
- **Different words in parallel passages.** Where the versions use different Latin words for the same thing, the difference is kept, in the running text if the languages allow it, otherwise in a note (`cross_version` in the table).
- **What was not touched.** Place-card decisions were not reopened. These include V08-universam-intensionem ('spanning') and V03-diesi-duplo-acutius.

## 1. Running text

### Xylander

| Latin | Segments | Before → after | Reason |
|---|---|---|---|
| componere | X46 | «слагается» → «составляется» | componere is «составлять» / 'compose' in X42 and X46. «слагаться» belongs to conflare. |
| conficere | X34 (twice), X42, X45, X52 | «составляется» / «создаётся» → «складывается»; EN X45, X52 'produced' → 'made' | It collided with componere in X42 and with efficere / comparare. Now it is «складываться» / 'make (up)' throughout. It is the same verb as Vinet's conficitur in the parallels X34 / V39 and X45 / V53. |
| conflare | X34, X45 | EN 'composed' → 'formed' | It is 'formed' in X27 and X49; 'composed' belongs to componere. |
| absolvere | X45 | «складывается из диес» → «осуществляется диесами»; EN 'made up of dieses' → 'completed by dieses' | As in X15 («осуществляется» / 'is completed'). Keeps it apart from conficitur in the same sentence. |
| constituere | X42 | EN 'made up of five strings' → 'constituted of five strings' | constituere is 'constitute' in X18, X26 and X35; 'made up' is conficere. |
| complecti / ambire / comprehendere | X42 | complectens «охватывает» → «объемлет»; ambiens «объемлющий» → «обнимающий» | Xylander's four verbs are now four words in Russian, as they already were in English: complecti «объемлет» (both times) / embrace; ambire «обнимающий» / encompass; comprehendere «охватывает» (as X47) / comprise. |
| reliquus | X26, X52, X53 | «прочие» → «остальные» | It is «остальной» in X40 and X47. «прочие» is Vinet's caetera (V60), the parallel of X52. |
| praeter | X28 | «Кроме них» → «Помимо них» | As X48 and Vinet V33. |
| nomen | X30 | «названия» → «имена» | As X44 and X51 («имя»). Card G11 keeps «название» for appellatio (X29 in the previous sentence, X34). |
| ex coalitu (no verb) | X51 | «образованный» / 'formed' → «[образованный]» / '[formed]' | An added word goes in square brackets (about.md § 4.6), as in Vinet V57 and V59. |
| Exodius | X56 | «заключительная песнь» → «песнь при выходе» | Card G36 decides once for X56 and V64. V64 has «песнь при выходе», and the English of both is 'exit song'. |
| divisio | X56 | «разделений» → «делений» | As X12 («деления») and the parallel V64 («делениям»). |
| discrimen | X57 | «различием» → «различением» | It had coincided with differentia «различие» (X41, X56) and with Vinet's differentia in the parallel V65. The English was already distinct ('distinction' / 'difference'). |
| admiserit | X26 | EN 'rhythm allows' → 'rhythm admits' | Vinet's tulerit in the parallel V31 is 'allows'. The Russian was already distinct («допустит» / «позволит»). |

### Vinet

| Latin | Segments | Before → after | Reason |
|---|---|---|---|
| conficere | V18, V32, V39, V53, V55, V65 | «составляется» / «образуется» / «получается» / «составлен» / «создаются» → «складывается» / «сложен»; EN V53 'there results' → 'is made', V65 'produced' → 'made' | It had five renderings and collided with componere (V52, V61 «составлять») and efficere. It is now «складываться» / 'make (up)', as in Xylander. Place card V02-ex-his-conficitur (the composition reading) is respected. |
| efficere | V04, V53 | EN 'is produced' / 'results' → 'is brought about'; RU V53 «получается» → «создаётся» | One rendering, as V04's parallel X03 (efficiatur 'brought about'). |
| fieri | V31 (V04) | «образуются» / 'arise' → «возникают» / 'come to be' | As V04 «возникающего» / 'come to be'. Xylander's constituuntur in the parallel X26 keeps «образуются». |
| fieri (quae … fit) | V47 | «создаётся» → «производится» | As in the parallel X41 («производимому»). «создаётся» is efficere. |
| peragere | V53, V59 | «осуществляется» / «проходит через», 'carried out' / 'proceeds through' → «проводится» / 'is carried through' | One rendering. Xylander's procedat in the parallel X51 is 'proceeds'. «осуществляется» is now Xylander's absolvere. |
| constituere | V18 | EN 'is made the beginning' → 'is constituted the beginning' | It stood beside conficitur 'is made up' in the same sentence. It is 'constitute' in V60 and V61. |
| complecti | V49 | «охватывающий» → «объемлющий» | As Xylander X42. It is kept apart from comprehendens «охватывающая» in the same sentence; that wording is fixed by place card V08. |
| nomen | V34, V39 | «названия» / «названия» → «имена» / «имени» | Kept apart from appellatio «название» (V35 in the next sentence; V10, V17; card G11), as in Xylander. It also keeps visible Xylander's appellationem («названия») in the parallel X34 / V39 and appellationes in X29 / V34. |
| cognominare | V56 | «называемый» / 'called' → «прозванный» / 'named' | As V52 and V59 («прозвание», 'named after'). vocatum in V53 stays «называемый» / 'called'. |
| varius / diversus | V10, V17, V65 | varius «различный» → «разнообразный» (V10, V17); V65 diversae «разнообразные» → «различные» | varius is now «разнообразный» in both versions (Xylander X57), and diversus is «различный» (Xylander X14). Before, V65 gave variis and diversae the same word. The parallel X14 diversae / V17 variae is now distinct. |
| infinitae | V65 | «бесчисленные» → «бесконечные» | Kept apart from Xylander's innumera («бесчисленные») in the parallel X57. |
| efferre, edere | V15, V16 (twice), V54 | EN 'produced' → 'uttered' | Xylander's same words in the parallels X12 and X13 are 'uttered' (temere editus = 'uttered at random' in both versions now). This also frees 'produce' / 'bring about' for efficere. |
| voluptas | V08 | «удовольствие» → «наслаждение» | The same word in the parallel X07 is «наслаждение». |
| deprehendere | V08 | EN 'found' → 'detected' | As V47 ('found and detected', where invenire is 'found') and Xylander X41. |
| sciendum | V43 | EN 'It must be understood' → 'It must be known' | As Xylander's scire in the parallel X37. 'Understood' is intelligere in Xylander. |
| aptare | V52 | EN 'fit them to' → 'adapt them to' | As Xylander's aptantur (X56, card G03). |
| cognoscetur | V31 | «станет ясно» → «станет понятно» | As the same phrase in the parallel X26. |

## 2. First-occurrence notes: duplicates removed or made cross-references

The Latin word and its gloss now stand once per version, at the first occurrence (or at the first note that treats the word). Later repeats are cut or replaced by "see the note to …".

**Xylander**
- **X25.0.** The rule that proportio is 'proportion' and ratio 'ratio' repeated X02.3. It is now a cross-reference. The numerical sense of proportio, which the agreed point wants noted at X25, stays.
- **X30.1.** The rationale for the double names repeated X28.0. It is now "rendered as there (see the note to X28)".
- **X32.3.** The Boethian gloss of proportionalitas repeated X04.1. It is now a short cross-reference; its source is "note to X04".
- **X37.0.** The three words for 'string' repeated X15.2. It is now "'String' here is fides (see the note to X15)".
- **X37.1.** "Intensio, literally 'tension'" repeated X08.0. It is now "(see the note to X08)".
- **X48.0.** "Constitutio is rendered 'constitution', as in X43" repeated X43.1. Removed, with the card reference in its source.
- **X49.0.** "Vinet has confusio … 'fusion'" repeated X27.4. It is now a cross-reference.
- **X50.0.** "In Russian both are rendered by «слияние»" repeated X27.4. It is now a cross-reference. "(card G19)" was removed from the English: the Russian never had it, and the card stays in the source.

**Vinet**
- **V11.1.** "The cognate convenientia is 'accord' (V05)" repeated V05.1. It is now a cross-reference. "The note must be produced" is now "uttered", matching the running text of V15.
- **V15.1.** The statement of the 'capable of accord — to accord' link repeated V05.1. It is now a cross-reference.
- **V34.0.** "Vinet keeps this term apart from simplicia" repeated V31.1. It is now a cross-reference.
- **V34.3.** The gloss of the three Greek names repeated V33.0. It is now "On the Greek names see the note to V33".
- **V35.0.** "Greek Dia-pason means …" is now marked as a reference to V33. The brief gloss is kept because the argument of the note needs it.
- **V42.0.** "Xylander (X36) specifies the name: super bipartiens tertias" repeated V40.0. Removed.
- **V45.0.** The literal "from the tension of the high" repeated the intensio gloss of V11.0. It is now "(see the note to V11)". The note on acuti required by the agreed point stays.
- **V47.3.** ", literally 'tension'" repeated the intensio gloss of V11.0. Removed. V49.2 keeps its literal gloss because place card V08 requires it.
- **V49.1.** The 8 + 8 − 1 arithmetic and the [system] / [instrument] remark repeated V18.0 and V18.1. They are now "see the notes there".
- **V57.0.** The simplex / non-compositum explanation and the Theon parallel repeated V31.1. Shortened to the sense ('incomposite') plus "rendered 'simple' (see the note to V31)". Card G47's distinction between sense and word is kept. The Theon source was removed with the sentence; it stays at V31.1.

## 3. Notes: differences between the versions made visible, and corrections

- **V03.0** adds "Xylander has universum (X02)". The two words share the rendering «вселенная» / 'universe', so only the note can show the difference.
- **X30.0** adds "Vinet has repetitis at this place (V35)". Both are rendered «повторяются» / 'repeated'.
- **V47.0** adds "Xylander at this place has tensio (X41)". Both are 'tension'.
- **V63.0** adds "Xylander has simplex at this place, X55". simplum and simplex are both «прост» / 'simple' by the agreed point.
- **V65.0** now names transitus / transitio and pulsatio / pulsus. Each pair has one rendering by the agreed point. The same note also misquoted the Xylander running text of X57: «косвенные» and 'quicker' are now «окольные» and 'swifter', as printed in X57.
- **X29.2** adds that the Russian also distinguishes nomen «имя» (X30, X44, X51) from appellatio and nomenclatio.
- **Quotations and anchors brought into line with the changed running text.** V18.2 (the quoted «… складывается»); anchors X30.3, X34.1, X56.1, V18.1, V18.2, V39.0 and V47.0.

## 4. Left for the editor

1. **X45 'completed by dieses'.** This is absolvere, matching X15 'is completed'. The English could be misread as "finished off by dieses". 'Accomplished' in both places would be clearer, but it would change the X15 wording quoted in card G13.
2. **New Russian words.** X42 ambiens «обнимающий» (alternative «окружающий»). V18 'is constituted the beginning' is stiff (alternative 'is set up as the beginning'; the Russian «становится началом» is unchanged).
3. **Ordinary verbs, one-off or idiomatic, left as they were.** They can be unified if strict G01 (a) is wanted:
   - comparare (X57) and efficere (X03) are both «создаётся» / 'brought about';
   - efficere is «получить» / 'produce' in X23 (an active construction, another sense);
   - partiri, distribuere and dividere are all «разделить» / 'divide' (X23, V24, V27), while distribuere is «распределяется» in V64;
   - carere and vacare are both «не иметь» (V11, V15, V39), while vacet is «лишена» in V03;
   - incedunt and ingrediatur are both «проходит» / 'proceeds' in V34, as is Xylander's transire (X29);
   - fieri nequit «невозможно» (X46) against fieri non potest «не может быть» (X23);
   - the verbs of calling (vocare, dicere, appellare: «называть» / 'call').
4. **intelligere.** In X43 it is «постигаются» (apprehended by the intellect); in X36 and X38 «понять». I treated these as two senses; the English is 'understood' throughout.
5. **Pairs that share a rendering by decision.** The difference shows only in the English or in a note:
   - auctio / adauctus; complexus / complexio; transitus / transitio; pulsatio / pulsus; coalitus / confusio (Russian); cantilena / melos (Russian);
   - tensio / intensio (V47); intellectus / mens (Russian); universum / universitas; aequalitate quadam (X32) / aequabiliter (V37).
6. **Pairs left for the editor (Russian or English only).** Each pair is two different Latin words in parallel passages that share one rendering in one language; the other language and, where noted, a note show the difference:
   - haud inconvenienter / non inepte, both «не без основания» (X05 / V06);
   - miraculum / admiratio, both «восхищение» (X06 / V07; X06.0 glosses miraculum);
   - exornat / ornat, both 'adorns' (X07 / V08);
   - disseremus / disceptabimus, both 'discuss' (X07 / V09).
7. **The words for 'together' and 'at the same time'.** simul is «вместе» in X32 (the card G26 wording) but «одновременно» in V37, where pariter and una are both «вместе». Not unified, because card G26 fixes X32.
8. **No note added for Vinet's nomen / appellatio distinction.** The running text («имена» / «названия») shows it; the editor may want a one-line note at V34.
