from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

ingredients = ["lime", "orange juice", "tequila"] #testing git

#data the dictionary used for quiz pages
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

# glass the array of what user adds in the glass durin quiz
glass = []

cocktails = {
    "margarita":{
        "name": "Margarita",
        "image": "../static/images/margarita",
        "glass_image": "../static/images/margarita_glass",
        "video": "https://www.youtube.com/embed/2BiT4wfRfWg",
        "ingredients":{
            "alcohol":{
                "tequila":{
                    "name": "Tequila",
                    "ingredient_image": "../static/images/tequila",
                    "volume": "1.5",
                    "timestamp": "0:15",
                },
                "orange_tequila":{
                    "name": "Orange Tequila",
                    "ingredient_image": "../static/images/orange_tequila",
                    "volume": "0.75",
                    "timestamp": "0:12",
                }
            },
            "juice":{
                "fresh_lime_juice":{
                    "name": "Fresh Lime Juice",
                    "ingredient_image": "../static/images/fresh_lime_juice",
                    "volume": "0.75",
                    "timestamp": "0:09"
                }
            },
            "syrup":{
                "simple_syrup":{
                    "name": "Simple Syrup",
                    "ingredient_image": "../static/images/simple_syrup",
                    "volume": "0.25",
                    "timestamp": "0:11"
                }
            }  
        },
        "facts": {
            "fun_fact": "Using a salt-rimmed glass makes the drink sweeter",
            "taste": "Margaritas taste like agave, from the tequila",
            "goes_well_with": "Tacos"
        }
    },
    "pina_colada":{
        "name": "Piña Colada",
        "image": "../static/images/pina_colada",
        "glass_image": "../static/images/pina_colada_glass",
        "video": "https://www.youtube.com/embed/nyzeEdPkfOw",
        "ingredients":{
            "alcohol":{
                "tequila":{
                    "name": "Tequila",
                    "ingredient_image": "../static/images/tequila",
                    "volume": "2.0",
                    "timestamp": "0:04",
                }
            },
            "juice":{
                "pineapple_juice":{
                    "name": "Pineapple Juice",
                    "ingredient_image": "../static/images/pineapple_juice",
                    "volume": "2.0",
                    "timestamp": "0:10"
                },
                "fresh_lime_juice":{
                    "name": "Fresh Lime Juice",
                    "ingredient_image": "../static/images/fresh_lime_juice",
                    "volume": "0.5",
                    "timestamp": "0:09"
                }
            },
            "syrup":{
                "cream_of_coconut":{
                    "name": "Cream of Coconut",
                    "ingredient_image": "../static/images/cream_of_coconut",
                    "volume": "2.0",
                    "timestamp": "0:06"
                }
            }  
        },
        "facts": {
            "fun_fact": "\"Piña\" means pineapple, and \"colada\" means strained",
            "taste": "Piña Coladas taste like pineapple and coconut",
            "goes_well_with": "Seafood"
        }
    },
    "moscow_mule":{
        "name": "Moscow Mule",
        "image": "../static/images/moscow_mule",
        "glass_image": "../static/images/moscow_mule_glass",
        "video": "https://www.youtube.com/embed/FirpAjZomHA",
        "ingredients":{
            "alcohol":{
                "vodka":{
                    "name": "Vodka",
                    "ingredient_image": "../static/images/vodka",
                    "volume": "2.0",
                    "timestamp": "0:10",
                },
                "ginger_beer":{
                    "name": "Ginger Beer",
                    "ingredient_image": "../static/images/ginger_beer",
                    "volume": "As you wish",
                    "timestamp": "0:13",
                }
            },
            "juice":{
                "fresh_lime_juice":{
                    "name": "Fresh Lime Juice",
                    "ingredient_image": "../static/images/fresh_lime_juice",
                    "volume": "1.0",
                    "timestamp": "0:03"
                }
            },
            "syrup":{
                "ginger_syrup":{
                    "name": "Ginger Syrup",
                    "ingredient_image": "../static/images/ginger_syrup",
                    "volume": "0.75",
                    "timestamp": "0:04"
                }
            }  
        },
        "facts": {
            "fun_fact": "This cocktail is not from Moscow. It was invented at a Hollywood bar!",
            "taste": "Moscow Mule tastes like ginger",
            "goes_well_with": "Spicy Food"
        }
    }
}


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

@ app.route("/quizResult")
def quizResult():
    return render_template("quizResult.html")

if __name__ == '__main__':
    app.run(debug=True)
