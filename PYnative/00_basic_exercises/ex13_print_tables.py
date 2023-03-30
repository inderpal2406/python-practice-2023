"""Module to print tables from 1 to a given number between 1 to 100"""

# Import modules.

import custom_module_clear_screen
import sys

# Define function.

def print_tables(fn_num):
    """Function to print tables of numbs from 1 to fn_num number"""
    for i in range(1,fn_num+1,1):
        print(f"Table of {i}:", end="\t")
        for j in range(1,11,1):
            product = i * j
            print(f"{product}", end="\t")
        print()  # bring cursor to new line.
    return None

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print('''
    This script accepts a number between 1 to 100 & then prints tables of all
    numbers from 1 to the given number.
    ''')
    try:
        num = int(input("Enter number: "))
    except ValueError:
        print("Invalid input. Please enter an integer only. Exiting script!\n")
        sys.exit(1)
    else:
        if num not in range(1,101,1):
            print("Entered number not in range from 1 to 100. Exiting script!\n")
            sys.exit(1)
    print()
    print_tables(num)
    print()
    return None

# Call main() when the script is executed explicitly.

if __name__ == "__main__":
    main()
