from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template("glowna.html")


@app.route("/glowna")
def main_page_pl():
    return render_template("glowna.html")


@app.route("/o_nas")
def about_us_pl():
    return render_template("o_nas.html")


@app.route("/kontakt")
def contact_us_pl():
    return render_template("kontakt.html")


@app.route("/dla_firm")
def for_company():
    return render_template("dla_firm.html")


@app.route("/cennik")
def price_list():
    return render_template("cennik.html")


@app.route("/cennik-pozostale")
def price_list_another():
    return render_template("cennik-pozostale.html")


@app.route("/cennik-huawei")
def price_list_huawei():
    return render_template("cennik-huawei.html")


@app.route("/cennik-samsung")
def price_list_samsung():
    return render_template("cennik-samsung.html")


@app.route("/cennik-iphone")
def price_list_iphone():
    return render_template("cennik-iphone.html")


@app.route("/cennik-xiaomi")
def price_list_xiaomi():
    return render_template("cennik-xiaomi.html")


@app.route("/cennik-sony")
def price_list_sony():
    return render_template("cennik-sony.html")


@app.route("/cennik-lg")
def price_list_lg():
    return render_template("cennik-lg.html")


@app.route("/h-seria-mate")
def price_list_huawei_mate():
    return render_template("cennik-huawei-mate.html")


@app.route("/h-seria-p")
def price_list_huawei_p():
    return render_template("cennik-huawei-p.html")


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
