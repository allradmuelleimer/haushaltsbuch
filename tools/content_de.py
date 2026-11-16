"""Deutsche Texte. Anrede "du" wie in der App. Fakten nur aus der App (siehe build.py).
Beispielbetraege sind erfunden und gerundet - nie Gideons echte Zahlen.

Suchanfragen, auf die die Seiten zielen (Recherche 16.11.2026): Bei "Haushaltsbuch" allein
ranken Banken, Testportale und Excel-Vorlagen. Erreichbar sind genaue Fragen:
- wie viel darf ich pro Tag ausgeben / Tagesbudget berechnen
- Fixkosten Liste / was gehört zu Fixkosten / was bleibt nach Fixkosten übrig
- jährliche Kosten (Versicherung, Kfz-Steuer) im Monatsbudget einplanen
- Haushaltsbuch App ohne Bankverbindung / ohne Anmeldung / offline
- Budget ab Gehaltseingang / Gehalt kommt am 28. / Monatsbudget nicht ab dem 1.
- Geld übrig am Monatsende / Übertrag in den nächsten Monat
- Haushaltsbuch führen Tipps / durchhalten
"""

APP = "Einfaches Haushaltsbuch"

C = {
    "app_name": APP,
    "lang_name": "Deutsch",
    "og_locale": "de_DE",
    "ui": {
        "skip": "Zum Inhalt springen",
        "nav": "Hauptnavigation",
        "guides": "Anleitungen",
        "privacy": "Datenschutz",
        "imprint": "Impressum",
        "faq": "Häufige Fragen",
        "toc": "Inhalt",
        "crumbs": "Brotkrumen",
        "updated": "Stand:",
        "with_app": "Mit der App",
        "more_guides": "Weitere Anleitungen",
        "play_soon": "Bald bei Google Play – die App ist im letzten Test.",
        "play_cta": "Bei Google Play laden",
        "footer_tag": "Haushaltsbuch für Android, radikal einfach.",
        "trademark": "Google Play und Android sind Marken von Google LLC.",
    },

    # ------------------------------------------------------------ Startseite
    "home": {
        "title": "Einfaches Haushaltsbuch – Android-App ohne Bankverbindung und Anmeldung",
        "desc": "Betrag eintippen, speichern, fertig. Das Haushaltsbuch für Android zeigt, was nach den Fixkosten übrig ist – ohne Konto, ohne Bank, alles auf dem Telefon.",
        "kicker": "Haushaltsbuch-App für Android",
        "h1": "Haushaltsbuch, radikal einfach.",
        "lead": "Eine Ausgabe eintragen heißt: **Betrag eintippen, Speichern antippen.** Die App zeigt dir in einer großen Zahl, wie viel nach den Fixkosten in diesem Monat noch übrig ist. Kein Konto, keine Bankverbindung, keine Cloud.",
        "meter_label": "Verfügbar",
        "meter_num": "612",
        "meter_cents": ",40 €",
        "meter_note": "Der Balken zeigt, wie viel schon ausgegeben ist, der Strich, wie weit der Monat ist.",
        "meter_aria": "Beispiel: verfügbar 612,40 Euro. Der Balken ist zu 38 Prozent gefüllt, der Monat zur Hälfte vorbei.",
        "hero_shot": "de-start.webp",
        "shots": [
            ["de-start.webp", "Startbildschirm des Haushaltsbuchs: oben groß „Verfügbar 1.222,65 €“ mit Balken, darunter der eingetippte Betrag 4,20 €, Felder für Kategorie und Bezeichnung, Ziffernfeld und der grüne Knopf Speichern."],
            ["de-kassenzettel.webp", "Die Kamera liest einen Kassenzettel; die Summenzeile „SUMME EUR 22,42“ ist grün markiert."],
            ["de-verlauf.webp", "Verlauf im dunklen Modus: Ausgaben nach Tagen mit Bezeichnung, Kategorie und Betrag."],
            ["de-auswertung.webp", "Auswertung: Ausgegeben 380,55 €, Übrig 1.218,45 €, Pro Tag 31,71 € im Schnitt, darunter ein Tagesdiagramm und die Zusammensetzung aus Einnahmen und Fixkosten."],
        ],
        "features": [
            {"kicker": "Erfassen", "h2": "Eine Ausgabe in zwei Tipps",
             "body": ["Betrag eintippen, Speichern antippen – mehr ist nicht Pflicht. Kategorie, Bezeichnung, Datum und Notiz sind freiwillig und lassen sich auch später noch am Eintrag ergänzen.",
                      "Kurz nach dem Speichern erscheint **Rückgängig**, falls du dich vertippt hast. Vergessene Ausgaben trägst du im Verlauf mit Datum und Uhrzeit nach."],
             "shot": "de-verlauf.webp"},
            {"kicker": "Kassenzettel", "h2": "Vor die Kamera halten statt abtippen",
             "body": ["Tipp auf das Kamera-Symbol und halte den Kassenzettel ins Bild. Die App liest Summe, Geschäft, Datum und Uhrzeit und trägt sie ein.",
                      "Die Texterkennung läuft auf dem Telefon. Das Bild wird weder gespeichert noch irgendwohin geschickt."],
             "shot": "de-kassenzettel.webp"},
            {"kicker": "Fixkosten", "h2": "Einmal eintragen, dann vergessen",
             "body": ["Miete, Strom, Versicherungen, Abos: Bei der Einrichtung fragt die App Posten für Posten nach dem Betrag – was du nicht hast, lässt du leer. Jährliche Kosten wie die Haftpflichtversicherung bekommen ein Fälligkeitsdatum.",
                      "Danach zieht die App die Fixkosten jeden Monat selbst ab. Die große Zahl auf dem Startbildschirm ist das, was dir wirklich bleibt."],
             "shot": "meter"},
            {"kicker": "Auswertung", "h2": "Der ganze Monat in drei Zahlen",
             "body": ["Ausgegeben, übrig, pro Tag im Schnitt. Dazu ein Diagramm nach Tagen und darunter, wie sich dein Monat zusammensetzt: Einnahmen, Fixkosten, zum Ausgeben.",
                      "Keine Dashboards, keine zwölf Diagramme. Was übrig bleibt, kann auf Wunsch in den nächsten Monat wandern."],
             "shot": "de-auswertung.webp"},
        ],
        "nots_h2": "Deine Zahlen bleiben auf deinem Telefon",
        "nots_lead": "Alles, was du einträgst, liegt nur auf deinem Gerät. Es gibt keinen Server, auf dem deine Finanzen landen könnten.",
        "nots": [
            "**Kein Konto, keine Anmeldung** – App öffnen und loslegen.",
            "**Keine Bankverbindung** – du gibst nirgends Zugangsdaten ein.",
            "**Keine Cloud, keine Nutzungsstatistik, keine Absturzberichte.** Deshalb gibt es auch keine Synchronisierung zwischen Geräten.",
            "**Werbung ab dem siebten Tag:** ein Banner oben auf dem Startbildschirm. Die Werbung bekommt keine Zahl aus deinem Haushaltsbuch zu sehen. Ein einmaliger Kauf entfernt sie dauerhaft – ein Abo gibt es nicht.",
            "**Sieben Sprachen:** Deutsch, Englisch, Spanisch, Französisch, Italienisch, Niederländisch, Portugiesisch. Die Währung richtet sich nach deiner Region.",
        ],
        "privacy_link": "Datenschutzerklärung lesen",
        "guides_h2": "Anleitungen rund ums Monatsbudget",
        "guides_lead": "Auch ohne App nützlich: Tagesbudget ausrechnen, Fixkosten sammeln, jährliche Kosten einplanen.",
        "faq": [
            ["Was kostet die App?",
             ["Die App ist mit Werbung nutzbar. Ab dem siebten Tag zeigt sie einen Werbebanner oben auf dem Startbildschirm. Mit dem einmaligen Kauf „Werbung entfernen“ ist er dauerhaft weg; ein Abo gibt es nicht."]],
            ["Brauche ich ein Konto oder meine Bankdaten?",
             ["Nein. Es gibt weder Anmeldung noch Bankverbindung. Du trägst Einnahmen, Fixkosten und Ausgaben selbst ein, und alles bleibt auf deinem Telefon."]],
            ["Muss ich bei jeder Ausgabe eine Kategorie wählen?",
             ["Nein. Nur der Betrag ist Pflicht. Kategorie, Bezeichnung und Notiz sind freiwillig. Wenn du eine Bezeichnung tippst, schlägt die App eine passende Kategorie vor – gelernt aus deinen eigenen Einträgen, nur auf dem Gerät und abschaltbar."]],
            ["Kann ich die App auf zwei Handys gleichzeitig nutzen?",
             ["Nein. Weil es keine Cloud und keinen Server gibt, synchronisiert die App nichts zwischen Geräten. Das ist der Preis dafür, dass deine Zahlen dein Telefon nie verlassen."]],
            ["Was passiert mit dem Geld, das am Monatsende übrig ist?",
             ["Das entscheidest du in den Einstellungen: Mit „Plus mitnehmen“ wandert der Rest in den nächsten Monat, mit „Minus mitnehmen“ wird ein Fehlbetrag im nächsten Monat abgezogen. Beides lässt sich getrennt ein- und ausschalten. Mehr dazu: [Geld übrig am Monatsende](/anleitungen/rest-am-monatsende/)."]],
            ["Wann erscheint die App?",
             ["Die App ist im letzten geschlossenen Test und erscheint in Kürze bei Google Play für Android."]],
        ],
        "final_h2": "Wissen, was übrig ist. Ohne Aufwand.",
        "final_body": "Eine Zahl, ein Balken, zwei Tipps pro Ausgabe. Für Android.",
    },

    "guides_index": {
        "title": "Anleitungen: Monatsbudget, Fixkosten, Tagesbudget – Einfaches Haushaltsbuch",
        "desc": "Anleitungen fürs Haushaltsbuch: Tagesbudget berechnen, Fixkosten-Liste, jährliche Kosten einplanen, Budget ab Gehaltseingang – mit Rechenbeispielen.",
        "h1": "Anleitungen",
        "lead": "Kurze, praktische Antworten auf die Fragen, die beim Haushaltsbuch wirklich auftauchen. Jede Anleitung funktioniert auch mit Stift und Papier – die App macht es nur schneller.",
        "app": "Das **Einfache Haushaltsbuch** rechnet all das für dich: Fixkosten einmal eintragen, dann zeigt eine große Zahl, was in diesem Monat noch übrig ist.",
    },

    # ------------------------------------------------------------ Anleitungen
    "guides": [
        {
            "id": "daily",
            "slug": "wie-viel-darf-ich-pro-tag-ausgeben",
            "title": "Wie viel darf ich pro Tag ausgeben? Tagesbudget in 3 Schritten berechnen",
            "desc": "Tagesbudget berechnen: Einkommen minus Fixkosten und Sparrate, geteilt durch die Tage. Mit Beispiel, Formel für die Monatsmitte und Tempo-Probe.",
            "h1": "Wie viel darf ich pro Tag ausgeben?",
            "teaser": "Tagesbudget in drei Schritten – am Monatsanfang und mittendrin.",
            "answer": "**Nimm dein Netto-Einkommen, zieh Fixkosten und Sparrate ab und teile den Rest durch die Tage des Monats.** Bei 2.100 € Einkommen, 1.150 € Fixkosten und 100 € Sparrate bleiben 850 € – das sind in einem Monat mit 30 Tagen gut 28 € pro Tag. Mitten im Monat teilst du, was noch übrig ist, durch die verbleibenden Tage.",
            "updated": "2026-11-16",
            "updated_label": "November 2026",
            "sections": [
                ["schritte", "Das Tagesbudget in drei Schritten", [
                    {"steps": [
                        "**Einkommen feststellen.** Was im Monat netto auf dem Konto ankommt: Lohn oder Gehalt, dazu feste Einnahmen wie Kindergeld oder Unterhalt.",
                        "**Fixkosten und Sparrate abziehen.** Alles, was jeden Monat sicher abgeht: Miete, Strom, Versicherungen, Abos – und der Betrag, den du sparen willst. Eine vollständige Liste findest du unter [Fixkosten-Liste](/anleitungen/fixkosten-liste/).",
                        "**Durch die Tage teilen.** Den Rest durch die Anzahl der Tage im Monat (28 bis 31).",
                    ]},
                    {"formula": "Tagesbudget = (Einkommen − Fixkosten − Sparrate) ÷ Tage im Monat"},
                    {"calc": [["Netto-Einkommen", "2.100,00 €"], ["− Fixkosten", "1.150,00 €"], ["− Sparrate", "100,00 €"],
                              ["= frei für den Monat", "850,00 €"], ["÷ 30 Tage", ""], ["**Tagesbudget**", "28,33 €"]],
                     "caption": "Beispiel mit erfundenen Zahlen"},
                    "Diese 850 € sind dein Geld für alles Veränderliche: Lebensmittel, Drogerie, Essen gehen, Kleidung, Geschenke, kleine Reparaturen.",
                ]],
                ["mittendrin", "Mitten im Monat: Rest durch verbleibende Tage", [
                    "Am Monatsanfang ist die Rechnung leicht. Spannender ist die Frage am 18.: Reicht es noch? Dann rechnest du mit dem, was **noch** da ist, und den Tagen, die **noch** kommen – heute mitgezählt.",
                    {"formula": "Tagesbudget ab heute = noch verfügbar ÷ verbleibende Tage"},
                    {"calc": [["Noch verfügbar am 18.", "410,00 €"], ["Verbleibende Tage (18. bis 30.)", "13"], ["**Ab heute pro Tag**", "31,54 €"]],
                     "caption": "Beispiel: Monat mit 30 Tagen"},
                    "Liegt der neue Wert über deinem ursprünglichen Tagesbudget, bist du gut unterwegs. Liegt er darunter, weißt du es jetzt – und nicht erst am 29.",
                ]],
                ["kein-limit", "Warum das Tagesbudget kein Tageslimit ist", [
                    "Kaum jemand gibt jeden Tag gleich viel aus. Ein Wocheneinkauf kostet 60 €, dann kommen drei Tage ohne Ausgaben. Das Tagesbudget ist deshalb ein **Durchschnitt**, kein Verbot. Wer es als harte Grenze nimmt, fühlt sich am Einkaufstag als Versager und gibt auf.",
                    "Besser ist ein Blick aufs Tempo: Gibst du schneller aus, als der Monat vergeht?",
                ]],
                ["tempo", "Die Tempo-Probe: Prozent ausgegeben gegen Prozent Monat", [
                    "Vergleiche zwei Prozentzahlen:",
                    {"list": [
                        "**Wie viel vom Monat ist vorbei?** Am 12. eines 30-Tage-Monats sind es 40 %.",
                        "**Wie viel vom frei verfügbaren Geld ist ausgegeben?** 340 € von 850 € sind 40 %.",
                    ]},
                    {"table": [
                        ["Ausgegeben im Vergleich zum Monat", "Bedeutung"],
                        ["weniger als vergangen", "Du liegst im Plan, es bleibt Luft."],
                        ["etwa gleich", "Genau im Tempo – so geht es auf."],
                        ["deutlich mehr als vergangen", "Zu schnell. Ein paar ruhige Tage gleichen das aus."],
                    ]},
                    "Diese Probe verzeiht den großen Wocheneinkauf, solange der Rest der Woche ruhig bleibt – und sie warnt trotzdem früh genug.",
                ]],
                ["fallstricke", "Drei Dinge, die die Rechnung verfälschen", [
                    {"list": [
                        "**Jährliche Kosten vergessen.** Kfz-Versicherung oder Haftpflicht kommen einmal im Jahr und reißen dann ein Loch. So planst du sie ein: [Jährliche Kosten im Monatsbudget](/anleitungen/jaehrliche-kosten-im-budget/).",
                        "**Gehalt kommt nicht am 1.** Dann passt der Kalendermonat nicht zu deinem Geld. Lösung: [Budget ab Gehaltseingang](/anleitungen/budget-ab-gehaltseingang/).",
                        "**Ausgaben nur im Kopf.** Wer nicht aufschreibt, schätzt fast immer zu niedrig. Schon der Betrag allein reicht – ohne Kategorie.",
                    ]},
                ]],
            ],
            "app": {
                "h2": "Das Einfache Haushaltsbuch rechnet mit",
                "body": [
                    "Du trägst Einkommen und Fixkosten einmal ein. Danach zeigt der Startbildschirm groß, was in diesem Monat noch **verfügbar** ist – jede gespeicherte Ausgabe zieht die App sofort ab.",
                    "Der **Balken** darunter ist genau die Tempo-Probe: Die Füllung zeigt, wie viel ausgegeben ist, ein Strich, wie weit der Monat ist. Läuft die Füllung über den Strich hinaus, färbt sie sich als Vorwarnung um. In der Auswertung steht zusätzlich, wie viel du bisher **pro Tag im Schnitt** ausgegeben hast.",
                ],
                "shot": "de-start.webp",
                "alt": "Startbildschirm: Verfügbar 1.222,65 € mit Balken und Zeitstrich.",
            },
            "faq": [
                ["Soll ich die Sparrate vorher abziehen?",
                 ["Ja. Was du sparen willst, behandelst du wie eine Fixkostenposition und ziehst es am Monatsanfang ab. Was am Ende übrig bleibt, ist dann ein Bonus – nicht deine einzige Sparquelle."]],
                ["Zählen Lebensmittel zu den Fixkosten?",
                 ["Nein. Lebensmittel schwanken von Woche zu Woche und gehören in das Tagesbudget. Fixkosten sind Beträge, die jeden Monat gleich oder fast gleich abgehen."]],
                ["Was ist ein realistisches Tagesbudget?",
                 ["Das hängt ganz von Einkommen und Fixkosten ab – eine allgemeine Zahl gibt es nicht. Wichtiger als die Höhe ist, dass du sie kennst und mitten im Monat nachrechnest."]],
                ["Wie rechne ich in einem Monat mit 31 Tagen?",
                 ["Genauso, nur durch 31 teilen. Bei 850 € sind das 27,42 € statt 28,33 € pro Tag. Im Februar sind es mehr pro Tag, weil derselbe Betrag auf weniger Tage verteilt wird."]],
            ],
        },
        {
            "id": "fixed",
            "slug": "fixkosten-liste",
            "title": "Fixkosten-Liste: Was gehört dazu – und was bleibt danach übrig?",
            "desc": "Fixkosten-Liste für den Privathaushalt: monatliche und jährliche Posten, wo du die Beträge findest und wie du ausrechnest, was danach übrig bleibt.",
            "h1": "Fixkosten-Liste: Was gehört dazu – und was bleibt übrig?",
            "teaser": "Checkliste mit allen typischen Posten und der Rechnung, was danach bleibt.",
            "answer": "**Fixkosten sind Ausgaben, die regelmäßig in fester Höhe abgehen** – Miete, Strom, Versicherungen, Verträge, Abos. Zieh ihre Summe von deinem Netto-Einkommen ab, dann weißt du, wie viel dir für alles andere bleibt. Die Liste unten hilft, keinen Posten zu vergessen.",
            "updated": "2026-11-16",
            "updated_label": "November 2026",
            "sections": [
                ["definition", "Fixkosten oder variable Kosten?", [
                    "Eine einfache Probe: **Geht der Betrag auch ab, wenn du diesen Monat gar nichts unternimmst?** Dann ist es Fixkosten. Miete, Handyvertrag und Versicherung laufen weiter, ob du ausgehst oder nicht. Lebensmittel, Essen gehen, Kleidung und Tanken hängen davon ab, was du tust – das sind variable Kosten.",
                    {"note": "Auch die **Sparrate** gehört in die Liste. Wer sie wie eine feste Rechnung behandelt, spart, bevor das Geld verplant ist."},
                ]],
                ["monatlich", "Checkliste: monatliche Fixkosten", [
                    {"table": [
                        ["Bereich", "Typische Posten"],
                        ["Wohnen", "Miete oder Kreditrate, Nebenkosten, Heizkosten, Strom (Wasser steckt bei Mietern meist in den Nebenkosten)"],
                        ["Kommunikation", "Internet, Festnetz, Mobilfunk, Rundfunkbeitrag"],
                        ["Mobilität", "ÖPNV-Abo, Kfz-Rate oder Leasing"],
                        ["Versicherungen", "Krankenversicherung (wenn nicht vom Lohn abgezogen), Zusatz-Krankenversicherung, Berufsunfähigkeit, weitere"],
                        ["Sparen", "Sparkonto, ETF-Sparplan"],
                        ["Abos und Mitgliedschaften", "Musik- und Video-Streaming, Fitnessstudio, Zeitung, Software- und KI-Abos, Musikschule, Vereine"],
                    ]},
                ]],
                ["jaehrlich", "Checkliste: jährliche und vierteljährliche Fixkosten", [
                    "Diese Posten werden am häufigsten vergessen, weil sie selten kommen:",
                    {"list": [
                        "Haftpflicht-, Hausrat- und Rechtsschutzversicherung",
                        "Kfz-Versicherung und Kfz-Steuer, Automobilclub",
                        "Jahresgebühr für Kreditkarte oder Bankkarte",
                        "Vereinsbeiträge, die jährlich abgebucht werden",
                        "Jahresabos (Streaming, Versand-Mitgliedschaften, Domain, Software)",
                        "Rundfunkbeitrag, wenn du ihn vierteljährlich zahlst",
                    ]},
                    "Wie du sie einplanst, ohne dass ein Monat plötzlich leer ist: [Jährliche Kosten im Monatsbudget](/anleitungen/jaehrliche-kosten-im-budget/).",
                ]],
                ["finden", "Wo du die Beträge findest", [
                    {"steps": [
                        "**Kontoauszüge der letzten drei Monate** durchgehen: Daueraufträge und Lastschriften, die jeden Monat gleich auftauchen, sind deine monatlichen Fixkosten.",
                        "**Die letzten zwölf Monate** nach Beträgen durchsuchen, die nur einmal oder viermal auftauchen – das sind die jährlichen und vierteljährlichen.",
                        "**Verträge und Bescheide** prüfen: Versicherungsschein, Kfz-Steuerbescheid und Mietvertrag nennen Betrag und Fälligkeit.",
                    ]},
                ]],
                ["rest", "Was nach den Fixkosten übrig bleibt", [
                    {"calc": [["Netto-Einkommen", "2.100,00 €"], ["− Miete und Nebenkosten", "780,00 €"], ["− Strom, Internet, Handy", "105,00 €"],
                              ["− Versicherungen", "65,00 €"], ["− Abos und Verein", "40,00 €"], ["− ÖPNV-Abo", "58,00 €"], ["− Sparrate", "100,00 €"],
                              ["**Bleibt zum Ausgeben**", "952,00 €"]],
                     "caption": "Beispiel mit erfundenen Zahlen"},
                    "Diese Zahl ist die wichtigste in deinem Haushaltsbuch. Teilst du sie durch die Tage des Monats, hast du dein [Tagesbudget](/anleitungen/wie-viel-darf-ich-pro-tag-ausgeben/).",
                    "Sind die Fixkosten so hoch, dass kaum etwas bleibt, lohnt der Blick auf Abos und Verträge zuerst – sie lassen sich am leichtesten kündigen oder wechseln.",
                ]],
            ],
            "app": {
                "h2": "Fixkosten einmal eintragen, dann vergessen",
                "body": [
                    "Die Einrichtung des Einfachen Haushaltsbuchs geht diese Liste mit dir durch: Posten für Posten – Miete, Heizkosten, Strom, Nebenkosten, Internet und so weiter – tippst du den Betrag ein oder lässt das Feld leer, wenn du den Posten nicht hast. Über das Plus kommen weitere dazu, mit Vorschlägen wie Streaming, Fitnessstudio oder Kfz-Versicherung.",
                    "Jährliche Posten bekommen ein Fälligkeitsdatum. Danach zieht die App die Fixkosten jeden Monat selbst ab, und der Startbildschirm zeigt nur noch, was dir wirklich bleibt.",
                ],
                "shot": "de-auswertung.webp",
                "alt": "Auswertung mit der Zusammensetzung: Einnahmen 2.600,00 €, Fixkosten −1.001,00 €, zum Ausgeben 1.599,00 €.",
            },
            "faq": [
                ["Ist die Sparrate Fixkosten?",
                 ["Im Haushaltsbuch: ja. Wer sie wie eine feste Rechnung zu Monatsbeginn abzieht, spart verlässlich. Was am Ende zusätzlich übrig bleibt, ist ein Bonus."]],
                ["Gehören Lebensmittel zu den Fixkosten?",
                 ["Nein, auch wenn sie jeden Monat anfallen. Ihr Betrag schwankt und hängt von dir ab. Sie gehören zu den variablen Ausgaben."]],
                ["Wie viel Prozent des Einkommens dürfen Fixkosten sein?",
                 ["Eine feste Grenze gibt es nicht. Entscheidend ist, dass nach den Fixkosten genug für Essen, Alltag und Unvorhergesehenes bleibt. Rechne es mit deinen eigenen Zahlen aus – die Tabelle oben zeigt wie."]],
                ["Was ist mit Kosten, die sich leicht ändern, wie Strom?",
                 ["Nimm den aktuellen Abschlag. Ändert er sich, passt du den Betrag an. Im Haushaltsbuch zählt, dass der Posten überhaupt drinsteht."]],
            ],
        },
        {
            "id": "yearly",
            "slug": "jaehrliche-kosten-im-budget",
            "title": "Jährliche Kosten im Monatsbudget einplanen: Versicherung, Kfz-Steuer & Co.",
            "desc": "Jährliche Kosten wie Haftpflicht, Kfz-Versicherung oder Kfz-Steuer im Monatsbudget: durch zwölf teilen und zurücklegen oder im Fälligkeitsmonat reservieren.",
            "h1": "Jährliche Kosten im Monatsbudget einplanen",
            "teaser": "Haftpflicht, Kfz-Steuer & Co.: zwei Methoden, damit kein Monat plötzlich leer ist.",
            "answer": "Für jährliche Kosten gibt es zwei saubere Wege: **Entweder du teilst den Jahresbetrag durch zwölf und legst ihn jeden Monat zurück, oder du reservierst ihn komplett im Monat der Fälligkeit** – dann aber ab dem ersten Tag dieses Monats, nicht erst bei der Abbuchung. Falsch ist nur, ihn zu vergessen.",
            "updated": "2026-11-16",
            "updated_label": "November 2026",
            "sections": [
                ["problem", "Warum jährliche Kosten das Budget sprengen", [
                    "Im Januar kommen Kfz-Versicherung und Haftpflicht, im Mai die Kfz-Steuer, im Herbst die Jahresgebühr der Kreditkarte. Jeder Betrag für sich ist überschaubar. Aber er trifft einen Monat, in dem du nicht mit ihm gerechnet hast – und dann fehlt das Geld für den Alltag.",
                ]],
                ["methoden", "Zwei Methoden im Vergleich", [
                    {"table": [
                        ["", "Durch zwölf teilen", "Im Fälligkeitsmonat reservieren"],
                        ["So geht’s", "Jahresbetrag ÷ 12 jeden Monat beiseitelegen, am besten auf ein eigenes Konto", "Den vollen Betrag im Monat der Abbuchung einplanen, vom ersten Tag an"],
                        ["Vorteil", "Jeder Monat ist gleich, keine Spitzen", "Kein zweites Konto, kein Hin- und Herbuchen"],
                        ["Nachteil", "Braucht Disziplin und meist ein Rücklagenkonto", "Der Fälligkeitsmonat ist spürbar knapper"],
                        ["Passt, wenn …", "viele oder große Jahresposten zusammenkommen", "es wenige Posten sind und du die Monate kennst"],
                    ]},
                    {"calc": [["Haftpflicht", "60,00 €"], ["Hausrat", "84,00 €"], ["Kfz-Versicherung", "420,00 €"], ["Kfz-Steuer", "96,00 €"],
                              ["Summe im Jahr", "660,00 €"], ["**÷ 12 = monatlich zurücklegen**", "55,00 €"]],
                     "caption": "Beispiel mit erfundenen Zahlen"},
                ]],
                ["kalender", "Erst den Kalender, dann die Methode", [
                    {"steps": [
                        "**Alle Jahresposten sammeln** – die Liste unter [Fixkosten-Liste](/anleitungen/fixkosten-liste/) hilft.",
                        "**Zu jedem Posten den Monat notieren.** Er steht im Versicherungsschein, im Steuerbescheid oder in den Kontoauszügen des Vorjahres.",
                        "**Monate mit mehreren Posten markieren.** Häufen sich zwei, drei Beträge in einem Monat, ist Durch-zwölf-Teilen meist entspannter.",
                        "**Vierteljährliche Posten** genauso behandeln: entweder ÷ 3 jeden Monat oder voll in den vier Fälligkeitsmonaten.",
                    ]},
                ]],
                ["warum-ab-erstem", "Warum ab dem ersten Tag des Monats?", [
                    "Wird die Versicherung am 20. abgebucht, sieht dein Konto bis zum 19. besser aus, als es ist. Wer das Geld bis dahin ausgibt, fehlt am 20. Deshalb gehört der Betrag **vom Monatsanfang an** aus dem verfügbaren Geld heraus – egal, wann er tatsächlich abgeht.",
                ]],
            ],
            "app": {
                "h2": "Jährliche Fixkosten mit Fälligkeitsdatum",
                "body": [
                    "Im Einfachen Haushaltsbuch fragt schon die Einrichtung nach jährlichen Posten wie Haftpflichtversicherung, Kreditkarte und Bankkarte – jeweils mit dem Datum der Fälligkeit. Weitere, etwa Kfz-Versicherung, Kfz-Steuer oder Hausrat, kommen über das Plus dazu. Fixkosten können monatlich, vierteljährlich, jährlich oder einmalig sein.",
                    "Die App reserviert den Betrag nur in dem Monat, in dem er fällig ist – und dort vom ersten Tag an. Wer lieber durch zwölf teilt, trägt stattdessen einen monatlichen Posten „Rücklage“ ein.",
                ],
            },
            "faq": [
                ["Muss ich für die Rücklage ein eigenes Konto haben?",
                 ["Nicht unbedingt, aber es hilft. Liegt das Geld auf dem Girokonto, sieht es aus wie verfügbares Geld und wird leicht ausgegeben. Ein Tagesgeld- oder Unterkonto trennt es sichtbar."]],
                ["Was mache ich mit Nachzahlungen, etwa bei den Nebenkosten?",
                 ["Eine Nachzahlung kommt einmal und in unbekannter Höhe. Wer sie fürchtet, legt monatlich einen kleinen Betrag zurück. Kommt sie, zieht man sie von der Rücklage ab, nicht vom laufenden Monat."]],
                ["Lohnt sich jährliche Zahlung statt monatlicher?",
                 ["Manche Versicherungen sind bei jährlicher Zahlung günstiger. Dann lohnt es sich – vorausgesetzt, du planst den Betrag wie oben beschrieben ein."]],
            ],
        },
        {
            "id": "nobank",
            "slug": "haushaltsbuch-app-ohne-bankverbindung",
            "title": "Haushaltsbuch-App ohne Bankverbindung und ohne Anmeldung: worauf achten",
            "desc": "Haushaltsbuch-App ohne Bankverbindung und ohne Konto: was du gewinnst, was du in Kauf nimmst und wie du im Play Store prüfst, wo deine Daten landen.",
            "h1": "Haushaltsbuch-App ohne Bankverbindung und ohne Anmeldung",
            "teaser": "Was du gewinnst, was du in Kauf nimmst und wie du eine App vor der Installation prüfst.",
            "answer": "Eine Haushaltsbuch-App ohne Bankverbindung und ohne Anmeldung speichert alles nur auf deinem Telefon. Dafür trägst du Ausgaben selbst ein, und es gibt keine Synchronisierung zwischen Geräten. **Ob eine App das wirklich hält, siehst du im Play Store unter „Datensicherheit“** – und daran, ob sie beim ersten Start ein Konto verlangt.",
            "updated": "2026-11-16",
            "updated_label": "November 2026",
            "sections": [
                ["warum", "Warum ohne Bankverbindung?", [
                    "Apps mit Kontoanbindung lesen deine Umsätze automatisch ein. Bequem – aber du gibst dafür Zugangsdaten an einen Dienst weiter, und deine Kontobewegungen liegen auf fremden Servern. Viele wollen das für ein Haushaltsbuch nicht.",
                    "Es gibt noch einen zweiten Grund: **Wer selbst einträgt, merkt, was er ausgibt.** Der automatische Import erklärt dir am Monatsende, wohin das Geld gegangen ist. Das eigene Eintippen sagt es dir in dem Moment, in dem du bezahlst.",
                ]],
                ["kompromiss", "Was du dafür in Kauf nimmst", [
                    {"table": [
                        ["", "Mit Bankverbindung", "Ohne Bankverbindung"],
                        ["Ausgaben erfassen", "automatisch, mit Verzögerung", "selbst eintragen, sofort"],
                        ["Bargeld", "fehlt meist", "trägst du genauso ein"],
                        ["Zugangsdaten", "gehen an den Dienst", "bleiben bei dir"],
                        ["Daten", "liegen auf Servern", "bleiben auf dem Telefon"],
                        ["Mehrere Geräte", "meist möglich", "meist nicht"],
                    ]},
                    "Der Aufwand hängt fast nur davon ab, wie viele Felder eine App pro Ausgabe verlangt. Muss man jedes Mal Kategorie, Konto und Datum wählen, gibt man nach zwei Wochen auf. Ist nur der Betrag Pflicht, dauert ein Eintrag wenige Sekunden.",
                ]],
                ["pruefen", "So prüfst du eine App vor der Installation", [
                    {"steps": [
                        "**Abschnitt „Datensicherheit“ im Play Store öffnen.** Dort steht, welche Daten die App erhebt und ob sie sie weitergibt. Achte auf „Finanzinformationen“.",
                        "**Nach Konto oder Anmeldung suchen.** Steht in der Beschreibung „Registrierung“, „Login“ oder „Cloud-Sync“, liegen deine Daten nicht nur auf dem Telefon.",
                        "**Werbung beachten.** Werbefinanzierte Apps binden ein Werbenetzwerk ein. Entscheidend ist, ob die Werbung etwas von deinen Einträgen erfährt – das sollte die Datenschutzerklärung klar beantworten.",
                        "**Datenschutzerklärung lesen.** Eine gute sagt in wenigen Sätzen, was das Gerät verlässt und was nicht.",
                    ]},
                ]],
                ["alltag", "Damit Selbst-Eintragen nicht nervt", [
                    {"list": [
                        "**Sofort eintragen**, direkt an der Kasse – dann sind es zehn Sekunden statt einer Stunde am Sonntag.",
                        "**Nur den Betrag** ist Pflicht. Kategorie und Bezeichnung höchstens, wenn sie dir etwas sagen.",
                        "**Vergessenes nachtragen**, statt das Haushaltsbuch abzuschreiben. Ein fehlender Kaffee verfälscht nichts.",
                    ]},
                    "Mehr dazu: [Haushaltsbuch führen und durchhalten](/anleitungen/haushaltsbuch-fuehren-tipps/).",
                ]],
            ],
            "app": {
                "h2": "So hält es das Einfache Haushaltsbuch",
                "body": [
                    {"list": [
                        "**Kein Konto, keine Anmeldung, keine Bankverbindung.** Einnahmen, Fixkosten, Ausgaben und Einstellungen liegen nur auf deinem Telefon.",
                        "**Keine Cloud, keine Nutzungsstatistik, keine Absturzberichte** – und deshalb auch keine Synchronisierung zwischen Geräten.",
                        "**Kassenzettel-Scan auf dem Gerät:** Die Texterkennung läuft auf dem Telefon, das Bild wird weder gespeichert noch verschickt.",
                        "**Werbung:** ab dem siebten Tag ein Banner von Google, der keine Zahl aus deinem Haushaltsbuch sieht. Ein einmaliger Kauf entfernt ihn.",
                    ]},
                    "Alles im Detail: [Datenschutzerklärung](/datenschutz/).",
                ],
                "shot": "de-verlauf.webp",
                "alt": "Verlauf im dunklen Modus mit den Ausgaben nach Tagen.",
            },
            "faq": [
                ["Ist eine Haushaltsbuch-App ohne Bankverbindung sicherer?",
                 ["Sie gibt weniger aus der Hand: keine Zugangsdaten, keine Umsätze auf fremden Servern. Dein Telefon selbst solltest du trotzdem mit Displaysperre schützen."]],
                ["Was passiert mit meinen Daten, wenn ich das Handy wechsle?",
                 ["Bei einer App ohne Cloud wandern die Daten nicht automatisch mit. Prüfe vor dem Wechsel, ob die App eine Sicherung oder einen Export anbietet, oder fang im neuen Monat frisch an."]],
                ["Funktioniert so eine App ohne Internet?",
                 ["Das Haushaltsbuch selbst braucht kein Internet. Bei werbefinanzierten Apps lädt nur der Werbebanner etwas aus dem Netz."]],
            ],
        },
        {
            "id": "payday",
            "slug": "budget-ab-gehaltseingang",
            "title": "Monatsbudget ab Gehaltseingang: wenn das Gehalt nicht am 1. kommt",
            "desc": "Gehalt kommt am 15. oder am 28.? So legst du deinen Budgetmonat auf den Zahltag, was bei kurzen Monaten passiert und wann es besser ist, trotzdem am 1. zu beginnen.",
            "h1": "Monatsbudget ab Gehaltseingang",
            "teaser": "Wenn das Gehalt am 15. oder 28. kommt: den Budgetmonat auf den Zahltag legen.",
            "answer": "Kommt dein Gehalt nicht am 1., **lass deinen Budgetmonat am Zahltag beginnen** – etwa vom 15. bis zum 14. des Folgemonats. Dann gehört jedes Gehalt genau zu einem Budgetmonat. Kommt es am 28. oder später, ist die Alternative oft einfacher: Behandle es als Geld für den nächsten Monat und beginne trotzdem am 1.",
            "updated": "2026-11-16",
            "updated_label": "November 2026",
            "sections": [
                ["problem", "Das Problem mit dem Kalendermonat", [
                    "Wer am 15. Gehalt bekommt, hat am 1. die Hälfte des Geldes schon ausgegeben – und rechnet trotzdem mit einem frischen Monat. Die Zahlen passen nie zusammen: Im ersten Halbmonat ist scheinbar zu viel übrig, im zweiten zu wenig.",
                ]],
                ["zahltag", "Weg 1: Budgetmonat beginnt am Zahltag", [
                    {"steps": [
                        "**Den Tag nehmen, an dem das Gehalt meistens da ist**, zum Beispiel den 15.",
                        "**Fixkosten diesem Zeitraum zuordnen.** Die Miete vom 1. fällt dann in den Budgetmonat, der am 15. des Vormonats begann.",
                        "**Tagesbudget mit den echten Tagen rechnen.** Vom 15. Januar bis 14. Februar sind es 31 Tage, vom 15. Februar bis 14. März je nach Jahr 28 oder 29.",
                    ]},
                    {"note": "Kommt das Geld mal einen Tag früher oder später, ändert das am Plan nichts. Wichtig ist ein fester Stichtag, nicht der genaue Eingang."},
                ]],
                ["kurz", "Zahltag am 29., 30. oder 31.?", [
                    "Nicht jeder Monat hat diese Tage. Dann gilt sinnvollerweise **der Monatsletzte**: Wer am 31. Gehalt bekommt, beginnt im Februar am 28. (oder 29.), im April am 30.",
                ]],
                ["vorschuessig", "Weg 2: Gehalt vom 28. als Geld für den nächsten Monat", [
                    "Kommt das Gehalt kurz vor Monatsende, lassen viele den Budgetmonat trotzdem am 1. beginnen. Das Geld vom 28. wird nicht angerührt – es ist das Budget für den kommenden Monat.",
                    {"table": [
                        ["", "Budget ab Zahltag", "Budget ab dem 1."],
                        ["Passt gut bei", "Gehalt zur Monatsmitte", "Gehalt in den letzten Tagen des Monats"],
                        ["Vorteil", "Jeder Zeitraum hat genau ein Gehalt", "Rechnungen und Abos ordnen sich nach Kalendermonaten"],
                        ["Braucht", "Umdenken bei Monatsnamen", "ein paar Tage Polster, bis das Gehalt kommt"],
                    ]},
                    "Der zweite Weg braucht einmalig einen Puffer: Beim ersten Mal muss das Gehalt vom 28. ja bis zum Ende des nächsten Monats reichen.",
                ]],
            ],
            "app": {
                "h2": "Budgetbeginn frei wählen",
                "body": [
                    "Im Einfachen Haushaltsbuch stellst du unter **Einstellungen → Budget beginnt** einen Tag zwischen dem 1. und dem 31. ein. Bei 29 bis 31 nimmt die App in kürzeren Monaten den Monatsletzten. Die Änderung gilt ab dem nächsten Zeitraum, damit der laufende nicht durcheinandergerät.",
                    "Einnahmen haben einen eigenen Termin („Kommt am“). Die App zählt ein Gehalt erst ab dem Tag, an dem es kommt – vorher kann die große Zahl niedriger sein oder ins Minus gehen. Rot wird der Balken davon nicht; das passiert nur, wenn du wirklich mehr ausgibst, als der Monat hergibt.",
                ],
            },
            "faq": [
                ["Was ist mit Fixkosten, die am 1. abgehen?",
                 ["Sie gehören in den Budgetmonat, in dem der 1. liegt. Beginnt dein Zeitraum am 15., ist die Miete vom 1. also eine Ausgabe des Zeitraums, der am 15. des Vormonats begonnen hat – du bezahlst sie mit dem Gehalt, das davor kam."]],
                ["Ich bekomme zweimal im Monat Geld. Was dann?",
                 ["Nimm den Tag der größeren Zahlung als Beginn und plane die zweite als weitere Einnahme im selben Zeitraum ein."]],
                ["Wie stelle ich um, ohne dass ein Monat doppelt zählt?",
                 ["Am einfachsten zum nächsten Zahltag: Der laufende Zeitraum endet am Tag davor, ab dem Zahltag beginnt der neue. Ein einmalig kürzerer oder längerer Übergangszeitraum ist normal."]],
            ],
        },
        {
            "id": "leftover",
            "slug": "rest-am-monatsende",
            "title": "Geld übrig am Monatsende – oder zu wenig? Übertrag oder Neustart",
            "desc": "Was tun mit dem Rest am Monatsende? Übertrag in den nächsten Monat, sparen oder Neustart – und was passiert, wenn du überzogen hast. Mit Entscheidungshilfe.",
            "h1": "Geld übrig am Monatsende – oder zu wenig?",
            "teaser": "Übertrag, Sparen oder Neustart: was mit dem Rest passiert und was bei einem Minus hilft.",
            "answer": "Bleibt am Monatsende etwas übrig, kannst du es **in den nächsten Monat mitnehmen, sparen oder den neuen Monat bei null beginnen.** Ein Minus solltest du dagegen fast immer mitnehmen – sonst rechnet dein Haushaltsbuch mit Geld, das es nicht gibt.",
            "updated": "2026-11-16",
            "updated_label": "November 2026",
            "sections": [
                ["plus", "Wenn etwas übrig ist: drei Möglichkeiten", [
                    {"table": [
                        ["Möglichkeit", "Was passiert", "Gut, wenn …"],
                        ["Mitnehmen (Übertrag)", "Der Rest erhöht das Budget im nächsten Monat", "teure Monate (Urlaub, Geschenke) bevorstehen"],
                        ["Sparen", "Der Rest geht aufs Sparkonto, der neue Monat startet normal", "du ein Sparziel hast"],
                        ["Neustart", "Jeder Monat beginnt mit demselben Betrag", "du jeden Monat für sich betrachten willst"],
                    ]},
                    "Mitnehmen ist bequem, hat aber einen Haken: Ein dickes Polster lädt zum Ausgeben ein. Wer sparen will, überweist den Rest besser bewusst und startet frisch.",
                ]],
                ["minus", "Wenn es nicht gereicht hat", [
                    "Ein Minus am Monatsende heißt meist: Der Dispo oder das Ersparte hat ausgeholfen. Fängt der neue Monat trotzdem bei vollem Budget an, fehlt das Geld unsichtbar weiter.",
                    {"steps": [
                        "**Minus mitnehmen:** Der Fehlbetrag wird im nächsten Monat abgezogen. Unangenehm, aber ehrlich.",
                        "**Ursache suchen:** War es ein Ausreißer (Reparatur, Geschenk) oder läuft es jeden Monat so? Ein Blick in den Verlauf zeigt es.",
                        "**Bei wiederholtem Minus die Fixkosten prüfen** – dort steckt meist das größte Potenzial. Die [Fixkosten-Liste](/anleitungen/fixkosten-liste/) hilft beim Durchgehen.",
                    ]},
                ]],
                ["frueh", "Besser: es vor dem Monatsende merken", [
                    "Ob es reicht, siehst du nicht erst am 30. Vergleiche mitten im Monat, wie viel vom Geld ausgegeben ist und wie viel vom Monat vorbei ist. Wie das geht: [Wie viel darf ich pro Tag ausgeben?](/anleitungen/wie-viel-darf-ich-pro-tag-ausgeben/#tempo)",
                ]],
            ],
            "app": {
                "h2": "Plus und Minus getrennt einstellen",
                "body": [
                    "Im Einfachen Haushaltsbuch gibt es in den Einstellungen zwei Schalter: **Plus mitnehmen** – der Rest wandert in den nächsten Zeitraum – und **Minus mitnehmen** – ein Fehlbetrag wird im nächsten Zeitraum abgezogen. Du kannst beide, einen oder keinen einschalten. Änderungen gelten ab dem nächsten Zeitraum.",
                    "Rot zeigt die App nur bei echter Überziehung, also wenn du mehr ausgegeben hast, als der Monat hergibt. Läufst du dem Monat nur voraus, färbt sich der Balken jenseits des Zeitstrichs als Vorwarnung um.",
                ],
                "shot": "de-auswertung.webp",
                "alt": "Auswertung mit Ausgegeben, Übrig und Pro Tag.",
            },
            "faq": [
                ["Ist es schlimm, wenn ich einen Monat überziehe?",
                 ["Ein einzelner Monat mit Reparatur oder Geburtstagen ist normal. Wichtig ist, das Minus mitzunehmen oder bewusst aus dem Ersparten auszugleichen – und zu sehen, ob es ein Ausreißer war."]],
                ["Soll ich den Rest lieber sparen oder mitnehmen?",
                 ["Wenn du ein Sparziel hast: sparen. Wenn teure Monate kommen: mitnehmen. Beides ist besser, als den Rest unbemerkt im nächsten Monat zu verbrauchen."]],
            ],
        },
        {
            "id": "habit",
            "slug": "haushaltsbuch-fuehren-tipps",
            "title": "Haushaltsbuch führen und durchhalten: 7 Tipps, die wirklich helfen",
            "desc": "Warum die meisten ihr Haushaltsbuch nach zwei Wochen aufgeben – und 7 Tipps, wie es klappt: nur den Betrag, sofort eintragen, Fixkosten einmal.",
            "h1": "Haushaltsbuch führen und durchhalten: 7 Tipps",
            "teaser": "Warum die meisten nach zwei Wochen aufgeben – und wie es dauerhaft klappt.",
            "answer": "Ein Haushaltsbuch scheitert selten an der Mathematik, sondern am Aufwand. **Je weniger du pro Ausgabe tun musst, desto länger hältst du durch:** nur den Betrag eintragen, und zwar sofort. Fixkosten einmal festhalten. Statt vieler Diagramme auf eine Zahl schauen – was noch übrig ist.",
            "updated": "2026-11-16",
            "updated_label": "November 2026",
            "sections": [
                ["tipps", "Sieben Tipps", [
                    {"steps": [
                        "**Nur den Betrag aufschreiben.** Kategorie, Geschäft und Notiz sind nett, aber nicht nötig. Der Betrag allein beantwortet die wichtigste Frage: Wie viel ist noch da?",
                        "**Sofort eintragen, nicht abends.** An der Kasse dauert es Sekunden. Abends hast du die Hälfte vergessen, am Sonntag alles.",
                        "**Fixkosten einmal erfassen, nicht jeden Monat.** Miete und Versicherungen ändern sich selten. Einmal sauber notiert, rechnen sie sich selbst ab.",
                        "**Vergessenes nachtragen statt aufgeben.** Ein fehlender Eintrag ist kein Grund, das ganze Haushaltsbuch abzuschreiben. Trag ihn mit Datum nach, wenn er dir einfällt.",
                        "**Eine Zahl beobachten.** Was nach Fixkosten und Ausgaben übrig ist – mehr brauchst du im Alltag nicht. Auswertungen sind etwas für das Monatsende.",
                        "**Kassenzettel nutzen.** Wer lieber nicht tippt, hebt die Bons auf oder fotografiert sie und trägt die Summe ein.",
                        "**Einmal im Monat zurückschauen.** Fünf Minuten: Was war ungewöhnlich? Wo ging mehr hin als gedacht? Daraus entsteht der eigentliche Nutzen.",
                    ]},
                ]],
                ["warum", "Warum Haushaltsbücher scheitern", [
                    {"list": [
                        "**Zu viele Pflichtfelder.** Kategorie, Konto, Datum, Notiz – nach einer Woche fühlt sich jeder Kaffee wie Buchhaltung an.",
                        "**Perfektionismus.** Ein vergessener Betrag, und alles scheint falsch. Dabei verfälschen ein paar Euro das Bild kaum.",
                        "**Zu viele Kategorien.** Wer zwanzig Kategorien hat, grübelt bei jeder Ausgabe. Eine Handvoll reicht – oder gar keine.",
                        "**Keine Antwort im Alltag.** Eine Tabelle, die man nur am Monatsende ansieht, hilft im Supermarkt nicht. Eine Zahl, die man jederzeit sieht, schon.",
                    ]},
                ]],
                ["papier", "Papier, Excel oder App?", [
                    {"table": [
                        ["", "Papier", "Tabelle (Excel)", "App"],
                        ["Immer dabei", "selten", "nein", "ja"],
                        ["Rechnet selbst", "nein", "ja, wenn eingerichtet", "ja"],
                        ["Aufwand pro Ausgabe", "gering", "hoch (erst am Rechner)", "gering"],
                        ["Daten privat", "ja", "ja", "je nach App – siehe [ohne Bankverbindung](/anleitungen/haushaltsbuch-app-ohne-bankverbindung/)"],
                    ]},
                    "Entscheidend ist nicht das Werkzeug, sondern dass du es im Moment des Bezahlens zur Hand hast.",
                ]],
            ],
            "app": {
                "h2": "Gebaut für genau diese Tipps",
                "body": [
                    {"list": [
                        "**Betrag eintippen, Speichern antippen** – alles andere ist freiwillig.",
                        "**Fixkosten einmal** bei der Einrichtung, danach zieht die App sie jeden Monat selbst ab.",
                        "**Nachtragen** über das Plus im Verlauf, mit Datum und Uhrzeit.",
                        "**Kassenzettel** vor die Kamera halten: Summe, Geschäft, Datum und Uhrzeit werden erkannt.",
                        "**Vorschläge:** Tippst du eine Bezeichnung, schlägt die App eine Kategorie vor – aus deinen eigenen Einträgen gelernt, nur auf dem Gerät, abschaltbar.",
                        "**Eine große Zahl** auf dem Startbildschirm: was diesen Monat noch verfügbar ist.",
                    ]},
                ],
                "shot": "de-start.webp",
                "alt": "Startbildschirm mit Ziffernfeld und dem grünen Knopf Speichern.",
            },
            "faq": [
                ["Muss ich wirklich jede Kleinigkeit aufschreiben?",
                 ["Am Anfang ja – gerade die Kleinigkeiten überraschen. Nach ein paar Monaten weißt du, wo dein Geld hingeht, und ein vergessener Kaffee ändert nichts am Bild."]],
                ["Wie viele Kategorien sind sinnvoll?",
                 ["So wenige wie möglich. Für den Überblick reichen Lebensmittel, Essen gehen, Mobilität, Freizeit und eine Handvoll weitere. Wer keine Kategorie wählen will, lässt sie weg."]],
                ["Was mache ich mit Bargeld?",
                 ["Trag die Ausgabe ein, wenn du bezahlst – nicht das Abheben am Automaten. Sonst zählt das Geld doppelt oder gar nicht."]],
            ],
        },
    ],
}
