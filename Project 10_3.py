#!/usr/bin/env python3

from decimal import *

def display_title():
    print("Interest Calculator")
    print()
    
def inputs():
    loan_amt = input("Enter loan amount: ")
    loan_amt = loan_amt.removeprefix("$")
    loan_amt = loan_amt.replace(",","")
    loan_amt2 = loan_amt.find("K")
    if loan_amt2 > 0:
        loan_amt = loan_amt.replace("K","")
        loan_amt = Decimal(loan_amt)
        loan_amt2 = (loan_amt * 1000)
        loan_amt = loan_amt2
        
    else:
        loan_amt = Decimal(loan_amt)
    
    interest_rate = input("Enter interest rate: ")
    interest_rate = interest_rate.removeprefix("%")
    interest_rate = interest_rate.removesuffix("%")
    interest_rate = Decimal(interest_rate)/100
    print()
    return loan_amt, interest_rate

def calculations(loan_amt, interest_rate):
    interest_amt = loan_amt * (interest_rate)
    return interest_amt

def inputsplus(loan_amt, interest_rate, interest_amt):
    print(f"Loan amount:         ${loan_amt:,.2f}")
    print(f"Interest rate:        {interest_rate:.3%}")
    print(f"Interest amount:     ${interest_amt:,.2f}")
    print()
    
 
def main():    
    display_title()
    choice = "y"
    while choice == "y":    
        loan_amount, interest_rate = inputs()
        interest_amt = calculations(loan_amount, interest_rate)
        inputsplus(loan_amount, interest_rate, interest_amt)
        choice = input("Continue? (y/n): ")
        print()
    print("Bye!")
    
if __name__ == "__main__":
        main()    