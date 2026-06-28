# TODO: Fill in the details of the items you plan to buy
orders = [
    {
    "Name": "Phone",
    "Info": "70,000",
    "Brand": "Apple",
    "Color": "Yellow"
    },
    {
    "Name": "Watch",
    "Info": "20,000",
    "Brand": "Samsung",
    "Color": "Black"
    }
]

# TODO: Print the item details in the following format (for each order):
for order in orders:
    print("Order:")
    for key,value in order.items():
        print((f"{key}: {value}"))
