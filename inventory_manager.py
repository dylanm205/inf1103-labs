import json

class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def update_stock(self, quantity):
        if quantity < 0:
            print("Stock cannot be negative.")
            return
        self.__stock = quantity

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")

    def to_dict(self):
        return {"id": self.__product_id, "name": self.__name,
                "price": self.__price, "stock": self.__stock}

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self):
        print("\nCurrent Inventory")
        print("-" * 48)
        for product in self.__products:
            product.display_information()
        print("-" * 48)

    def to_list(self):
        product_list = []
        for product in self.__products:
            product_list.append(product.to_dict())
        return product_list

example_products = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
]

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


def display_all(inventory):
    print("\nCurrent Inventory")
    print("-" * 48)
    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | Price: ${product['price']:.2f} | Stock: {product['stock']}")
    print("-" * 48)

def add_product(inventory):
    product_id, product_name, price, stock = get_valid_input()
    product = {"id": product_id, "name": product_name, "price": price, "stock": stock}
    inventory.append(product)
    save_inventory(inventory)
    print("\nProduct added successfully!")  


def load_inventory():
    try:
        with open("inventory.json", "r") as f:
            inventory = json.load(f)
        print("inventory.json found.")
        print("Inventory loaded successfully.")
        return inventory
    except FileNotFoundError:
        print("inventory.json not found. Starting with an empty inventory.")
        return []

def save_inventory(inventory):
    with open("inventory.json", "w") as f:
        json.dump(inventory, f, indent=4)

def search_product(inventory, product_id):
    for product in inventory:
        if product["id"] == product_id:
            return product
    return None

def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ")
    product = search_product(inventory, product_id)
    if product == None:
        print("\nProduct not found.")
        return

    print("\nProduct Found:")
    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")
    print()
    while True:
        user_input = input("New Stock Quantity: ")
        if user_input.isdigit() == False:
            print("Invalid input. Please enter a non-negative whole number.")
            continue
        product["stock"] = int(user_input)
        break
    print("\nStock updated successfully!")

def show_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")
    product = search_product(inventory, product_id)
    if product == None:
        print("\nProduct not found.")
        return

    print("\nProduct Found")
    print("------------------------------------------------")
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Stock: {product['stock']}")
    print("------------------------------------------------")


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
        display_all(inventory)
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