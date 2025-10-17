import json


def load_categories():
    with open("data/cates.json", encoding="utf-8") as f:
        cates = json.load(f)
        return cates

def load_products(q=None, c=None):
    with open("data/products.json", encoding="utf-8") as f:
        products = json.load(f)
        if c:
            products=[p for p in products if int(c) == int(p['cate_id'])]
        if q:
            products = [p for p in products if p["name"].find(q) >= 0]

        return products


def load_product_details(id):
    with open("data/products.json", encoding="utf-8") as f:
        products = json.load(f)
        for p in products:
            if p["id"].__eq__(id):
                return p



if __name__ == "__main__":
    print(load_products(None, 2))