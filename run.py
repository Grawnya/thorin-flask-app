from flask import Flask
import os

app = Flask(__name__) # first argument is the name of the application's module

@app.route("/") # route decorator to tell Flask what URL should trigger the function that follows.
def index():
    return '<h1>Hello</h1> <h2>World</h2>'

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
        # debug should not be True in a production application or for final project submission
        # as this allows for arbitrary code to run, which is a security flaw
    )