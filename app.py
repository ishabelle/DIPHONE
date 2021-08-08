from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def home_view():
    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    PORT = process.env.PORT | '3000'
    app.run()
    app.run(
        host='localhost',
        port=PORT,
        debug=True,
    )
