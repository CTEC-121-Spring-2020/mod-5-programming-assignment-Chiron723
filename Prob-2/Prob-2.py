# Module 4
#   Programming Assignment 5
#       Prob-2.py

# <Stephen Guild>

#inputs: total cost of items, amount tendered
#process: calculate change in terms of number of each denomination
#output: summery line, number of each denomination

# function definition
from math import *

def changeCalculator(totalCost, amountTendered):
    change=float(amountTendered) - float(totalCost)
    changeDue=int(round(change*100))
    tens=changeDue//1000
    if tens>=1:
        print("tens:",tens)
    changeDue=changeDue-(tens*1000)
    fives=changeDue//500
    if fives>=1:
        print("fives:",fives)
    changeDue=changeDue-(fives*500)
    ones=changeDue//100
    if ones>=1:
        print("ones:",ones)
    changeDue=changeDue-(ones*100)
    quarters=changeDue//25
    if quarters>=1:
        print("quarters:",quarters)
    changeDue=changeDue-(quarters*25)
    dimes=changeDue//10
    if dimes>=1:
        print("dimes:",dimes)
    changeDue=changeDue-(dimes*10)
    nickels=changeDue//5
    if nickels>=1:
        print("nickels:",nickels)
    changeDue=changeDue-(nickels*5)
    pennies=changeDue
    if pennies>=1:
        print("pennies:",pennies)
    else:
        print("not applicable")


# main function definition

def main():
    totalCost=float(input("input cost:"))
    amountTendered=float(input("input charge:"))
    change=float(amountTendered) - float(totalCost)
    changeCalculator(totalCost,amountTendered)
    print("Cost:",totalCost,"Tendered:",amountTendered,"Change:",change)

main()
