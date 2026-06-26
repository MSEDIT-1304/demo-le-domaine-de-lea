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

@app.route("/reservation", methods=["GET", "POST"])
def reservation():

    if request.method == "POST":

        arrivee = request.form["arrivee"]
        depart = request.form["depart"]
        adultes = int(request.form["adultes"])
        enfants = int(request.form["enfants"])
        nom = request.form["nom"]
        prenom = request.form["prenom"]
        telephone = request.form["telephone"]
        email = request.form["email"]
        message = request.form["message"]

        date_arrivee = datetime.strptime(arrivee, "%Y-%m-%d")
        date_depart = datetime.strptime(depart, "%Y-%m-%d")

        nuits = (date_depart - date_arrivee).days

        mois = date_arrivee.month

        if mois in [7, 8]:
            prix_nuit = PRIX["haute"]
            saison = "Haute saison"

        elif mois in [5, 6, 9]:
            prix_nuit = PRIX["moyenne"]
            saison = "Moyenne saison"

        else:
            prix_nuit = PRIX["basse"]
            saison = "Basse saison"

        total = nuits * prix_nuit

        session["reservation"] = {
            "arrivee": arrivee,
            "depart": depart,
            "adultes": adultes,
            "enfants": enfants,
            "nom": nom,
            "prenom": prenom,
            "telephone": telephone,
            "email": email,
            "message": message,
            "nuits": nuits,
            "prix_nuit": prix_nuit,
            "saison": saison,
            "total": total
        }

        return redirect("/panier")

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

    if reservation is None:
        return redirect("/reservation")

    if request.method == "POST":
        return redirect("/confirmation")

    return render_template(
        "paiement.html",
        reservation=reservation
    )
@app.route("/confirmation")
def confirmation():

    reservation = session.get("reservation")

if reservation is None:
        return redirect("/")

    return render_template(
        "confirmation.html",
        reservation=reservation
    )
if __name__ == "__main__":
    app.run(debug=True)
