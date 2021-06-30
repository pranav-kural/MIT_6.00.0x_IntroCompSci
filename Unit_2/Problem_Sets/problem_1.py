"""
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print:

Remaining balance: 813.41
"""
"""
A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""
"""
pseudo-code 

1 - calculate unpaid balance (for last month) at start of each month
  a - balance of previous month - minimum payment
2 - calculate balance for this month 
  a - unpaid balance of last month + interest on it
3 - print balance at end of 12 months


recursion:
 base case:
  - if month 1, return balance
  - if month 1+n, return
   - balance = unpaid balance + interest
"""

# Test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# initialize iteration variables
remainingBalance, monthsRemaining = 0, 12

# compute remaining balance for each month for 12 months
while monthsRemaining > 0:
    unpaidBalance = balance - (balance * monthlyPaymentRate)
    remainingBalance = unpaidBalance + (unpaidBalance * (annualInterestRate/12))
    balance = remainingBalance
    monthsRemaining -= 1

# print result
print("Remaining balance:", round(remainingBalance, 2))

"""
# Result Your Code Should Generate Below:
	Remaining balance: 31.38
"""