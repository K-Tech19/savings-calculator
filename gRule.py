paycheck = float(input("What is your amount of your check this pay period? \n"))
print("Nice paycheck " + str(paycheck) + "!")
print("What rule would you like to do today ?")
answer = input("Golden or Snowball ?\n").lower()

if "golden" == answer:
    expenses = round(paycheck * .75)
    saving = round(paycheck * .15)
    investments = round(paycheck * .10)
    print(f"Golden rule Breakdown ---- \n" + "Expenses: $" +str(expenses)+ "\nSavings: $" +str(saving)+"\nInvestments: $" + str(investments))
elif "snowball" == answer:
    expenses = round(paycheck * .75)
    saving = round(paycheck * .25)
    print(f"Snowball Breakdown ---- \n" + "Expenses: $" +str(expenses)+ "\nSavings: $" +str(saving))
else:
    print(f"Your selection isn't vaildate please choose the correct options of golden rule or snowball.")

    # input amount of your check
# ask if you want to implement the golden rule of saving or snow ball effect
# if "golden rule" == golden rule:
#   divide number into 3 ways
#   75% goes to expenses account
#   15% goes to savings account
#   10% goes to investment account
#   return expenses, savings, investment account balances
# elif "bigSaver" == bigSaver:
#   divide into 2 ways
#   75% goes to expenses
#   25% goes to savings account
#   return expenses & savings account balances

