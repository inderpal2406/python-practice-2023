"""Module to print number pattern"""

# Import modules.

import sys
import custom_module_clear_screen

# Define functions.

def print_num_pattern(fn_num):
    """Function to print pattern of numbers for fn_num number"""
    print("The pattern is:")
    for i in range(fn_num,0,-1):
        for j in range(i,0,-1):
            print(f"{j}", end=" ")
        print()  # bring cursor to new line for next line printing.

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script accepts a number from 1 to 20 & prints its equivalent pattern.\n")
    try:
        num = int(input("Enter number: "))
    except ValueError:
        print("Invalid input. Please enter an integer only. Exiting script!\n")
        sys.exit(1)
    else:
        if num not in range(1,21,1):
            print("Entered number not in range 1 to 20. Exiting script!\n")
            sys.exit(1)
    print()
    print_num_pattern(num)
    print()

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
