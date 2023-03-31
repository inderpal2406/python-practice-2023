"""Module to have an exponent function to calculate power of a num"""

# In mathematics, exponentiation is an operation involving two numbers,
# the base and the exponent or power. Exponentiation is written as bⁿ,
# where b is the base and n is the power.

# Import modules.

import custom_module_clear_screen
import sys

# Define functions.

def exponent(fn_base, fn_exp):
    """Function to calculate power of base number"""
    # if loop to handle 0 raised to -ve num, which is division by 0.
    if fn_base == 0 and fn_exp < 0:
        return None
    else:
        fn_ans = fn_base ** fn_exp
        return round(fn_ans,2)  # Round off if power is negative.

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print('''
    This script accepts 2 numbers - a base & an exponent.
    It'll then calculate value of base num raised to the power of exponent num.
    ''')
    try:
        base = int(input("Enter base number: "))
        exp = int(input("Enter exponent number: "))
    except ValueError:
        print("Please enter an integer only. Exiting script!\n")
        sys.exit(1)
    ans = exponent(base, exp)
    if ans is None:
        print(f"\n{base} raised to the power of {exp} translates to division by 0, which is undefined.\n")
    else:
        print(f"\n{base} raised to the power of {exp} is: {ans}\n")
    return None

# Call main() when the script is executed explicitly.

if __name__ == "__main__":
    main()
