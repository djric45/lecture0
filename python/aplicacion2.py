from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
	headline = "Hello, world"
	return render_template("hello3.html", headline=headline)

@app.route("/adios")
def adios():
	headline = "adios"
	return render_template("hello3.html", headline=headline)