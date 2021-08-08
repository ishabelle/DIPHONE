from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/glowna")
def main_page_pl():
    return render_template("glowna.html")


# na heroku:
# if __name__ == "__main__":
#     app.debug = True
#     PORT = process.env.PORT | '8080'
#     app.run()
#     app.run(
#         host='localhost',
#         port=PORT,
#         debug=True,
#     )


# lokalnie:
if __name__ == "__main__":
    app.debug = True
    # PORT = process.env.PORT | '8080'
    app.run()
    app.run(
        host='localhost',
        # port=PORT,
        port=5000,
        debug=True
    )
