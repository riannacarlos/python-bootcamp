# Price notification template
price_notification = "The price of {} is ${}."

# TODO: Post: Latte ($3.5)

formatted_message=price_notification.format("Latte","3.5")
print(formatted_message)

# TODO: Post: Espresso ($2.75)
new_message=price_notification.format("Espresso","2.75")
print(new_message)

# TODO: Post: Cappuccino ($4.0)
formatted_message=price_notification.format("Cappuccino","4.0")
print(formatted_message)