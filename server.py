from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

ingredients = ["lime", "orange juice", "tequila"]  # testing git


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

cocktails = {
    "margarita": {
        "name": "Margarita",
        "image": "",
        "video": "https://www.youtube.com/embed/2BiT4wfRfWg",
        "ingredients": {
            "alcohol": {
                "tequila": {
                    "name": "Tequila",
                    "ingredient_image": "",
                    "volume": "1.5",
                    "timestamp": "0:15"
                },
                "orange_tequila": {
                    "name": "Orange Tequila",
                    "ingredient_image": "",
                    "volume": "0.75",
                    "timestamp": "0:12"
                }
            },
            "juice": {
                "fresh_lime_juice": {
                    "name": "Fresh Lime Juice",
                    "ingredient_image": "",
                    "volume": "0.75",
                    "timestamp": "0:09"
                }
            },
            "syrup": {
                "simple_syrup": {
                    "name": "Simple Syrup",
                    "ingredient_image": "",
                    "volume": "0.25",
                    "timestamp": "0:11"
                }
            }
        }
    },
    "pina_colada": {
        "name": "Piña Colada",
        "image": "",
        "video": "https://www.youtube.com/embed/nyzeEdPkfOw",
        "ingredients": {
            "alcohol": {
                "tequila": {
                    "name": "Tequila",
                    "ingredient_image": "",
                    "volume": "2.0",
                    "timestamp": "0:04"
                }
            },
            "juice": {
                "pineapple_juice": {
                    "name": "Pineapple Juice",
                    "ingredient_image": "",
                    "volume": "2.0",
                    "timestamp": "0:10"
                },
                "fresh_lime_juice": {
                    "name": "Fresh Lime Juice",
                    "ingredient_image": "",
                    "volume": "0.5",
                    "timestamp": "0:09"
                }
            },
            "syrup": {
                "cream_of_coconut": {
                    "name": "Cream of Coconut",
                    "ingredient_image": "",
                    "volume": "2.0",
                    "timestamp": "0:06"
                }
            }
        }
    },
    "moscow_mule": {
        "name": "Moscow Mule",
        "image": "",
        "video": "https://www.youtube.com/embed/FirpAjZomHA",
        "ingredients": {
            "alcohol": {
                "tequila": {
                    "name": "Tequila",
                    "ingredient_image": "",
                    "volume": "1.5",
                    "timestamp": "0:15"
                },
                "orange_tequila": {
                    "name": "Orange Tequila",
                    "ingredient_image": "",
                    "volume": "0.75",
                    "timestamp": "0:12"
                }
            },
            "juice": {
                "fresh_lime_juice": {
                    "name": "Fresh Lime Juice",
                    "ingredient_image": "",
                    "volume": "0.75",
                    "timestamp": "0:09"
                }
            },
            "syrup": {
                "simple_syrup": {
                    "name": "Simple Syrup",
                    "ingredient_image": "",
                    "volume": "0.25",
                    "timestamp": "0:11"
                }
            }
        }
    }
}

glass = []
# ROUTES


@ app.route("/")
def home():
    return render_template("home.html", cocktails=cocktails)


@ app.route("/learn/<name>")
def learnCocktail(name=None):
    global cocktails
    cocktail = cocktails[name]
    return render_template("learn.html", cocktail=cocktail)


@ app.route("/quiz", methods=['GET', 'POST'])
def quiz():
    global data
    global glass

    ingredients = data["margarita"]["ingredients"]
    correct_ingredients = data["margarita"]["correct_ingredients"]

    return render_template("quiz.html", ingredients=ingredients, glass=glass, correct_ingredients=correct_ingredients)


if __name__ == '__main__':
    app.run(debug=True)
