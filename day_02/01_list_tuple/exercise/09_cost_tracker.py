def spend(expenses):
    money=int(input("Money:"))
    expenses.append(money)


def refund(expenses):
   expenses.pop(-1)


def show(expenses):
    print(expenses)



def main():
    running = True
    current_expenses = []

    while running:
        command = input("Command: ")
        if command == "spend":
            spend(current_expenses)
        elif command == "refund":
            refund(current_expenses)
        elif command == "show":
            show(current_expenses)
        elif command == "exit":
            running = False



main()
