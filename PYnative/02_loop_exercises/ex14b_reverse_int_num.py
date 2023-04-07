"""Module to reverse an integer number"""

# Import modules.

import sys
import custom_module_clear_screen

# Define functions.

def reverse_the_num(fn_num):
    """Function to reverse the number"""
    fn_rev_num = 0
    if fn_num == 0:
        return fn_rev_num
    else:
        digitlist = []
        abs_num = abs(fn_num)  # To handle negative integers.
        while abs_num != 0:
            digit = abs_num % 10
            digitlist.append(digit)
            abs_num = abs_num // 10
        digitlist.reverse()
        power = 0
        for digit in digitlist:
            product = digit * (10 ** power)
            fn_rev_num = fn_rev_num + product
            power = power + 1
        if fn_num < 0:
            return 0-fn_rev_num
        else:
            return fn_rev_num

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script accepts an integer & reverses it.\n")
    try:
        num = int(input("Enter number: "))
    except ValueError:
        print("Invalid input. Please enter an integer only. Exiting script!\n")
        sys.exit(1)
    rev_num = reverse_the_num(num)
    print(f"\nOriginal number: {num}")
    print(f"Reverse number: {rev_num}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
