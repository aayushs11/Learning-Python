#Expendses of the week

Sun=1500
Mon=1800
Tue=1200
Wed=1500
Thu=1200
Fri=3000
Sat=1400

Expenses= Sun+Mon+Tue+Wed+Thu+Fri+Sat

#Average expenses per day in decimal
avg_expenses = Expenses//7


print(f"The total expenses of the week is {Expenses}")
print(f"The average expenses of the day is {avg_expenses}")