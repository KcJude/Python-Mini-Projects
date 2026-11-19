#Expense tracking system 

monthly_budget = input("Add your monthly budget:  ")
monthly_budget_int = int(monthly_budget)
expenses = 0

while True:
    expense = input("Add an expense:  ")
    expense_int = int(expense)
    expenses += expense_int
    print(f"Your budget balance is {monthly_budget_int - expenses}")
    print("*******")
    if expenses == monthly_budget_int:
        print(f"Warning! This expense will exhaust your budget")
        print()
        print("Do you wish to continue?...Yes or No")
        answer = input("Yes/No")
        if answer == "yes":
            continue
        else:
            expenses -= expense_int
            continue
    elif expenses < monthly_budget_int:
        print("Expense added..")
        print("*******")
        continue
    else:
        print(f"You have exceeded your monthly budget of {monthly_budget_int} by {expenses - monthly_budget_int}")
        break