import json

# first commit kinda nervous!

def get_valid_id():
    while True:
        id_value = input("What is your product ID ?")

        if id_value == "quit":
            return "quit"

        try:
            id_value = int(id_value)

            if id_value <= 1000:
                print("------Id starts from 1000!------")
                return False

            for product in inventory: #product is the inner list of the list inventory 
                if id_value == product[0]: #search the id of each inner list against the list of product
                    return product 

                else:
                    pass
            new_product = [id_value,"nil",0]
            return new_product
                     
        except (ValueError, TypeError):
            print("------Invalid input, please enter an id greater than 1000 or type 'quit' to exit------")
            return False



def get_valid_description(inventory):
    while True:
        description_value = input("What item are you processing")

        if description_value == "quit": #make sure to call reportfunction 
            return "quit"

        try: #nothing to check, string input 
            str(description_value) #just in case 
            return description_value

        except (ValueError, TypeError):
            print("------Invalid input, please enter a digit greater than 0 or type 'quit' to exit------")
            return False

def get_valid_quantity(inventory):
    while True:
        quantity_value = input(
            "Current inventory: " + str((inventory[2])) +
            "\nHow much inventory do you want?: "
        )

        if quantity_value == "quit":
            print("-----Cannot quit after entering product description!------")

        try:
            quantity_value = int(quantity_value)

            if quantity_value <= 0:
                print("------Inventory cannot be less than zero------")
                return False

            elif quantity_value + inventory > 500:
                print("------!!!!Inventory cannot exceed 500, OVERSTOCK ALERT!!!------")
                return False

            return quantity_value

        except (ValueError, TypeError):
            print("------Invalid input, please enter a digit greater than 0 or type 'quit' to exit------")
            return False


def process_delivery(product_id,valid_description,current_total, new_value): #collect all 3 values of list, quantity tally done here
    new_total = current_total + new_value
    with open("inventory.json", "w") as f:
        f.write(str([product_id,valid_description,new_total]))


    return new_total


def calculate_tax(quantity_value):
    taxable_amount = quantity_value *0.10
    return taxable_amount 


def generate_report(total_units, failed_attempts):
    print("------Inventory Report------")
    print("Total unit processed:", total_units)
    print("Failed entries:", failed_attempts)

#ask if can use Json 
def persistence(): 
    try:
        f = open("inventory.json", "r") #variable f will be assigned the file opened with flag -r
        inventory=  json.load(f) #convert json file into python, load the python value as "inventory"
        return inventory 

    except (FileNotFoundError):
        inventory = [[1000, "nil", 0]] #create a variable called inventory

        f = open("inventory.json", "w") #create inventory.json file , -w is important
        json.dump(inventory, f) #convert the python value of Inventory into Json 
        f.close()

        return inventory
        



inventory = persistence()
failed_attempts = 0
total_tax = 0
quanity_value = 0

while True:
    if quantity_value!= 0:
        print("taxable amount:$", calculate_tax(quantity_value))

    product_description = get_valid_description (inventory[1])
    quantity_value = get_valid_quantity(inventory[2])


    if get_valid_id() == "quit": #user can only quit while editing ID
        generate_report(inventory, failed_attempts)
        break 

    if quantity_value is False:
        failed_attempts += 1
        continue

    new_inventory = process_delivery(inventory, quantity_value) #adds current input with previous input, returning sum as (new total)


    inventory = new_inventory #slots the return value "new total" of "new inventory" into the variable inventory
    total_tax += calculate_tax(quantity_value) #assigning return value called amount from calculate tax funcion into total tax

    # done
    # persistent() is done (load inventory function is this )
    # id funciton is done

    #to do
    # add the 2 other function to update descripton and quantiy
    # create a function similar to process_inventory, but records each list as seperate, regarless of ID
    #convert the rest of quantity function to grep from innerlist value
    #integration 

    
