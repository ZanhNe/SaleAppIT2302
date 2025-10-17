from flask import Flask, render_template
import dao

app = Flask(__name__)


@app.route("/")
def trang_chu():
    cates = dao.load_categories()
    return render_template("index.html", cates=cates)


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
