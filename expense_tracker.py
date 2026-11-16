print("================================")
print("    PERSONAL EXPENSE TRACKER")
print("================================")

name = input("Enter your name: ")

budget = float(input("Enter your total budget: "))

expenses = []

# Load previously saved expenses
try:
    with open("expenses.txt", "r") as file:
        for line in file:
            expense_name, amount = line.strip().split(",")
            expenses.append((expense_name, float(amount)))

except FileNotFoundError:
    pass


while True:

    print("\n================================")
    print("           MAIN MENU")
    print("================================")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spending")
    print("4. Show Remaining Budget")
    print("5. Exit")
    print("6. Reset All Expenses")

    choice = input("\nEnter your choice: ")

    # Option 1: Add Expense
    if choice == "1":

        expense_name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expenses.append((expense_name, amount))

        with open("expenses.txt", "a") as file:
            file.write(f"{expense_name},{amount}\n")

        print("\nExpense added successfully!")

    # Option 2: View Expenses
    elif choice == "2":

        if len(expenses) == 0:
            print("\nNo expenses added yet!")

        else:
            print("\n------ YOUR EXPENSES ------")

            for expense_name, amount in expenses:
                print(expense_name, ":", amount)

    # Option 3: Show Total Spending
    elif choice == "3":

        total = sum(amount for expense_name, amount in expenses)

        print("\nTotal Spending: Rs.", total)

    # Option 4: Show Remaining Budget
    elif choice == "4":

        total = sum(amount for expense_name, amount in expenses)

        remaining = budget - total

        print("\nYour Budget: Rs.", budget)
        print("Total Spending: Rs.", total)
        print("Remaining Budget: Rs.", remaining)

        if remaining < 0:
            print("Warning! You have exceeded your budget.")

        elif remaining == 0:
            print("Your entire budget has been spent!")

        else:
            print("You are within your budget!")

    # Option 5: Exit
    elif choice == "5":

        print("\nThank you for using Expense Tracker!")
        print("Goodbye", name, "!")
        break

    # Option 6: Reset All Expenses
    elif choice == "6":

        confirm = input(
            "\nAre you sure you want to delete all expenses? (yes/no): "
        )

        if confirm.lower() == "yes":

            expenses.clear()

            with open("expenses.txt", "w") as file:
                pass

            print("\nAll expenses deleted successfully!")

        else:
            print("\nReset cancelled!")

    # Invalid Choice
    else:
        print("\nInvalid choice! Please try again.")