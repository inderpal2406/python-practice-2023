"""Module to print a pattern of downward half pyramid"""

# Import modules.

import custom_module_clear_screen
import sys

# Define functions.

def down_half_pyramid(fn_num):
    """Function to print downward half pyramid for fn_num no. of lines"""
    print("The pattern is:\n")
    while fn_num != 0:
        i = 1
        while i <= fn_num:
            print("*", end="")
            i = i + 1
        print()  # Bring cursor to new line after printing * in one line.
        fn_num = fn_num - 1
    return None

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print('''
    This script accepts a number n between range of 1 to 20 &
    prints a pattern of downward half pyramid with n number of lines.
    ''')
    try:
        num = int(input("Enter number: "))
    except ValueError:
        print("Invalid input. Please enter an integer only. Exiting script!\n")
        sys.exit(1)
    else:
        if num not in range(1,21,1):
            print("Please enter a number between range of 1 to 20. Exiting script!\n")
            sys.exit(1)
    print()
    down_half_pyramid(num)
    print()
    return None

# Call main() when the script is executed explicitly.

if __name__ == "__main__":
    main()
