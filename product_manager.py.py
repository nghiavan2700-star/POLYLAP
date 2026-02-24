# POLYLAP product manager module
# product_manager.py
import json

DATA_FILE = "products.json"


def load_data():
    print("Loading data...")
    """
    Read data from products.json.
    If file does not exist, return empty list.
    """
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_data(products):
    """
    Save product list to products.json.
    """
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)


def _generate_new_id(products):
    """
    Generate new ID like LT01, LT02...
    Based on the largest existing number.
    """
    max_num = 0
    for p in products:
        pid = str(p.get("id", "")).upper()
        if pid.startswith("LT"):
            num_part = pid[2:]
            if num_part.isdigit():
                max_num = max(max_num, int(num_part))
    return f"LT{max_num + 1:02d}"


def _input_int(prompt, allow_empty=False, default=None):
    """
    Read an integer from input with validation.
    allow_empty=True: empty input returns default (used in update).
    """
    while True:
        try:
            price = int(input("Enter price: "))
            break
        except:
            print("Price must be an integer.")

    while True:
        try:
            quantity = int(input("Enter quantity: "))
            break
        except:
            print("Quantity must be an integer.")


def add_product(products):
    new_id = "LT" + str(len(products) + 1).zfill(2)

    name = input("Enter product name: ")
    brand = input("Enter brand: ")
    price = int(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    product = {
        "id": new_id,
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity
    }

    products.append(product)
    print("Product added successfully.")
    return products

def update_product(products):
    pid = input("Enter product ID to update: ")

    for product in products:
        if product["id"] == pid:
            product["name"] = input("New name: ")
            product["brand"] = input("New brand: ")
            product["price"] = int(input("New price: "))
            product["quantity"] = int(input("New quantity: "))
            print("Product updated.")
            return products

    print("Product not found.")
    return products


def update_product(products):
    pid = input("Enter product ID to update: ")

    for product in products:
        if product["id"] == pid:
            new_name = input("New name (leave blank to keep): ")
            if new_name != "":
                product["name"] = new_name

            new_brand = input("New brand (leave blank to keep): ")
            if new_brand != "":
                product["brand"] = new_brand

            new_price = input("New price (leave blank to keep): ")
            if new_price != "":
                product["price"] = int(new_price)

            new_qty = input("New quantity (leave blank to keep): ")
            if new_qty != "":
                product["quantity"] = int(new_qty)

            print("Product updated.")
            return products

    print("Product not found.")
    return products


def delete_product(products):
    pid = input("Enter product ID to delete: ")

    for product in products:
        if product["id"] == pid:
            products.remove(product)
            print("Product deleted.")
            return products

    print("Product not found.")
    return products

def delete_product(products):
    pid = input("Enter product ID to delete: ")

    for product in products:
        if product["id"] == pid:
            confirm = input("Confirm delete (y/n): ").lower()
            if confirm == "y":
                products.remove(product)
                print("Product deleted.")
            else:
                print("Delete cancelled.")
            return products

    print("Product not found.")
    return products

def search_product_by_name(products):
    keyword = input("Enter keyword to search: ").lower()
    found = False

    for product in products:
        if keyword in product["name"].lower():
            print("-----------------------------")
            print("ID:", product["id"])
            print("Name:", product["name"])
            print("Brand:", product["brand"])
            print("Price:", product["price"])
            print("Quantity:", product["quantity"])
            found = True

    if not found:
        print("No matching product found.")
        
def display_all_products(products):
    if len(products) == 0:
        print("Inventory is empty.")
        return

    for product in products:
        print("-----------------------------")
        print("ID:", product["id"])
        print("Name:", product["name"])
        print("Brand:", product["brand"])
        print("Price:", product["price"])
        print("Quantity:", product["quantity"])

def _print_products(products):
    """
    Print product list as a formatted table.
    """
    print("-" * 85)
    print(f"{'ID':<8} | {'Name':<35} | {'Brand':<12} | {'Price':>10} | {'Qty':>5}")
    print("-" * 85)
    for p in products:
        pid = str(p.get("id", ""))
        name = str(p.get("name", ""))
        brand = str(p.get("brand", ""))
        price = int(p.get("price", 0))
        qty = int(p.get("quantity", 0))

        if len(name) > 35:
            name = name[:32] + "..."

        print(f"{pid:<8} | {name:<35} | {brand:<12} | {price:>10} | {qty:>5}")
    print("-" * 85)