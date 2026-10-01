failed = 0
inventory = 0 
deliveries_processed = 0 
def get_valid_input():
    global failed
    while True:
        user_input = input("Enter stock quantity (or type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            return "quit"
        else:
            if "-"  in user_input:
                    if user_input.strip("-").isdigit() == True:
                        print("Invalid input. Please enter a non-negative stock quantity.")
                        failed += 1
                        continue
            if user_input.isdigit() == False:
                        print("Invalid input. Please enter a valid stock quantity.")
                        failed += 1
                        continue
            return int(user_input)
        
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
    history = []
    try:
        with open("inventory.txt", "r") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                print(lines[i].strip())
                history.append(lines[i].strip())
        return history
    except FileNotFoundError:
        return []


     
inventorycheck = load_inventory()
if inventorycheck == []:
    print("No previous orders found.")
while True:
    input_result = get_valid_input()
    if input_result == "quit":
        generate_report(deliveries_processed, failed)
        break
    else:
        inventory = process_delivery(inventory, input_result)
        tax = calculate_tax(input_result)
        deliveries_processed += 1
        print("Current inventory:", inventory)
        print("Tax for this delivery:", tax)
