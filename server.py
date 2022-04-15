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
    "ingredients": ["Fresh Lime Juice",
    "Pineapple Juice",
    "Ginger Syrup",
    "Simple Syrup",
    "Orange Tequila",
    "Tequila",
    "Vodka",
    "Ginger Beer",
    "Cream of Coconut"],
    "correct_ingredients": ["Fresh Lime Juice", "Simple Syrup", "Orange Tequila", "Tequila"]
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

@ app.route("/quiz", methods=['GET', 'POST'])
def quiz():
    global data
    global glass

    ingredients = data["margarita"]["ingredients"]
    correct_ingredients = data["margarita"]["correct_ingredients"]

    return render_template("quiz.html", ingredients=ingredients, glass=glass, correct_ingredients=correct_ingredients)



if __name__ == '__main__':
    app.run(debug=True)
