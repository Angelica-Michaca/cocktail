from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

ingredients = ["lime", "orange juice", "tequila"] #testing git


data = {
    "moscow_mule": {
    "ingredients": 
    "video": "",
    "jpegs": "",
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
    }
    "true_ingredients": ["Fresh Lime Juice", "Simple Syrup", "Orange Tequila", "Tequila"]
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

@ app.route("/quiz/<drink>", methods=['GET', 'POST'])
def quiz(drink):
    global data
    global glass

    ingredients = data[drink]["ingredients"]
    true_ingredients = data[drink]["true_ingredients"]

    return render_template("quiz.html", ingredients=ingredients, glass=glass, true_ingredients=true_ingredients)



if __name__ == '__main__':
    app.run(debug=True)
