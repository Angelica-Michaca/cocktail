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
