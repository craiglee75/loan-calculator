# loan-calculator
Simple loan calculator in python using the terminal for inputs

calculates loan attributes based on user input including:-
principal
number of periods until repayment
amount of interest paid
monthly payment

User determines if the loan has fixed (annuity) or differentiated (diff) monthly payments.  The calculator will require 3 parameters to be input and the calculator will calculate the 4th parameter from principal, periods, monthly payment and interest.  User is required to provide the rate of interest to be used.

example:

python3 creditcalc.py --type="diff" --principal=500000 --periods=8 --interest=7.8
# Month 1: payment is 65750 !
# ...
# Month 8: payment is 62907
# Overpayment = 14628

python3 creditcalc.py --type="annuity" --payment=8722 --periods=120 --interest=5.6
# You're loan principal = 800018
# overpayment = 246622

python3 creditcalc.py --type="annuity" --principal=500000 --payment=23000 --interest=7.8
# It will take 2 years to repay your loan!
# overpayment = 52000
