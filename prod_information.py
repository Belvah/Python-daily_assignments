#Create a dictionary to store product information (name, price, quantity). Allow users to add, update, and remove items from the inventory.

inventory = {} #initialize an empty dictionary to store product information

def add_product(name, price, quantity): #parameter name, price, quantity

    inventory[name] = {"price": price, "quantity": quantity} #uses the name as the key and a nested dictionary to store price and quantity

def update_product(name, price=None, quantity=None):
    if name in inventory:
        if price is not None:
            inventory[name]["price"] = price
        if quantity is not None:
            inventory[name]["quantity"] = quantity

def remove_product(name):
    if name in inventory:
        del inventory[name]

       