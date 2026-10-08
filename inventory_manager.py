import json

example_products = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
]

failed = 0
deliveries_processed = 0 

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
    print("\nProduct added successfully!")        
        
def process_delivery(current_total,new_value):
     current_total += new_value
     return current_total

def calculate_tax(amount):
     tax = amount * 0.10
     return tax

def generate_report(total_units, failed_attempts):
     print("Total Deliveries Processed:", total_units)
     print("Total Failed Attempts:", failed_attempts)

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

def save_inventory(total, inventory_data):
    with open("inventory.txt", "w") as f:
        f.write(f"Total: {total}\n")
        for item in inventory_data:
            f.write(f"{item}\n")


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
    



inventory, inventorycheck = load_inventory()
if inventorycheck == []:
    print("No previous orders found.")
while True:
    input_result = get_valid_input()
    if input_result == "quit":
        save_inventory(inventory, inventorycheck)
        print("\n Order successfully saved to inventory.txt")
        generate_report(deliveries_processed, failed)
        break
    else:
        product_name, quantity = input_result
        inventory = process_delivery(inventory, quantity)
        tax = calculate_tax(quantity)
        deliveries_processed += 1
        print("Current inventory:", inventory)
        print("Tax for this delivery:", tax)
        order_id = 1000 + len(inventorycheck) + 1
        inventorycheck.append(f"{order_id}, {product_name}, {quantity}")
        print(f"\nNew Order Added:\n{order_id},{product_name},{quantity}")
