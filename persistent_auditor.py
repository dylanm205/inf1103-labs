failed = 0
inventory = 0 
deliveries_processed = 0 

def get_valid_input():
    global failed
    while True:
        product_name = input("\nEnter Product name (or type 'quit' to exit): ")
        if product_name.lower() == 'quit':
            return "quit"
        if product_name.strip() == "":
            print("Invalid input. Product name cannot be empty.")
            failed += 1
            continue
        if product_name.strip().isdigit():
            print("Invalid input. Product name cannot be a number.")
            failed += 1
            continue

        while True:
            user_input = input("Enter Quantity: ") 
            if "-"  in user_input:
                    if user_input.strip("-").isdigit() == True:
                        print("Invalid input. Please enter a non-negative stock quantity.")
                        failed += 1
                        continue
            if user_input.isdigit() == False:
                        print("Invalid input. Please enter a valid stock quantity.")
                        failed += 1
                        continue
            return product_name,int(user_input)
        
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
    print("Current Orders:\n")
    history = []
    total = 0
    try:
        with open("inventory.txt", "r") as f:
            lines = f.readlines()
            if lines:
                total = int(lines[0].replace("Total:", "").strip())
                lines = lines[1:]
            for i in range(len(lines)):
                print(lines[i].strip())
                history.append(lines[i].strip())
        return total, history
    except FileNotFoundError:
        return 0, []

def save_inventory(total, inventory_data):
    with open("inventory.txt", "w") as f:
        f.write(f"Total: {total}\n")
        for item in inventory_data:
            f.write(f"{item}\n")
     
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
