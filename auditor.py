#first commit kinda nervous!p
# increment = 0

def add_inventory():
    inventory = 0
    Fe = 0 #failed entry 
    increment = 0
    while True:
        try:
            input_value = int(input(  "Current inventory: " + str(inventory) + "\n" + "how much inventory do you want?:"))
        
            if  input_value == "quit":
                        print("total unit processed:", increment)
                        print("failed entries:", Fe)
                        break 
            
            elif input_value + inventory >= 500:
                print("Inventory cannot exceed 500")
                Fe += 1
                
            elif input_value < 0:
                print("Inventory cannot be negative")
                Fe += 1

            else:
                increment += input_value
                inventory += input_value
                print("Current inventory:", inventory)


        except(ValueError, TypeError): 
                print("Invalid input, please enter a digit greater than 0 or type 'quit' to exit")
                Fe += 1
                break




add_inventory()
