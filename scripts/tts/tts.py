"""Voice the translations of a text page with Silero TTS (pre-recorded audio for the static site).

For every chapter and language the script makes <lang>-c<chapter>-<hash>.mp3, uploads it to the GitHub
release "audio-<textKey>" of the site's repository (the audio is not kept in git, so it does not pile up
in the history) and records its URL in src/_data/audio/<textKey>.json. A local copy stays in the cache
folder (see NEOSCHOLIA_TTS_CACHE). <hash> is the first 10 hex digits of the SHA-1 of
the chapter's translation as it stands in src/_data/texts/<textKey>.json. The page template computes
the same hash at build time and shows the play button only if they match, so a chapter edited after
it was voiced simply loses its button until the script is run again.

Usage (from the project root, in the TTS environment, see scripts/tts/README.md):
  python scripts/tts/tts.py zacher-1                 # voice what is missing or out of date
  python scripts/tts/tts.py zacher-1 --lang ru --chapters 14,15 --force
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.request
import wave
from pathlib import Path

import numpy as np
import torch

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CACHE = Path(os.environ.get("NEOSCHOLIA_TTS_CACHE", Path.home() / ".cache" / "neoscholia-tts"))

# Silero models (official list: https://github.com/snakers4/silero-models, models.yml).
VOICES = {
    "ru": {"model": "v5_6_ru", "url": "https://models.silero.ai/models/tts/ru/v5_6_ru.pt", "speaker": "xenia", "chunk": 700},
    "en": {"model": "v3_en", "url": "https://models.silero.ai/models/tts/en/v3_en.pt", "speaker": "en_0", "chunk": 0},
}
SAMPLE_RATE = 24000
PAUSE = 0.3          # seconds of silence between chunks
BITRATE = "32k"      # mono MP3; plenty for speech


def text_hash(s):
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:10]


def load_stress():
    """scripts/tts/stress-ru.txt: 'stem = stem with +' per line; the stem is matched at the start of a word."""
    rules = []
    for line in (HERE / "stress-ru.txt").read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            plain, marked = (x.strip() for x in line.split("="))
            rules.append((re.compile(r"(?<![\w+])" + re.escape(plain)), marked))
    return rules


def prepare(text, lang, stress):
    t = re.sub(r"\[([^\]]*)\]", r"\1", text)          # editorial brackets: keep the words
    t = t.replace("…", "...")
    if lang == "ru":
        for rx, marked in stress:
            t = rx.sub(marked, t)
        t = t.replace("—", "–")
    else:
        t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("—", ", ")
    return re.sub(r"\s+", " ", t).strip()


def sentences(t):
    t = re.sub(r"([.!?]+[»”\"']?)\s+(?=[«“\"'А-ЯЁA-Z])", "\\1\n", t)
    return [p.strip() for p in t.split("\n") if p.strip()]


def chunks(t, limit):
    if not limit:
        return sentences(t)
    out, cur = [], ""
    for s in sentences(t):
        if cur and len(cur) + len(s) + 1 > limit:
            out.append(cur)
            cur = s
        else:
            cur = (cur + " " + s).strip()
    return out + ([cur] if cur else [])


def model_for(lang):
    v = VOICES[lang]
    path = CACHE / f"{v['model']}.pt"
    if not path.exists():
        CACHE.mkdir(parents=True, exist_ok=True)
        print(f"downloading {v['url']}", flush=True)
        urllib.request.urlretrieve(v["url"], path)
    m = torch.package.PackageImporter(str(path)).load_pickle("tts_models", "model")
    m.to(torch.device("cpu"))
    return m


def synth(model, text, lang):
    v = VOICES[lang]
    parts = []
    for c in chunks(text, v["chunk"]):
        parts.append(model.apply_tts(text=c, speaker=v["speaker"], sample_rate=SAMPLE_RATE).numpy())
        parts.append(np.zeros(int(PAUSE * SAMPLE_RATE), dtype=np.float32))
    return np.concatenate(parts)


def write_mp3(audio, path):
    pcm = (np.clip(audio, -1, 1) * 32767).astype(np.int16)
    with tempfile.TemporaryDirectory() as tmp:
        wav = Path(tmp) / "a.wav"
        with wave.open(str(wav), "wb") as f:
            f.setnchannels(1)
            f.setsampwidth(2)
            f.setframerate(SAMPLE_RATE)
            f.writeframes(pcm.tobytes())
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(wav), "-af", "loudnorm=I=-18:TP=-1.5:LRA=11",
                        "-ac", "1", "-ar", str(SAMPLE_RATE), "-b:a", BITRATE, str(path)], check=True)
    return len(audio) / SAMPLE_RATE


def gh(*args, check=True):
    return subprocess.run(["gh", *args], check=check, capture_output=True, text=True, encoding="utf-8")


def ensure_release(repo, tag, title):
    if gh("release", "view", tag, "--repo", repo, check=False).returncode != 0:
        notes = (f"Озвучка переводов на странице «{title}»: синтез речи Silero (модели v5_6_ru и v3_en, лицензия моделей "
                 "CC BY-NC-SA 4.0). Файлы называются <язык>-c<глава>-<отпечаток текста>.mp3; список и отпечатки — "
                 "src/_data/audio/ в репозитории. Обновляется скриптом scripts/tts/tts.py.")
        gh("release", "create", tag, "--repo", repo, "--title", f"Озвучка: {title}", "--notes", notes, "--latest=false")
    return {a["name"] for a in json.loads(gh("release", "view", tag, "--repo", repo, "--json", "assets").stdout)["assets"]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("key", help="text key, e.g. zacher-1 (src/_data/texts/<key>.json)")
    ap.add_argument("--lang", default="ru,en")
    ap.add_argument("--chapters", default="", help="comma-separated chapter numbers (default: all)")
    ap.add_argument("--force", action="store_true", help="voice again even if up to date")
    a = ap.parse_args()

    data = json.loads((ROOT / "src" / "_data" / "texts" / f"{a.key}.json").read_text(encoding="utf-8"))
    man_path = ROOT / "src" / "_data" / "audio" / f"{a.key}.json"
    manifest = json.loads(man_path.read_text(encoding="utf-8")) if man_path.exists() else {}
    want = {int(x) for x in a.chapters.split(",") if x.strip()}
    site = json.loads((ROOT / "src" / "_data" / "site.json").read_text(encoding="utf-8"))
    repo = site["repo"].split("github.com/")[1]
    tag = f"audio-{a.key}"
    assets = ensure_release(repo, tag, data["title"])
    stress = load_stress()
    torch.set_num_threads(os.cpu_count() or 4)

    for lang in a.lang.split(","):
        v = VOICES[lang]
        entries = manifest.setdefault(lang, {})
        manifest.setdefault("voices", {})[lang] = {"engine": "Silero", "model": v["model"], "speaker": v["speaker"]}
        todo = [c for c in data["chapters"] if (not want or c["chapter"] in want)
                and (a.force or entries.get(str(c["chapter"]), {}).get("hash") != text_hash(c[lang]))]
        if not todo:
            print(f"{lang}: up to date")
            continue
        model = model_for(lang)
        out_dir = CACHE / "audio" / a.key / lang
        out_dir.mkdir(parents=True, exist_ok=True)
        for c in todo:
            ch, h = c["chapter"], text_hash(c[lang])
            for old in out_dir.glob(f"{lang}-c{ch}-*.mp3"):
                old.unlink()
            t0 = time.perf_counter()
            mp3 = out_dir / f"{lang}-c{ch}-{h}.mp3"
            seconds = write_mp3(synth(model, prepare(c[lang], lang, stress), lang), mp3)
            gh("release", "upload", tag, str(mp3), "--repo", repo, "--clobber")
            for old in [n for n in assets if n.startswith(f"{lang}-c{ch}-") and n != mp3.name]:
                gh("release", "delete-asset", tag, old, "--repo", repo, "-y")
                assets.discard(old)
            assets.add(mp3.name)
            entries[str(ch)] = {"url": f"https://github.com/{repo}/releases/download/{tag}/{mp3.name}", "hash": h, "seconds": round(seconds, 1)}
            print(f"{lang} ch {ch}: {seconds:.0f} s of audio in {time.perf_counter() - t0:.0f} s", flush=True)
            man_path.parent.mkdir(parents=True, exist_ok=True)
            for attempt in range(5):  # on Windows the file may be briefly locked by a reader (e.g. a site build)
                try:
                    man_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
                    break
                except OSError:
                    time.sleep(2)
            else:
                raise


if __name__ == "__main__":
    main()
