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
        "image": "/static/images/pina_colada",
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
                    "ingredient_image": "/static/images/pineapple_juice.png",
                    "volume": "2.0",
                    "timestamp": "0:10"
                },
                "fresh_lime_juice": {
                    "name": "Fresh Lime Juice",
                    "ingredient_image": "/static/images/fresh_lime_juice.png",
                    "volume": "0.5",
                    "timestamp": "0:09"
                }
            },
            "syrup": {
                "cream_of_coconut": {
                    "name": "Cream of Coconut",
                    "ingredient_image": "/static/images/cream_of_coconut.png",
                    "volume": "2.0",
                    "timestamp": "0:06"
                }
            }
        }
    },
    "moscow_mule": {
        "name": "Moscow Mule",
        "image": "/static/images/moscow_mule",
        "video": "https://www.youtube.com/embed/FirpAjZomHA",
        "facts": {
            "fun_fact": "Using a salt-rimmed glass makes the drink sweeter",
            "taste": "Margaritas taste like agave, from the tequila",
            "goes_well_with": "Tacos"
        },
        "ingredients": {
            "alcohol": {
                "vodka": {
                    "name": "Vodka",
                    "ingredient_image": "/static/images/vodka.png",
                    "volume": "2",
                    "timestamp": "0:05"
                },
            },
            "juice": {
                "fresh_lime_juice": {
                    "name": "Fresh Lime Juice",
                    "ingredient_image": "/static/images/fresh_lime_juice.png",
                    "volume": "1",
                    "timestamp": "0:03"
                },
                "ginger_beer": {
                    "name": "Ginger Beer",
                    "ingredient_image": "/static/images/ginger_beer.png",
                    "volume": "N/A",
                    "timestamp": "0:12"
                }
            },
            "syrup": {
                "ginger_syrup": {
                    "name": "Ginger Syrup",
                    "ingredient_image": "/static/images/ginger_syrup.png",
                    "volume": "0.75",
                    "timestamp": "0:04"
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
    juices = drink["ingredients"]["juice"]
    syrups = drink["ingredients"]["syrup"]

    # get length of items
    alcohol_items = []

    drink_name = []
    test = drink["name"]
    drink_name.append(test)
    alcohol_img = []
    alcohol_vol = []
    alcohol_timestamp = []
    alcohol_name = []

    juice_img = []
    juice_vol = []
    juice_timestamp = []
    juice_name = []

    syrup_img = []
    syrup_vol = []
    syrup_timestamp = []
    syrup_name = []

    for alcohol in alcohols.keys():

        alcohol_img.append(alcohols[alcohol]["ingredient_image"])
        alcohol_vol.append(alcohols[alcohol]["volume"])
        alcohol_timestamp.append(alcohols[alcohol]["timestamp"])
        alcohol_name.append(alcohols[alcohol]["name"])

    for juice in juices.keys():

        juice_img.append(juices[juice]["ingredient_image"])
        juice_vol.append(juices[juice]["volume"])
        juice_timestamp.append(juices[juice]["timestamp"])
        juice_name.append(juices[juice]["name"])

    for syrup in syrups.keys():

        syrup_img.append(syrups[syrup]["ingredient_image"])
        syrup_vol.append(syrups[syrup]["volume"])
        syrup_timestamp.append(syrups[syrup]["timestamp"])
        syrup_name.append(syrups[syrup]["name"])



    return render_template("learn.html", 
        video_url=video_url, 
        alcohol_img=alcohol_img, 
        alcohol_vol=alcohol_vol, 
        alcohol_timestamp=alcohol_timestamp, 
        drink_name=drink_name, 
        alcohol_name=alcohol_name, 
        juice_img=juice_img,
        juice_vol=juice_vol,
        juice_timestamp=juice_timestamp,
        juice_name=juice_name,
        syrup_name=syrup_name,
        syrup_img=syrup_img,
        syrup_vol=syrup_vol,
        syrup_timestamp=syrup_timestamp)


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
