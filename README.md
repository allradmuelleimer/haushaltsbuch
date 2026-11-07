# Einfaches Haushaltsbuch — Website

Die öffentliche Datenschutzerklärung, die Google Play und AdMob verlangen, dazu Impressum und
eine kleine Startseite. Deutsch und englisch. Reines HTML und ein Stylesheet, kein Build-Schritt.

**Live:** <https://allradmuelleimer.github.io/haushaltsbuch/>

```
index.html              Startseite DE
datenschutz/            Datenschutzerklärung DE   <- diese URL geht zu Google Play und AdMob
impressum/              Impressum DE (§ 5 DDG)
privacy/                Privacy policy EN
privacy/es,fr,it,nl,pt/ Privacy policy in weiteren Sprachen (Stand gleich, Deutsch ist verbindlich)
imprint/                Imprint EN
404.html
css/site.css            Das einzige Stylesheet, Palette wie in der App (ui/theme/Theme.kt)
.nojekyll               Verhindert, dass GitHub Pages die Dateien durch Jekyll schickt
robots.txt              Crawlen erlaubt, keine Sitemap - alle Seiten tragen noindex
```

**Nicht indizieren:** Jede Seite trägt `<meta name="robots" content="noindex, nofollow">`. Die
Anschrift steht nur hinter einem Ausklapper (`<details class="anschrift">`).

**Pfade hängen am Repository-Namen** (`/haushaltsbuch/…`). Bei Umbenennung alle Verweise mitziehen.

**Ändert sich die App** (andere Daten, neue Dienste): `datenschutz/` und `privacy/` nachziehen
und oben das Datum hochsetzen. Gilt auch für die Angaben zur Datensicherheit in der Play Console.
