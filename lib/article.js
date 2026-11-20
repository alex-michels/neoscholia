// Renders a research article written in Markdown (research/studies/<slug>/article.md) for the site.
// One source for the text: the page template takes the abstract, the numbered sections, the
// appendix of source texts and the bibliography from the Markdown file.
//   - Footnotes [^n] become margin notes (open on tap on narrow screens).
//   - "## N. Title" headings get ids s1, s2, … and make up the table of contents (toc).
//   - Blocks wrapped in <!-- web:NAME --> … <!-- /web:NAME --> are replaced on the site by the
//     partial src/_includes/<prefix>NAME.njk (the Markdown keeps a plain version for other readers).
//
// Markup contract. Styles: src/assets/css/layouts/article.css; behaviour: src/assets/js/article.js;
// the ids n1… and s1… are link targets in src/_data/indexes.json (scripts/build-indexes.py).
//   note     <button class="sn-ref" aria-controls="nN">N</button><span class="sn" id="nN"><span class="sn-n">N</span>…</span>
//   heading  <h2 id="sN"><span class="no">N.</span> Title</h2>   (the full stop is for screen readers only)
//   table    <div class="table-wrap wide" role="region" tabindex="0" aria-label="…"><table class="table" style="--cols: N">;
//            a paragraph in italics right after a table becomes its <caption>
//   quote    <blockquote class="grc" lang="grc"> for Greek, <blockquote class="tr"> for its translation
//   refs     <h3 class="overline"> for the groups of the bibliography
import { readFileSync } from "node:fs";
import markdownIt from "markdown-it";

const md = markdownIt({ html: true, linkify: false, typographer: false });
const GREEK = /[Ͱ-Ͽἀ-῿]/g;
const LETTERS = /[\p{L}]/gu;

function sidenote(n, text) {
  return `<button type="button" class="sn-ref" aria-expanded="false" aria-controls="n${n}" aria-label="Примечание ${n}">${n}</button>`
    + `<span class="sn" id="n${n}" role="note"><span class="sn-n">${n}</span>${md.renderInline(text)}</span>`;
}

/** Section heading: a small line above (the number) and the title; the page template builds its own headings the same way. */
function heading(id, over, titleHtml) {
  return `<h2 id="${id}"><span class="no">${over}<span class="sr-only">.</span></span> ${titleHtml}</h2>`;
}

function polish(html, links) {
  let out = html
    // A paragraph set in italics right after a table ("*Таблица. …*") is its caption.
    .replace(/<table>((?:(?!<\/table>)[\s\S])*)<\/table>\s*<p><em>((?:(?!<\/?em>)[\s\S])*)<\/em><\/p>/g,
      (all, inner, caption) => `<table><caption>${caption}</caption>${inner}</table>`)
    // A table scrolls sideways inside a focusable region named after its column heads;
    // --cols (the number of columns) keeps the columns readable on a narrow screen.
    .replace(/<table>([\s\S]*?)<\/table>/g, (all, inner) => {
      const heads = [...inner.matchAll(/<th[^>]*>([\s\S]*?)<\/th>/g)].map((m) => m[1].replace(/<[^>]+>/g, "").trim());
      const label = heads.length ? `Таблица: ${heads.join(", ")}` : "Таблица";
      return `<div class="table-wrap wide" role="region" tabindex="0" aria-label="${label}"><table class="table" style="--cols: ${heads.length}">`
        + inner.replace(/<th>/g, '<th scope="col">') + "</table></div>";
    })
    // Greek quotations get lang="grc"; a translation that follows a Greek quotation is marked as such.
    .replace(/<blockquote>([\s\S]*?)<\/blockquote>/g, (all, inner) => {
      const text = inner.replace(/<[^>]+>/g, "");
      const greek = (text.match(GREEK) || []).length;
      const letters = (text.match(LETTERS) || []).length || 1;
      return greek / letters > 0.5
        ? `<blockquote class="grc" lang="grc">${inner}</blockquote>`
        : `<blockquote class="tr">${inner}</blockquote>`;
    });
  for (const [from, to] of Object.entries(links || {})) out = out.split(`href="${from}"`).join(`href="${to}"`);
  return out;
}

/**
 * @param {string} path  Markdown file, relative to the project root
 * @param {object} links map of hrefs to rewrite for the site, e.g. {"dossier.md": "laestrygonians-dossier.md"}
 * @returns {{abstractRu: string, abstractEn: string, body: Array<{html?: string, block?: string}>, refs: string,
 *            toc: Array<{href: string, n: string, label: string}>,
 *            appendixIntro: string, appendix: Array<{ref: string, lemma: string, chips: Array<{text: string, who: boolean}>, greek: string, tr: string, crit: string, notes: string[]}>,
 *            notes: number}}
 *   toc lists the numbered sections; a title of the form "Short: the rest" is shortened to "Short" there.
 */
