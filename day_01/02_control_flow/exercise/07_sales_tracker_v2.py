# TODO: Ask the user how many items will be calculated
input_count = int(input("How many items:"))
total = 0

# TODO: Use a for loop to ask for more than one cost and count
for item_price in range(input_count):
    item_cost = int(input("Enter Price Item:"))
    item_count = int(input("Enter Count of Item :"))
    item_total = item_cost * item_count
    total += item_total

print("Total of the price:", total)
