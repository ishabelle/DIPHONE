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


@app.route("/h-seria-nova")
def price_list_huawei_nova():
    return render_template("cennik-huawei-nova.html")


@app.route("/h-seria-y")
def price_list_huawei_y():
    return render_template("cennik-huawei-y.html")


@app.route("/h-seria-honor")
def price_list_huawei_honor():
    return render_template("cennik-huawei-honor.html")


@app.route("/s-seria-a")
def price_list_samsung_a():
    return render_template("cennik-samsung-a.html")


@app.route("/s-seria-m")
def price_list_samsung_m():
    return render_template("cennik-samsung-m.html")


@app.route("/s-seria-s")
def price_list_samsung_s():
    return render_template("cennik-samsung-s.html")


@app.route("/s-seria-z")
def price_list_samsung_z():
    return render_template("cennik-samsung-z.html")


@app.route("/s-seria-note")
def price_list_samsung_note():
    return render_template("cennik-samsung-note.html")


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
