from flask import Flask, render_template

app = Flask(__name__, template_folder = "templates")

@app.route('/')
def login():
  return render_template("index.html")

@app.route('/home')
def home():
  return render_template("home.html")

@app.route('/form')
def form():
  return render_template("form.html")

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80)