// Copies the voiced chapters listed in src/_data/audio/<textKey>.json from the GitHub releases into the built site,
// as <site>/audio/<textKey>/<file>.mp3, so that GitHub Pages serves them as audio/mpeg from the site itself.
// GitHub serves release assets as application/octet-stream, with nosniff and no file extension in the final URL,
// and Safari (also on iPhone) will not play them. The audio stays out of git: it is fetched at every deploy.
// A file that cannot be fetched is not fatal: its button falls back to the release (text.js), and a warning is shown.
// Usage: node scripts/fetch-audio.mjs site   (after the build; files already present are kept)
import { existsSync, mkdirSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const OUT = process.argv[2] || "site";
const DATA = "src/_data/audio";

async function get(url) {
  for (let i = 1; ; i++) {
    try {
      const r = await fetch(url);
      if (!r.ok) throw new Error(`HTTP ${r.status}`);
      return Buffer.from(await r.arrayBuffer());
    } catch (err) {
      if (i === 3) throw err;
      await new Promise((ok) => setTimeout(ok, 2000 * i));
    }
  }
}

let fetched = 0, kept = 0, failed = 0, bytes = 0;
for (const f of readdirSync(DATA).filter((f) => f.endsWith(".json"))) {
  const key = f.replace(/\.json$/, "");
  const data = JSON.parse(readFileSync(join(DATA, f), "utf8"));
  const dir = join(OUT, "audio", key);
  mkdirSync(dir, { recursive: true });
  for (const lang of ["ru", "en"]) {
    for (const e of Object.values(data[lang] || {})) {
      const file = join(dir, e.url.split("/").pop());
      if (existsSync(file)) { kept++; continue; }
      try {
        const buf = await get(e.url);
        writeFileSync(file, buf);
        fetched++; bytes += buf.length;
      } catch (err) {
        failed++;
        console.log(`::warning::audio not copied, the page will use the release: ${e.url} (${err.message})`);
      }
    }
  }
}
console.log(`audio: ${fetched} fetched (${(bytes / 1048576).toFixed(1)} MB), ${kept} already present, ${failed} failed -> ${OUT}/audio`);
