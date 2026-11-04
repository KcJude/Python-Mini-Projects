# Monthly Expense Recorder.
# Records your expenses for the month and continues adding it to the already existing expenses.
# Tells you when you've equalled the monthly budget and when you've exceeded it. 

monthly_budget = input('Please enter your monthly expense budget: ')
actual_monthly_budget = int(monthly_budget)

expenses = 0

while True:
    expense = input("Please enter your latest expenses: ")
    real_expense = int(expense)
    expenses += real_expense
    print()
    print("-------------------------------------------------")
    print(f"Your cumulated expenses for the month is {expenses} now")
    print("-------------------------------------------------")
    print()