# Einfaches Haushaltsbuch — Website

Startseite und Anleitungen (deutsch und englisch, indexierbar), dazu die Datenschutzerklärung,
die Google Play und AdMob verlangen, und das Impressum (noindex).

**Live:** <https://allradmuelleimer.github.io/haushaltsbuch/>

## Erzeugt oder handgeschrieben?

Startseiten, Anleitungen, `sitemap.xml` und `robots.txt` **erzeugt** `tools/build.py` aus den
Texten in `tools/content_de.py` und `tools/content_en.py`. Diese HTML-Dateien nie direkt ändern:

```bash
python -I tools/build.py        # baut alles neu
python -I tools/check_site.py   # Links, JSON-LD, hreflang, Titel-/Beschreibungslänge
```

```
index.html, en/                  Startseite DE / EN                       (erzeugt, index)
anleitungen/<slug>/              7 Anleitungen DE                         (erzeugt, index)
en/guides/<slug>/                7 Anleitungen EN                         (erzeugt, index)
datenschutz/, privacy/…          Datenschutzerklärung, alle Sprachen      (Hand, noindex)
impressum/, imprint/             Impressum DE / EN                        (Hand, noindex)
404.html                                                                  (Hand, noindex)
css/site.css                     einziges Stylesheet, Palette aus ui/theme/Theme.kt
fonts/                           TeX Gyre Heros als woff2-Teilmenge (GUST-Lizenz liegt bei)
img/                             Bildschirmfotos aus store/build/roh (Demo-Daten), *-dark für den Dunkelmodus
```

**Datenschutz und Impressum bleiben noindex** – Name und Anschrift sollen nicht in
Suchmaschinen erscheinen. Die Anschrift steht nur hinter einem Ausklapper.

## Regeln für Texte

- Nur behaupten, was die App wirklich kann (Quellen: `../CLAUDE.md`, `../docs/`, Code,
  `../store/beschreibung-*.md`). Im Zweifel weglassen.
- Beispielbeträge sind erfunden. Nie Gideons echte Zahlen.
- Jede Anleitung muss ohne App nützlich sein; die App kommt am Ende als Werkzeug.
- Keine Rang- oder Superlativ-Aussagen („beste“, „einfachste“).
- Neue Anleitung: in beiden `content_*.py` mit derselben `id` anlegen, dann bauen – hreflang,
  Sitemap, Übersicht und „Weitere Anleitungen“ ergeben sich von selbst.

## Wenn die App öffentlich ist

In `tools/build.py` `PLAY_LIVE = True` setzen und neu bauen: Aus „Bald bei Google Play“ wird
überall ein Knopf zum Store, und das JSON-LD bekommt `installUrl` und `offers`.

## IndexNow (Bing, DuckDuckGo, Copilot, ChatGPT-Suche)

Nach jedem Push, sobald GitHub Pages fertig gebaut hat, einmal:

```bash
python tools/indexnow.py
```

Meldet nur neue und geänderte Seiten aus `sitemap.xml` und merkt sich den Stand in
`tools/indexnow_state.json` (mit committen). Schlüssel: `e8b62a185f203fd3d2982d02fef6f9af.txt` im
Wurzelordner. Weil die Seite unter `/haushaltsbuch/` liegt, schickt das Skript `keyLocation` mit.
Eingerichtet 21.11.2026.

## Search Console

GitHub Pages liefert `robots.txt` hier unter `/haushaltsbuch/robots.txt` aus; Suchmaschinen lesen
robots.txt aber nur an der Wurzel der Domain. Die Sitemap deshalb direkt in der Search Console
einreichen: `https://allradmuelleimer.github.io/haushaltsbuch/sitemap.xml`.

**Pfade hängen am Repository-Namen** (`/haushaltsbuch/…`, `BASE` in `build.py`). Bei Umbenennung
alles mitziehen.

**Ändert sich die App** (andere Daten, neue Dienste): `datenschutz/` und `privacy/` nachziehen,
oben das Datum hochsetzen, und die Anleitungstexte auf veraltete Aussagen prüfen.
