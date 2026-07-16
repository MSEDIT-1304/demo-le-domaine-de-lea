from flask import Flask, render_template, request, redirect, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "domaine_lea_demo_2026"
PRIX = {
    "basse": 120,
    "moyenne": 150,
    "haute": 190
}


@app.route("/")
def accueil():
    return render_template("index.html")


@app.route("/chalet")
def chalet():
    return render_template("chalet.html")


@app.route("/photos")
def photos():
    return render_template("photos.html")


@app.route("/tarifs")
def tarifs():
    return render_template("tarifs.html")


from datetime import datetime

@app.route("/reservation")
def reservation():

    session["reservation"] = {

        "nom": "Dupont",

        "prenom": "Jean",

        "arrivee": "15/08/2026",

        "depart": "22/08/2026",

        "adultes": 2,

        "enfants": 2,

        "nuits": 7,

        "saison": "Haute saison",

        "prix_nuit": 190,

        "total": 1330

    }

    return render_template("reservation.html")
    
@app.route("/supplements")
def supplements():
    return render_template("supplements.html")


@app.route("/actualites")
def actualites():
    return render_template("actualites.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/panier")
def panier():

    reservation = session.get("reservation")

    return render_template(
        "panier.html",
        reservation=reservation
    )

@app.route("/paiement", methods=["GET", "POST"])
def paiement():

    reservation = session.get("reservation")

    return render_template(
        "paiement.html",
        reservation=reservation
    )
    
@app.route("/confirmation")
def confirmation():

    reservation = session.get("reservation")

    return render_template(
        "confirmation.html",
        reservation=reservation
    )
    return render_template(
        "confirmation.html",
        reservation=reservation
    )
if __name__ == "__main__":
    app.run(debug=True)
