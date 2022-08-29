# save this as app.py
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    print("get request string")
    return render_template("index.html")

@app.route('/', methods = ['POST'])
def home_post():
    print("get post request")
    return render_template("index.html")


app.run(host="0.0.0.0")
