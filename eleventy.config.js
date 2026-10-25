// Neoscholia — static site build (Eleventy 3).
// Sources: src/ (pages *.njk, data src/_data/*.yaml|json, layout and partials src/_includes, assets src/assets).
// Output: site/ — plain HTML with relative links; works on any host, in a subfolder, or opened from disk.
import { execFileSync } from "node:child_process";
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

  eleventyConfig.addPassthroughCopy({ "src/assets": "assets" });
  // Research dossiers published next to their articles.
  eleventyConfig.addPassthroughCopy({ "research/studies/laestrygonians/dossier.md": "laestrygonians-dossier.md" });

  // "../" prefixes so that shared links and assets work from pages in subfolders.
  eleventyConfig.addFilter("rootPrefix", (url) => "../".repeat(Math.max(0, String(url || "/").split("/").length - 2)));
  eleventyConfig.addFilter("repoPath", (inputPath) => String(inputPath || "").replace(/^\.\//, ""));
  eleventyConfig.addFilter("lastChange", lastChange);
  // Research articles: the page takes its text from research/studies/<slug>/article.md (see lib/article.js).
  eleventyConfig.addFilter("article", (path, links) => renderArticle(path, links));
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
