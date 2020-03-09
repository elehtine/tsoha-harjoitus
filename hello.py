from flask import Flask, render_template
app = Flask(__name__)

class Item:
    def __init__(self, name):
        self.name = name

nimi = "Matti meikalainen"
lista = range(10)
esineet = []
esineet.append(Item("kyna"))
esineet.append(Item("tietokone"))
esineet.append(Item("vihko"))
esineet.append(Item("juomapullo"))

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/demo")
def content():
    return render_template("demo.html", nimi=nimi, lista=lista, esineet=esineet)


if __name__ == "__main__":
    app.run(debug=True)
