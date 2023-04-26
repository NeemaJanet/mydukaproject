from flask import Flask,render_template
var = Flask(__name__)
@var.route("/")
def home():

    return render_template("index.html")

@var.route("/products")
def products():
    return render_template("index2.html")

var.run()
