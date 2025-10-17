from flask import Flask, render_template, request
import dao

app = Flask(__name__)

@app.route("/")
def trang_chu():
    c = request.args.get('cate')
    q = request.args.get('q')
    cates = dao.load_categories()
    products = dao.load_products(q, c)
    return render_template("index.html", cates=cates, products=products, c_id=int(c))



if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
