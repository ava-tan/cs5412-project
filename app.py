from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route('/')
def login():
    return render_template("index.html")


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
