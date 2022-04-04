from flask import Flask, render_template

App = Flask(__name__)



@App.route("/")
def search():
    return render_template("Login.html")
@App.route("/Register")
def home():
    return render_template("Register.html")


if __name__ == "__main__":
    App.run()