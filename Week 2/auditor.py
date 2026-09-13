inventory = 0 
while True:
    user_input = input("Enter stock quantity (or type 'quit' to exit): ")
    if user_input.lower() == 'quit':
        break
    else:
        if user_input.isdigit() == False:
            print("Invalid input. Please enter a valid stock quantity.")
            continue
        user_input = int(user_input)
