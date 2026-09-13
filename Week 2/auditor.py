inventory = 0 
failed = 0
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
            failed += 1
            break
        else:
            inventory += user_input
            print("Current inventory:", inventory)
