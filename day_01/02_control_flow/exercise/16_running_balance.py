total = 0
running = True
while running:
    command = input("Provide command: ")

    if command == "add":
        var=int(input("Give number:"))
        total= var+total
        print(total)
        # TODO: Ask for number
        # TODO: Add that number to the total
        # TODO: Print the current total
        pass
    if command == "sub":
        var = int(input("Give number:"))
        total = var + total
        print(total)
        # TODO: Ask for number
        # TODO: Add that number to the total
        # TODO: Print the current total
        pass
    elif command == "exit":
        running = False
