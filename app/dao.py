import json


def load_categories():
    with open("data/cates.json", encoding="utf-8") as f:
        cates = json.load(f)
        return cates

def load_products():
    with open("data/products.json", encoding="utf-8") as f:
        products = json.load(f)
        return products


if __name__ == "__main__":
    print(load_products())