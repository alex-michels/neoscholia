# Fact-check of the notes, U001–U028 (1.11.2026)

Every reference, quotation, lexicon claim, modern-scholarship claim and calculation in the notes of
`compose/final/U001.json`–`U028.json` was checked against the source itself, on the web. Status per claim:
**confirmed** / **WRONG** (with correction) / **doubtful** / **not found online** (where I looked).
Earlier "checked" marks were ignored.

## Sources used (all read online; nothing downloaded on purpose)

| Key | Where read |
|---|---|
| Hiller (Theon) | archive.org OCR of Hiller 1878: https://archive.org/stream/theonissmyrnaei00theogoog/theonissmyrnaei00theogoog_djvu.txt (scan: https://archive.org/details/theonissmyrnaei00theogoog). Page = running head; lines counted from the margin numbers 5, 10, 15, 20, 25 and checked against Hiller's apparatus line numbers. |
| Jan | https://archive.org/stream/musiciscriptoresjank/musiciscriptoresjank_djvu.txt (Musici scriptores Graeci 1895) |
| Friedlein (Boethius) | https://archive.org/stream/aniciimanliitor00friegoog/aniciimanliitor00friegoog_djvu.txt |
| Düring 1930 (Ptolemy) | https://archive.org/details/die-harmonielehre-des-klaudios-ptolemaios (OCR text; index and Book III headings) |
| Vincent 1847 | https://archive.org/details/vincent-1847-notice-sur-divers-manuscrits-grecs-relatifs-a-la-musique (OCR text, pp. 337–339) |
| LSJ, DGE, Bailly 2024, Pape, Middle Liddell | Logeion data service (same data as logeion.uchicago.edu): https://anastrophe.uchicago.edu/logeion-api/detail?type=normal&w=… |
| LSJ section labels, Dvoretsky | https://lsj.gr/wiki/μέλος, https://lsj.gr/wiki/ὑποτέμνω |
| Plato (Burnet) | PerseusDL canonical-greekLit XML, e.g. https://raw.githubusercontent.com/PerseusDL/canonical-greekLit/master/data/tlg0059/tlg024/tlg0059.tlg024.perseus-grc2.xml (Meno), tlg010 (Philebus), tlg031 (Timaeus) |
| Euclid, Elements I.3 | https://www.claymath.org/library/historical/euclid/files/elem.1.3.html (Heiberg text) |
| Synodal Eph. 4:16 | https://bible-teka.com/verse-en/56/4/16/ |
| Shchetnikov 2009 (Theon) | https://classics.nsu.ru/schole/3/3-2-theon.pdf (PDF p. 1 = journal p. 466) |
| Shchetnikov 2008a (Nicomachus) | https://classics.nsu.ru/schole/assets/files/2-1-nikomach.pdf |
| Shchetnikov 2008b («Алгоритм…») | https://classics.nsu.ru/schole/assets/files/2-1-schetnikov.pdf |
| Aleksandrova, Myakin 2009 | https://classics.nsu.ru/schole/assets/files/schole-3-1.pdf (pp. 161–201 of the PDF) |
| Aleksandrova 2025 | https://vestnik.nsglinka.ru/uploads/pdf/2025-T13-4/009-021.pdf |
| Tsypin 2014 (Cleonides) | https://nv.mosconsv.ru/sites/default/files/2021-11/Cleonides_2014_3.pdf (record: https://nv.mosconsv.ru/en/node/470) |
| Strunk (Cleonides) | https://www.attalus.org/translate/cleonides.html |
| DGE coverage | https://datos.cchs.csic.es/en/dataset/diccionario-griego-espanol-en-linea (online DGE: α–ἔξαυος; printed vol. VIII to ἐπισκήνωσις) |

Not available online (claims marked "not found online"): Barker, GMW II (1989); Tsypin 2013 (book); Gertsman 2010, 2024;
Heiberg 1929 (Anonymi logica et quadrivium). Readings of Bas., Par., H, V, P were checked only against this project's
edition files (`compose/edition/section-*.md`), not against the witnesses themselves, except P, checked in Vincent 1847.
Technical note: archive.org texts and PDFs were read as text inside the built-in browser (fetch + pdf.js, nothing saved);
one WebFetch call stored a copy of the Theon PDF in the session's tool-results folder automatically; it was not used.

---

## U001

**Note 1 (term).**
- LSJ s.v. σύνοψις: "a seeing all together, general view" (sense 1), "epitome, recapitulation" (2). **Confirmed.**
- LSJ s.v. ἀκριβόω: "make exact or accurate". **Confirmed.**
- "The word heads each of the four mathematical sciences of the Quadrivium of 1008". **Not found online.** Heiberg 1929 and the
  Basel 1556 print are not online in searchable form; searched archive.org, Google; not in the edition files either
  (`units/U001.md` says only "second of the four mathematical synopses").
- Bas. inverts the order (ἠκριβωμένη σύνοψις). **Confirmed** against the edition (section-1.md, apparatus at Bas. 23.2:
  "σύνοψις ἠκριβωμένη H Par. V] ἠκριβωμένη σύνοψις Bas."). Vincent 1847, p. 337, also cites the title as
  Τῆς μουσικῆς σύνοψις ἠκριβωμένη for Paris. gr. 2448.

