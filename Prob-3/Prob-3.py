# Module 4
#   Programming Assignment 5
#       Prob-3.py

# <Stephen Guild>

#input: job size in square feet, cost of paint per gallon
#process: calculate estimate
#output: print estimate
from math import *
# function definition
def estimate(squareFeet, paintCost):
    laborFee=35.00
    setupFee=99.00
    wallPaint=112
    hoursFeet=int(wallPaint)//8
    gallonsNeeded=ceil(int(squareFeet//wallPaint))
    paintCost=paintCost*gallonsNeeded
    hours=ceil(int(squareFeet)/int(hoursFeet))
    jobEstimate=setupFee+(gallonsNeeded*paintCost)+(laborFee*hours)
    print("Gallons of paint needed:",gallonsNeeded)
    print("hours of labor:",hours)
    print("Cost of paint: $",paintCost)
    print("Labor Charges: $",laborFee)
    print("Total cost of the Paint Job: $",jobEstimate)
    return

# main function definition
#get size of project in square feet from user
def main():
    squareFeet=eval(input("square feet of job:"))
    paintCost=float(input("price for paint Gallon: $"))
    print(estimate(squareFeet,paintCost))

main()
