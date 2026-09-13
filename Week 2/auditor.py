inventory = 0 
while True:
    user_input = input("Enter stock quantity (or type 'quit' to exit): ")
    if user_input.lower() == 'quit':
        break
    else:
        if "-"  in user_input:
            if user_input.strip("-").isdigit() == True:
                print("Invalid input. Please enter a non-negative stock quantity.")
                continue
        if user_input.isdigit() == False:
            print("Invalid input. Please enter a valid stock quantity.")
            continue
        user_input = int(user_input)
        inventory += user_input
        print("Current inventory:", inventory)
