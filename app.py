from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "domaine_lea_demo_2026"


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


@app.route("/reservation")
def reservation():
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
    return render_template("panier.html")


if __name__ == "__main__":
    app.run(debug=True)
