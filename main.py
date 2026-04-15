# Prototype_1-Expense-Tracker-CLI

# Load at start
import json

try:
    with open("expenses_data.json", "r") as file: # read file
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []

# Add Expenses
expenses = [] 
while True:
    print("====================\n1. Add")
    print("2. View")
    print("3. Total")
    print("4. Remove")
    print("5. Exit")
    try: 
        choice = int(input("====================\nChoose: "))
    except:
        print("--------------------\nWrong input. Try again.")
        continue

    if choice == 1:
        name = str(input("Name: "))
        amount = float(input("Amount: "))
        expenses.append([name, amount]) # 0 and 1 value in position of the parameter

        with open("expenses_data.json", "w") as file: # overwrites the file
            json.dump(expenses, file)
        print("Expenses added.")

# View all expenses
    elif choice == 2:
        if not expenses:
            print("\n--------------------\nNo expenses yet. Try again.")
        else:
            for expense in expenses:
                print(f"\n====================\nHere are your expenses: {expense}")
# See total spending 
    elif choice == 3:
        total = 0
        for expense in expenses:
            total += expense[1]
        print(f"\n====================\n{total} is your total.")
# Remove expense
    elif choice == 4:
        if not expenses:
            print("\n--------------------\nNo expenses yet. Try again.")
        else:
            for i in range(len(expenses)):
                print(i + 1, expenses[i])

            remove_num = int(input("Enter the number you want to remove: "))
            removed_num = expenses.pop(remove_num - 1)

            with open("expenses_data.json", "w") as file: # overwrites the expenses_data file
                json.dump(expenses, file)

            print(f"Removed expense: {removed_num}")
# Exit 
    elif choice == 5:
        print("Thank you for using the Expense Tracker CLI!")
        break