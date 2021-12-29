# wikipedia reference: https://en.wikipedia.org/wiki/Mortgage_calculator
from mortgage_functions import monthly_payment, amortization_schedule

# Getting the variables from the user (r, N, P)
r = float(input('What is your annual interest rate in percentage? ')) /100 
n = float(input("How long is your loan's term in months? "))
p = float(input("What is your principal amount? "))

# Calculate monthly payment
c = monthly_payment(p, r, n)
print('Your monthly payment is $' + str(c))

# Amortization
a = amortization_schedule(p, c, r)
for key, values in a.items():
	print(key, values)