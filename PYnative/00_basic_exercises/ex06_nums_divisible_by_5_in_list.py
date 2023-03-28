"""Module to find nums divisible by 5 in a list"""

# Import modules.

import custom_module_clear_screen
import sys

# Define functions.

def divisible_by_5(fn_numlist):
    """Function to find nums from list which are divisible by 5"""
    print(f"Given list: {fn_numlist}")
    print("Numbers divisible by 5 are as below,")
    fn_count = 0
    for num in fn_numlist:
        if num % 5 == 0:
            print(f"{num}")
            fn_count = fn_count + 1
    if fn_count == 0:
        print("No numbers found in the list which are divisible by 5.")
    return None

def accept_nums(fn_count):
    """Function to accept nums from user and return list of them"""
    index = 0
    fn_numlist = []
    while index < fn_count:
        try:
            #num = float(input("Enter number: "))  # Notes at bottom.
            num = int(input("Enter number: "))
        except ValueError:
            print("Invalid input. Please enter an int non-decimal num. Exit script!\n")
            sys.exit(1)
        fn_numlist.append(num)
        index = index + 1
    return fn_numlist

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print('''
    This script accepts a maximum of 10 nums & then
    finds nums divisible by 5 from them.\n
    ''')
    try:
        count = int(input("How many numbers do you want to enter: "))
    except ValueError:
        print("Invalid input. Please enter an integer only. Exiting script!\n")
        sys.exit(1)
    else:
        if count < 0:
            print("Please enter non-negative integer only. Exiting script!\n")
            sys.exit(1)
        elif count > 10:
            print("Script accepts maximum of 10 nums. Exiting script!\n")
            sys.exit(1)
        elif count == 0:
            print("As zero is entered, nothing will be done. Exiting script!\n")
            sys.exit(1)
    print()
    numlist = accept_nums(count)
    print()
    divisible_by_5(numlist)
    print()
    return None

# Call main() when the script is executed explicitly.

if __name__ == "__main__":
    main()

# Notes:
# We say x is divisible by y if the quotient is a whole number.
# A whole num is a num without fraction.
# Whole nums include 0 and all positive integers.
# If x is a float num and y is a whole num, then quotient will be a float num (decimal num).
# If quotient is a decimal num, which means a fraction, we say x is not divisible by y.
# When we know all decimal nums will give quotient as a fraction, we won't accept it as
# input, because we want to narrow down to whole nums only in quotient, to prove
# divisibility.
