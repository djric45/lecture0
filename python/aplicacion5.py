from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def index():
	return render_template("hello4.html")

@app.route("/hello", methods=["GET", "POST"])
def hello():
		if request.method == "GET":
			return "Por favor agregar nombre"
		else:
			name = request.form.get("name")
			return render_template("hello5.html", name=name)
