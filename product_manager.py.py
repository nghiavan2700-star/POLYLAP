# product_manager.py
import json

DATA_FILE = "products.json"


def load_data():
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
        s = input(prompt).strip()
        if allow_empty and s == "":
            return default
        if s.isdigit():
            return int(s)
        print("Invalid input. Please enter an integer.")


def add_product(products):
    """
    Ask user for new product info, auto-generate ID, add to list.
    Return updated list.
    """
    new_id = _generate_new_id(products)
    print("New product ID:", new_id)

    name = input("Enter product name: ").strip()
    brand = input("Enter brand: ").strip()
    price = _input_int("Enter price (integer): ")
    qty = _input_int("Enter quantity (integer): ")

    product = {
        "id": new_id,
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": qty
    }

    products.append(product)
    print("Product added.")
    return products


def update_product(products):
    """
    Update product by ID. If not found, show message.
    If found, allow updating name, brand, price, quantity.
    Press Enter to keep old value.
    """
    pid = input("Enter product ID to update (e.g., LT01): ").strip().upper()

    for p in products:
        if str(p.get("id", "")).upper() == pid:
            print("Product found. Press Enter to keep current value.")

            new_name = input(f"Name ({p['name']}): ").strip()
            if new_name != "":
                p["name"] = new_name

            new_brand = input(f"Brand ({p['brand']}): ").strip()
            if new_brand != "":
                p["brand"] = new_brand

            p["price"] = _input_int(
                f"Price ({p['price']}): ",
                allow_empty=True,
                default=p["price"]
            )

            p["quantity"] = _input_int(
                f"Quantity ({p['quantity']}): ",
                allow_empty=True,
                default=p["quantity"]
            )

            print("Product updated.")
            return products

    print("Product ID not found.")
    return products


def delete_product(products):
    """
    Delete product by ID.
    """
    pid = input("Enter product ID to delete (e.g., LT01): ").strip().upper()

    for i, p in enumerate(products):
        if str(p.get("id", "")).upper() == pid:
            confirm = input("Confirm delete? (y/n): ").strip().lower()
            if confirm == "y":
                products.pop(i)
                print("Product deleted.")
            else:
                print("Delete cancelled.")
            return products

    print("Product ID not found.")
    return products


def search_product_by_name(products):
    """
    Search products by keyword in name (case-insensitive).
    Display all matches.
    """
    keyword = input("Enter keyword: ").strip().lower()
    results = [p for p in products if keyword in str(p.get("name", "")).lower()]

    if not results:
        print("No matching products found.")
        return

    print("Matching products:", len(results))
    _print_products(results)


def display_all_products(products):
    """
    Display all products in a readable table.
    If empty, show message.
    """
    if not products:
        print("Inventory is empty.")
        return
    _print_products(products)


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