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

ort_datum = f"{plz_ort.split()[1]}, den {datetime.now().strftime('%d.%m.%Y')}"