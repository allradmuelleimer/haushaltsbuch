"""Meldet neue und geaenderte Seiten per IndexNow an Bing, DuckDuckGo, Copilot, ChatGPT-Suche & Co.

Nach jedem Ausliefern einmal ausfuehren:

    python tools/indexnow.py            # nur neue/geaenderte URLs aus sitemap.xml melden
    python tools/indexnow.py --all      # alle URLs der Sitemap melden (z. B. beim ersten Mal)
    python tools/indexnow.py --dry-run  # nur anzeigen, was gemeldet wuerde

Wie "geaendert" erkannt wird: Fuer jede URL der Sitemap wird die gebaute Datei im Ordner
(…/index.html) gehasht und mit tools/indexnow_state.json verglichen. Die Datei wird nur nach
einer erfolgreichen Meldung (HTTP 200/202) aktualisiert und gehoert mit ins Git.

Der Schluessel ist die einzige <32 Hex-Zeichen>.txt im Wurzelordner; sie muss VOR der Meldung
online sein, sonst lehnt IndexNow ab (403). Liegt die Seite in einem Unterpfad (GitHub Pages),
wird keyLocation mitgeschickt.
Nur Standardbibliothek, kein pip noetig."""

import argparse
import hashlib
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "tools" / "indexnow_state.json"
ENDPOINT = "https://api.indexnow.org/indexnow"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


def find_key() -> str:
    keys = [p.stem for p in ROOT.glob("*.txt") if re.fullmatch(r"[0-9a-f]{32}", p.stem)
            and p.read_text(encoding="utf-8").strip() == p.stem]
    if len(keys) != 1:
        sys.exit(f"Erwartet genau eine IndexNow-Schluesseldatei im Wurzelordner, gefunden: {keys}")
    return keys[0]


def sitemap_urls() -> list[str]:
    tree = ET.parse(ROOT / "sitemap.xml")
    return [loc.text.strip() for loc in tree.getroot().findall("sm:url/sm:loc", NS)]


def site_base(urls: list[str]) -> str:
    """Gemeinsamer Anfang aller URLs bis zum letzten '/' - die Wurzel der Seite."""
    first = urls[0]
    u = urlparse(first)
    base = f"{u.scheme}://{u.netloc}/"
    prefix = min(urls, key=len)
    for p in urls:
        while not p.startswith(prefix):
            prefix = prefix[:-1]
    path = urlparse(prefix).path
    path = path[: path.rfind("/") + 1] or "/"
    return base.rstrip("/") + path


def local_file(url: str, base: str) -> Path:
    rel = url[len(base):]
    if rel == "" or rel.endswith("/"):
        rel += "index.html"
    return ROOT / rel


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else "missing"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="alle URLs melden, nicht nur geaenderte")
    ap.add_argument("--dry-run", action="store_true", help="nichts senden, nur anzeigen")
    args = ap.parse_args()

    key = find_key()
    urls = sitemap_urls()
    base = site_base(urls)
    host = urlparse(base).netloc
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}
    current = {u: digest(local_file(u, base)) for u in urls}
    todo = urls if args.all else [u for u in urls if state.get(u) != current[u]]

    print(f"{len(urls)} URLs in der Sitemap, {len(todo)} zu melden ({host}).")
    if not todo:
        return
    if args.dry_run:
        print("\n".join(todo))
        return

    body = {"host": host, "key": key, "urlList": todo}
    if urlparse(base).path != "/":
        body["keyLocation"] = base + key + ".txt"
    req = urllib.request.Request(ENDPOINT, data=json.dumps(body).encode("utf-8"), method="POST",
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            status = r.status
    except urllib.error.HTTPError as err:
        status = err.code
    print(f"IndexNow antwortet {status}.")
    if status not in (200, 202):
        sys.exit("Nicht gemeldet. 403: Schluesseldatei noch nicht online? 422: URL passt nicht zum Host.")
    state.update({u: current[u] for u in todo})
    STATE.write_text(json.dumps(state, indent=1, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
