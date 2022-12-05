from flask import Flask, render_template, request, flash
import os
import json
if os.path.exists("env.py"):
    import env

app = Flask(__name__) # first argument is the name of the application's module
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/") # route decorator to tell Flask what URL should trigger the function that follows.
def index():
    return render_template("index.html")


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member) # where member parameter is file name and equal member value is the member dict at start of func


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash(f"Thanks {request.form.get('name')}, we have received your message")
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
        # debug should not be True in a production application or for final project submission
        # as this allows for arbitrary code to run, which is a security flaw
    )