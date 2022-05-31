total = 0
expenses = []
num_expenses = int(input("enter # of expenses:"))
for i in range(7):
    expenses.append(float(input("enter an expense :")))

total = sum(expenses)

print("you spent $" , total, sep='')     