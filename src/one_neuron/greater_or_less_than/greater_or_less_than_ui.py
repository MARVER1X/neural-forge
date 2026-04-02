import greater_or_less_than as neuron

# User Interface
# Selecting required task
while True:
    task = ""
    while True:
        task = input("\nSelect task to perform \n1: Greater than \n2: Less than \n3: Quit \nEnter 1-3: ")
        if task == "1" or task == "2" or task == "3":
            break
        else:
            print("\nInvalid Input\n")
    if task == "3":
        print("\nShutting down neuron...")
        break
    print("\nEnter only values within 0-9 or thier string representation zero-nine\n")
    while True:
        try:
            # Collect two raw inputs from the user as strings
            # encoder_router in neuron handles type detection and validation internally
            user_input = [input("Enter A: "), input("Enter B: ")]
            # Handling equal values in UI
            if neuron.encoder_router(user_input) - neuron.encoder_router(user_input, 1) == 0:
                result = 0.5
            else:
                result = neuron.forward(user_input)
            # Using 0 as geometric boundary and 0.5 for decision treshhold based on training data (rule: x > 0.5 True, x = 0.5 Eqaul, x <= 0.5 False)
            if task == "1":
                if result > 0.5:
                    print("Result: True")
                    break
                elif result == 0.5:
                    print("Result: Equal")
                    break
                else: 
                    print("Result: False")
                    break
            elif task == "2":
                if result < 0.5:
                    print("Result: True")
                    break
                elif result == 0.5:
                    print("Result: Equal")
                    break
                else: 
                    print("Result: False")
                    break
        except Exception as e:
            print(e)