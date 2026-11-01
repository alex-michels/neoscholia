# Fact-check of the notes, U029–U042 (1 Nov 2026)

Every claim in the notes of `final/U029.json`–`final/U042.json` was checked against a source opened on the web in this pass. The earlier `"verified": "checked"` marks were ignored. Edition-internal claims (readings of Bas., Par., H, V, P; Vincent's pages and footnotes; Xylander's marginalia; the edition's apparatus and decisions) cannot be checked online. They are listed as *edition* and were not checked, as the task requires.

Verdicts: **confirmed** / **wrong** (with the correction) / **imprecise** / **not found online** (with where I looked).

## Sources opened

| Key | What | URL |
|---|---|---|
| THEON-TEI | Theon, ed. Hiller 1878, TEI text with Hiller's `<pb>` and `<lb>` (First1KGreek) | https://raw.githubusercontent.com/OpenGreekAndLatin/First1KGreek/master/data/tlg1724/tlg001/tlg1724.tlg001.1st1K-grc1.xml |
| THEON-OCR | Theon, ed. Hiller 1878, scan OCR (Harvard/Google copy) | https://archive.org/stream/theonissmyrnaei00theogoog/theonissmyrnaei00theogoog_djvu.txt |
| DUPUIS | Theon, ed. and tr. Dupuis 1892 (OCR), for the figures | https://archive.org/stream/thenossmyrnaioup00theo/thenossmyrnaioup00theo_djvu.txt |
| SHCH2009 | Щетников 2009, Theon translation, ΣΧΟΛΗ 3.2 (marginal Hiller page numbers) | https://classics.nsu.ru/schole/3/3-2-theon.pdf |
| SHCH2012 | Щетников 2012, Sectio canonis, ΣΧΟΛΗ 6.1 | https://classics.nsu.ru/schole/6/6-1-sec-can.pdf |
| SHCH-PR | Щетников 2012, [Arist.] Problems XIX, ΣΧΟΛΗ 6.1 (Bekker lines) | https://classics.nsu.ru/schole/6/6-1-arist.pdf |
| SHCH2008a | Щетников 2008а, Nicomachus' Manual, ΣΧΟΛΗ 2.1 | https://classics.nsu.ru/schole/assets/files/2-1-nikomach.pdf |
| SHCH2008b | Щетников 2008б, «Алгоритм Никомаха», ΣΧΟΛΗ 2.1 | https://classics.nsu.ru/schole/2/2-1-schetnikov.pdf |
| TSYP2014 | Цыпин 2014, Cleonides translation, Научный вестник МГК 2014/3 | https://nv.mosconsv.ru/sites/default/files/2021-11/Cleonides_2014_3.pdf |
| STRUNK | Strunk's Cleonides, attalus.org | https://www.attalus.org/translate/cleonides.html |
| JAN | Jan, Musici scriptores Graeci 1895 (Toronto copy OCR) | https://archive.org/stream/musiciscriptores01jank/musiciscriptores01jank_djvu.txt |
| HOCHE | Nicomachus, Introductio arithmetica, ed. Hoche 1866 (OCR) | https://archive.org/stream/nicomachigerasen00nicouoft/nicomachigerasen00nicouoft_djvu.txt |
| BELL | Bellermann 1841 (OCR) | https://dn790007.ca.archive.org/0/items/bellermann-1841-anonymi-scriptio-de-musica/Bellermann%201841%20Anonymi%20Scriptio%20de%20Musica_djvu.txt |
| MACRAN | Macran 1902 (OCR) | https://archive.org/stream/harmonicsofarist00aris/harmonicsofarist00aris_djvu.txt |
| LSJ | lsj.gr (LSJ, DGE, Pape, Dvoretsky as printed there) | https://lsj.gr/wiki/<lemma> |

The PDFs were read through WebFetch, which saved them to the tool-results folder; their text was extracted with a local script in the scratchpad. Nothing was saved inside the project.

---

## U029

**Note 1** (comparison of the P passage with U021–U022). *Edition*; it compares Greek texts within the work. Not checked.

**Note 2**
- ἀριθμητικῇ, a conjecture for P's ἀριθμητικόν; τῆς for τοῦ. *Edition*.
- "ἀνεγχώρητος … LSJ, from the scholia to Hermogenes only". **Confirmed.** LSJ, https://lsj.gr/wiki/ἀνεγχώρητος: "impossible, Sch.Hermog. in Rh.7.135 W.", which is the only citation.
- "DGE, from Gregory of Nazianzus". **Confirmed.** The DGE entry on the same page cites Greg. Naz. (PG 36.116C), with Hesychius and the Hermogenes scholia beside it. Pape gives «unzulässig, unmöglich», Sp.
- "Lampe p. 131". **Not found online.** I found no online Lampe. Searched the web and archive.org.
- "attested only predicatively, never with an attributive adjective". **Not found online** as a universal claim. All the loci quoted in LSJ, DGE and the Greek LS on lsj.gr are predicative. This is consistent, but it is not proof.

## U030

**Note 1.** Cross-references only (U023, U031). Confirmed against the Greek of U023.

**Note 2**
- "ἑξκαιδέκατος is a lemma of its own in LSJ (Hippocrates, Epidemics 1.26)". **Confirmed.** https://lsj.gr/wiki/ἑξκαιδέκατος: "sixteenth, Hp.Epid.1.26". The Hippocratic passage itself was not opened.
- "Vincent printed ἑξδέκατον, a form not in LSJ". **Confirmed** for LSJ: https://lsj.gr/wiki/ἑξδέκατος returns 404. Vincent's print is *edition*.
- "ὁ ἔνατος ἀριθμός = 9 in U018". **Confirmed** from the Greek of U018: ὡς ὁ ἔνατος ἀριθμὸς πρὸς τὸν ὄγδοον.
- Arithmetic: 16 = 4²; 8 and 32 are not squares; 11 is not a square. **Confirmed.**

## U031

**Note 1**
- "LSJ s.v. περιτίθημι: π. τινὰ ὕβρει, Diogenes Laertius 6.33". **Confirmed.** It is LSJ II.2, "reversely, π. τινὰ ὕβρει envelop him with…", D.L. 6.33. https://lsj.gr/wiki/περιτίθημι
- "No correction is needed: περιτίθημι also takes the reverse construction". **Doubtful.** In LSJ's reverse construction the thing put round is in the *dative* (ὕβρει). P has two accusatives, τετράγωνον αὐτήν. Neither LSJ, Dvoretsky, Bailly nor Pape on that page records a double accusative. So the parallel supports the accusative of the thing enveloped only together with a dative. *Question* for the editor.
- Other differences (γεωμέτρης without the article; λαβών / μεταλαβών). Confirmed against the Greek of U024.

## U032

**Note 1.** Structure of the P passage; Vincent's εἰρήσθω. *Edition*. Cross-references U026–U031 are consistent with the Greek.

## U033

**Note 1.** Παρὰ / Περὶ. *Edition*.

**Note 2**
- "established fourth, fifth and octave (Цыпин 2013; Цыпин 2014; Щетников 2012)".
  - **Confirmed** for Цыпин 2014: «Консонансы — кварта, квинта, октава» (TSYP2014, ch. 5).
  - **Confirmed** for Щетников 2012: «Каждый из интервалов кварты и квинты…», Prop. 11 (SHCH2012).
  - Цыпин 2013 **not found online.** The archive.org item 2013_20210528 exists, but its full-text file could not be fetched (404 on the redirect).
- "Theon of Smyrna (p. 51.4–20 Hiller) explains διὰ πασῶν from the eight-stringed lyre … hypate … nete; the names were kept". **Confirmed.**
  - THEON-TEI p. 51, lb 10–15: ἀπὸ τῆς ὀκταχόρδου λύρας ὁ πρῶτος καὶ βαρύτατος … ὑπάτη … τῇ νήτῃ.
  - Before lb 20: τῶν πρώτων συμφωνιῶν αἱ προσηγορίαι φυλάττονται, διὰ τεσσάρων, διὰ πέντε, διὰ πασῶν.
  - SHCH2009 p. 493 agrees. The passage belongs to Adrastus' report, which Theon introduces at p. 49.6 (ὁ δὲ περιπατητικὸς Ἄδραστος). The note says "Theon"; U034 says "Adrastus in Theon". Both are acceptable.
- Ratios 4:3, 3:2, 2:1. Confirmed.

## U034

**Note 1**
- "ἄμεσος of premises without a middle term (Aristotle, Prior Analytics 68b30; Posterior Analytics 72b19)". **Confirmed** through the lexica.
  - LSJ, https://lsj.gr/wiki/ἄμεσος: "ἄμεσα καὶ ἀναπόδεικτα, of propositions that cannot be proved syllogistically by means of a middle term, Arist.APr.68b30, APo.72b19".
  - DGE on the same page also cites APr. 68b30 and APo. 72b19.
  - The Greek text at Bekker 68b30 and 72b19 was not opened directly: Perseus refuses WebFetch (403). The passages are APr. II 23 (πρώτης καὶ ἀμέσου προτάσεως) and APo. I 3 (τὴν τῶν ἀμέσων ἀναπόδεικτον); this identification is from memory and agrees with LSJ.
- "ἔμμεσος, 'having a middle term', in the late commentators (Simplicius, Olympiodorus; LSJ, DGE)". **Confirmed, with detail** (open point). https://lsj.gr/wiki/ἔμμεσος:
  - DGE I.2, "que tiene término medio", opposed to ἄμεσος: Olymp. in Mete. 242.28; τὰ ἔ. (contraries that admit an intermediate, opposed to τὰ ἄμεσα): Simp. in Cael. 340.33.
  - DGE I.3 "mediato": Eustr. in EN 331.2.
  - DGE II, adverb ἐμμέσως, "indirectamente, de forma mediata": Eust. 1097.16; cf. Them. in APo. 31.6; **Anon. Bellerm. 4**.
  - LSJ has "intermediate" (Olymp. in Mete. 242.28), "having an intermediate term" (ἔ. ἐναντία, Simp. in Cael. 340.33), "mediate" (Eustr.), and ἐμμέσως "mediately" (Them. in APo. 31.6).
  - So in Simplicius the word is used of *contraries with an intermediate*, not of premises. The syllogistic sense "mediate" is clearest in Themistius (adverb) and Eustratius. *Improvement*: name the loci.
- "Anonymus Bellermanni §§ 4–6: ἀμέσως 'to the adjacent note', ἐμμέσως 'through three, four, five notes'". **Confirmed in substance.**
  - BELL § 4: ποικίλως, ἀμέσως τε καὶ διὰ μέσου. §§ 5–6: ἀμέσως μὲν … ἐμμέσως δὲ διὰ τριῶν, with examples labelled διὰ τεσσάρων, διὰ πέντε.
  - ἀμέσως is not glossed in words. It is illustrated by a step to the adjacent degree.
  - DGE cites Anon. Bellerm. 4 for ἐμμέσως.
- "Cleonides' ἑξῆς / μὴ ἑξῆς φθόγγοι, ch. 5". **Confirmed.** JAN p. 188: ἀσύνθετα μὲν οὖν διαστήματά ἐστι τὰ ὑπὸ τῶν ἑξῆς φθόγγων περιεχόμενα … σύνθετα δὲ τὰ ὑπὸ τῶν μὴ ἑξῆς.
- "Strunk: 'consecutive notes'". **Confirmed.** STRUNK § 5: "The incomposite intervals are those bounded by consecutive notes".
- "Tsypin 2014 (смежные / несмежные)". **Confirmed.** TSYP2014 ch. 5: «Несоставные интервалы охватываются смежными звуками … а составные — несмежными».

**Note 2**
- "Adrastus in Theon (p. 51.4–20 Hiller): of notes tuned in succession, the first to be concordant are those fourth in order …, then fifth, then eighth". **Confirmed.**
  - THEON-TEI p. 51 lb 5: τέταρτοι τάξει συμφωνοῦσι πρὸς ἀλλήλους … ἔπειτα οἱ πέμπτοι … ὄγδοοι, τὴν διὰ πασῶν.
  - SHCH2009 p. 492: «В последовательно настроенных голосах первыми будут те, что созвучны … через четыре».
- Counting: 4 notes / 3 intervals etc. Confirmed.

**Note 3.** τελειούμενον / τελούμενον, the readings. *Edition*. The general sense of περαίνω ("bring to an end") is uncontroversial and was not opened.

## U035

**Note 1**
- "Theon (p. 51.4–20 Hiller) explains the name … from the eight-stringed lyre". **Confirmed**, as at U033.
- "φερωνυμία, 'aptness of a name', the fitness of a name to its object (LSJ)". **Imprecise.** LSJ, https://lsj.gr/wiki/φερωνυμία, has two senses:
  - "name received from an event or action, Opp.H.1.243";
  - "accordance of a name with an event, Eust.776.49".
  - LSJ does not say "aptness" or "to its object". Pape's entry runs the same way: «das Tragen des Namens nach einer Begebenheit, Handlung». Correction proposed in the findings.

**Note 2**
- Classical double fourth / double fifth = 16:9 and 9:4, not consonant (Euclid, Sectio canonis 11; [Aristotle], Problems XIX 41). **Confirmed.**
  - Euclid 11: JAN OCR τὸ ἄρα … διάστημα δὶς διὰ τεσσάρων … ἐστὶ διάφωνον, then αὐτὴ δὲ ἀπόδειξις καὶ ἐπὶ τοῦ διὰ πέντε. SHCH2012, Prop. 11: «интервал двойной кварты … является разнозвучным … такое же доказательство даётся для квинты».
  - Problems XIX 41 (921b1). SHCH-PR: «Почему двойная квинта и двойная кварта не являются созвучными, а двойная октава является?». JAN OCR: Διὰ τί δὶς μὲν δι' ὀξειῶν … δὶς διὰ τεττάρων οὐ συμφωνεῖ, δὶς διὰ πασῶν δέ.
  - Euclid states the double fifth only by the "same proof". That is enough for the note.
- "usual names … διὰ πασῶν καὶ διὰ τεσσάρων / καὶ διὰ πέντε (Theon of Smyrna, pp. 52, 56 Hiller; Cleonides ch. 8; Цыпин 2014)". **Confirmed.**
  - Theon p. 52: SHCH2009 p. 493 «(52) … октаву и кварту, или октаву и квинту, или двойную октаву».
  - Theon p. 56: THEON-TEI τοὺς μὲν διὰ πασῶν καὶ διὰ τεσσάρων ἐν λόγῳ τῶν η΄ πρὸς γ΄ … τοὺς δὲ διὰ πασῶν καὶ διὰ πέντε ἐν λόγῳ τριπλασίῳ.
  - Cleonides ch. 8: STRUNK "diapason plus diatessaron … diapason plus diapente".
  - TSYP2014 ch. 8: «четвертая — октава с квартой … пятая — октава с квинтой».
- "ундецима и дуодецима (Цыпин 2013)". **Not found online** (Цыпин 2013 unavailable, see U033). The terms are standard; SHCH2009 p. 493 n. 42 equates октава и кварта = ундецима, октава и квинта = дуодецима.
- "ἐπαναδιπλουμένων ('repeated again'; LSJ s.v. ἐπαναδιπλόω)". **Confirmed.** LSJ: "repeat yet again, Arist.Pr.910b25 …; Pass., be repeated". https://lsj.gr/wiki/ἐπαναδιπλόω
- Xylander's proposals; readings of H, Par., V, Bas. *Edition* (skipped as instructed).
- Arithmetic: 16:9, 9:4, 8:3, 3:1, 4:1. Confirmed.

## U036

**Note 1**
- "The division goes back to Thrasyllus in Theon of Smyrna (p. 48 Hiller): antiphonic, like the octave and the double octave; paraphonic, like the fifth and the fourth". **Confirmed.**
  - THEON-TEI p. 48 (from lb 15): σύμφωνα μὲν τά τε κατ' ἀντίφωνον, οἷόν ἐστι τὸ διὰ πασῶν καὶ τὸ δὶς διὰ πασῶν, καὶ τὰ ⟨κατὰ⟩ παράφωνον, οἷον τὸ διὰ πέντε, τὸ διὰ τεσσάρων.
  - RU quotation from Щетников 2009 **confirmed verbatim**: «антифонными, каковы октава и двойная октава, и парафонными, каковы квинта и кварта» (SHCH2009 p. 491).
- "Thrasyllus does not have the octave and a fourth / octave and a fifth among them". **Confirmed** (same passage).
- "ἀντίφωνον for the octave is already in [Aristotle], Problems XIX 39 (boys' and men's voices; LSJ s.v. ἀντίφωνος III)". **Confirmed.**
  - LSJ III: "as subst., ἀντίφωνον, τό, concord in the octave, τὸ ἀ. σύμφωνόν ἐστι διὰ πασῶν Arist.Pr.918b30, 921a8". 921a8 is XIX 39.
  - SHCH-PR XIX 39: «антифон создаётся юными мальчиками и мужчинами». JAN OCR: ἐκ παίδων νέων καὶ ἀνδρῶν γίνεται τὸ ἀντίφωνον.
- "(Jan p. 100)". **Doubtful.** The running head of the JAN OCR near XIX 39 reads "Problemata XIX 38—39b. 101". That suggests XIX 39 begins on p. 101. The OCR is poor, so this is a *question*.
- "Gaudentius (Harmonic Introduction 8): παράφωνοι … between consonance and dissonance (tritone, ditone)". **Confirmed.** JAN OCR (Gaudentius ch. 8):
  - παράφωνοι δὲ οἱ μέσοι μὲν συμφώνου καὶ διαφώνου, ἐν δὲ τῇ κρούσει φαινόμενοι σύμφωνοι;
  - examples ἐπὶ τριῶν τόνων ἀπὸ παρυπάτης μέσων ἐπὶ παραμέσην and ἐπὶ δύο τόνων ἀπὸ μέσων διατόνου ἐπὶ παραμέσην.
- "(Jan pp. 337–338)". **Not found online.** The OCR shows Meibom's page markers but no legible Jan running heads.

**Note 2.** Xylander at Bas. 28.11. *Edition*.

## U037

**Note 1**
- "LSJ gives ἀνισόχρονος as 'of unequal duration'". **Confirmed.** "of unequal duration, Herodic. ap. Orib.8.4.6; in Metric, composed of unequal times, Aristid.Quint.1.24". https://lsj.gr/wiki/ἀνισόχρονος
- "LSJ s.v. αὐτός IV.4: κατὰ τὸ αὐτό 'together, at the same time'". **Confirmed.** It is IV.4 (adverbial phrases with prepositions), "together, at the same time", Act.Ap.14.1. https://lsj.gr/wiki/αὐτός
- "Theon, p. 51 Hiller: κατὰ ταὐτὸ … ἅμα κρουσθέντων". **Confirmed.** THEON-TEI: the sentence begins after `<pb n="51"/>`, κατὰ ταὐτὸ δὲ ἀμφοῖν ἅμα κρουσθέντων ἡδεῖα καὶ προσηνὴς … φωνή. SHCH2009: «два голоса, извлечённые вместе» (the RU gloss is confirmed).
- "Thrasyllus in Theon (pp. 48.16–49.2 Hiller) defines the two kinds otherwise". **Confirmed.**
  - THEON-TEI / OCR p. 48.21–49.2: τά τε γὰρ κατ' ἀντίφωνον σύμφωνά ἐστιν, ἐπειδὰν τὸ ἀντικείμενον τῇ ὀξύτητι βάρος συμφωνῇ, τά τε κατὰ παράφωνόν ἐστι σύμφωνα, ἐπειδὰν μήτε ὁμότονον φθέγγηται φθόγγος φθόγγῳ μήτε διάφωνον, ἀλλὰ παρά τι γνώριμον διάστημα ὅμοιον.
  - By the OCR line count the classification begins at 48.17, so "48.16" is at most one line off. Not reported as a finding.
- "[Aristotle], Problems XIX 39 (consonance as a ratio of motions, like feet in metre; antiphon of boys' and men's voices sounding together)". **Confirmed.**
  - JAN OCR: καθάπερ ἐν τοῖς μέτροις οἱ πόδες ἔχουσι πρὸς αὑτοὺς λόγον.
  - SHCH-PR XIX 39: «голоса созвучия состоят друг к другу в отношении движений».
- "XIX 18 (only the octave is magadized)". **Confirmed.** SHCH-PR XIX 18 (918b40ff.): «Почему в пении употребляется одно лишь созвучие октавы? Ведь только оно употребляется в магадиде».
- "(Jan pp. 88, 100–101)". p. 88 **not found online**. For 100–101 see U036: the XIX 39 material is on p. 101 at least.
- "Equal vibration periods cannot be meant: the notes of an octave have different periods". This is correct physics. But XIX 39, which the note cites, explains the octave by the coincidence of the notes' periods. JAN OCR: ἔτι δὲ ὑπάτῃ συμβαίνει τὴν αὐτὴν τελευτὴν τῶν ἐν τοῖς φθόγγοις περιόδων ἔχειν. SHCH-PR: in the other consonances the voices are «потенциально не равны». This "coincident periods" model is a third possible background for ἰσοχρόνως / ἀνισοχρόνως, and the note does not mention it. *Question*.

**Note 2.** Readings at Bas. 28.15–18. *Edition*. The parallel "Theon, p. 48 Hiller: τὸ ἀντικείμενον τῇ ὀξύτητι βάρος" is **confirmed** (THEON-TEI p. 48, lb 20–21).

**Note 3.** Arithmetic and note positions. **Confirmed.**
- Against U014 (1 proslambanomenos, 4 hypate diatonos = lichanos hypaton, 5 hypate meson, 8 mese, 11 diatonos diezeugmene, 12 nete diezeugmene, 15 nete hyperbolaion). In the standard diatonic Greater Perfect System these are A, D, E, a, d, e, a′.
- 8–1, 11–4, 12–5 and 15–8 are octaves.
- 11, 12 and 15 against 1 give 8:3, 3:1 and 4:1.

**Note 4**
- "Plato, Republic 349e (tightening / slackening of strings)". **Confirmed** through LSJ s.v. ἐπίτασις 1: "ἐπίτασις καὶ ἄνεσις τῶν χορδῶν tightening and slackening, Pl.R.349e". LSJ s.v. ἄνεσις also cites R. 349e.
- "Cleonides ch. 2 … raising and lowering of pitch". **Confirmed.** JAN p. 181: ἐπίτασίς ἐστι καὶ ἄνεσις, ἀποτέλεσμα δὲ τούτων ὀξύτης καὶ βαρύτης.
- "Цыпин 2014: «повышение и понижение»". **Confirmed.** TSYP2014 ch. 2: «То, что делает различными высоты, — повышение и понижение».
- "Macran 1902; Strunk: 'tension / relaxation'". **Confirmed.**
  - MACRAN: "Tension is the continuous transition of the voice from a lower position to a higher, relaxation that from a higher to a lower."
  - STRUNK § 2: "The causes of the difference between pitches are tension and relaxation".
- "Theon, p. 57 Hiller: διὰ τῆς ἐπιτάσεως καὶ ἀνέσεως τοῦ πνεύματος". **Confirmed.** THEON-TEI p. 57, line 5: ἢ διὰ τῆς ἐπιτάσεως καὶ ἀνέσεως τοῦ πνεύματος. SHCH2009 «по усилению и ослаблению дыхания» is confirmed (before the marker (57), on p. 495).

## U038

**Note 1**
- The quotation of Thrasyllus in Theon, p. 49.3–5 Hiller: διάφωνοι δ' εἰσὶ καὶ οὐ σύμφωνοι φθόγγοι, ὧν ἐστι τὸ διάστημα τόνου ἢ διέσεως· ὁ γὰρ τόνος καὶ ἡ δίεσις ἀρχὴ μὲν συμφωνίας, οὔπω δὲ συμφωνία. **Confirmed verbatim.**
  - THEON-TEI and THEON-OCR. The OCR lines of p. 49 are: line 2 ends "… ὅμοιον. διά-", line 3 "φωνοι δ' εἰσὶ καὶ οὐ …", line 4 "διάστημα τόνου ἢ διέσεως· ὁ γὰρ τόνος καὶ ἡ δίεσις", line 5 "ἀρχὴ μὲν συμφωνίας, οὔπω δὲ συμφωνία." with marginal 5.
  - Strictly 49.2–5; the cited 49.3–5 is acceptable. Line 6 begins Adrastus, so the attribution to Thrasyllus is right.
- "Thrasyllus names only the tone and the diesis". Confirmed.

## U039

**Note 1**
- "figures 2½, 3½, 6, 8½, 9½, 12 … as in Cleonides ch. 8". **Confirmed.**
  - JAN: ἐλάχιστον μὲν τὸ διὰ τεσσάρων, τόνων δύο ἡμίσεος … ἕκτον τὸ δὶς διὰ πασῶν, τόνων δώδεκα.
  - STRUNK § 8 and TSYP2014 ch. 8 agree.
- "(Jan p. 194)". **Not verified exactly.** In the OCR the running head "… c. 7. 8 … 193" stands just before the start of ch. 8, and no "194" head is legible. The list may begin at the foot of p. 193.
- "Pythagorean octave < 6 tones, fourth < 2½ tones (Euclid, Sectio canonis 14–15)". **Confirmed.** SHCH2012: Prop. 14 «Октава меньше шести тонов»; Prop. 15 «Кварта меньше двух тонов и полутона, и квинта меньше трёх тонов и полутона». The JAN OCR has the same propositions. "(Jan pp. 160–161)": **not verified**, since no legible Jan running heads.
- Arithmetic, recomputed with Python (fractions and log₂). **All confirmed.**
  - (4/3)/(9/8)² = 256/243.
  - 2.5 × 203.910 − 498.045 = 11.73 c.
  - 2 × 203.910 + 104.955 − 498.045 = 14.73 c (17:16 = 104.955 c).
  - (9/8)⁶/2 = 531441/524288 = 23.46 c.
  - 1/8 + 1/8 + 1/16 = 15/48 against 16/48; 1/48 < 1/32.
  - U018 gives 8½:8 = 17:16 and 8¼:8 = 33:32, as the note says.
- "Theon of Smyrna (pp. 66–67 Hiller) reports … Aristoxenus 2½ tones … Plato two tones and the so-called leimma … τὸ δὲ λεῖμμα τοῦτό φησιν ἀκατονόμαστον εἶναι". **Confirmed** (open point).
  - THEON-TEI: the paragraph begins on p. 66. After `<pb n="67"/>`: ἀλλ' Ἀριστόξενος [lb 10] μέν φησιν ἐκ δύο ἡμίσους τόνων αὐτὸ συγκεῖσθαι τελείων, Πλάτων δὲ ἐκ δύο τόνων καὶ τοῦ καλουμένου λείμματος. τὸ δὲ λεῖμμα τοῦτό φησιν ἀκατονόμαστον εἶναι, ἐν λόγῳ δὲ εἶναι ἀριθμοῦ πρὸς ἀριθμὸν ὃν ἔχει τὰ σνϛ΄ πρὸς σμγ΄ … [lb 15] ὑπεροχὴ ιγ΄.
  - The quoted Greek is exact. The precise place is p. 67.9–13. *Improvement*: cite "p. 67.9–13 Hiller".
  - Hiller's apparatus marks ἐκ δύο ἡμίσους τόνων as suspect. SHCH2009 renders it «из двух тонов и совершенного полутона», so the sense "2½" holds.

**Note 2**
- Arithmetic: octave + two fourths = 6 + 5 = 11 tones, 2 × (4/3)² = 32/9; octave + two fifths = 6 + 7 = 13 tones, 2 × (3/2)² = 9/2. **Confirmed.**
- Xylander's *abundant omnino, et delenda sunt*. *Edition*.

## U040

**Note 1**
- "The specific name for 8:3 in Nicomachus is διπλασιεπιδιμερής (Introduction to Arithmetic I 23)". **Confirmed** (open point).
  - HOCHE p. 64 (running head "64 ΝΙΚΟΜΑΧΟΥ ΓΕΡΑΣΗΝΟΥ"), ch. κγ΄ Περὶ πολλαπλασιεπιμεροῦς. OCR, raw: "οίον ὁ μεν η τού γ διπλαΰιεπιδιμερής και ὁ ις τού ς διπλαΰιεπιδιμερης καϊ κα&όλον οι από όγδοάδος όγδοάδι διαφέροντες".
  - That is: οἷον ὁ μὲν η΄ τοῦ γ΄ διπλασιεπιδιμερής, καὶ ὁ ιϛ΄ τοῦ ϛ΄ διπλασιεπιδιμερής, καὶ καθόλου οἱ ἀπὸ ὀγδοάδος ὀγδοάδι διαφέροντες ….
  - Nicomachus thus gives **16:6**, the author's own example in U041, beside 8:3. *Improvement.*
- "Theon of Smyrna (p. 56.12–17 Hiller) calls 8:3 πολλαπλασιεπιμερής … (διπλάσιος γὰρ καὶ δισεπίτριτος)". **Confirmed.** THEON-TEI p. 56, ll. 13–15: ὅς ἐστι πολλαπλασιεπιμερής, διπλάσιος γὰρ καὶ δισεπίτριτός ἐστι.
- EN: "LSJ renders the class name ἐπιμερής 'superpartient'". **Confirmed.** "superpartient, of numbers of the form 1+2/x, 1+3/x, etc., Theo Sm.p.76H., Nicom.Ar.1.17". https://lsj.gr/wiki/ἐπιμερής
- RU: "«Двукратное сверхчастное» … Цыпин 2013, у которого «сверхчастные» — ἐπιμερεῖς, а «сверхчастичные» — ἐπιμόριοι". **Not found online** (Цыпин 2013 full text unavailable; card P03 records an earlier reading of the archive.org OCR).
- RU: "У Щетникова (Щетников 2008а) «сверхчастное» означает ἐπιμόριος …, а ἐπιμερής — «сверхмногочастное»". **Wrong reference.**
  - The whole text of Щетников 2008а (Nicomachus' Manual, ch. 1–12 and afterword, extracted completely) contains neither «сверхчастное» nor «сверхмногочастное». It uses only «полуторное, сверхтретье, сверхвосьмерное, двукратное».
  - The usage is in **Щетников 2008б** («Алгоритм Никомаха», same issue), p. 56: «сверхчастное (ἐπιμόριον), сверхмногочастное (ἐπιμερές)».
  - It is also in Щетников 2009 p. 495 («многократным-и-сверхмногочастным») and Щетников 2012 p. 101 («в сверхчастном, либо в сверхмногочастном»).
  - Correction in the findings.

**Note 2.** Readings of δίς at Bas. 29.14–15. *Edition*.

**Note 3**
- "Complete lists: Theon of Smyrna, pp. 56, 63 Hiller (τὸ δὶς διὰ πασῶν ἐν λόγῳ τετραπλασίῳ)". **Confirmed.**
  - p. 56 has the full list 4:3, 3:2, 2:1, 8:3, 3:1, 4:1 (… τοὺς δὲ δὶς διὰ πασῶν ἐν τετραπλασίῳ).
  - p. 63 has the quoted words verbatim: ὁμοίως δὲ τὸ δὶς διὰ πασῶν ἐν λόγῳ τετραπλασίῳ.
  - p. 63 composes 8:3, 3:1 and 4:1 only, while 4:3, 3:2, 2:1 are on p. 62. "pp. 56, 62–63" would be more exact. Minor; not reported.
- "Gaudentius, Harmonic Introduction 10 (Jan pp. 339–340)". **Confirmed** for the content: JAN OCR, Gaudentius ch. 10, has τῆς μὲν διὰ τεσσάρων ἐπίτριτος … ἡμιόλιος … διπλάσιος … τριπλάσιος … τετραπλάσιος. Gaudentius names 8:3 διπλασιεπιδίμοιρος. Jan pages **not verified**.
- "cf. Euclid, Sectio canonis 12 (without the octave and a fourth)". **Confirmed** (open point).
  - SHCH2012, Prop. 12, derives 3:2, 4:3, 2:1, then «интервал октавы и квинты будет трёхкратным. А двойная октава является четырёхкратной». JAN OCR: ὥστε καὶ τὸ διὰ πασῶν καὶ τὸ διὰ πέντε τριπλάσιον. τὸ δὲ δὶς διὰ πασῶν τετραπλάσιόν ἐστιν.
  - 8:3 is absent. It is neither multiple nor epimoric, and the Sectio's introduction admits only those for consonances: «каждое созвучие называется … либо кратному, либо сверхчастному», SHCH2012 p. 101. Щетников's introduction notes that the Pythagorean theory leaves the octave and fourth aside.
  - "(Jan p. 160)" **not verified.**
- Arithmetic: 8:3 = 2⅔. Confirmed.

## U041

**Note 1.** Arithmetic and cross-references. **Confirmed.**
- 8:6 = 4:3, 9:6 = 3:2, 12:6 = 2:1, 16:6 = 8:3, 18:6 = 3:1, 24:6 = 4:1; 16 = 2 × 6 + 4.
- U018 has ὁ ἔνατος ἀριθμὸς πρὸς τὸν ὄγδοον.

**Note 2**
- "Theon of Smyrna uses the same series 6, 8, 9, 12, 16, 18, 24 on the base 6 (pp. 62–64 Hiller, with the diagram on p. 64)". **Wrong.**
  - THEON-TEI and SHCH2009 pp. 496–497, Hiller pp. 62–63:
    - Theon uses 6, 8, 12 and 6, 9, 12 (p. 62);
    - for the octave and a fourth he uses **3, 4, 8**: τὸ ἐξ ἀμφοῖν ἐν λόγῳ τῶν η΄ πρὸς τὰ γ΄; SHCH2009 «вместе они дают отношение 8 к 3, ведь для 3 сверхтретьим будет 4, и для 4 двукратным будет 8»;
    - 6, 9, 18 for the octave and a fifth; 6, 12, 24 and 6, 18, 24 (and 6, 8, 24) for the double octave (p. 63).
  - The number 16 does not occur on pp. 62–64.
  - The p. 64 figure is a set of diagrams of compounded ratios, not the series. Its labels are ἡ διὰ δ΄ … ἡμιόλιος ἐπίτριτος … διπλάσιος καὶ δισεπίτριτος … τριπλάσιος τετραπλάσιος. DUPUIS's figure shows the terms "8 4 3" (octave and fourth, 2 + 2/3) and "18 9 6" (octave and fifth, 3).
  - The pair 16:6 is in Nicomachus, Arith. I 23 (see U040). Correction in the findings.
- "6, 8, 9 and 12 are the numbers of hypate, mese, paramese and nete in Nicomachus (Manual 6)". **Confirmed.** SHCH2008a, ch. 6: «Гипатой был назван голос, которому соответствует число 6, месой — число 8 …, парамесой — 9 …, нетой — 12». "(Jan p. 248)": **not verified**. Щетников gives Jan pp. 236–265 for the whole Manual.
- Notes 1, 4, 5, 8, 11, 12, 15 at proslambanomenos = 6. **Confirmed** by calculation (see U037 note 3).

## U042

**Note 1.** Extent and readings of the second P passage. *Edition*.

**Note 2.** Cross-reference to U034. See U034.

**Note 3.** μέλος. *Edition* and cross-references.

**Note 4.** 16, 18, 24 to 6 = 8:3, 3:1, 4:1. **Confirmed.**

**Note 5**
- "Cleonides (ch. 8) likewise shows the six consonances from the proslambanomenos". **Wrong in detail.** Only five of the six are exemplified from the proslambanomenos; the fourth is given from hypate hypaton to hypate meson.
  - JAN OCR: τὸ διὰ τεσσάρων … οἷόν ἐστι τὸ ἀπὸ ὑπάτης ὑπατῶν ἐπὶ ὑπάτην μέσων; then ἀπὸ προσλαμβανομένου ἐπὶ ὑπάτην μέσων (fifth), … ἐπὶ μέσην (octave), … ἐπὶ νήτην συνημμένων (octave and fourth), … ἐπὶ νήτην διεζευγμένων (octave and fifth), … ἐπὶ νήτην ὑπερβολαίων (double octave).
  - STRUNK § 8: "that from the hypate hypaton to hypate meson".
  - TSYP2014 ch. 8: «от гипаты низших до гипаты средних».
  - Correction in the findings.
- "(Jan p. 194.5–16)". **Not verified** (see U039).
- Arithmetic: (9/8)² = 81/64; (9/8)³ = 729/512; 81/64 × 256/243 = 4/3. **Confirmed.**
- "ποιός … as in U009–U010". Cross-reference, not checked.

**Note 6.** Cross-references to U026–U027. Consistent with the Greek of U026 and U027 (σύμφθαρσις in U027).

**Note 7**
- "LSJ gives 'call to account; keep accounts'". **Confirmed.** LSJ: "call to account, Epimyth. ad Aesop. 406 …; keep accounts, Antioch.Astr. …". https://lsj.gr/wiki/λογοθετέω
- "in medieval Greek the verb also means 'serve as logothete'". **Confirmed** in the Modern Greek dictionary on the same lsj.gr page: μσν. «ασκώ το αξίωμα του λογοθέτη». LSJ itself does not have it, and the note does not say it does.

---

## Open points (task list)

- **U034.** APr. 68b30 and APo. 72b19 are confirmed through LSJ and DGE. ἔμμεσος occurs in Olymp. in Mete. 242.28 (DGE I.2; LSJ "intermediate") and in Simp. in Cael. 340.33, of contraries that admit an intermediate. The logical "mediate" sense is in Eustr. in EN 331.2, and the adverb in Them. in APo. 31.6. DGE cites Anon. Bellerm. 4 for ἐμμέσως. *Improvement* proposed.
- **U035.** Euclid 11, Problems XIX 41, Theon pp. 52 and 56 and Cleonides ch. 8 are all confirmed. Xylander was skipped.
- **U039.** Theon p. 67.9–13 (the paragraph begins on p. 66) is confirmed verbatim. All cents and comma figures recomputed and confirmed.
- **U040.** Nicomachus I 23 is fully confirmed (8:3 and 16:6, Hoche p. 64). Euclid 12 is confirmed: 8:3 is absent.

## Not verifiable online

- Lampe p. 131 (ἀνεγχώρητος); the universal claim "only predicative".
- Цыпин 2013 (terms; ундецима / дуодецима): the archive.org item 2013_20210528 exists, but its full text could not be fetched.
- Jan page numbers. The OCR of the Toronto and Google copies has no legible running heads at these places:
  - Euclid 12 (p. 160), 14–15 (pp. 160–161);
  - Cleonides ch. 8 (p. 194, 194.5–16);
  - Gaudentius 8 (pp. 337–338), 10 (pp. 339–340);
  - Nicomachus, Manual 6 (p. 248);
  - Problems XIX 18 (p. 88).
- Primary texts of Diogenes Laertius 6.33, Hippocrates, Epid. 1.26, Aristotle, APr. 68b30 / APo. 72b19, Simplicius and Olympiodorus: checked only through the LSJ and DGE citations. Perseus and Scaife refused WebFetch (403 / bot wall).
- All edition-internal claims (readings of Bas., Par., H, V, P; Vincent's pages and footnotes; Xylander), as instructed.
