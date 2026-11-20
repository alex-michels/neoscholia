// Neoscholia — static site build (Eleventy 3).
// Sources: src/ (pages *.njk, data src/_data/*.yaml|json, layout and partials src/_includes, assets src/assets).
// Output: site/ — plain HTML with relative links; works on any host, in a subfolder, or opened from disk.
import { execFileSync } from "node:child_process";
import { createHash } from "node:crypto";
import { load as loadYaml } from "js-yaml";
import { renderArticle } from "./lib/article.js";

const gitCache = new Map();

/** Last commit that touched a source file: { date: "дд.мм.гггг", subject } or null. */
function lastChange(inputPath) {
  const file = String(inputPath || "").replace(/^\.\//, "");
  if (!file) return null;
  if (!gitCache.has(file)) {
    let value = null;
    try {
      const out = execFileSync("git", ["log", "-1", "--format=%cs%x09%s", "--", file], { encoding: "utf8", stdio: ["ignore", "pipe", "ignore"] }).trim();
      if (out) {
        const [iso, subject] = out.split("\t");
        const [y, m, d] = iso.split("-");
        value = { date: `${d}.${m}.${y}`, subject };
      }
    } catch {
      value = null; // not a git checkout, or git is unavailable
    }
    gitCache.set(file, value);
  }
  return gitCache.get(file);
}

/** Current versions of the published pages: { "zacher-1": "0.3", … } — page file name → front matter "version". */
const versionCache = new WeakMap();
function versionsOf(pages) {
  if (!versionCache.has(pages)) {
    const map = {};
    for (const p of pages) if (p.data && p.data.version) map[p.fileSlug] = p.data.version;
    versionCache.set(pages, map);
  }
  return versionCache.get(pages);
}

/** Wraps runs of Greek script in <span lang="grc"> (outside tags and outside elements already marked as Greek).
    A run starts with a Greek letter: a lone combining accent, as in the Russian «бо́льшая», is not Greek. */
const GREEK_RUN = /\p{Script=Greek}[\p{Script=Greek}̀-ͯ]*(?:[\s,.;·’'ʼ-]+\p{Script=Greek}[\p{Script=Greek}̀-ͯ]*)*/gu;
const VOID_TAG = /^<(?:br|hr|img|input|wbr|meta|link|source|col)\b/i;
function markGreek(html) {
  const stack = [];
  return String(html ?? "").split(/(<[^>]+>)/).map((part) => {
    if (part.startsWith("<")) {
      if (part.startsWith("</")) stack.pop();
      else if (!part.startsWith("<!") && !VOID_TAG.test(part) && !part.endsWith("/>")) {
        const lang = part.match(/\slang="([^"]*)"/);
        stack.push(lang ? /^(grc|el)/.test(lang[1]) : stack.length > 0 && stack[stack.length - 1]);
      }
      return part;
    }
    return stack.length && stack[stack.length - 1] ? part : part.replace(GREEK_RUN, (run) => `<span lang="grc">${run}</span>`);
  }).join("");
}

export default function (eleventyConfig) {
  eleventyConfig.addDataExtension("yaml,yml", (contents) => loadYaml(contents));
  eleventyConfig.addGlobalData("layout", "layouts/base.njk");
  // Build stamp appended to CSS and JS links: GitHub Pages lets browsers cache files for 10 minutes,
  // and a fresh page with a stale script breaks (e.g. the audio buttons had no handler).
  eleventyConfig.addGlobalData("build", Date.now().toString(36));

  eleventyConfig.addPassthroughCopy({ "src/assets": "assets" });
  // Research dossiers published next to their articles.
  eleventyConfig.addPassthroughCopy({ "research/studies/laestrygonians/dossier.md": "laestrygonians-dossier.md" });
  eleventyConfig.addPassthroughCopy({ "research/dissertation/mikhaylov-2015-entgrenzung-und-begrenzung-alexanders.pdf": "docs/mikhaylov-2015-dissertation.pdf" });

  // "../" prefixes so that shared links and assets work from pages in subfolders.
  eleventyConfig.addFilter("rootPrefix", (url) => "../".repeat(Math.max(0, String(url || "/").split("/").length - 2)));
  eleventyConfig.addFilter("repoPath", (inputPath) => String(inputPath || "").replace(/^\.\//, ""));
  eleventyConfig.addFilter("lastChange", lastChange);
  // Full address of a page for <link rel="canonical"> and share tags; the home page is the site root.
  eleventyConfig.addFilter("absUrl", (url, base) => String(base || "").replace(/\/+$/, "") + (url === "/index.html" ? "/" : String(url || "/")));
  // "25.10.2026" → "2026-10-25" (for <time datetime> and bibliographic meta tags).
  eleventyConfig.addFilter("isoDate", (d) => String(d || "").split(".").reverse().join("-"));
  // Version numbers are never typed in content: "{version:zacher-1}" in a data string or a template is replaced
  // with the current version of that page. Usage: {{ html | fill(collections.all) | safe }}.
  eleventyConfig.addFilter("fill", (html, pages) => String(html ?? "").replace(/\{version:([\w-]+)\}/g, (all, slug) => {
    const v = versionsOf(pages || [])[slug];
    if (!v) throw new Error(`{version:${slug}}: there is no page "${slug}" with a "version" in its front matter`);
    return v;
  }));
  eleventyConfig.addFilter("pageVersion", (slug, pages) => versionsOf(pages || [])[slug] || "");
  // Greek inside running text gets lang="grc": the right font, hyphenation and pronunciation for screen readers.
  eleventyConfig.addFilter("greek", markGreek);
  // Published pages of one library section (for «Опубликовано в разделе»): cards whose sectionHref is the section page.
  eleventyConfig.addFilter("inSection", (cards, href) => cards.filter((c) => c.sectionHref === href));
  // Items of a list that have a truthy field: {{ (items | where("nowhere")).length }}.
  eleventyConfig.addFilter("where", (items, key) => (items || []).filter((i) => i && i[key]));
  // Fingerprint of a chapter's translation; scripts/tts/tts.py names its audio files with the same hash,
  // so a chapter edited after it was voiced loses its play button until it is voiced again.
  eleventyConfig.addFilter("textHash", (s) => createHash("sha1").update(String(s), "utf8").digest("hex").slice(0, 10));
  // Research articles: the page takes its text from research/studies/<slug>/article.md (see lib/article.js).
  eleventyConfig.addFilter("article", (path, links) => renderArticle(path, links));

  // History of the site's content: the version histories of texts and studies (front matter "versions"
  // or texts[textKey].versions) and the content news in src/_data/news.yaml, newest first.
  eleventyConfig.addFilter("changeFeed", (pages, texts, news) => {
    const iso = (d) => String(d).split(".").reverse().join("-");
    const items = [];
    for (const p of pages) {
      const d = p.data;
      if (!d.version) continue;
      const versions = d.versions || (d.textKey && texts[d.textKey] && texts[d.textKey].versions) || [];
      // новая версия без записи в истории версий не попала бы ни в «Историю изменений», ни в блок «Версии»
      if (!versions.length || versions[0].version !== d.version)
        throw new Error(`${p.inputPath}: version "${d.version}" has no entry at the top of its "versions" list (found "${versions.length ? versions[0].version : "nothing"}")`);
      for (const v of versions) {
        items.push({ at: v.at || iso(v.date), date: v.date, href: p.url.replace(/^\//, ""),
          title: (d.card && d.card.title) || d.title, version: v.version, text: v.short || v.text });
      }
    }
    for (const n of news || []) items.push({ at: n.at || iso(n.date), date: n.date, text: n.text });
    return items.sort((a, b) => (a.at < b.at ? 1 : a.at > b.at ? -1 : 0));
  });
  eleventyConfig.addFilter("byDate", (items) => items.reduce((days, x) => {
    if (!days.length || days[days.length - 1].date !== x.date) days.push({ date: x.date, items: [] });
    days[days.length - 1].items.push(x);
    return days;
  }, []));
  // Published texts and studies for the home page: pages with a "card" in the front matter.
  eleventyConfig.addFilter("publishedCards", (pages) => pages.filter((p) => p.data.card && p.data.version)
    .map((p) => ({ ...p.data.card, href: p.url.replace(/^\//, ""), version: p.data.version, updated: p.data.updated,
      ladder: p.data.ladder, status: p.data.status, textKey: p.data.textKey }))
    .sort((a, b) => (a.order || 99) - (b.order || 99)));
  eleventyConfig.addWatchTarget("research/studies/");
  // Mark ladder steps up to the current status as done.
  eleventyConfig.addFilter("ladderSteps", (steps, status) => {
    const current = steps.findIndex((s) => s.key === status);
    if (current < 0) throw new Error(`Unknown status "${status}"; expected one of: ${steps.map((s) => s.key).join(", ")}`);
    return steps.map((s, i) => ({ ...s, done: i <= current, current: i === current }));
  });

  return {
    dir: { input: "src", output: "site", includes: "_includes", data: "_data" },
    templateFormats: ["njk", "md"],
    htmlTemplateEngine: "njk",
    markdownTemplateEngine: "njk",
  };
}
