# Module 4
#   Programming Assignment 5
#       Prob-1.py

# <Stephen Guild>

# input: a number between 1 and 10
# process: convert number to Roman Numeral
# output: a string representing the Roman numeral of that number.

# function definition
def romanNumeral(number):
    
    if number == 1:
        return "I"
    elif number == 2:
        return "II"
    elif number == 3:
        return "III"
    elif number == 4:
        return "IV"
    elif number == 5:
        return "V"
    elif number == 6:
        return "VI"
    elif number == 7:
        return "VII"
    elif number == 8:
        return "VIII"
    elif number == 9:
        return "IX"
    elif number ==10:
        return "X"
    else:
        return "Unknown"

# unit test function
def unitTest():
    print("number: 0\tRoman numeral:", romanNumeral(0))
    print("number: 1\tRoman numeral:", romanNumeral(1))
    print("number: 2\tRoman numeral:", romanNumeral(2))
    print("number: 3\tRoman numeral:", romanNumeral(3))
    print("number: 4\tRoman numeral:", romanNumeral(4))
    print("number: 5\tRoman numeral:", romanNumeral(5))
    print("number: 6\tRoman numeral:", romanNumeral(6))
    print("number: 7\tRoman numeral:", romanNumeral(7))
    print("number: 8\tRoman numeral:", romanNumeral(8))
    print("number: 9\tRoman numeral:", romanNumeral(9))
    print("number: 10\tRoman numeral:", romanNumeral(10))

    print()

unitTest()

def main():
    number=eval(input())

    print("number",number, "Translates to", romanNumeral(number), "in Roman Numerals.")


main()