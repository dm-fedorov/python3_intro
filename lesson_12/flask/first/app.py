import datetime

from flask import Flask, render_template

app = Flask(__name__)

#def histogram():


@app.route("/")
def index():
    now = datetime.datetime.now()
    if now.hour > 12:
        headline = "Обед!!!!"
    	#return "<h1>Hello, Flask!!!!</h1>"
        return render_template("index.html", headline_tpl=headline)
    else:
        headline = "Завтрак!!!!"
        return render_template("index.html", headline_tpl=headline)

@app.route("/bye")
def bye():
    headline = "Goodbye"
    return render_template("index.html", headline_tpl=headline)

#@app.route("/<string:name>")
#def hello(name):
    #return f"Hello, {name}"



