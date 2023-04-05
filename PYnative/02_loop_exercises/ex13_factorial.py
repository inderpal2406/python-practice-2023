"""Module to find factorial of a number"""

# Import modules.

import sys
import custom_module_clear_screen

# Define functions.

def calculate_factorial(fn_num):
    """Function to calculate factorial of fn_num number"""
    if fn_num == 0:
        return 1
    else:
        product = 1
        for i in range(fn_num,0,-1):
            product = product * i
        return product

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script accepts a number & finds its factorial.\n")
    try:
        num = int(input("Enter number: "))
    except ValueError:
        print("Invalid input. Please enter an integer only. Exiting script!\n")
        sys.exit(1)
    else:
        if num < 0:
            print("Please enter a positive integer only. Exiting script!\n")
            sys.exit(1)
    factorial = calculate_factorial(num)
    print(f"\n{num}! = {factorial}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
