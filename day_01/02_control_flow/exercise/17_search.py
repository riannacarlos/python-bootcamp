items = ["rice", "noodles", "toyo", "spam", "coffee"]
item_to_find = "spam"

for item in items:
    food= input("Enter item:")
    if food == item_to_find:
        print("Item found")
        break
    # TODO: If item equals the item_to_find
    #  # print and exit loop
    pass
