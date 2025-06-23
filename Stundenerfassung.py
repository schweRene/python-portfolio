from datetime import datetime
import calendar

def tageImMonat(monat, jahr):
    try:
        tage = calendar.monthrange(jahr, monat)[1]
        return tage
    except ValueError:
        return None


# Aktualisiertes 2D-Array für das Jahr 2023
arbeitsstunden = [
    ["2023-10-02", 8, 10, ""],
    ["2023-10-02", 17, 20, ""],
    ["2023-10-03", 7, 50, ""],
    ["2023-10-06", 8, 00, ""],
    ["2023-10-06", 16, 00, ""],
    ["2023-10-07", 16, 30, ""],
    ["2023-10-08", 8, 20, ""],
    ["2023-10-08", 16, 40, ""],
    ["2023-10-30", 8, 10, ""],
]

def schreibeKopf(persnr, jahr, monat):
    # Formatierter Kopf für die Übersicht mit Tabstopps
    kopfzeile = f"Mitarbeiter: {persnr}\t\t\t\t\t\t\t  {datetime(jahr, monat, 1).strftime('%B')} {jahr}\n"

    # Ausgabe des Kopfes
    print("\n" + kopfzeile)

# Beispielaufruf der Funktion
persnr = 12345  # Beispiel-Personalnummer
jahr = 2023
monat = 10  # Beispiel für Oktober
schreibeKopf(persnr, jahr, monat)

def erzeugeListe(arbeitsstunden):
    # Anzahl der Tage im aktuellen Monat ermitteln
    anzahl_tage = tageImMonat(monat, jahr)

    if anzahl_tage is None:
        print("Ungültiger Monat oder Jahr.")
        return

    arbeitszeit_info = []

    for tag in range(1, anzahl_tage + 1):
        aktuelles_datum = f"{jahr}-{monat:02d}-{tag:02d}"
        kommen = None
        gehen = None
        bemerkungen = ""

        # Suche nach Buchungen für das aktuelle Datum
        for eintrag in arbeitsstunden:
            datum, stunden, minuten, bemerkung = eintrag
            if datum == aktuelles_datum:
                eintragszeit = f"{stunden:02d}:{minuten:02d}"
                if kommen is None:
                    kommen = eintragszeit
                else:
                    gehen = eintragszeit

        # Verarbeite die Arbeitszeit für das aktuelle Datum
        if kommen is not None:
            if gehen is None:
                bemerkungen = "Buchung fehlt"
                gehen = ""
            arbeitszeit_kommen = datetime.strptime(kommen, "%H:%M")
            arbeitszeit_gehen = datetime.strptime(gehen, "%H:%M") if gehen else arbeitszeit_kommen
            arbeitszeit_delta = arbeitszeit_gehen - arbeitszeit_kommen
            anwesenheit_stunden = arbeitszeit_delta.seconds // 3600
            anwesenheit_minuten = (arbeitszeit_delta.seconds % 3600) // 60
            anwesenheitszeit = f"{anwesenheit_stunden:02d}:{anwesenheit_minuten:02d}"
        else:
            bemerkungen = "Nicht anwesend"
            anwesenheitszeit = "00:00"

        arbeitszeit_info.append({
            "Datum": aktuelles_datum,
            "Kommen": kommen if kommen else "",
            "Gehen": gehen if gehen else "",
            "Anwesenheit": anwesenheitszeit,
            "Bemerkungen": bemerkungen
        })

    return arbeitszeit_info


# Arbeitszeit berechnen
arbeitszeit_info = erzeugeListe(arbeitsstunden)

# Ausgabe der Arbeitszeit und Bemerkungen
print(f"{'Datum':<12}{'Kommen':<8}{'Gehen':<8}{'Anwesenheit':<15}{'Bemerkungen':<15}")
print("-" * 60)  # Trennlinie
print("-" * 60)  # Zweite Trennlinie
for info in arbeitszeit_info:
    print(
        f"{info['Datum']:<12}{info['Kommen']:<8}{info['Gehen']:<8}{info['Anwesenheit']:<15}{info['Bemerkungen']:<15}")


def schreibeZeile(arbeitsstunden, monat, jahr):
    # Anzahl der Tage im aktuellen Monat ermitteln
    anzahl_tage = tageImMonat(monat, jahr)

    if anzahl_tage is None:
        print("Ungültiger Monat oder Jahr.")
        return

    arbeitszeit_info = []

    for tag in range(1, anzahl_tage + 1):
        aktuelles_datum = f"{jahr}-{monat:02d}-{tag:02d}"
        kommen = None
        gehen = None
        bemerkungen = ""

        # Suche nach Buchungen für das aktuelle Datum
        for eintrag in arbeitsstunden:
            datum, stunden, minuten, bemerkung = eintrag
            if datum == aktuelles_datum:
                eintragszeit = f"{stunden:02d}:{minuten:02d}"
                if kommen is None:
                    kommen = eintragszeit
                else:
                    gehen = eintragszeit

        # Verarbeite die Arbeitszeit für das aktuelle Datum
        if kommen is not None:
            if gehen is None:
                bemerkungen = "Buchung fehlt"
                gehen = ""
            arbeitszeit_kommen = datetime.strptime(kommen, "%H:%M")
            arbeitszeit_gehen = datetime.strptime(gehen, "%H:%M") if gehen else arbeitszeit_kommen
            arbeitszeit_delta = arbeitszeit_gehen - arbeitszeit_kommen
            anwesenheit_stunden = arbeitszeit_delta.seconds // 3600
            anwesenheit_minuten = (arbeitszeit_delta.seconds % 3600) // 60
            anwesenheitszeit = f"{anwesenheit_stunden:02d}:{anwesenheit_minuten:02d}"
        else:
            bemerkungen = "Nicht anwesend"
            anwesenheitszeit = "00:00"

        arbeitszeit_info.append({
            "Datum": aktuelles_datum,
            "Kommen": kommen if kommen else "",
            "Gehen": gehen if gehen else "",
            "Anwesenheit": anwesenheitszeit,
            "Bemerkungen": bemerkungen
        })

    return arbeitszeit_info



def schreibeFuss(anwesenheitMonat):
    # Gesamtanzahl der Anwesenheitsstunden formatieren
    gesamt_anwesenheit = f"Summe Anwesenheit:          {anwesenheitMonat}"

    # Ausgabe der Gesamtanzahl der Anwesenheitsstunden
    print("-" * 60)  # Trennlinie
    print("-" * 60)  # Trennlinie
    print(gesamt_anwesenheit)

# Arbeitszeit berechnen
arbeitszeit_info = erzeugeListe(arbeitsstunden)

# Gesamtanzahl der Anwesenheitsstunden berechnen
gesamt_anwesenheit_stunden = 0
gesamt_anwesenheit_minuten = 0

for info in arbeitszeit_info:
    anwesenheit_stunden, anwesenheit_minuten = info['Anwesenheit'].split(':')
    gesamt_anwesenheit_stunden += int(anwesenheit_stunden)
    gesamt_anwesenheit_minuten += int(anwesenheit_minuten)

gesamt_anwesenheit_stunden += gesamt_anwesenheit_minuten // 60
gesamt_anwesenheit_minuten = gesamt_anwesenheit_minuten % 60

gesamt_anwesenheit = f"{gesamt_anwesenheit_stunden:02d}:{gesamt_anwesenheit_minuten:02d}"

# Gesamtanzahl der Anwesenheitsstunden an die Funktion schreibeFuss übergeben
schreibeFuss(gesamt_anwesenheit)