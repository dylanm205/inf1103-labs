import json
from product_factory import ProductFactory
from can_be_shipped import CanBeShipped
from inventory import Inventory
from supplier import Supplier

failed = 0

def get_valid_input():
    global failed
    print("\nAdd New Product")
    while True:
        product_id = input("Product ID: ")
        if product_id.strip() == "":
            print("Invalid input. Product ID cannot be empty.")
            failed += 1
            continue

        product_name = input("Product Name: ")
        if product_name.strip() == "":
            print("Invalid input. Product name cannot be empty.")
            failed += 1
            continue
        if product_name.strip().isdigit():
            print("Invalid input. Product name cannot be a number.")
            failed += 1
            continue

        while True:
            price_input = input("Price: ")
            if "-" in price_input:
                print("Invalid input. Please enter a non-negative price.")
                failed += 1
                continue
            if price_input.replace(".", "", 1).isdigit() == False:
                print("Invalid input. Please enter a valid price.")
                failed += 1
                continue
            price = float(price_input)
            break

        while True:
            user_input = input("Stock Quantity: ")
            if "-" in user_input:
                if user_input.strip("-").isdigit() == True:
                    print("Invalid input. Please enter a non-negative stock quantity.")
                    failed += 1
                    continue
            if user_input.isdigit() == False:
                print("Invalid input. Please enter a valid stock quantity.")
                failed += 1
                continue
            return product_id, product_name, price, int(user_input)



def add_product(inventory):
    product_id, product_name, price, stock = get_valid_input()
    while True:
        product_type = input("Product Type (1 = Physical, 2 = Digital): ")
        if product_type == "1" or product_type == "2":
            break
        print("Invalid input. Please enter 1 or 2.")

    if product_type == "1":
        product_type = "physical"
        prompt = "Weight (kg): "
    else:
        product_type = "digital"
        prompt = "Download Size (MB): "

    while True:
        value = input(prompt)
        if "-" in value:
            print("Invalid input. Please enter a non-negative number.")
            continue
        if value.replace(".", "", 1).isdigit() == False:
            print("Invalid input. Please enter a valid number.")
            continue
        value = float(value)
        break
    supplier_id = input("Supplier ID: ")
    supplier_name = input("Supplier Name: ")
    supplier_email = input("Supplier Email: ")
    supplier = Supplier(supplier_id, supplier_name, supplier_email)

    weight = 0.0
    download_size = 0.0
    if product_type == "physical":
        weight = value
    else:
        download_size = value

    product = ProductFactory.create(product_type, product_id, product_name, price, stock, supplier, weight, download_size)

    inventory.add_product(product)
    save_inventory(inventory)
    print("\nProduct added successfully!")


def load_inventory():
    inventory = Inventory()
    try:
        with open("inventory.json", "r") as f:
            data = json.load(f)
        suppliers = {}
        for item in data:
            s = item["supplier"]
            if s["supplier_id"] not in suppliers:
                suppliers[s["supplier_id"]] = Supplier(s["supplier_id"], s["name"], s["contact_email"])
            supplier = suppliers[s["supplier_id"]]
            product = ProductFactory.create(item["type"], item["id"], item["name"], item["price"], item["stock"],supplier, item.get("weight", 0.0), item.get("download_size", 0.0))
            inventory.add_product(product)
        print("inventory.json found.")
        print("Inventory loaded successfully.")
    except FileNotFoundError:
        print("inventory.json not found. Starting with an empty inventory.")
    return inventory

def save_inventory(inventory):
    with open("inventory.json", "w") as f:
        json.dump(inventory.to_list(), f, indent=4)


def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ")
    product = inventory.find_product(product_id)
    if product == None:
        print("\nProduct not found.")
        return

    print("\nProduct Found:")
    product.display_information()
    print()
    while True:
        user_input = input("New Stock Quantity: ")
        if user_input.isdigit() == False:
            print("Invalid input. Please enter a non-negative whole number.")
            continue
        product.update_stock(int(user_input))
        break
    print("\nStock updated successfully!")

def show_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")
    product = inventory.find_product(product_id)
    if product == None:
        print("\nProduct not found.")
        return

    print("\nProduct Found")
    product.display_information()
    print(product.get_fulfilment_info())


print("=========================================")     
print("INVENTORY MANAGEMENT SYSTEM")
print("=========================================")
inventory = load_inventory()
print("------------MENU------------")
print("1. Display All Products\n2. Add Product\n3. Update Stock\n4. Search Product\n5. Save Inventory\n6. Exit")
print("----------------------------")
while True:
    option = input("Enter Option:")
    if option == "1":
        inventory.display_all()
    elif option == "2":
        add_product(inventory)
    elif option == "3":
        update_stock(inventory)
    elif option == "4":
        show_product(inventory)
    elif option == "5":
        print("\nSaving inventory...")
        save_inventory(inventory)
        print("Inventory saved successfully to inventory.json.")
    elif option == "6":
        print("\nSaving inventory before exit...")
        save_inventory(inventory)
        print("Inventory saved successfully.")
        print("\nThank you for using Inventory Management System.")
        print("Program terminated.")
        break
    else:
        print("\nInvalid option. Please try again.")