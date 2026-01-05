from flask import Flask, render_template, request, redirect, url_for, flash, make_response
import json
import os
from daten import (vorname, nachname, straße, plz_ort, telefon, email,
                   ort_datum, softskills, linkedin, berufserfahrung, praktika, zertifikate,
                   anschreiben, deckblatt_titel)


app = Flask(__name__)
app.secret_key = 'werderbremen1899'

ADMIN_PASSWORD = "werderbremen1899"

@app.route("/view_anschreiben")
def view_anschreiben():
    global anschreiben
    return render_template("anschreiben.html",
                           vorname=vorname,
                           nachname=nachname,
                           straße=straße,
                           plz_ort=plz_ort,
                           telefon=telefon,
                           email=email,
                           ort_datum=ort_datum,
                           anschreiben=anschreiben)

@app.route("/lebenslauf")
def lebenslauf():
    return render_template("lebenslauf.html",
                            vorname=vorname,
                            nachname=nachname,
                            straße=straße,
                            plz_ort=plz_ort,
                            telefon=telefon,
                            email=email,
                            linkedin=linkedin,
                            softskills=softskills,
                            berufserfahrung=berufserfahrung,
                            praktika=praktika,
                            zertifikate=zertifikate,
                            ort_datum=ort_datum
                        )

#Startseite
@app.route("/")
def startseite():
    return render_template("index.html")

#Deckblatt
@app.route("/deckblatt")
def deckblatt():
    return render_template("deckblatt.html",
                           deckblatt_titel=deckblatt_titel)

#Admin-Login
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        if request.form.get("password") == ADMIN_PASSWORD:
            return redirect(url_for("admin_panel"))
        else:
            flash("Falsches Passwort")
    return render_template("admin_login.html")

#Admin-Panel
@app.route("/admin/panel", methods=["GET", "POST"])
def admin_panel():
    global berufserfahrung, praktika, zertifikate, deckblatt_titel, anschreiben

    if request.method == "POST":
        typ = request.form["typ"]

        if typ == "job":
            new_job = {
                "zeit": request.form["zeit"],
                "position": request.form["position"],
                "firma": request.form["firma"],
                "aufgaben": request.form["aufgaben"].split("\n") if request.form["aufgaben"] else []
            }
            berufserfahrung.insert(0, new_job)

        elif typ == "praktika":
            new_praktikum = {
                "zeit": request.form["zeit"],
                "position": request.form["position"],
                "firma": request.form["firma"]
            }
            praktika.insert(0, new_praktikum)

        elif typ == "zertifikat":
            zertifikate.insert(0, request.form["zertifikat"])

        elif typ == "deckblatt":
            global deckblatt_titel
            deckblatt_titel = request.form["deckblatt_titel"]

        elif typ == "anschreiben":
            global anschreiben
            anschreiben = {
                "firma_name": request.form["firma_name"],
                "firma_strasse": request.form["firma_strasse"],
                "firma_plz_ort": request.form["firma_plz_ort"],
                "anrede": request.form["anrede"],
                "betreff": request.form["betreff"],
                "text": [line.strip() for line in request.form["text"].split("\n") if line.strip()]
            }

        # === HIER WAR DER FEHLER: Alles zusammen speichern ===
        data = {
            "berufserfahrung": berufserfahrung,
            "praktika": praktika,
            "zertifikate": zertifikate,
            "deckblatt_titel": deckblatt_titel,
            "anschreiben": anschreiben
        }

        with open("daten.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        flash("Änderungen erfolgreich gespeichert!")

    return render_template("admin_panel.html",
                           berufserfahrung=berufserfahrung,
                           praktika=praktika,
                           zertifikate=zertifikate,
                           deckblatt_titel=deckblatt_titel,
                           anschreiben=anschreiben)


if __name__ == "__main__":
    app.run(debug=True)