**Note 2 (doctrine).** Theon pp. 16.24–17.15 Hiller. **Confirmed, with a nuance (question).**
16.24–25: πρῶτον δὲ μνημονεύσομεν τῶν ἀριθμητικῶν θεωρημάτων, οἷς συνέζευκται καὶ τὰ τῆς ἐν ἀριθμοῖς μουσικῆς;
17.8–9: ἡμῖν δ' ἀναγκαῖον δευτέραν αὐτὴν τάττειν μετὰ ἀριθμητικήν; 17.11–13: ἡ ἐν ἀριθμοῖς μουσική, δευτέρα ἂν ταχθείη.
But Theon says this is the order "for our study" (πρὸς τὴν ἡμετέραν θεωρίαν, 17.13–14, 17.22–23); "by nature" (πρὸς τὴν
φυσικὴν τάξιν, 17.14–19, 17.23–25) the order is arithmetic, geometry, stereometry, astronomy, and music (the harmony of the
cosmos) fifth. The note's "This is the order of the mathematical sciences in Theon" simplifies this (finding Q, U001).

## U002

**Note 1.** Theon pp. 12.10–13.1 Hiller. **Content confirmed; range WRONG.**
12.10–12: καὶ οἱ Πυθαγορικοὶ … τὴν μουσικήν φασιν ἐναντίων συναρμογὴν καὶ τῶν πολλῶν ἕνωσιν; 12.14–15: τέλος γὰρ αὐτῆς τὸ
ἑνοῦν τε καὶ συναρμόζειν; 12.19–21: ἐν κόσμῳ μὲν ἁρμονία, ἐν πόλει δ' εὐνομία, ἐν οἴκοις δὲ σωφροσύνη γίνεσθαι πέφυκε.
The paragraph ends at 12.25 (συναρμογῆς καὶ συντάξεως); 12.26–13.1 begin the next paragraph, a quotation of the Republic
(13.1 καὶ τάδε ἔφη· ἀγαθὸς δὲ ἀνήρ …). Correct range: p. 12.10–21 (or 12.10–25).
**Note 2.** Plato, Timaeus 31c–32c: 31c δεσμῶν δὲ κάλλιστος … τοῦτο δὲ πέφυκεν ἀναλογία κάλλιστα ἀποτελεῖν; 32c τὸ τοῦ κόσμου
σῶμα ἐγεννήθη δι' ἀναλογίας ὁμολογῆσαν. **Confirmed.** LSJ s.v. ἀναλογία: "mathematical proportion, Pl. Ti. 31c, 32c".
**Confirmed.** Timaeus 35b–36b: division of the soul-mixture, hemiolic, epitritic and epogdoic intervals, leimma 256:243
(36b). **Confirmed.**

## U003

**Note 1.** Philebus 64d–e: 64d μέτρου καὶ τῆς συμμέτρου φύσεως; 64e μετριότης γὰρ καὶ συμμετρία κάλλος δήπου καὶ ἀρετὴ
πανταχοῦ συμβαίνει γίγνεσθαι. **Confirmed.** LSJ s.v. συμμετρία II: "symmetry, due proportion, one of the characteristics of
beauty and goodness … cf. Pl. Phlb. 64e sq." **Confirmed.**

## U004

**Note 1.** αὐτοσυμμετρία: Logeion returns no entry in any dictionary (LSJ, DGE, Bailly 2024, Pape). **Confirmed**
(DGE covers α, so the negative is meaningful).
**Note 2.** U055 has οὐ μὴν τὸ πᾶν διὰ τόνων … οὐδὲ τὸ πᾶν ἐκ διέσεων. **Confirmed.** Punctuation of Par. (stop after τὸ πᾶν),
H and V (after ἀναλογία), Bas. (commas): **confirmed** against section-1.md (alternatives at Bas. 24.1–3).

## U005

**Note 1.** Eph. 4:16 text. **Confirmed** (see note 2).
**Note 2.** Eph. 4:16 ἐξ οὗ πᾶν τὸ σῶμα συναρμολογούμενον καὶ συμβιβαζόμενον; Eph. 2:21 ἐν ᾧ πᾶσα οἰκοδομὴ
συναρμολογουμένη; Col. 2:19 … συμβιβαζόμενον. **Confirmed.** Synodal «составляемое и совокупляемое»: **confirmed**
(bible-teka.com). LSJ s.v. συναρμολογέω: "Pass., to be fitted or framed together, Ep.Eph. 2.21, 4.16" (otherwise only
"compagino, Gloss."). **Confirmed.** LSJ s.v. συμβιβάζω 1: "Pass., to be put together, to be knit together, framed, ἔκ τινος
Ep.Eph. 4.16, Ep.Col. 2.19". **Confirmed.**

## U006 — no notes.

## U007

**Note 1.** Greek syntax, no external reference (marked from memory): nothing to check externally; the construal is sound.
**Note 2.** Theon pp. 46.20–47.3: 46.20 ἐπεὶ δὲ καὶ συμφώνους τινάς φασιν ἀριθμούς …; 47.1–3 ἥτις συμφωνία τὴν μεγίστην
ἔχει ἰσχύν, ἐν λόγῳ μὲν οὖσα ἀλήθεια, ἐν βίῳ δὲ εὐδαιμονία, ἐν δὲ τῇ φύσει ἁρμονία. **Confirmed** (Hiller's preface also
dates the music part from 46.20). p. 47.3–10: ἁρμονία … ἐν κόσμῳ …, ἥτις ἐστὶ καὶ νοητή, ἡ δὲ νοητὴ ῥᾷον ἀπὸ τῆς αἰσθητῆς
κατανοεῖται … τῆς τ' αἰσθητῆς ἐν ὀργάνοις καὶ τῆς νοητῆς ἐν ἀριθμοῖς … τῆς ἐν κόσμῳ ἁρμονίας. **Confirmed.**
pp. 16.24–17.8: music ἐν ἀριθμοῖς (16.25), ἐν ὀργάνοις (16.26), ἐν κόσμῳ (17.2, 17.6). **Confirmed.**

## U008

