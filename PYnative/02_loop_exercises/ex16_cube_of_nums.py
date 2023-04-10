"""Module to calculate cubes of all nums from 1 to a given num"""

# Import modules.

import sys
import time
import custom_module_clear_screen

# Define functions.

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print('''
    This script accepts a number & then calculates cubes of
    all numbers from 1 to the given number.
    ''')
    try:
        num = int(input("Enter number: "))
    except ValueError:
        print("Invalid input. Please enter an integer only. Exiting script!\n")
        sys.exit(1)
    else:
        if num <= 0:
            print("Please enter a num > 0. Exiting script!\n")
            sys.exit(1)
    print()
    for i in range(1,num+1,1):
        cube = i ** 3
        print(f"Current number is: {i} and its cube is: {cube}")
        time.sleep(1)
    print()

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
