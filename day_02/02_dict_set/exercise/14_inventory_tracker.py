from os import name


def add(inventory):
    name=input("Name:")
    info=input("Info:")
    stock=int(input("Stock:"))

    item= {
       "name": name,
       "info": info,
       "stock":stock
   }
    inventory.append(item)
    """TODO:
        Ask for item name, info, and stock
        Create a dictionary with key: name, info, stock
        Add that dictionary to inventory
    """


def remove(inventory):
    index1= int(input("Index 1:"))
    remove_index= inventory.pop(index1)
    """TODO:
        Ask for item index (int)
        Remove item in that index in inventory
    """



def read(inventory):
    index2=int(input("Index 2:"))
    print(inventory[index2])


    """TODO:
        Ask for item index (int)
                Show item in that index in inventory
    """
def show(inventory):
    print(inventory)

def main():
    """Created to test functions"""
    running = True
    item_detail = str | int | float
    inventory: list[dict[str, item_detail]] = []

    while running:
        command = input("Command: ")
        if command == "add":
            # TODO: Use add command"""
            add(inventory)
        elif command == "remove":
            #  TODO: Use remove command"""
            remove(inventory)
        elif command == "read":
            # TODO: Use read command"""
            read(inventory)
        elif command == "show":
            # TODO: Use show command"""
            show(inventory)
        elif command == "exit":
            running = False


main()
