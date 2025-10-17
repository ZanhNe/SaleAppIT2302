import json


def load_categories():
    with open("data/cates.json", encoding="utf-8") as f:
        cates = json.load(f)
        return cates


if __name__ == "__main__":
    print(load_categories())