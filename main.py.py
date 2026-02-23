import json

DATA_FILE = "products.json"

# ==============================
# ĐỌC / GHI FILE
# ==============================

def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(products):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

# ==============================
# CHỨC NĂNG SẢN PHẨM
# ==============================

def display_all_products(products):
    if not products:
        print("Kho hàng trống")
        return

    print("\n===== DANH SÁCH LAPTOP =====")
    for p in products:
        print("-" * 40)
        print(f"Mã sản phẩm: {p["id"]}")
        print(f"Tên sản phẩm: {p['name']}")
        print(f"Thương hiệu: {p['brand']}")
        print(f"Giá: {p['price']} VNĐ")
        print(f"Số lượng: {p['quantity']}")

def add_product(products):
    product_id = f"LT{len(products) + 1:02d}" 
    name = input("Nhập tên của sản phẩm: ")
    brand = input("Nhập thương hiệu: ")

    while True:
        try:
            price = int(input("Nhập giá: "))
            break
        except ValueError:
            print("Giá phải là số nguyên.")

    while True:
        try:
            quantity = int(input("Nhập số lượng: "))
            break
        except ValueError:
            print("Số lượng phải là số nguyên.")

    products.append({
        "id": product_id,
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity
    })

    print("Đã thêm sản phẩm thành công.")

def update_product(products):
    product_id = input("Nhập mã sản phẩm cần cập nhật: ")

    for p in products:
        if p["id"] == product_id:
            p["name"] = input("Tên mới: ")
            p["brand"] = input("Thương hiệu mới: ")

            while True:
                try:
                    p["price"] = int(input("Giá mới: "))
                    break
                except ValueError:
                    print("Giá phải là số.")

            while True:
                try:
                    p["quantity"] = int(input("Số lượng mới: "))
                    break
                except ValueError:
                    print("Số lượng phải là số.")

            print("Cập nhật thành công.")
            return

    print("Không tìm thấy sản phẩm.")

def delete_product(products):
    product_id = input("Nhập mã sản phẩm cần xóa: ")

    for p in products:
        if p["id"] == product_id:
            products.remove(p)
            print("Đã xoá sản phẩm.")
            return

    print("Không tìm thấy sản phẩm.")

def search_product_by_name(products):
    keyword = input("Nhập từ khoá tìm kiếm: ").lower()
    found = False

    for p in products:
        if keyword in p["name"].lower():
            print("-" * 40)
            print(f"Mã: {p['id']}")
            print(f"Tên: {p['name']}")
            print(f"Hãng: {p['brand']}")
            print(f"Giá: {p['price']} VNĐ")
            print(f"Số lượng: {p['quantity']}")
            found = True

    if not found:
        print("Không tìm thấy sản phẩm nào phù hợp.")

# ==============================
# GIAO DIỆN CHÍNH
# ==============================

def main():
    products = load_data()

    while True:
        print("\n===== POLYLAP =====")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm sản phẩm")
        print("3. Cập nhật sản phẩm")
        print("4. Xóa sản phẩm")
        print("5. Tìm kiếm sản phẩm theo tên")
        print("0. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            display_all_products(products)
        elif choice == "2":
            add_product(products)
        elif choice == "3":
            update_product(products)
        elif choice == "4":
            delete_product(products)
        elif choice == "5":
            search_product_by_name(products)
        elif choice == "0":
            save_data(products)
            print("Đã lưu dữ liệu. Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()