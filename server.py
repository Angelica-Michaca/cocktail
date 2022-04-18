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
        "image": "static/images/margarita",
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
                    "ingredient_image": "/static/images/tequila.png",
                    "volume": "1.5",
                    "timestamp": "0:15"
                },
                "orange_tequila": {
                    "name": "Orange Tequila",
                    "ingredient_image": "/static/images/orange_tequila.png",
                    "volume": "0.75",
                    "timestamp": "0:12"
                }
            },
            "juice": {
                "fresh_lime_juice": {
                    "name": "Fresh Lime Juice",
                    "ingredient_image": "/static/images/fresh_lime_juice.png",
                    "volume": "0.75",
                    "timestamp": "0:09"
                }
            },
            "syrup": {
                "simple_syrup": {
                    "name": "Simple Syrup",
                    "ingredient_image": "/static/images/simple_syrup.png",
                    "volume": "0.25",
                    "timestamp": "0:11"
                }
            }
        }
    },
    "pina_colada": {
        "name": "Piña Colada",
        "image": "static/images/pina_colada",
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
                    "ingredient_image": "/static/images/tequila.png",
                    "volume": "2.0",
                    "timestamp": "0:04"
                }
            },
            "juice": {
                "pineapple_juice": {
                    "name": "Pineapple Juice",
                    "ingredient_image": "/static/images/pineapple_juice",
                    "volume": "2.0",
                    "timestamp": "0:10"
                },
                "fresh_lime_juice": {
                    "name": "Fresh Lime Juice",
                    "ingredient_image": "/static/images/fresh_lime_juice",
                    "volume": "0.5",
                    "timestamp": "0:09"
                }
            },
            "syrup": {
                "cream_of_coconut": {
                    "name": "Cream of Coconut",
                    "ingredient_image": "/static/images/cream_of_coconut",
                    "volume": "2.0",
                    "timestamp": "0:06"
                }
            }
        }
    },
    "moscow_mule": {
        "name": "Moscow Mule",
        "image": "static/images/moscow_mule",
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
                    "ingredient_image": "/static/images/tequila.png",
                    "volume": "1.5",
                    "timestamp": "0:15"
                },
                "orange_tequila": {
                    "name": "Orange Tequila",
                    "ingredient_image": "/static/images/orange_tequila",
                    "volume": "0.75",
                    "timestamp": "0:12"
                }
            },
            "juice": {
                "fresh_lime_juice": {
                    "name": "Fresh Lime Juice",
                    "ingredient_image": "/static/images/fresh_lime_juice",
                    "volume": "0.75",
                    "timestamp": "0:09"
                }
            },
            "syrup": {
                "simple_syrup": {
                    "name": "Simple Syrup",
                    "ingredient_image": "/static/images/simple_syrup",
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


@ app.route("/practice")
def practicePage(name=None):
    return render_template("practice.html")


@ app.route("/learn/<name>")
def learnCocktailpage(name=None):
    # for currCocktail in cocktails.values():
    #    if name == currCocktail["name"]:
    #        cocktail = currCocktail

    drink = cocktails[name]
    print(drink)
    video_url = drink["video"]
    print(video_url)

    alcohols = drink["ingredients"]["alcohol"]
    print(alcohols)
    print(alcohols.keys())

    # get length of items
    alcohol_items = []

    drink_name = []
    test = drink["name"]
    drink_name.append(test)
    alcohol_img = []
    alcohol_vol = []
    alcohol_timestamp = []
    alcohol_name = []

    for alcohol in alcohols.keys():

        alcohol_img.append(alcohols[alcohol]["ingredient_image"])
        alcohol_vol.append(alcohols[alcohol]["volume"])
        alcohol_timestamp.append(alcohols[alcohol]["timestamp"])
        alcohol_name.append(alcohols[alcohol]["name"])

    print("alcohol_img:", alcohol_img)
    print("drink_name:", drink_name)

    # juice_img = drink[]
    # syrup_img = drink[]
    #ingredients = cocktails[ingredients]

    return render_template("learn.html", video_url=video_url, alcohol_img=alcohol_img, alcohol_vol=alcohol_vol, alcohol_timestamp=alcohol_timestamp, drink_name=drink_name, alcohol_name=alcohol_name, alcohol_items=alcohol_items)


@ app.route("/quiz/<drink>", methods=['GET', 'POST'])
def quiz(drink=None):
    global data
    global glass

    #ingredients = data["margarita"]["ingredients"]
    ingredients = data[drink]["ingredients"]
    correct_ingredients = data[drink]["correct_ingredients"]

    if drink == "moscow_mule":
        drink_name = "Moscow Mule"
        drink_link = "moscow_mule"
    elif drink == "margarita":
        drink_name = "Margarita"
        drink_link = "margarita"
    elif drink == "pina_colada":
        drink_name = "Pina Colada"
        drink_link = "pina_colada"

    return render_template("quiz.html", ingredients=ingredients, glass=glass, correct_ingredients=correct_ingredients, drink=drink_name, drink_link=drink_link)


@ app.route("/quizResult/<drink>", methods=['GET', 'POST'])
def quizResult(drink=None):
    if drink == "margarita":
        drink_list = ["Margarita", "Pina Colada", "Moscow Mule"]
        drink_link = ["pina_colada", "moscow_mule"]
    elif drink == "pina_colada":
        drink_list = ["Pina Colada", "Margarita", "Moscow Mule"]
        drink_link = ["margarita", "moscow_mule"]
    elif drink == "moscow_mule":
        drink_list = ["Moscow Mule", "Margarita", "Pina Colada"]
        drink_link = ["margarita", "pina_colada"]

    return render_template("quizResult.html", drink=drink, drink_list=drink_list, drink_link=drink_link)


if __name__ == '__main__':
    app.run(debug=True)