**Note 1.**
- Thrasyllus in Theon p. 47.18–19: Theon has indirect speech, 47.18–20: Θράσυλλος τοίνυν … φθόγγον φησὶν εἶναι φωνῆς
  ἐναρμονίου | τάσιν (τάσιν begins line 20). The note prints a reconstructed direct form, φθόγγος ἐστὶ φωνῆς ἐναρμονίου
  τάσις, as if quoted. **WRONG (wording and line range):** quote φθόγγον … εἶναι φωνῆς ἐναρμονίου τάσιν, p. 47.18–20.
- Nicomachus, Manual 4, Jan pp. 242–243: τάσιν δὲ μονήν τινα καὶ ταὐτότητα κατὰ μέγεθος φθόγγου ἀδιαστάτου. **Confirmed,
  but doubtful as cited:** Jan prints the whole definition block [φθόγγον δὲ φωνῆς ἐμμελοῦς ἀπλατῆ τάσιν … σύνθεσιν.] in
  square brackets (pp. 242.21–243.5), i.e. as suspect. A closer, unbracketed parallel: Nicomachus, Manual 12, Jan p. 261,
  ὡς δ' ἔνιοι, ἦχος ἀπλατὴς κατὰ τόπον ἀδιάστατος.
- Cleonides ch. 1, Jan p. 179.9–10: Φθόγγος μὲν οὖν ἐστι φωνῆς πτῶσις ἐμμελὴς ἐπὶ μίαν τάσιν. **Confirmed.**
- Cleonides ch. 2 (Jan p. 180): τὰς μὲν οὖν μονὰς τάσεις καλοῦμεν, τὰς δὲ μεταβάσεις τὰς ἀπὸ τάσεων ἐπὶ τάσεις διαστήματα.
  **Confirmed.**
**Note 2.** LSJ s.v. τάσις 3: "τάσεις τῆς φωνῆς pitch of the voice". **Confirmed.** U037 (ἐν ταῖς τάσεσιν ἢ ἀνέσεσι) and U049
(τῆς τάσεως γινομένης κατὰ τὴν στροφὴν τῶν κολλάβων): **confirmed.**
**Note 3.** LSJ s.v. ἐναρμόνιος I: "of musical sound, musical … metaph., in harmony with"; II: "in Music, enharmonic".
**Confirmed.** U053 ἁρμονικὸν προσαγορευόμενον: **confirmed.**
**Note 4.** LSJ s.v. ἀδιάστατος II: "without extension or dimension". **Confirmed.**

## U009

**Note 1.** Theon p. 48.8–13: 48.8–10 διάστημα δέ φησιν εἶναι φθόγγων τὴν πρὸς ἀλλήλους ποιὰν σχέσιν, οἷον διὰ τεσσάρων,
διὰ πέντε, διὰ πασῶν. **Confirmed** (quotation and examples). Cleonides ch. 1, Jan p. 179.11–12: Διάστημα δὲ τὸ περιεχόμενον
ὑπὸ δύο φθόγγων ἀνομοίων ὀξύτητι καὶ βαρύτητι. **Confirmed.**
**Note 2.** Same formula in Theon. **Confirmed.** U042 τὴν ποιὰν τῶν λόγων ἕξιν. **Confirmed.**

## U010

**Note 1.** Theon p. 48.10–12: σύστημα δὲ διαστημάτων ποιὰν περιοχήν, οἷον τετράχορδον, πεντάχορδον, ὀκτάχορδον.
**Confirmed.** Shchetnikov 2009, p. 491 (PDF p. 26): «Совокупность интервалов производит систему». **Confirmed.**
Barker 1989, p. 212, "a specifically qualified container of intervals": **not found online** (GMW II not accessible; Google
and Google Books search gave no hit). LSJ s.v. περιοχή 3: "generally, compass, extent … aggregate, Dam. Pr. 88".
**Confirmed.** Cleonides ch. 1, Jan p. 180.2–3: Σύστημα δέ ἐστι τὸ ἐκ πλειόνων ἢ ἑνὸς διαστημάτων συγκείμενον.
**Confirmed.** U051 (τετράχορδον, πεντάχορδον, ὀκτάχορδον): **confirmed.**

## U011

**Note 1.** Theon p. 48.12–13: ἁρμονία δέ ἐστι συστημάτων σύνταξις, οἷον Λύδιος, Φρύγιος, Δώριος. **Confirmed.**
U065 λύδιον, φρύγιον, δώριον (same order): **confirmed.** U053, U061 συντάττει: **confirmed.**

## U012

**Note 1.** Nicomachus, Manual 12, Jan p. 261: Φθόγγος ἐστὶ φωνὴ ἄτομος, οἷον μονὰς κατ' ἀκοήν. **Confirmed.**
Excerpta ex Nicomacho 6, Jan pp. 276–277: … ὁ φθόγγος, ὃ δὴ ἐν ἀριθμῷ μὲν μονάς, ἐν δὲ γεωμετρίᾳ σημεῖον, ἐν δὲ γράμμασι
στοιχεῖον. **Confirmed.**
**Note 2.** Theon pp. 47.19–48.7: 47.20–22 ἐναρμόνιος δὲ λέγεται, ἐπὰν δύνηται καὶ τοῦ ὀξέος ὀξύτερος εὑρεθῆναι καὶ τοῦ
βαρέος βαρύτερος· καὶ ὁ αὐτὸς καὶ μέσος ἐστίν. **Confirmed** (strictly 47.20–48.8; the one-line offset is immaterial).

## U013

