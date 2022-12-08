from flask import Flask, render_template
from flask import request, redirect
import azure.functions as func
import logging
# from CreateUser import main as createUser
# from CreateUser.__init__ import main as createUser
# from CreateUser.__init__ import login_blueprint

app = Flask(__name__, template_folder="templates")


@app.route('/')
def login():
    return render_template("index.html")


@app.route('/signup', methods=['POST'])
def signup():
    print(request.form['email'])
    return render_template('form.html')


# app.register_blueprint(login_blueprint)


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/form')
def form():
    return render_template("form.html")


@app.route('/generate')
def generate():
    return render_template("generate.html")


@app.route('/recommended')
def recommend():
    return render_template("recommended.html")


@app.route('/lists')
def lists():
    return render_template("lists.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
