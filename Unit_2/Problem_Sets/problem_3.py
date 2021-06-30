"""
Problem 3 - Using Bisection Search to Make the Program Faster

Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)^12) / 12.0

Test Case 1:
balance = 320000
annualInterestRate = 0.2

Result Your Code Should Generate:
-------------------
Lowest Payment: 29157.09

"""

balance = 320000
annualInterestRate = 0.20

def calcFixedPayments(totalBalance, annualInterestRate):

  # compute initial guess
  monthlyLowerBound = totalBalance / 12
  monthlyUpperBound = (totalBalance * (1 + annualInterestRate/12) ** 12) / 12
  guess = (monthlyLowerBound + monthlyUpperBound) / 2

  # iterate until break
  while True:
    # compute remaining balance given a value of guess
    remainingBalance = calcRemainingBalance(totalBalance, guess, annualInterestRate)
    # if remaining balance lower than 0.01
    if abs(remainingBalance) <= 0.01:
      break
    elif remainingBalance > 0:
      # if balance higher after payments, increase lower bound
      monthlyLowerBound = guess
    elif remainingBalance < 0:
      # if balance lower after payments, decrease the upper bound
      monthlyUpperBound = guess
    # update guess
    guess = (monthlyLowerBound + monthlyUpperBound) / 2

  return guess

def calcRemainingBalance(currentBalance, fixedPayment, annualInterestRate):

  # compute remaining balance for each month for 12 months
  for i in range(12):
    unpaidBalance = currentBalance - fixedPayment
    currentBalance = unpaidBalance + (unpaidBalance * (annualInterestRate/12))

  return currentBalance

fixedPayment = calcFixedPayments(balance, annualInterestRate)

print("Lowest Payment:", round(fixedPayment,2))