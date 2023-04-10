from flask import Flask, render_template, request, redirect, session

application = Flask(__name__)
application.secret_key = (
    "This is my secret key, there are many like it, but this one is mine"
)


@application.route("/")
def index():
    session.clear()
    return render_template("index.html")


@application.route("/process", methods=["POST"])
def process():
    for key in request.form:
        session[key] = request.form[key]
    return redirect("/result")


@application.route("/result")
def show_result():
    return render_template("result.html")


if __name__ == "__main__":
    application.run(debug=True, port=5000)
