from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

sergio_test = []
sergio_test2 = []

ingredients = ["lime", "orange juice", "tequila"]  # testing git

practice_data = {
    "moscow_mule": {
        "correct_ingredients": ["fresh_lime_juice", "ginger_syrup", "vodka", "ginger_beer"]
    },
    "pina_colada": {
        "correct_ingredients": ["tequila", "cream_of_coconut", "pineapple_juice", "fresh_lime_juice"]
    },
    "margarita": {
        "correct_ingredients": ["fresh_lime_juice", "simple_syrup", "orange_tequila", "tequila"]
    }
}

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
        "correct_ingredients": ["Fresh Lime Juice", "Ginger Syrup", "Vodka", "Ginger Beer"]
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
        "correct_ingredients": ["Tequila", "Cream of Coconut", "Pineapple Juice", "Fresh Lime Juice"]
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
        "image": "static/images/margarita.png",
        "learnUrl":"http://127.0.0.1:5000/learn/margarita",
        "quizUrl":"http://127.0.0.1:5000/quiz/margarita",
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
        "image": "/static/images/pina_colada.png",
        "learnUrl":"http://127.0.0.1:5000/learn/pina_colada",
        "quizUrl":"http://127.0.0.1:5000/quiz/pina_colada",
        "video": "https://www.youtube.com/embed/nyzeEdPkfOw",
        "facts": {
            "fun_fact": " Pina means pineapple and colada means strained",
            "taste": "Pina Colada tastes like pineapple and coconut",
            "goes_well_with": "Seafood"
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
        "learnUrl":"http://127.0.0.1:5000/learn/moscow_mule",
        "quizUrl":"http://127.0.0.1:5000/quiz/moscow_mule",
        "image": "/static/images/moscow_mule.png",
        "video": "https://www.youtube.com/embed/FirpAjZomHA",
        "facts": {
            "fun_fact": "This cocktail is not from Moscow. It was invented at a Hollywood bar!",
            "taste": "Moscow Mule tastes like ginger",
            "goes_well_with": "Spicy Food"
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


@ app.route("/")
def home():
    return render_template("home.html", cocktails=cocktails)


# @ app.route("/home")
# def home():
#     return render_template("home.html", cocktails=cocktails)


@ app.route("/practice")
def practicePage(name=None):
    return render_template("practice.html")

@ app.route("/practice/<name>")
def practiceCocktailPage(name=None):
    global practice_data
    global cocktails

    ingredients_in_order = practice_data[name]["correct_ingredients"]
    ingredients_names_in_order = data[name]["correct_ingredients"]

    alcohols = cocktails[name]["ingredients"]["alcohol"]
    juices = cocktails[name]["ingredients"]["juice"]
    syrups = cocktails[name]["ingredients"]["syrup"]

    all_ingredients_with_volume = dict()

    all_ingredients_with_volume.update(alcohols)
    all_ingredients_with_volume.update(juices)
    all_ingredients_with_volume.update(syrups)

    names_and_volumes = dict()

    for ingredient in ingredients_in_order:
        names_and_volumes[ingredient] = all_ingredients_with_volume[ingredient]["volume"]

    if name == "moscow_mule":
        drink_name = "Moscow Mule"
        drink_link = "moscow_mule"
    elif name == "margarita":
        drink_name = "Margarita"
        drink_link = "margarita"
    elif name == "pina_colada":
        drink_name = "Pina Colada"
        drink_link = "pina_colada"

    drink_info = {"name":drink_name,
                "link": drink_link}

    return render_template("practice.html",
        ingredients_names_in_order=ingredients_names_in_order,
        names_and_volumes=names_and_volumes,
        all_ingredients_with_volume=all_ingredients_with_volume,
        ingredients_in_order=ingredients_in_order,
        drink_info=drink_info)


@ app.route("/learn/<name>")
def learnCocktailpage(name=None):
    
    
    drink = cocktails[name]
    print("DRINK: ", drink)
    print("Drink Name: ")
    print(drink["name"])
    video_url = drink["video"]
    



    alcohols = drink["ingredients"]["alcohol"]
    juices = drink["ingredients"]["juice"]
    syrups = drink["ingredients"]["syrup"]

    
    fun_fact = drink["facts"]

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
                           name=name,
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
                           syrup_timestamp=syrup_timestamp,
                           fun_fact=fun_fact, drink=drink)


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
