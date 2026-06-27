# Ask the cost and pax or count for three separate items
item_cost_1 = int(input("Enter Price of Item 1:"))
item_count_1 = int(input("Enter Count of Item 1:"))

item_cost_2 = int(input("Enter Price of Item 2:"))
item_count_2 = int(input("Enter Count of Item 2:"))

item_cost_3 = int(input("Enter Price of Item 3:"))
item_count_3 = int(input("Enter Count of Item 3:"))

# Calculate the total
total = item_cost_1 * item_count_1 + item_cost_2 * item_count_2 + item_cost_3 * item_count_3
print(f"{item_cost_1}*{item_count_1}+{item_cost_2}*{item_count_2}{item_cost_3}*{item_count_3}={total}")
print("Total is:",total)