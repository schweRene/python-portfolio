from datetime import datetime
import json
import os

# -- Persönliche Daten ---
vorname = "René"
nachname = "Schwemer"
straße = "Vierbergen 5a"
plz_ort = "22111 Hamburg"
telefon = "0176 55696997"
email = "schwemerrene@gmail.com"
linkedin = "https://www.linkedin.com/in/rené-schwemer-786b48266/"


# Softskills
softskills = {
    "Zeitmanagement",
    "Teamfähigkeit",
    "Loyalität",
    "Lernbereitschaft",
    "Problemlösungsfähigkeit",
    "Analytisches Denken"
}

# === DYNAMISCHE DATEN AUS JSON (Jobs, Praktika, Zertifikate) ===
DATA_FILE = "daten.json"

# Default-Werte
default_data = {
    "berufserfahrung": [],
    "praktika": [],
    "zertifikate": [],
    "deckblatt_titel": "Softwareentwickler",
    "anschreiben": {
        "firma_name": "Musterfirma GmbH",
        "firma_strasse": "Musterstraße 1",
        "firma_plz_ort": "12345 Musterstadt",
        "anrede": "Sehr geehrte Damen und Herren,",
        "betreff": "Bewerbung als Softwareentwickler",
        "text": [
            "hiermit bewerbe ich mich um die ausgeschriebene Stelle.",
            "",
            "Ich bringe fundierte Kenntnisse in Python und Webentwicklung mit.",
            "",
            "Mit freundlichen Grüßen"
        ]
    }
}

# Lade aus JSON oder nutze Defaults
if os.path.exists(DATA_FILE):
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            loaded = json.load(f)
        berufserfahrung = loaded.get("berufserfahrung", default_data["berufserfahrung"])
        praktika = loaded.get("praktika", default_data["praktika"])
        zertifikate = loaded.get("zertifikate", default_data["zertifikate"])
        deckblatt_titel = loaded.get("deckblatt_titel", "Softwareentwickler")
        anschreiben = loaded.get("anschreiben", default_data["anschreiben"])
    except:
        berufserfahrung = default_data["berufserfahrung"]
        praktika = default_data["praktika"]
        zertifikate = default_data["zertifikate"]
        deckblatt_titel = "Softwareentwickler"
        anschreiben = default_data["anschreiben"]
else:
    berufserfahrung = default_data["berufserfahrung"]
    praktika = default_data["praktika"]
    zertifikate = default_data["zertifikate"]
    deckblatt_titel = "Softwareentwickler"
    anschreiben = default_data["anschreiben"]



# Beruflicher Werdegang
berufserfahrung = [
    {
        "zeit": "08/2024 - 12/2025", 
        "position": "Junior Softwareentwickler", 
        "firma": "CPC Profiling Company, Hamburg", 
        "aufgaben": [
            "Umsetzung internationaler Multichannel-Kampagnen in der SFMC",
            "SQL-Datenbanken",
            "Programmieren mit AmpScript umd HTML",
            "Prozessmanagement"
        ]
    },
    {
        "zeit":  "10/2021 - 05/2024",
        "position": "Fortbildung zum Anwendungsentwickler",
        "firma": "Bfw Berlin-Brandenburg"
    },
    {
        "zeit": "01/2021 - 10/2021",
        "position": "Berufliche Neuorientierung",
        "firma": "Bfw Stralsund"
    },
    {
        "zeit": "10/2017 - 07/2020",
        "position": "Disponent",
        "firma": "Steinofen-Meister GmbH & Co.KG",
        "aufgaben": [
            "Erstellung von Lieferscheinen",
            "Organisation und Koordination von Transporten"
        ]
    },
    {
        "zeit": "06/2017 - 10/2017",
        "position": "Produktionsmitarbeiter",
        "firma": "Personaldienstleistung Maruschke"
    },
    {
        "zeit": "12/2016 - 05/2017",
        "position": "Medizinische Schreibkraft",
        "firma": "Rehaklinik Feldberger Seenlandschaft",
        "aufgaben": [
            "Erstellung medizinischer Schriftstücke"
        ]
    },
    {
        "zeit": "08/2014 - 11/2016",
        "position": "Bürokaufmann",
        "firma": "ABC Office 24 GmbH",
        "aufgaben": [
            "Erstellung medizinischer Schriftstücke",
            "Erstellung von Statistiken und Analysen"
        ]
    },
    {
        "zeit": "12/2013 - 07/2014",
        "position": "Fortbildung medizinische Schreibkraft",
        "firma": "ÜaZ Waren-Grevesmühlen GmbH"
    },
    {
        "zeit": "09/2008 - 12/2011",
        "position": "Bürokaufmann",
        "firma": "MAW Waren GmbH"
    },
    {
        "zeit": "08/2004 - 01/2005",
        "position": "Fortbildung Bürokaufmann",
        "firma": "Wirtschaftsakademie Neubrandenburg"
    },
    {
        "zeit": "09/2000 - 08/2004",
        "position": "Zeitsoldat",
        "firma": "BMVG Bonn"
    },
    {
        "zeit": "08/1997 - 07/2000",
        "position": "Ausbildung Maler/Lackierer",
        "firma": "Malerbetrieb Henner Haug"
    }
]

