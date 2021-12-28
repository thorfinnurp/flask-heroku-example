"""Flask App Project."""

from flask import Flask, jsonify
from flask import render_template, request
from threading import Thread
import sys, pygame, ctypes
from keras.models import Model
from time import time
from flask import redirect
import wheel as wheel_functions
import random
import math
app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    json_data = {'Hello': 'World!'}
    return jsonify(json_data)

@app.route("/", methods=['GET', 'POST'])
def home():
    global name
    global name2
    global game_loop

    if request.method == 'POST':
        # Then get the data from the form
        name = request.form['value']
        return render_template("home.html", value=name)
    else:
        return render_template("home.html", value=name)


if __name__ == '__main__':
    app.run()
