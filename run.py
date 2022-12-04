from flask import Flask, render_template
import os

app = Flask(__name__) # first argument is the name of the application's module

@app.route("/") # route decorator to tell Flask what URL should trigger the function that follows.
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
        # debug should not be True in a production application or for final project submission
        # as this allows for arbitrary code to run, which is a security flaw
    )