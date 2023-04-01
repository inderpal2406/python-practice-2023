"""Module to print multiplication table of a given number"""

# Import modules.

import sys
import custom_module_clear_screen

# Define functions.

def print_multiplication_table(fn_num):
    """Function to print multiplication table of fn_num number"""
    print(f"Multiplication table of {fn_num} is:")
    for i in range(1,11,1):
        product = fn_num * i
        print(f"{product}")

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script accepts a number & prints its multiplication table.\n")
    try:
        num = int(input("Enter number: "))
    except ValueError:
        print("Invalid input. Please enter an integer only. Exiting script!\n")
        sys.exit(1)
    print()
    print_multiplication_table(num)
    print()

# Call main() when the script is executed explicitly.

if __name__ == "__main__":
    main()
