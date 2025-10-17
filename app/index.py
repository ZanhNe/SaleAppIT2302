from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def trang_chu():
    name = "Diep Bao Doanh"
    return render_template("index.html", name=name)

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)


