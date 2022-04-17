from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

ingredients = ["lime", "orange juice", "tequila"]  # testing git


data = {
    "moscow_mule": {
    "ingredients": ["Fresh Lime Juice",
    "Pineapple Juice",
    "Ginger Syrup",
    "Simple Syrup",
    "Orange Tequila",
    "Tequila",
    "Vodka",
    "Ginger Beer",
    "Cream of Coconut"],
    "correct_ingredients": ["Vodka", "Ginger Beer", "Fresh Lime Juice", "Ginger Syrup"]
    },
    "pina_colada": {
    "ingredients": ["Fresh Lime Juice",
    "Pineapple Juice",
    "Ginger Syrup",
    "Simple Syrup",
    "Orange Tequila",
    "Tequila",
    "Vodka",
    "Ginger Beer",
    "Cream of Coconut"],
    "correct_ingredients": ["Tequila", "Pineapple Juice", "Fresh Lime Juice", "Cream of Coconut"]
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
        "facts": {
            "fun_fact": "Using a salt-rimmed glass makes the drink sweeter",
            "taste": "Margaritas taste like agave, from the tequila",
            "goes_well_with": "Tacos"
        },
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
        "facts": {
            "fun_fact": "Using a salt-rimmed glass makes the drink sweeter",
            "taste": "Margaritas taste like agave, from the tequila",
            "goes_well_with": "Tacos"
        },
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
        "facts": {
            "fun_fact": "Using a salt-rimmed glass makes the drink sweeter",
            "taste": "Margaritas taste like agave, from the tequila",
            "goes_well_with": "Tacos"
        },
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
def defaultPage():
    return render_template("home.html")


@ app.route("/home")
def home():
    return render_template("home.html", cocktails=cocktails)


@ app.route("/learn/<name>")
def learnCocktailpage(name=None):
    #for currCocktail in cocktails.values():
    #    if name == currCocktail["name"]:
    #        cocktail = currCocktail

    drink = cocktails[name]
    print(drink)
    video_url = drink["video"]
    print(video_url)

    
    return render_template("learn.html", video_url = video_url)

@ app.route("/quiz/<drink>", methods=['GET', 'POST'])
def quiz(drink=None):
    global data
    global glass

    #ingredients = data["margarita"]["ingredients"]
    ingredients = data[drink]["ingredients"]
    correct_ingredients = data[drink]["correct_ingredients"]


    if drink == "moscow_mule":
        drink_name = "Moscow Mule"
    elif drink == "margarita":
        drink_name = "Margarita"
    elif drink == "pina_colada":
        drink_name = "Pina Colada"



    return render_template("quiz.html", ingredients=ingredients, glass=glass, correct_ingredients=correct_ingredients, drink=drink_name)


if __name__ == '__main__':
    app.run(debug=True)
