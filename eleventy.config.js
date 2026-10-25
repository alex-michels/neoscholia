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
