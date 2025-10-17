from flask import Flask, render_template
import dao

app = Flask(__name__)


@app.route("/")
def trang_chu():
    cates = dao.load_categories()
    products = dao.load_products()
    return render_template("index.html", cates=cates, products=products)


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