**Note 1.** LSJ s.v. ἀπηχής: "discordant, v.l. in Pl. Phdr. 257b (Hermias), cf. Aristid. Or. 40(5).8, Luc. Vit.Auct. 10".
**Confirmed.** LSJ s.v. ἀπηχέω: "sound back, re-echo … 2 utter" (also II "to be out of tune"). **Confirmed.**
**Note 2.**
- LSJ s.v. ἄλλως II: "otherwise than something implied, differently"; II.3: "otherwise than should be, at random, without
  aim or purpose"; under II.3 "with Subst., εἴδωλον ἄ. mere image". **Confirmed.**
- Thrasyllus in Theon pp. 47.18–48.8 (thunder 48.1–3; οὐ πᾶσα φωνή … ἀλλ' ἡ ἐναρμόνιος 48.6–8). **Confirmed.**
- p. 50.14–16: ὑπὸ μὲν οὖν τῶν ἀλόγων ἄλογοι καὶ ἐκμελεῖς γίνονται ψόφοι, οὓς οὐδὲ φθόγγους χρὴ καλεῖν κυρίως, ἤχους δὲ μόνον.
  Content **confirmed**, but the note presents it under "Cf. Thrasyllus in Theon". **WRONG attribution:** pp. 49.6–50.16
  are Adrastus (49.6 Ἄδραστος … φησί) reporting the Pythagoreans (50.4 φησὶ δὲ καὶ τοὺς Πυθαγορικοὺς περὶ αὐτῶν οὕτω
  τεχνολογεῖν); Hiller's apparatus cites Porphyry: ὁ γοῦν περιπατητικὸς Ἄδραστος τὰ κατὰ τοὺς Πυθαγορείους ἐκτιθέμενος γράφει.
**Note 3.** γάρ H Par. V, δέ Bas.: **confirmed** against section-1.md (apparatus at Bas. 24.23).

## U014

**Note 1.** Cleonides ch. 4, Jan p. 182 (diatonic note list, λιχανὸς ὑπάτων διάτονος …). **Confirmed.** Nicomachus, Manual 11,
Jan pp. 257–259 (list προσλαμβανόμενος … νήτη ὑπερβολαίων). **Confirmed.** U041 numbers 6, 8, 9, 12, 16, 18, 24: **confirmed.**
Arithmetic recomputed: on 6, the positions get 4 → 8, 5 → 9, 8 → 12, 11 → 16, 12 → 18, 15 → 24, 2 → 27/4 = 6¾, 9 → 27/2 = 13½;
octaves 1–8, 4–11, 5–12, 8–15 all 2:1; letters A … a′ and tetrachord limits correct. **Confirmed.** U037 (8th–1st, 11th–4th,
12th–5th, 15th–8th): **confirmed.**
**Note 2.**
- Nicomachus 11 (Jan p. 258): λιχανὸς μέσων, ὃν καὶ διάτονον καλοῦσιν ἀπ' αὐτοῦ τοῦ γένους τοῦ διατονικοῦ προσαγορεύοντες.
  **Confirmed.** Nicomachus 12 (Jan p. 262): διατονικὸν καλεῖται, ἐκ τοῦ προχωρεῖν διὰ τῶν τόνων αὐτὸ μονώτατον τῶν ἄλλων.
  **Confirmed.**
- Shchetnikov 2008a: «диатон или лиханос нижних» (ch. 11), «её называют также диатоном»; mixed list ch. 12: «диатоника
  нижних», «диатоника средних». **Confirmed** (both «диатон» and «диатоника»).
- Aleksandrova, Myakin 2009: «диатон или «палец» (λιχανός)» (ch. 11, PDF p. 188), «его называют также диатоном» (p. 189).
  **Confirmed.**
- Tsypin 2014 (p. 7 of the PDF, list of diatonic notes): «диатоническая паранета высших», «диатоническая лихана средних».
  **Confirmed.**
- Barker transliterates "diatonos" (EN). **Not found online.**
- Gaudentius 6, Jan p. 332: λιχανὸν ὑπάτων … ἥτις καὶ διάτονος ὑπάτων ἐκαλεῖτο. **Confirmed.**
**Note 3.**
- All witnesses 14 names; Xylander's «διάτονος μέσων addo»: **confirmed** against section-2.md (internal).
- Gaudentius 6, Jan p. 333: ἡ λιχανὸς τῶν μέσων ἤτοι διάτονος μέσων. **Confirmed.**
- Boethius I 22 (Friedlein p. 214): "atque hinc lichanos meson, simpliciter in diatono quidem genere diatonos meson".
  **Confirmed.**
- Euclid, Sectio canonis 20, Jan p. 165: τὸν … μέσων διάτονον. **Confirmed.**
- Theon codex A diagram, Hiller p. [206] (after p. 205): προσλαμβανόμενος, ὑπάτη ὑπατῶν, παρυπάτη ὑπατῶν, ὑπάτη διάτονος,
  ὑπάτη μέσων, παρυπάτη μέσων, μέσων διάτονος, μέση, παραμέση, τρίτη διεζευγμένη, διεζευγμένη διάτονος, νήτη διεζευγμένη,
  τρίτη ὑπερβολαίων, διάτονος ὑπερβολαίων, νήτη ὑπερβολαίων; Hiller: "Exstat haec descriptio neglegentissime facta in cod. A
  post finem eius partis qua de musica agitur (p. 72)". **Confirmed** (μέσων διάτονος 7th).
- Codex A = Marc. 307, "saeculi XI. vel XII." (Hiller, praefatio). **Confirmed.**
- Nicomachus 12, Jan p. 264 mixed list: διάτονος ὑπατῶν, μέσων διάτονος, συνημμένων διάτονος, διάτονος διεζευγμένων, διάτονος
  ὑπερβολαίων. **Confirmed** as worded (meson genitive first; hypaton, diezeugmenon, hyperbolaion διάτονος first).
- Theon p. 92.11–12: ἕξομεν τὴν τῶν | μέσων διάτονον. **Confirmed** (92.2 διάτονος συνημμένων).
**Note 4.** μόνως Bas. Par. V; H μόν(ος): **confirmed** against section-2.md (internal).
**Note 5.** Nicomachus 11, Jan p. 258: εἶτα παράμεσος μετὰ ὅλον τόνον. **Confirmed.** Barker p. 265 "paramesos": **not found
online.** Codex A diagram shares ὑπάτη διάτονος, μέσων διάτονος, nominative διεζευγμένη, plain μέση; has παραμέση and
διεζευγμένη διάτονος: **confirmed.** "the codex is later than 1008" / «кодекс моложе 1008 г.»: **doubtful** — Hiller dates
it s. XI or XII, which does not exclude 1001–1008 (the edition's own resolved doubt says "s. XI-XII or XII").
Tsypin 2014 qualifiers «низших», «средних», «отделенных», «высших» (also «соединенных»): **confirmed** (PDF p. 7).

## U015

**Note 1.** Aleksandrova 2025: «15-звуковая система соединенных», «15-звуковая система раздельных» (pp. 9, 14 of the
article). **Confirmed.** Barker "a series of fifteen notes": **not found online.**
Theon p. 64.1–6 (Adrastus): φησὶν ὁ Ἄδραστος … οἱ δὲ νεώτεροι τὸ πεντεκαιδεκάχορδον τρόπον μέγιστον ἐπὶ τὸ τρὶς διὰ πασῶν καὶ
τόνον διεστηκός. **Confirmed** (a 15-tropos diagram of three octaves and a tone, not the two-octave system).
Shchetnikov 2009, p. 497 (PDF p. 32): «пятнадцатиструнным ладом, величиной в три октавы и тон». **Confirmed.**
Barker "fifteen-stringed", pp. 212, 220 n. 50, 264–265, 361: **not found online.**
LSJ s.v. ὀκτάχορδος: "with eight strings or notes … Theo Sm. p.49 H."; s.v. πεντεκαιδεκάχορδος: "with fifteen strings, Adrast.
ap. Theon. Sm. p.64 H., Ptol. Harm. 3.1 tit., Porph. in Harm. p.168 D." **Confirmed.** ἑκκαιδεκάχορδος: no entry in any
Logeion dictionary (LSJ, DGE; DGE covers ἐκ-). **Confirmed.**
**Omission:** LSJ's own second citation, Ptolemy, Harmonics III 1, title (Düring p. 82.2): Πῶς ἂν ἡ δι' ὅλου χρῆσίς τε καὶ
ἀνάκρισις γίνοιτο τῶν λόγων διὰ πεντεκαιδεκαχόρδου κανόνος — the 15-string canon for the whole double-octave system, i.e.
exactly the two-octave sense the note says is absent from Theon. Worth adding (finding I, U015).

## U016

**Note 1.** Ratios 2:1, 2:1, 4:1: **confirmed.** Nicomachus 11, Jan p. 258: ἵνα ὀκτάχορδα ἑκατέρωθεν τῆς μέσης ὑπάρξῃ τὰ
συστήματα, καὶ ἡ μὲν ὡς ἀληθῶς μέση γένηται ἐν πεντεκαίδεκα φθόγγοις ὀγδόη ἑκατέρωθεν κειμένη. **Confirmed.**

## U017 — no notes.

## U018

**Note 1.** Theon p. 55.11–13: δίεσιν δὲ καλοῦσιν ἐλαχίστην οἱ περὶ Ἀριστόξενον τὸ τεταρτημόριον τοῦ τόνου, ἥμισυ δὲ
ἡμιτονίου. **Confirmed.** Cleonides ch. 5, Jan p. 187: ἐλάττω μὲν οὖν ἐστι τοῦ διὰ τεσσάρων δίεσις, ἡμιτόνιον, τόνος, δίτονον
(τριημιτόνιον only in M²L, Jan's apparatus). **Confirmed.** Theon p. 53.8–16: τὸ μέντοι ἡμιτόνιον οὐχ ὡς ἥμισυ τόνου λέγεται,
ὥσπερ Ἀριστόξενος ἡγεῖται … τὰ γὰρ θ' οὐχ οἷόν τε διαιρεθῆναι εἰς ἴσα. **Confirmed.** Euclid, Sectio canonis 16, Jan p. 161:
Ὁ τόνος οὐ διαιρεθήσεται εἰς δύο ἴσα οὔτε εἰς πλείω. **Confirmed.**
**Note 2.** Tsypin 2013 list of calques: **not found online.** Shchetnikov 2008b: «сверхдвухчастное» (p. 3), «двукратное-и-
половинное» (p. 3). **Confirmed.** Gertsman 2010 («эпитритное», «эпогдоосное», «эпогдоос»): **not found online.**
Aleksandrova, Myakin 2009: «эпогдоон» (PDF pp. 167, 183), «эпитрит», «гемиолий» (pp. 165, 184). **Confirmed.**
LSJ: ἐπόγδοος "1 1/8 … ratio of 9:8"; ἐπιτέταρτος "ratio of 5:4"; ἐπιδιμερής "containing 1 2/3"; διπλασιημιόλιος "ratio of
5/2". **Confirmed.** ἡμιεπόγδοος: no entry in LSJ, Bailly, Pape (**confirmed**); "not in DGE" is **vacuous** — DGE has not
reached η (online α–ἔξαυος). διπλασιεπιμερής: no LSJ entry (the note does not cite one). Latin equivalents (sesquioctavus,
sesquitertius, sesquialter, sesquiquartus, superbipartiens): standard Boethian terms, **confirmed** (Friedlein: "sesquioctava",
"sesqualtera" in I–IV).
**Note 3.** Arithmetic: 8½:8 = 17:16; 8¼:8 = 33:32; (33/32)² = 1089/1024 vs 1088/1024; (17/16)² = 289/256 vs 288/256;
√(9/8) = √72/8 = 1.06066; cents 203.910 / 101.955 / 50.978 / 104.955 / 53.273. **All confirmed** (recomputed).
Theon p. 69 (SRC: 69.13–17): the passage is 69.12–70.1. 69.12–15: ὅτι δὲ τοῦτο τὸ διάστημα τὸ τῶν σνϛ' πρὸς σμγ', τουτέστι τὰ
ιγ', ἔλαττόν ἐστιν ἡμιτονίου, δῆλον. τοῦ γὰρ τόνου ἐπογδόου ὄντος τὸ ἡμιτόνιον δὶς ἐπόγδοον ἔσται, τουτέστιν ἐφεκκαιδέκατον;
69.17–70.1: οὐδὲ γὰρ οἷόν τε τὸ ἐπόγδοον διαίρεσιν ἐπιδέξασθαι, εἰ καὶ οἱ μὴ λόγῳ ἀλλὰ τῇ ἀκοῇ ταῦτα κρίνοντες νομίζουσιν.
Quotation **confirmed**. **Open point answered:** Theon neither adopts 17:16 as the true semitone nor rejects it outright: in
proving that the leimma 256:243 (excess 13/243, under 1/18) is smaller than a semitone, he takes the semitone, the tone being
9:8, as δὶς ἐπόγδοον, "that is, ἐφεκκαιδέκατον" — a working value got by halving the excess, the same operation as the
compiler's — and at once adds that the epogdoic ratio cannot be divided at all, against those who judge by hearing (the
Aristoxenians). The note's "the semitone ἐφεκκαιδέκατον, 17:16" reads as Theon's doctrine; it should be qualified
(finding I, U018). Xylander's τοῦ ἐννέα πρὸς, ὅσον H V / οἷον Bas. Par.: **confirmed** against section-2.md.

## U019

**Note 1.** Theon pp. 19.20–20.3: 19.18–19 καὶ μονὰς τοίνυν ἐστὶν ἡ τοῦ ἑνὸς ἰδέα ἡ νοητή, ἥ ἐστιν ἄτομος; 20.2–4 ὥστε ἡ μὲν
μονὰς νοητὴ οὖσα ἀδιαίρετος, τὸ δὲ ἓν ὡς αἰσθητὸν εἰς ἄπειρον τμητόν. Content **confirmed**; range slightly **WRONG**
(19.20 begins mid-sentence and τμητόν is on 20.4): read 19.18–20.4. (Line count on p. 19 checked against Hiller's apparatus:
"19 ἥ] ἢ A", "21 inscr. τίς ἀρχὴ ἀριθμοῦ", "22 Stob.".)
**Open point (Adrastus, Theon p. 66).** Hiller p. 66 has nothing on the unit (66.1–11 lower notes and wind instruments;
66.12–18 κυριωτάτη δὲ πασῶν, φησίν, ἡ διὰ τεσσάρων συμφωνία; 66.19–24 the tone as first interval). The reviewer's line numbers
fit **p. 70**, not 66: 70.1–3 ἀμέλει τοῦ ἐπογδόου πυθμένος τὸ διάστημα τουτέστι τῶν θ' πρὸς τὰ η' ἡ μονὰς οὐ τέμνεται;
70.14–19 ὅτι δὲ ὁ τόνος δίχα οὐ διαιρεῖται δῆλον οὕτω. πρῶτον μὲν ὁ ἐπόγδοος πυθμὴν τὸ διάστημα ἔχει μονάδα, ἥτις ἀδιαίρετος …
καὶ γὰρ ἐπὶ τῶν σιϛ' πρὸς σμγ' ἡ ὑπεροχὴ κζ' οὐ τέμνεται εἰς ἴσα, ἀλλὰ εἰς ιγ' καὶ εἰς ιδ'· μονὰς γὰρ οὐ διαιρεῖται. So
ἡ μονὰς οὐ τέμνεται is verbatim in Theon. Attribution: no name at the sentence; Adrastus is named at 64.1 (φησὶν ὁ Ἄδραστος),
65–66 (φησί, φησίν) and 73.19 (φησιν Ἄδραστος), so the section probably follows him, but "Adrastus quoted by Theon" is not
explicit. Theon's continuation reverses the compiler's conclusion: 70.19–71.4 the tone is not always halved in numbers, nor in
perceptible, visible intervals (on the canon); 72.2–4 nor in voices; 72.19–20 ὁ δὲ νοήσει ληπτὸς τόνος δύναται νοεῖσθαι καὶ εἰς
ἴσα διαιρούμενος. Also Euclid, Sectio canonis 3 (Jan p. 152): ὥστε τὴν μονάδα διαιρεῖσθαι, ὅπερ ἀδύνατον. Proposed addition:
finding I, U019.

## U020

**Note 1.** νευράν Bas. Par. V; H μοιρὰν: **confirmed** against section-2.md. LSJ s.v. νευρά 2: "harpstring, Poll. 4.62"
(one citation); Bailly 2: "corde d'instrument, A. Aphr. Probl."; Pape: "bei Sp. auch die Darmsaite". The sense is
**confirmed**; "usual in later Greek (LSJ s.v. νευρά 2)" is **doubtful** — LSJ gives one late lexicographer, not usage.
**Note 2.** LSJ s.v. ὑποτέμνω: "cut away under or underneath … b trim … II cut off, intercept". **Confirmed.** Dvoretsky:
«подрезывать, перерезывать, подрубать» (1), no «делить» or «подразделять». **Confirmed.** Bailly ("couper en dessous",
"intercepter"), Pape ("darunter od. vorn wegschneiden"): no "divide". **Confirmed.**
**Note 3.** ἡμιεπόγδοος not in the lexica: **confirmed** (LSJ, Bailly, Pape; DGE not yet at η). Closest parallel in the
sources: Theon's δὶς ἐπόγδοον, τουτέστιν ἐφεκκαιδέκατον (p. 69.15) — worth a cross-reference (finding I, U020).

## U021

**Note 1.** Euclid, Elements I.3: Δύο δοθεισῶν εὐθειῶν ἀνίσων ἀπὸ τῆς μείζονος τῇ ἐλάσσονι ἴσην εὐθεῖαν ἀφελεῖν.
**Confirmed** (claymath.org, Heiberg text). P passage: τῇ ἐλάττονι προστίθησι καὶ πεποίηται μείζονα (Vincent p. 338; U029).
**Confirmed.**

## U022 — no notes.

## U023

**Note 1.** 16 = 4²; 8 and 32 not squares; four squares of 4 make 16. **Confirmed.** Marginal figures at 26.14, 26.18 in Bas.
Par. V: internal (edition description of witnesses), not checked online.

## U024

**Note 1.** Plato, Meno 82b–85b (marked "from memory"): 82b εἰπὲ δή μοι, ὦ παῖ, γιγνώσκεις τετράγωνον χωρίον …;
84d–85a the four 4-foot squares and the lines ἐκ γωνίας εἰς γωνίαν cutting each in half; 85b ἀπὸ τῆς διαμέτρου … γίγνοιτ' ἂν
τὸ διπλάσιον χωρίον, with καλοῦσιν δέ γε ταύτην διάμετρον οἱ σοφισταί. **Confirmed**: the range is exact; the inscribed square
of 8 is both half of the 16-square and double the 4-square, so both operations of U024 are in the Meno figure (the numbers
4/16 are the note's own). Arithmetic: side 2√2, area 8; 4√2, area 32. **Confirmed.** διάμετρος = diagonal (Meno 85b).
**Confirmed.** The source tag "[from memory]" can now be "checked".

## U025

**Note 1.** √72 = 8.485. **Confirmed.** Euclid, Sectio canonis 3, Jan pp. 152–153: Ἐπιμορίου διαστήματος οὐδεὶς μέσος, οὔτε
εἷς οὔτε πλείους, ἀνάλογον ἐμπεσεῖται ἀριθμός (p. 152; proof ends p. 153). **Confirmed.** Sectio 16, Jan p. 161: **confirmed.**
Boethius III 1, heading (Friedlein; book III opening and chapter list): "Adversum Aristoxenum demonstratio superparticularem
proportionem dividi in aequa non posse atque ideo nec tonum". **Confirmed.**

## U026

**Note 1.** Quarter-tone arithmetic (¾, 1½, 2, 3 tones): **confirmed.** τριδίεσις: no entry in LSJ, Bailly, Pape (nor any
Logeion dictionary). **Confirmed.** LSJ s.v. τρίτονος: "τρίτονον, τό, in Music, interval of three whole tones, Cleonid.
Harm. 5, Bacch. Harm. 47". **Confirmed.** Cleonides ch. 5 (Jan pp. 187–189): 188 τὸ τριημιτόνιον ἐν μὲν χρώματι ἀσύνθετον,
ἐν δὲ διατόνῳ σύνθετον· τὸ δίτονον ἐν μὲν ἁρμονίᾳ ἀσύνθετον …; 189.1–2 ὁμοίως δὲ καὶ τὰ μείζω τοῦ διτόνου πάντα σύνθετα.
**Confirmed.**
**Note 2.** LSJ s.v. τριημιτόνιον: "a tone and a half: in Music, minor third"; Pape: "anderthalb Töne … die kleine Terz".
**Confirmed.** «трёхполутон»: Shchetnikov 2008a (ch. 12, «несоставной трёхполутон») and Aleksandrova, Myakin 2009
(«несложенный трёхполутон», PDF p. 190). **Confirmed.** «трёхполутоний» (Gertsman 2010): **not found online.** «триполутон»,
«полуторатон»: Tsypin 2014 (PDF pp. 6, 10, 11). **Confirmed**; Tsypin 2013: **not found online.** EN "'trisemitone'
(Strunk)": **WRONG** — the Strunk translation at attalus.org (the bibliography's stated source) has "trihemitone" six times
and "trisemitone" nowhere (e.g. "sung in descending by trihemitone, semitone, and semitone").
**Note 3.** LSJ s.v. ῥυθμός: I "measured motion, time … rhythm"; II "measure, proportion or symmetry of parts"; III
"generally, proportion, arrangement, order". **Confirmed.**

## U027

**Note 1.** Cleonides ch. 5, Jan p. 188: ἀσύνθετα μὲν οὖν διαστήματά ἐστι τὰ ὑπὸ τῶν ἑξῆς φθόγγων περιεχόμενα … σύνθετα δὲ
τὰ ὑπὸ τῶν μὴ ἑξῆς; trihemitone incomposite in chromatic, composite in diatonic. **Confirmed.** Theon p. 54.22–23: τὸ
τριημιτονιαῖον ἀσύνθετον (also 55.4 τριημιτόνιον ἀσύνθετον). **Confirmed.** Gaudentius 4, Jan pp. 330–331: ἀσύνθετα δέ ἐστι
διαστήματα, ὅταν μεταξὺ τῶν περιεχόντων αὐτὰ φθόγγων μηδὲ εἷς δύνηται μελῳδεῖσθαι φθόγγος ἐμμελὴς … ἐν ἐκείνῳ τῷ γένει.
**Confirmed.**
**Note 2.** LSJ s.v. μέλος: the musical senses stand under **B** ("esp. musical member, phrase: hence, song, strain"; B.2
"tune"; B.3 "melody of an instrument"), both on Logeion and on lsj.gr; there is no "II". "LSJ s.v. μέλος II" is **doubtful**
(DECISIONS § 4 uses the same label as a style example). Glosses **confirmed.** Dvoretsky 2: «напев, мелодия». **Confirmed.**
Cleonides ch. 14, Jan p. 201: ἀγωγὴ μὲν οὖν ἐστιν ἡ διὰ τῶν ἑξῆς φθόγγων ὁδὸς τοῦ μέλους. **Confirmed.** Tsypin 2014:
«Ведéние (ἀγωγή) — движение мелодии по смежным звукам». **Confirmed.** Strunk: "a progression of the melody by consecutive
notes". **Confirmed.** «мелос»: Shchetnikov 2008a («о двух других родах мелоса»). **Confirmed**; Gertsman 2024: **not found
online.** «мелодия» (Tsypin 2014): **confirmed.**
**Note 3.** LSJ s.v. σύμφθαρσις: "simultaneous destruction, τῶν μιγνυμένων … Alex.Aphr. Mixt. 216.24 … 2 melting into one
another, (sc. τῶν ἰδεῶν) Hermog. Id. 1.12, cf. Iamb. in Nic. p.80 P." **Confirmed.** Pape: "das Ineinanderfließen und
Verschmelzen, bes. der Farben". **Confirmed.** LSJ s.v. συμφθείρω II: "Pass., of colours, melt or die away into each other,
Plu. Def.orac. 2.436b; of sounds, D.H. Dem. 48; … of π and σ in ψ, Id. Comp. 14". The note gives colours **and** sounds to
Dionysius: **WRONG** for colours (LSJ cites Plutarch; Bailly also D.H. Comp. 23, but the note cites LSJ).
"The lexica do not cite this text": **confirmed.**
**Note 4.** LSJ s.v. δύναμις: "e in Music, function, value, of a note in the scale, δ. ἐστι τάξις φθόγγου ἐν συστήματι Cleonid.
Harm. 14". **Confirmed.** LSJ s.v. ἰσχύς "strength". **Confirmed.** Cleonides ch. 2 τῇ δυνάμει (Jan p. 181); Tsypin 2014 «по функции
(τῇ δυνάμει)». **Confirmed.** Barker 1989 pp. 233, 287, 314, 406: **not found online.** Cleonides ch. 14, διάγραμμα … τὰς τῶν
μελῳδουμένων περιέχον δυνάμεις: text **confirmed** (Jan p. 201), but Jan prints the whole closing block [Διάγραμμα δὲ … ὑποθέσεως.]
in square brackets (an appendix found in M after the title Εἰσαγωγὴ ἁρμονικὴ Εὐκλείδου) — **doubtful** as cited without
mention. U042 κεκρυμμένων, U051 ἐμπεριέχον δυνάμεις, ἰσχύν: **confirmed.**

## U028

**Note 1.** Vincent 1847, p. 338: heading "Premier fragment de Psellus extrait du manuscrit 2448"; text Εἰ γὰρ καὶ τοῖς ἀριθμοῖς
σύμφρασις¹ … τὸ τῶν ἀριθμῶν² … καὶ τὴν σύμφρασιν³ εἶναι; notes: ¹ "Il est probable qu'il faut σύγκρασις; mais je n'ose pas
faire la correction", ² "Ms. τὸν τῶν ἀριθμόν", ³ "Ms. ἡ σύμφρασις". **Confirmed** (σύγκρασις proposed in a note; accusative
and τὸ τῶν ἀριθμῶν are Vincent's). Start at 338.4: **confirmed**; end at 340.2: not checked (OCR of p. 340 not read).
LSJ s.v. σύμφρασις: "continuous speech, Hdn.Gr. 1.10, Phot. Bibl. …; v.l. for συμφρόνησις, Philol. 10". **Confirmed.**
Absence from Bas. Par. H V: internal (edition), consistent with Vincent's statement that P adds three fragments.
**Note 2.** See U027 note 2 (μέλος "II" vs "B").
**Note 3.** LSJ s.v. ἐγγίγνομαι III: "ἐγγίγνεται, impers., it is allowed or possible, c. inf." **Confirmed.** Intervals compose by
multiplying ratios: **confirmed.**

---

## Summary of problems (also returned as findings)

Errors: U002 n.1 range; U008 n.1 quotation form and range; U013 n.2 attribution of Theon p. 50 to Thrasyllus; U019 n.1 range;
U026 n.2 "trisemitone (Strunk)"; U027 n.3 colours ascribed to Dionysius.
Questions: U001 n.2 didactic vs natural order; U008 n.1 bracketed Nicomachus 4; U014 n.5 "later than 1008"; U018/U020 DGE
negative for η; U020 n.1 "usual in later Greek"; U027 n.2 / U028 n.2 LSJ μέλος "II"; U027 n.4 bracketed Cleonides 14.
Improvements: U015 Ptolemy's πεντεκαιδεκάχορδος κανών; U018 n.3 Theon p. 69 qualified and line range; U019 Theon p. 70
(ἡ μονὰς οὐ τέμνεται) with the contrast of pp. 71–72; U020 n.3 cross-reference to Theon's δὶς ἐπόγδοον.
