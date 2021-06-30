"""

- take half of the principal amount
- calc total annual compound interest on half of principal amount
- starting guess = principal amount/12 + total interest calc'd in previous step
- starting guess = nearest multiple of 10 of the amount calc'd previously

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

Test Case 1:
	balance = 3329
	annualInterestRate = 0.2

	Result Your Code Should Generate:
	-------------------
  Lowest Payment: 310

"""

balance = 3926
annualInterestRate = 0.2

def computeInitialGuess(totalBalance, annualInterestRate):

  totalAnnualInterestWithoutWithdrawal = totalBalance * (1 + annualInterestRate/12) ** 12

  startingGuess = (totalBalance + ((totalAnnualInterestWithoutWithdrawal-totalBalance)/2)) / 12

  return (startingGuess // 10) * 10


def calcFixedPayments(totalBalance, annualInterestRate):
  
  fixedPayment = computeInitialGuess(totalBalance, annualInterestRate)

  while calcRemainingBalance(totalBalance, fixedPayment, annualInterestRate) > 0:
    fixedPayment += 10

  return fixedPayment

def calcRemainingBalance(currentBalance, fixedPayment, annualInterestRate):

  # compute remaining balance for each month for 12 months
  for i in range(12):
    unpaidBalance = currentBalance - fixedPayment
    currentBalance = unpaidBalance + (unpaidBalance * (annualInterestRate/12))

  return currentBalance

fixedPayment = calcFixedPayments(balance, annualInterestRate)

print("Lowest Payment:", int(fixedPayment))
