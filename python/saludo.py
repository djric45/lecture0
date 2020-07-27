from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
	return "Hola mundo!!!"

@app.route("/<string:name>")
def hola(name):
	name = name.capitalize()
	return f"<h1>Hola {name} </h1>"
