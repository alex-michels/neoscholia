// Checks the built site: every relative href/src points to an existing file, and every #anchor exists.
// Usage: node scripts/check-links.mjs site      (exit code 1 if anything is broken)
import { readFileSync, readdirSync, existsSync, statSync } from "node:fs";
import { join, dirname, normalize, relative } from "node:path";

const root = process.argv[2] || "site";
const pages = [];
(function walk(dir) {
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) walk(p);
    else if (p.endsWith(".html")) pages.push(p);
  }
})(root);

const idsCache = new Map();
function ids(file) {
  if (!idsCache.has(file)) {
    const html = readFileSync(file, "utf8");
    idsCache.set(file, new Set([...html.matchAll(/\sid="([^"]+)"/g)].map((m) => m[1])));
  }
  return idsCache.get(file);
}

const problems = [];
for (const page of pages) {
  const html = readFileSync(page, "utf8").replace(/<script[\s\S]*?<\/script>/g, "");
  for (const m of html.matchAll(/\s(?:href|src)="([^"]*)"/g)) {
    const ref = m[1];
    if (!ref || /^(https?:|mailto:|tel:|data:)/.test(ref)) continue;
    const [path, frag] = ref.split("#");
    const target = path ? normalize(join(dirname(page), path)) : page;
    if (path && !existsSync(target)) { problems.push(`${relative(root, page)}: missing file ${ref}`); continue; }
    if (frag && target.endsWith(".html") && !ids(target).has(decodeURIComponent(frag))) {
      problems.push(`${relative(root, page)}: missing anchor ${ref}`);
    }
  }
  if (/claude\.ai\/artifact\//.test(html)) problems.push(`${relative(root, page)}: link to a claude.ai artifact`);
}

if (problems.length) {
  console.error(problems.join("\n"));
  console.error(`\n${problems.length} problem(s) in ${pages.length} pages`);
  process.exit(1);
}
console.log(`links ok: ${pages.length} pages checked`);
