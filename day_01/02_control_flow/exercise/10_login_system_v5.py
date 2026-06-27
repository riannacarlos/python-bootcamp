# Expected username and password (you can change the value)
correct_username = "user"
correct_password = "pass"
admin_username = "admin"
admin_password = "admin"

# Enter username and password
username_input = input("Please provide username: ")
password_input = input("Please provide password: ")

# TODO: Notify user if credentials are valid or invalid
if ((correct_username == username_input) and (correct_password== password_input)) or ((admin_username == username_input) and (admin_password == username_input)):
    print("Access Granted")

else:
    print("Access Denied")