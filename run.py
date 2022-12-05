from flask import Flask, render_template
import os
import json


app = Flask(__name__) # first argument is the name of the application's module

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


@app.route("/contact")
def contact():
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