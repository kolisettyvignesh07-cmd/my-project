import datetime

def add_expense(expenses):
    print("\n--- Add Expense ---")
    print("1.Seeds  2.Fertilizer  3.Labour  4.Equipment  5.Pesticides")
    c = input("Enter category (1-5): ")
    cats = ["Seeds","Fertilizer","Labour","Equipment","Pesticides"]
    if c not in ["1","2","3","4","5"]:
        print("Invalid choice.Please pick a number from 1 to 5.")
        return

    amt = input("Enter amount: ")
    try:
        amt = float(amt)
    except ValueError:
        print("Oops, that's not a valid number. \n ")
        return

    d = datetime.date.today()
    expenses.append([d, cats[int(c)-1], amt])
    print("Expense added successfully.\n")

def view_expenses(expenses):
    print("\n--- Expense List ---")
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    t = 0
    for idx, exp in enumerate(expenses,start=1):
        print(f"{idx}. {exp[0]} | {exp[1]} | ₹{exp[2]}")

def summary(expenses):
    print("\n--- Summary ---")
    if not expenses:
        print("No data\n")
        return
    total =sum(exp[2] for exp in expenses)
    high = max(exp[2] for exp in expenses)

    print("Total entries:",len(expenses))
    print("Total spent:",total)
    print("Highest expense:",high)
    print("--------------\n")

def profit(expenses):
    inc = input("Enter income: ")
    try:
        inc = float(inc)
    except ValueError:
        print("Invalid number\n")
        return

    total_expenses = sum(exp[2] for exp in expenses)
    p = inc - total_expenses
    print("Income:",inc)
    print("Expenses:",total_expenses)

    if p>=0:
        print("You made a profit")
        print("Profit amount =",p)
    else:
        print("Oh no, you made a loss.")
        print("Loss amount = ",abs(p))
    print()

def edit_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return

    idx = input("Which one to edit: ")
    try:
        idx = int(idx)-1
    except ValueError:
        print("Please enter a valid number.\n")
        return

    if idx<0 or idx>=len(expenses):
        print("That option doesn't exist.\n")
        return

    newa = input("Enter new amount: ")
    try:
        newa=float(newa)
    except ValueError:
        print("Invalid amount entered.\n")
        return

    expenses[idx][2] = newa
    print("Expense updated.\n")

def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return

    d = input("Enter number to delete: ")
    try:
        d = int(d)-1
    except ValueError:
        print("Invalid input.\n")
        return

    if d<0 or d>=len(expenses):
        print("Could not delete. Check the number.\n")
        return

    expenses.pop(d)
    print("Deleted!!\n")

def sort_expenses(expenses):
    print("\nSort By")
    print("1.Date")
    print("2.Category")
    print("3.Amount")

    s = input("Enter choice: ")

    if s=="1":
        expenses.sort(key=lambda x:x[0])
    elif s=="2":
        expenses.sort(key=lambda x:x[1])
    elif s=="3":
        expenses.sort(key=lambda x:x[2])
    else:
        print("Invalid choice.Try again.\n")
        return

    print("Sorted\n")

def main():
    exps = []

    while True:
        print("\n======== Farm Expenses & Profit Tracker ========")
        print("1.Add")
        print("2.View")
        print("3.Summary")
        print("4.Profit/Loss")
        print("5.Edit")
        print("6.Delete")
        print("7.Sort")
        print("8.Exit")

        ch = input("Select: ")

        if ch=="1":
            add_expense(exps)
        elif ch=="2":
            view_expenses(exps)
        elif ch=="3":
            summary(exps)
        elif ch=="4":
            profit(exps)
        elif ch=="5":
            edit_expense(exps)
        elif ch=="6":
            delete_expense(exps)
        elif ch=="7":
            sort_expenses(exps)
        elif ch=="8":
            print("Bye")
            break
        else:
            print("Invalid option !!\n")

main()
