from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

ingredients = ["lime", "orange juice", "tequila"] #testing git

cocktails = {
    "margarita":{
        "name": "Margarita",
        "image": "",
        "video": "https://www.youtube.com/embed/2BiT4wfRfWg",
        "ingredients":{
            "alcohol":{
                "tequila":{
                    "name": "Tequila",
                    "ingredient_image": "",
                    "volume": "1.5",
                    "timestamp": "0:15",
                },
                "orange_tequila":{
                    "name": "Orange Tequila",
                    "ingredient_image": "",
                    "volume": "0.75",
                    "timestamp": "0:12",
                }
            },
            "juice":{
                "fresh_lime_juice":{
                    "name": "Fresh Lime Juice",
                    "ingredient_image": "",
                    "volume": "0.75",
                    "timestamp": "0:09"
                }
            },
            "syrup":{
                "simple_syrup":{
                    "name": "Simple Syrup",
                    "ingredient_image": "",
                    "volume": "0.25",
                    "timestamp": "0:11"
                }
            }  
        }
    },
    "pina_colada":{
        "name": "Piña Colada",
        "image": "",
        "video": "https://www.youtube.com/embed/nyzeEdPkfOw",
        "ingredients":{
            "alcohol":{
                "tequila":{
                    "name": "Tequila",
                    "ingredient_image": "",
                    "volume": "2.0",
                    "timestamp": "0:04",
                }
            },
            "juice":{
                "pineapple_juice":{
                    "name": "Pineapple Juice",
                    "ingredient_image": "",
                    "volume": "2.0",
                    "timestamp": "0:10"
                },
                "fresh_lime_juice":{
                    "name": "Fresh Lime Juice",
                    "ingredient_image": "",
                    "volume": "0.5",
                    "timestamp": "0:09"
                }
            },
            "syrup":{
                "cream_of_coconut":{
                    "name": "Cream of Coconut",
                    "ingredient_image": "",
                    "volume": "2.0",
                    "timestamp": "0:06"
                }
            }  
        }
    },
    "moscow_mule":{
        "name": "Moscow Mule",
        "image": "",
        "video": "https://www.youtube.com/embed/FirpAjZomHA",
        "ingredients":{
            "alcohol":{
                "tequila":{
                    "name": "Tequila",
                    "ingredient_image": "",
                    "volume": "1.5",
                    "timestamp": "0:15",
                },
                "orange_tequila":{
                    "name": "Orange Tequila",
                    "ingredient_image": "",
                    "volume": "0.75",
                    "timestamp": "0:12",
                }
            },
            "juice":{
                "fresh_lime_juice":{
                    "name": "Fresh Lime Juice",
                    "ingredient_image": "",
                    "volume": "0.75",
                    "timestamp": "0:09"
                }
            },
            "syrup":{
                "simple_syrup":{
                    "name": "Simple Syrup",
                    "ingredient_image": "",
                    "volume": "0.25",
                    "timestamp": "0:11"
                }
            }  
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

@ app.route("/quiz")
def quiz():
    return render_template("quiz.html")



if __name__ == '__main__':
    app.run(debug=True)
