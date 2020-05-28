##
## EPITECH PROJECT, 2020
## views
## File description:
## views
##

from app import app
from flask import render_template, Flask
from app import models
from app import controller
import jinja2

@app.route('/', methods=['GET'])
def route_index():
    return render_template("index.html")

@app.route('/user/<username>', methods=['POST'])
def route_add_user(username):
    return render_template("index.html",
        title="Hello " + username,
        myContent="My SUPER content for " + username + "!!!")

@app.route('/signout', methods=['POST'])
def route_signout():
    return

@app.route('/signin', methods=['POST'])
def route_signin():
    control = models.connection_data()
    log_in = controller.interact()
    rtn_value = log_in.connect_in(control.rtn_connect())
    if (rtn_value == 1):
        return (render_template("index.html"))
    else:
        return (render_template("profile.html"))

@app.route('/register', methods=['POST'])
def route_register():
    control = models.connection_data()
    log_in = controller.interact()
    rtn_value = log_in.register_user(control.rtn_connect())
    if (rtn_value == 0):
        return (render_template("profile.html"))
    else:
        return (render_template("index.html"))

@app.route('/user', methods=['GET'])
def route_user():
    return (render_template("profile.html"))

@app.route('/chart', methods=['GET'])
def route_chart():
    return (render_template("chart.html"))