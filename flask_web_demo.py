# save this as app.py
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    print("get request string")
    return render_template("index.html")

@app.route('/', methods = ['POST'])
def home_post():
    dim1 = request.form["dim_1"]
    dim2 = request.form["dim_2"]
    dim3 = request.form["dim_3"]

    volume = float(dim1) * float(dim2) * float(dim3)
    volume = int(volume)
    print(volume)

    return render_template("index.html",output = volume)


app.run(host="0.0.0.0")
