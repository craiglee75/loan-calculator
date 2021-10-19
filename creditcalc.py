import math
import argparse

parser = argparse.ArgumentParser(description="This is a loan calculator")
parser.add_argument("--type", type=str, choices=["diff", "annuity"],
                    help="choose between constant annuity or differentiated monthly payments")
parser.add_argument("--interest", type=float, help="provide interest rate")
parser.add_argument("--principal", type=int, help="provide loan principal")
parser.add_argument("--periods", type=int,
                    help="provide the number months to repay the loan")
parser.add_argument("--payment", type=int,
                    help="provide amount of monthly payment")
args = parser.parse_args()


def months_to_years(n):
    if n == 1:
        return ("It will take 1 month to repay the loan!")
    elif n <= 12:
        return (f"It will take {n} months to repay the loan!")
    elif n == 13:
        return (f"It will take 1 year and 1 month to repay the loan!")
    elif math.ceil(n % 12) == 1:
        return (f"It will take {(n // 12)} years and {math.ceil(n % 12)} month to repay the loan!")
    else:
        return (f"It will take {(n // 12)} years and {math.ceil(n % 12)} months to repay the loan!")


def differentiated_pmt(prin, n, m, i):
    d_pmt = int(math.ceil(((prin / n) + i * (prin - (prin * ((m - 1) / n))))))
    return d_pmt


# set variables
principal = args.principal
payment = args.payment
periods = args.periods
interest = args.interest

# i = interest / 12 / 100  # monthly interest as a decimal

params = [args.principal, args.payment, args.periods, args.interest]

# Check for relevant inputs
# list of params not equal to None
lst_exnone = [param for param in params if param is not None]
# list of negative params
lst_negs = [param for param in lst_exnone if param < 0]

if len(lst_exnone) < 3 or len(lst_negs) > 0:
    print("Incorrect parameters")
elif args.type == "annuity":

    i = interest / 12 / 100  # monthly interest as a decimal

    # Calculates loan parameters based off of annuity type and calcs the parameter not specified through the input
    if payment is None:
        payment = principal * ((i * pow(1 + i, periods)) /
                               (pow(1 + i, periods) - 1))
        if principal % periods != 0:
            mth_pmt = int(math.ceil(payment))
            last_pmt = ((periods) * int(math.ceil(payment))) - \
                ((periods - 1) * int(math.ceil(payment)))
            print(
                f"Your monthly payment = {mth_pmt} and the last payment = {last_pmt}!")
            print(
                f"Overpayment = {((mth_pmt * (periods - 1)) + last_pmt)- principal}")
        else:
            print(f"Your monthly payment = {int(math.ceil(payment))}!")
            print(
                f"Overpayment = {(int(math.ceil(payment)) * (periods)) - principal}")

    elif principal is None:
        principal = int(payment / ((i * pow(1 + i, periods)) /
                                   (pow(1 + i, periods) - 1)))
        print(f"You're loan principal = {principal}!")
        print(
            f"Overpayment = {int(math.ceil((payment * periods) - principal))}")

    elif periods is None:
        periods = int(
            math.ceil(math.log((payment / (payment - i * principal)), (1 + i))))
        print(months_to_years(periods))
        print(
            f"Overpayment = {(payment * periods) - principal}")

elif args.type == "diff":

    i = interest / 12 / 100  # monthly interest as a decimal

    tot_pmt = 0
    for mth in range(1, periods + 1):
        mth_pmt = differentiated_pmt(principal, periods, mth, i)
        tot_pmt += mth_pmt
        print(
            f"Month {mth}: payment is {mth_pmt}!")
    print()
    print(f"Overpayment = {tot_pmt - principal}")
