import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "Welcome!"


@app.route("/How are you")
def how_are_you():
    return "I'm fine, how about you?"


@app.route("/about")
def about():
    return "I'm just a small Flask app :)"


@app.route("/info")
def info():
    return "I have been created just to pass Pau's subject."


if __name__ == "__main__":
    app.run()
