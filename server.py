from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)



# ROUTES


@ app.route("/")
def defaultPage():
    return render_template("homepage.html")


@ app.route("/homepage")
def homePage():
    return render_template("homepage.html")





if __name__ == '__main__':
    app.run(debug=True)
