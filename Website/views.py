# File with the functions
# from datetime import datetime,timedelta
from flask import Blueprint, render_template
# , redirect, url_for, request, flash,session
from flask import Flask


views = Blueprint('views',__name__,static_folder="static/")

# Home page function
@views.route("/home", methods=["POST","GET"])
def home():
    return render_template("home.html")

@views.route("/welcome", methods=["POST","GET"])
def welcome():
    return render_template("welcome.html")

@views.route("/drag")
def drag():
    return render_template("drag.html")

@views.route("/mcq")
def mcq():
    return render_template("mcq.html")

@views.route("/image")
def image():
    return render_template("image.html")

@views.route("/newUser")
def newUser():
    return render_template("newUser.html")

@views.route("/correct")
def correct():
    return render_template("correct.html")

@views.route("/wrong1")
def wrong1():
    return render_template("wrong1.html")

@views.route("/wrong2")
def wrong2():
    return render_template("wrong2.html")

@views.route("/wrong3")
def wrong3():
    return render_template("wrong3.html")