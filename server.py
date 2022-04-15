from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

ingredients = ["lime", "orange juice", "tequila"] #testing git


data = {
    "moscow_mule": {
    "ingredients": ["lime", "lemon"],
    },
    "pina_colada": {
    "ingredients": ["lime", "lemon"],
    },
    "margarita": {
    "ingredients": ["Lime Juice",
    "Orange Juice",
    "Ginger Syrup",
    "Simple Syrup",
    "Lime Tequila",
    "Orange Tequila",
    "Lemon Tequila",
    "Tequila"],
    }
}

glass = []
# ROUTES


@ app.route("/")
def defaultPage():
    return render_template("home.html")


@ app.route("/home")
def home():
    return render_template("home.html")


@ app.route("/learn")
def learn():
    return render_template("learn.html")

@ app.route("/quiz")
def quiz():
    global data
    global glass

    margarita_ingredients = data["margarita"]["ingredients"]

    return render_template("quiz.html", ingredients=margarita_ingredients, glass=glass)



if __name__ == '__main__':
    app.run(debug=True)
