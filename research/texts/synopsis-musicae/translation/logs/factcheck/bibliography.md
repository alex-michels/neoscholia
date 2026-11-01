# Bibliography check (1.11.2026)

Input: `final/bibliography.json` (33 entries). Output: `factcheck/bibliography-proposed.json` (same 33 keys, same order).
RU entries follow the Russian scholarly style (Фамилия И. О. Название. Город: Издательство, год. С. N–M.; translations
as «Название / пер. … // Журнал. Год. Т., вып. С.»). EN entries follow Chicago author–date. The descriptive tails of the
old entries (how a work is cited, which platform was used) are kept after the bibliographic description.
«издание» / Edition is unchanged, as instructed.

PDF texts were read with a stdlib text extractor; page numbers were taken from the running heads of the PDFs.

## 1. Key–work check (every key grepped in the RU/EN notes and the source fields of `final/U*.json`)

| Key | Used for | Verdict |
|---|---|---|
| Цыпин 2013 / Tsypin 2013 | Ptolemy/Porphyry: ratio calques (U018), «триполутон» (U026), кварта/квинта/октава (U033), ундецима/дуодецима (U035), сверхчастные = ἐπιμερεῖς (U040) | matches the Ptolemy–Porphyry volume |
| Цыпин 2014 / Tsypin 2014 | Cleonides chs. 2, 5, 8, 14 (U014, U026, U027, U033–U035, U037, U066) | matches the Cleonides translation |
| Щетников 2008а / Shchetnikov 2008a | Nicomachus’ Manual: «диатон», «диатоника» (U014), «трёхполутон» (U026), «мелос» (U027) — all present in the PDF | matches, **except U040 note 1** (see below) |
| Щетников 2008б / Shchetnikov 2008b | «сверхдвухчастное», «двукратное-и-половинное» (U018) — both present in the PDF | matches |
| Щетников 2009 / Shchetnikov 2009 | Theon: p. 491 «Совокупность интервалов производит систему» (U010) — confirmed on PDF p. 491; «пятнадцатиструнным ладом» (U015) — present | matches |
| Щетников 2012 / Shchetnikov 2012 | Sectio canonis: кварта/квинта/октава (U033, U035) | matches |
| Александрова, Мякин 2009 | Nicomachus translation (U014, U018, U026) | matches the work; name order differs from the publication (question) |
| Александрова 2025 | «15-звуковая система» (U015) | matches (the article treats the 13- and 15-note systems) |
| Герцман 2010 | Boethius translation: «эпогдоос», «трёхполутоний» (U018, U026) | matches «Музыкальная боэциана» (2nd ed.) |
| Герцман 2024 | «мелос» (U027) | matches the RIII 2024 book on Theon (p. 37: «в любом мелосе», note «Буквально: «всякий мелос»») |
| Strunk | Cleonides chs. 2, 5, 14 (U027, U034, U037, U066) | matches attalus.org (Strunk 1950, pp. 34–46), **except U026 note 2 EN “trisemitone”** (see below) |
| Smyth | §§ 958, 1014, 2837 | numbering of A Greek Grammar for Colleges (1920), not of the 1916 book named in the entry |
| all others | lexica, editions, witnesses | match |

**Mismatch 1 (error): U040, note 1 (RU text and source field).** The note says: «У Щетникова (Щетников 2008а) «сверхчастное»
означает ἐπιμόριος …, а ἐπιμερής — «сверхмногочастное»», and the source field lists “Shchetnikov 2008a”. The Manual
translation (2008a) contains neither term: its ratio names are «полуторный, сверхтретий, сверхвосьмерной, двукратный»;
the string «сверхчаст» occurs 0 times in its text. The pair is in the Algorithm article (2008b, p. 55ff.):
«многократное (πολλαπλάσιον), сверхчастное (ἐπιμόριον), сверхмногочастное (ἐπιμερές)», where Shchetnikov translates
Nicomachus’ Introduction to Arithmetic. The consistency pass assigned U040 to 2008a only because the packet said
“Shchetnikov’s Nicomachus”. Fix: «Щетников 2008б» in the RU note and “Shchetnikov 2008b” in the source field.

**Mismatch 2 (error): U026, note 2 EN.** “The usual English term is “trihemitone”; “trisemitone” (Strunk) is a minority form.”
The Strunk text the bibliography describes (attalus.org, from Source Readings pp. 34–46, i.e. the 1950 edition) has
“trihemitone” throughout (§§ 3, 5, 7, 12) and never “trisemitone”. “Trisemitone” is reported only by Wikipedia
(“Pyknon”) for the revised edition (ed. Leo Treitler, 1998, pp. 36–37), which the project did not open (card P11:
“Strunk–Treitler”, via Wikipedia). Fix: “The usual English term is “trihemitone” (Strunk).”, or, if the editor
can check the 1998 revision, a separate key for it.

## 2. Entries

### Александрова 2025 / Aleksandrova 2025 — completed
Issue contents of Вестник музыкальной науки 13.4: Л. В. Александрова, «О формировании античной музыкальной системы в
трудах древних ученых», с. 9–21, DOI 10.63219/2308-1031-2025-4-9-21. The journal is published by the Novosibirsk Glinka
Conservatory (ISSN 2308-1031). The PDF head confirms: «Вестник музыкальной науки. 2025. Т. 13, № 4. С. 9–21».
- https://vestnik.nsglinka.ru/&journal_page=archive&id=53
- https://vestnik.nsglinka.ru/uploads/pdf/2025-T13-4/009-021.pdf

### Александрова, Мякин 2009 / Aleksandrova, Myakin 2009 — completed; name order is a question
PDF 3-1-nicomach-3.pdf, pages 161–205 of ΣΧΟΛΗ 3.1 (2009). It holds (a) Л. В. Александрова, «Никомах из Герасы.
Руководство по гармонике. О трактате и его источниках», pp. 161–178 (© Л. В. Александрова); (b) «Пифагорейца
Никомаха из Герасы Руководство по гармонике, продиктованное на скорую руку сообразно старине. Перевод Т. Г. Мякина и
Л. В. Александровой», pp. 179–205 (© Т. Г. Мякин, Л. В. Александрова). CEEOL lists the whole as one item, “Timothy
Myakin, Ludmila Alexandrova”, pp. 161–205. **On the publication Myakin comes first.** The key «Александрова, Мякин 2009»
is prescribed by DECISIONS.md § 4, so it is kept; the entry gives the published order. Question for the editor:
change the key to «Мякин, Александрова 2009» / “Myakin, Aleksandrova 2009”?
- https://classics.nsu.ru/schole/3/3-1-nicomach-3.pdf
- https://www.ceeol.com/search/article-detail?id=129818

### Bailly — completed
Logeion’s dictionary name (from its API, saved in earlier research) is literally “Bailly 2024”: the digital Bailly by
Gérard Gréco, André Charbonnet, Mark de Wilde and Bernard Maréchal, built on the 1935 printing of Bailly’s
Dictionnaire grec-français (Hachette, first ed. 1895), released as “Bailly 2020 Hugo Chávez” and updated since.
lsj.gr offers the “Bailly abrégé”; the Abrégé du dictionnaire grec-français first appeared in 1901 (Hachette). Which
printing of the Abrégé lsj.gr digitised is not stated on the site (not verified).
- https://latin-dict.github.io/dictionaries/Bailly2020.html
- https://lsj.gr/wiki/Main_Page

### Barker 1989 — completed
Andrew Barker, Greek Musical Writings, vol. II: Harmonic and Acoustic Theory, Cambridge University Press 1989,
Cambridge Readings in the Literature of Music (ISBN 0-521-30220-1; pb 2004).
- https://bvbvf1.bib-bvb.de/vufind/Record/DE-604.BV043923022
- https://biblio.co.uk/9780521302203

### Bas. — completed
BSB copy A.gr.b. 3057 (MDZ bsb10170656): title “Pselli, … Liber de quatuor mathematicis scientiis: arithmetica,
musica, geometria, & astronomia, Graece & Latine nunc primum edita”; “Guilielmo Xylandro interprete”; “Basileae:
Oporinus”; “[1556]”; 263 [i.e. 163], 175 S.; Greek and Latin; VD16 M 5144. The year is bracketed because it is not on
the title page (Xylander’s dedication to Ulrich Fugger is dated Augsburg, November 1556: Deutsche Biographie).
Penn Online Books: “Liber de quatuor mathematicis scientiis (Per Ioannem Oporinum, 1556)”. The project’s own witness
description (cmp/about.md) gives “Basel [1556], printed by Oporinus, edited by Xylander; pp. 23–33”. The title is
given in the catalogue’s transcription (with its ellipsis); the title page itself was not opened.
- https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb10170656/manifest
- https://onlinebooks.library.upenn.edu/webbin/who/Oporinus%2c%20Joannes%2c%201507%2d1568
- https://www.deutsche-biographie.de/pnd124331025.html

### Bellermann 1841 — completed
“Anonymi scriptio de musica. Bacchii senioris introductio artis musicae … annotationibus illustravit Fridericus
Bellermann”, Berolini: Foerstner, 1841, 108 p.
- https://zenon.dainst.org/Record/000224330

### DGE — completed
Diccionario Griego-Español, CSIC, Madrid, 1980– (in progress), dir. F. R. Adrados, then J. Rodríguez Somolinos;
online as DGE en línea. Logeion carries it under the name “DGE” (Logeion API). Details from the standard description;
the DGE site itself was not opened.

### Дворецкий / Dvoretsky — completed
И. Х. Дворецкий, Древнегреческо-русский словарь, в 2 т., под ред. С. И. Соболевского, М.: Государственное издательство
иностранных и национальных словарей, 1958, 1904 с. A web search confirmed 1958, two volumes, 1,904 pages; the editor
and publisher are the standard imprint (not seen on a catalogue page). lsj.gr hosts it as the Ancient Greek–Russian
dictionary.
- https://azbyka.ru/otechnik/Spravochniki/drevnegrechesko-russkij-slovar-i-h-dvoretskogo-tom-1/

### издание / Edition — unchanged (as instructed)

### Friedlein — confirmed, completed
“Anicii Manlii Torquati Severini Boetii De institutione arithmetica libri duo, De institutione musica libri quinque;
accedit Geometria quae fertur Boetii”, ed. Godofredus Friedlein, Lipsiae: Teubner, 1867, viii + 492 p. The year 1867
(“from memory” in the U007 packet) is correct.
- https://catalogue.etoncollege.com/B53664
- https://openlibrary.org/books/OL23380290M

### Герцман 2010 / Gertsman 2010 — completed
RIII bibliographic index of Gertsman’s works (2024), no. 5: «Музыкальная Боэциана. СПб.: Глагол, 1995. Второе издание:
СПб.: Невская нота, 2010. 480 с.» The imprint on the verso of the 2010 title page (OCR of the copy used in earlier
research) reads: «Герцман Е. В. Музыкальная боэциана. (Серия «История музыки: памятники и исследования»). СПб.: Невская
нота, 2010 — 504 с. Издание второе. ISBN 978-5-9901468-2-2». The entry follows the book’s own imprint (504 с.); the
index’s 480 с. is the only discrepancy.
- https://artcenter.ru/wp-content/uploads/2024/05/Герцман_библиографический_указатель.pdf

### Герцман 2024 / Gertsman 2024 — completed
Title page and imprint of the RIII PDF: «Е. В. Герцман. Последний античный пифагореец о музыке. (Музыкальные категории в
сочинении Теона Смирнского) / Российский институт истории искусств, СПб.: РИИИ, 2024. 60 с.», науч. ред.
С. Е. Энглин, ISBN 978-5-86845-303-8, signed for print 14.06.2024. This is the edition the verifiers used (PDF from
artcenter.ru; «всякий мелос» p. 37). Not to be confused with a book of the same main title: Герцман Е. В. Последний
античный пифагореец о музыке: монография / под науч. ред. Т. С. Исуповой. СПб.: Изд-во РГПУ им. А. И. Герцена, 2023.
88 с.
- https://artcenter.ru/publications/2021-2/
- https://artcenter.ru/wp-content/uploads/2024/10/Герцман_Последний_античный_пифагореец.pdf
- https://www.litres.ru/book/evgeniy-vladimirovich-gercman/posledniy-antichnyy-pifagoreec-o-muzyke-70470481/ (the 2023 Herzen University book)

### Hiller — confirmed, completed
“Theonis Smyrnaei philosophi Platonici Expositio rerum mathematicarum ad legendum Platonem utilium”, rec. Eduardus
Hiller, Lipsiae: Teubner, 1878, viii, 216 p. (so p. [206] lies within the volume).
- https://catalogue.etoncollege.com/B52877

### Jan — confirmed, completed
“Musici scriptores Graeci: Aristoteles, Euclides, Nicomachus, Bacchius, Gaudentius, Alypius et melodiarum veterum
quidquid exstat”, rec. Carolus Ianus, Lipsiae: Teubner, 1895, xciii, 503 p. (supplement “Melodiarum reliquiae”, 1899).
Shchetnikov 2008a cites Nicomachus from it as pp. 236–265, consistent with the notes’ Jan p. 258 = Manual 11.
- https://zenon.dainst.org/Record/000770186

### Kühner–Gerth — completed
Raphael Kühner, Ausführliche Grammatik der griechischen Sprache, Teil 2: Satzlehre, 3. Aufl. in neuer Bearbeitung
besorgt von Bernhard Gerth, 2 Bde., Hannover und Leipzig: Hahn, 1898 (Bd. 1, IX + 666 S.) and 1904 (Bd. 2).
- https://oeaw.ac.at/resources/Record/990000763230504498/Details
- https://nantilus.univ-nantes.fr/vufind/Record/PPN071396950

### Lampe — completed
G. W. H. Lampe (ed.), A Patristic Greek Lexicon, Oxford: Clarendon Press, issued in fascicles 1961–1968. Standard
imprint; the page (p. 131, s.v. ἀνεγχώρητος) comes from the edition’s apparatus and was not re-checked on the page.

### LSJ — completed
The Perseus LSJ XML header (sourceDesc): Liddell, Scott, “A Greek-English Lexicon”, “revised and augmented throughout
by Sir Henry Stuart Jones with the assistance of Roderick McKenzie”, Oxford: Clarendon Press, 1940 (9th ed.).
Logeion and lsj.gr serve the same 9th-edition text.
- https://github.com/PerseusDL/lexica (LSJ XML; header read from the copy saved in earlier research)

### Macran 1902 — completed
Henry S. Macran, Ἀριστοξένου Ἁρμονικὰ στοιχεῖα: The Harmonics of Aristoxenus, edited with translation, notes,
introduction and index of words, Oxford: Clarendon Press, 1902. Standard imprint (not re-opened).

### Meibom — completed
“Antiquae musicae auctores septem. Graece et Latine. Marcus Meibomius restituit ac notis explicavit”, 2 vols.,
Amstelodami: apud Ludovicum Elzevirium, 1652 (Willems no. 1148). Aristoxenus’ Elementa harmonica opens vol. 1.
- https://data.cerl.org/stcn/85245502X
- https://catalogue.etoncollege.com/B39320

### Pape — completed
Wilhelm Pape, Griechisch-deutsches Handwörterbuch, 3. Aufl., bearbeitet von M. Sengebusch, 2 Bde., Braunschweig:
Vieweg, 1880 (6th printing 1914, the text digitised on zeno.org as “Pape-1880”). Which printing Logeion and lsj.gr
digitised is not stated; the entry gives the edition.
- https://de.wikisource.org/wiki/Maximilian_Sengebusch

### Par. — completed
Title page of the BSB copy (A.gr.b. 298#Beibd.1, MDZ bsb10169572; image saved in earlier research):
«ΤΟΥ ΣΟΦΩΤΑΤΟΥ ΨΕΛΛΟΥ, ΣΥΝΤΑΓΜΑ ΕΥΣΥΝΟΠΤΟΝ εἰς τὰς τέσσαρας μαθηματικὰς ἐπιστήμας, ἀριθμητικήν, μουσικήν,
γεωμετρίαν, καὶ ἀστρονομίαν. DOCTISSIMI PSELLI Opus dilucidum in quattuor Mathematicas disciplinas, Arihmeticam
[sic], Musicam, Geometriam, & Astronomiam … PARISIIS, Excudebat Iacobus Bogardus. 1545.» The title page also lists
«Τῆς μουσικῆς σύνοψις ἠκριβωμένη». So the reprint is Paris: Jacques Bogard, 1545. That it reprints the Venice editio
princeps of 1532 rests on the edition’s witness description (cmp/about.md: “Paris 1545 (Jacques Bogard), a reprint of
the first edition (Venice 1532)”). Earlier research cites Pinelli’s catalogue (via Harles) for “Venetiis, de Sabio,
1532”, edited by Arsenios of Monemvasia; the 1532 printer was not confirmed on the web, so it is not in the entry.
- https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb10169572/manifest
- https://www.deutsche-digitale-bibliothek.de/item/5PW5VF5DIAHMQQCZJG2TK2LOZHJFOUZR

### Pistelli — completed
“Iamblichi in Nicomachi arithmeticam introductionem liber”, ad fidem codicis Florentini edidit Hermenegildus Pistelli,
Lipsiae: Teubner, 1894 (reprint with addenda by U. Klein, 1975).
- https://cir.nii.ac.jp/crid/1130000794885039616?lang=en

### Щетников 2008а / Shchetnikov 2008a — completed (one key misuse, see § 1)
PDF 2-1-nikomach.pdf: «Никомах Геразский. Руководство по гармонике», «© А. И. Щетников, предисловие и перевод, 2008»,
ΣΧΟΛΗ Vol. II.1 (2008); running heads p. 77 (PDF p. 3) to p. 89 (PDF p. 15), so pp. 75–89. CEEOL: pp. 75–89.
- https://classics.nsu.ru/schole/assets/files/2-1-nikomach.pdf
- https://www.ceeol.com/search/article-detail?id=63002

### Щетников 2008б / Shchetnikov 2008b — completed
PDF 2-1-schetnikov.pdf: «Алгоритм разворачивания всех числовых отношений из отношения равенства и идеальные числа
Платона», А. И. Щетников, ΣΧΟΛΗ Vol. II.1 (2008); running head p. 56 on PDF p. 2, 20 pages, so pp. 55–74 (DOAJ: 55–74).
- https://classics.nsu.ru/schole/2/2-1-schetnikov.pdf
- https://doaj.org/article/6c0cf8648aaa4dff8e45d54f3061b196

### Щетников 2009 / Shchetnikov 2009 — completed
PDF 3-2-theon.pdf, head: «ΣΧΟΛΗ Vol. 3. 2 (2009) 466–558 © А. И. Щетников, 2009»; title «Теон Смирнский. Изложение
математических предметов, полезных при чтении Платона»; English “Introduction, Russian translation and notes”.
CEEOL abbreviates the title («Изложение предметов…»); the PDF title is used. The U010 quotation is on p. 491.
- https://classics.nsu.ru/schole/3/3-2-theon.pdf
- https://www.ceeol.com/search/article-detail?id=33621

### Щетников 2012 / Shchetnikov 2012 — completed
PDF 6-1-sec-can.pdf: «Евклидов корпус. Деление канона», А. И. Щетников, “Introduction, Russian translation and notes”;
running heads «ΣΧΟΛΗ Vol. 6. 1 (2012) 99 … 109», so pp. 98–110 (CEEOL: 98–110).
- https://classics.nsu.ru/schole/6/6-1-sec-can.pdf
- https://ceeol.com/search/article-detail?id=162861

### Smyth — corrected (wrong book)
The entry named “A Greek Grammar for Schools and Colleges (1916)”. That is a separate, much shorter book (archive.org
copies dated 1916, ~520 page images). The section numbers in the notes (§ 958 neuter plural with singular verb, § 1014,
§ 2837 apodotic δέ) are those of A Greek Grammar for Colleges (New York: American Book Company, 1920), the text on
Perseus and in Alpheios (the 1956 Messing revision keeps most of this numbering). The SBL handbook blog warns against
citing the 1916 book as “Smyth”.
- https://sblhs2.com/2018/03/08/citing-smyths-greek-grammar/
- https://archive.org/metadata/greekgrammarfor00smyt/metadata

### Sophocles, Lexicon — completed
The archive.org copy used in earlier research has: “Memorial Edition. Greek Lexicon of the Roman and Byzantine Periods
(From B.C. 146 to A.D. 1100) by E. A. Sophocles … Cambridge: Harvard University Press; London: Humphrey Milford,
Oxford University Press, 1914”; copyright 1870. The entry gives 1914 (the copy used) and the first edition (1870).

### Strunk — completed (one attribution wrong, see § 1)
attalus.org: “The translation of this treatise is taken from O. Strunk, Source Readings in Music History, pp. 34–46”.
Pp. 34–46 are those of the one-volume first edition: Source Readings in Music History from Classical Antiquity through
the Romantic Era, selected and annotated by Oliver Strunk, New York: W. W. Norton, 1950 (xxi + 919 p.). The notes’
quotations (§ 2 “tension and relaxation”; § 5 “consecutive notes”; § 14 “a progression of the melody by consecutive
notes”) are on that page.
- https://www.attalus.org/translate/cleonides.html
- https://www.cambridge.org/core/journals/renaissance-news/article/source-readings-in-music-history-from-classical-antiquity-through-romantic-era-selected-and-annotated-by-oliver-strunk-new-york-w-w-norton-1950-xxi-and-919-p-850/1D87A7A814A19FEF6244B5B615A8177F
- https://en.wikipedia.org/wiki/Pyknon (source of “trisemitone”, 1998 revision)

### синодальный перевод / Synodal translation — completed with the first edition; question
The edition the composer used is not recorded anywhere in the materials. The entry gives the first complete Synodal
Bible (St Petersburg: Synodal Press, 1876; the New Testament in this translation 1862). The quoted wording of Eph. 4:16
(«составляемое и совокупляемое») is the standard Synodal text. If the editor prefers a modern printing (e.g. Russian
Bible Society), the year must be supplied.

### Цыпин 2013 / Tsypin 2013 — completed
Moscow Conservatory reference list: «Птолемей. Гармоника; Порфирий. Комментарий к Гармонике Птолемея / Издание
подготовил В. Г. Цыпин. М.: Московская консерватория, 2013.» Full title (Ruslania): «Клавдий Птолемей. Гармоника в трех
книгах. Порфирий. Комментарий к "Гармонике" Птолемея», 456 с., ISBN 978-5-89598-288-4; publisher «Научно-издательский
центр «Московская консерватория»».
- https://nv.mosconsv.ru/node/470
- https://ruslania.com/ru/noty/159159-klavdij-ptolemej-garmonika-v-treh-knigah-porfirij-kommentarij-k-garmonike-ptolemeja/
- https://www.twirpx.com/file/1459115/

### Цыпин 2014 / Tsypin 2014 — confirmed, completed
Journal page: «Клеонид. Введение в гармонику», authors С. Н. Лебедев (preface) and В. Г. Цыпин (new translation and
commentary), Научный вестник Московской консерватории, Том 5, Выпуск 3 (сентябрь 2014), с. 168–186,
DOI 10.26176/mosconsv.2014.18.3.09 (18 = running issue number).
- https://nv.mosconsv.ru/node/470

### Vinc. — completed
BnF: Vincent, Alexandre (1797–1868); «Notice sur divers manuscrits grecs relatifs à la musique comprenant une traduction
française et des commentaires, par M. A.-J.-H. Vincent», Paris: Imprimerie royale, 1847, 600 p., in-4°; series «Notices
et extraits des manuscrits de la Bibliothèque du Roi et autres bibliothèques, publiés par l’Institut royal de France;
Tome 16, Seconde partie».
- https://catalogue.bnf.fr/ark:/12148/cb433233440

## 3. Questions for the editor

1. Key order «Александрова, Мякин 2009»: the publication names Myakin first (see above).
2. Synodal translation: which printing was used?
3. Not in the bibliography, but relevant to the project: Gertsman’s bibliographic index (RIII 2024, no. 11) lists
   «“Синопсис музыки”, или Памятник агонии musica speculativa. М.: Композитор, 2000. 355 с.», and also «Музыкально-
   теоретические знания Михаила Пселла» (Византийский временник 54, 1993, 75–80). By its title the 2000 book is a
   study of a Byzantine “Synopsis of music”, very probably this treatise (Ps.-Psellus); whether it contains a Russian
   translation could not be confirmed online. Gertsman 2024 (p. 35) quotes a line of “Ps.-Psellus” in Russian, and his
   encyclopedia has an article on Ps.-Psellus (vol. 2, pp. 1098–1102). The editor may want to check the 2000 book
   before publication (the translation method allowed other translations only after both were done; they are done).

## 4. Not verified

- Lampe p. 131 (page taken from the edition; Lampe not opened).
- The printing of Bailly’s Abrégé on lsj.gr and of Pape on Logeion/lsj.gr.
- Dvoretsky’s editor and publisher (standard imprint; no catalogue page opened).
- The printer of the Venice editio princeps of 1532 (only via Pinelli/Harles in earlier research).
- The Basel title page itself (catalogue transcription used).
- Whether Strunk’s 1998 revision (ed. Treitler) really has “trisemitone” (only Wikipedia).
- Whether Gertsman 2000 contains a translation of this treatise.