praktika = [
    {
        "zeit": "03/2023 - 06/2023", 
        "position": "Pflichtpraktikum Webentwicklung", 
        "firma": "BetaWork inklusiv, Berlin", 
        "aufgaben": ["Erstellung Anzeigenpanel mit JHipster und Tauri"
                     ]
    },
    {
        "zeit": "01/2021 - 10/2021", 
        "position": "Praktikum Bürokaufmann", 
        "firma": "Stadtverwaltung Stavenhagen, Stavenhagen", 
        "aufgaben": [
            "Erstellung von Heizkostenabrechnungen",
            "Berechnung der Kosten von Feuerwehreinsätzen"
        ]
    }
]

zertifikate = [
    "Introduction Agile Development (10/2025)",
    "Introduction Cloud Computing (09/2025)",
    "Introduction DevOps (09/2025)",
    "Microsoft Python Development (05/2025 - 09/2025)" 
]

deckblatt_titel = "Softwareentwickler"  # oder dein gewünschter Default
# Dein vollständiger Anschreiben-Text (überschreibt den Default)
anschreiben = {
    "firma_name": "Musterfirma GmbH",
    "firma_strasse": "Musterstraße 1",
    "firma_plz_ort": "12345 Musterstadt",
    "anrede": "Sehr geehrte Damen und Herren,",
    "betreff": "Initiativbewerbung für eine Position im Bereich Kampagnenmanagement / Schnittstelle zwischen Fachprozess und technischer Umsetzung",
    "text": [
        "mit dieser Initiativbewerbung möchte ich mein Interesse an einer Tätigkeit in Ihrem Unternehmen bekunden. Besonders spannend finde ich Aufgaben an der Schnittstelle zwischen fachlichem Prozess und technischer Umsetzung, da ich hier meine Kenntnisse und meine Leidenschaft für komplexes Kampagnenmanagement optimal einbringen kann. Ich verfüge über fundierte Erfahrung in der Salesforce Marketing Cloud, die ich erfolgreich zur Umsetzung internationaler Multichannel-Kampagnen eingesetzt habe. Darüber hinaus bringe ich gute Kenntnisse in HTML, SQL und Ampscript mit, die mir ermöglichen, Kampagnen technisch präzise und effizient umzusetzen. ",
        "Meine Arbeitsweise ist geprägt von Pflichtbewusstsein, hoher Belastbarkeit und ausgeprägter Frustrationstoleranz – Eigenschaften, die mir helfen, auch in komplexen Projekten stets lösungsorientiert zu handeln. Zudem zeichne ich mich durch eine sehr gute Lernfähigkeit aus, sodass ich mich schnell in neue Systeme und Prozesse einarbeite.",
        "Im Team wie auch im Kundenkontakt bin ich für meine Hilfsbereitschaft und kooperative Haltung bekannt. Mein Fleiß und meine Einsatzbereitschaft gelten als vorbildlich und tragen dazu bei, Projekte erfolgreich und termingerecht abzuschließen. Für die tägliche Kommunikation in internationalen Projekten bringe ich solide Englischkenntnisse mit, die ich routiniert anwende. Ich bin überzeugt, dass ich mit meiner Kombination aus fachlichem Know-how, technischer Expertise und persönlicher Einsatzbereitschaft einen wertvollen Beitrag zu Ihrem Unternehmen leisten kann. ",
        "Gerne möchte ich in einem persönlichen Gespräch mit Ihnen erörtern, wie ich meine Fähigkeiten in Ihrem Team einbringen und weiterentwickeln kann. ",
        
        "Vielen Dank für Ihre Zeit und die Berücksichtigung meiner Bewerbung. ",
        
        "Mit freundlichen Grüßen"
    ]
}
ort_datum = f"{plz_ort.split()[1]}, den {datetime.now().strftime('%d.%m.%Y')}"