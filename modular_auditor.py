failed = 0
inventory = 0 
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

while True:
    user_input = input("Enter stock quantity (or type 'quit' to exit): ")
    if user_input.lower() == 'quit':
        print("Total Units Processed:", inventory)
        print("Total Failed Attempts:", failed)
        break
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

        user_input = int(user_input)
        if inventory + user_input > 500:
            print("Inventory exceeded 500 units! Check the inventory immediately.")
            break
        else:
            inventory += user_input
            print("Current inventory:", inventory)