export function renderArticle(path, links = {}) {
  const src = readFileSync(path, "utf8").replace(/\r\n/g, "\n");
  const notes = new Map();
  const text = src.replace(/^\[\^(\d+)\]:\s*(.+)$/gm, (_, n, t) => { notes.set(n, t.trim()); return ""; });

  const sections = [];
  for (const part of text.split(/^## /m).slice(1)) {
    const nl = part.indexOf("\n");
    sections.push({ title: part.slice(0, nl).trim(), body: part.slice(nl + 1).replace(/\n---\s*$/m, "") });
  }
  const find = (re) => sections.find((s) => re.test(s.title));
  const render = (markdown) => polish(
    md.render(markdown.replace(/\[\^(\d+)\]/g, (_, n) => `@@SN${n}@@`))
      .replace(/@@SN(\d+)@@/g, (_, n) => {
        if (!notes.has(n)) throw new Error(`${path}: footnote [^${n}] has no definition`);
        return sidenote(n, notes.get(n));
      }),
    links,
  );

  const body = [];
  const toc = [];
  for (const s of sections.filter((x) => /^\d+\.\s/.test(x.title))) {
    const [, no, title] = s.title.match(/^(\d+)\.\s+(.*)$/);
    toc.push({ href: `#s${no}`, n: no, label: md.renderInline(title.split(/:\s/)[0]) });
    let rest = s.body;
    let html = heading(`s${no}`, no, md.renderInline(title)) + "\n";
    const block = /<!-- web:([\w-]+) -->[\s\S]*?<!-- \/web:\1 -->/;
    let m;
    while ((m = rest.match(block))) {
      html += render(rest.slice(0, m.index));
      body.push({ html });
      body.push({ block: m[1] });
      html = "";
      rest = rest.slice(m.index + m[0].length);
    }
    body.push({ html: html + render(rest) });
  }

  const abstractRu = find(/^Аннотация/);
  const abstractEn = find(/^Abstract/);
  const refs = find(/^Литература/);
  const appx = find(/^Приложение/);
  return {
    abstractRu: abstractRu ? render(abstractRu.body) : "",
    abstractEn: abstractEn ? render(abstractEn.body) : "",
    body,
    toc,
    // the groups of the bibliography are headed by small labels
    refs: refs ? render(refs.body).replace(/<h3>/g, '<h3 class="overline">') : "",
    ...(appx ? appendix(appx.body, render) : { appendixIntro: "", appendix: [] }),
    notes: notes.size,
  };
}

/**
 * The appendix of source texts: an intro, then one "### " block per item.
 *   ### Σ 10.82 · τηλέπυλον · V · B Q T · *Кратет*   — reference, optional Greek lemma, chips (*…* = person)
 *   > Greek text
 *   Translation (one or more paragraphs)
 *   Аппарат: selected apparatus
 *   Примечание: a note, e.g. on a divergence between the two translations (one paragraph each)
 */
function appendix(markdown, render) {
  const [intro, ...items] = markdown.split(/^### /m);
  return {
    appendixIntro: render(intro),
    appendix: items.map((item) => {
      const nl = item.indexOf("\n");
      const [ref, ...parts] = item.slice(0, nl).trim().split(" · ");
      const lemma = parts.length && (parts[0].match(GREEK) || []).length ? parts.shift() : "";
      const chips = parts.map((p) => (/^\*.*\*$/.test(p) ? { text: p.slice(1, -1), who: true } : { text: p, who: false }));
      const paras = item.slice(nl + 1).trim().split(/\n\s*\n/);
      const greek = paras.filter((p) => p.startsWith(">")).map((p) => p.replace(/^>\s?/gm, "").trim()).join(" ");
      const crit = paras.filter((p) => p.startsWith("Аппарат:")).map((p) => p.replace(/^Аппарат:\s*/, "")).join(" ");
      const notes = paras.filter((p) => p.startsWith("Примечание:")).map((p) => md.renderInline(p.replace(/^Примечание:\s*/, "")));
      const tr = paras.filter((p) => !p.startsWith(">") && !p.startsWith("Аппарат:") && !p.startsWith("Примечание:"));
      return {
        ref, lemma, chips,
        greek: md.renderInline(greek),
        tr: tr.map((p) => md.renderInline(p)).join("<br>"),
        crit: crit ? md.renderInline(crit) : "",
        notes,
      };
    }),
  };
}
