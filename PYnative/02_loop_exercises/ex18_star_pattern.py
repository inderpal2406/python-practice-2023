"""Module to print pattern of stars"""

# Import modules.

import sys
import custom_module_clear_screen

# Define functions.

def print_star_pattern(fn_num):
    """Function to print the star pattern for number fn_num"""
    for i in range(1,fn_num+1,1):
        for j in range(1,i+1,1):
            print("*", end=" ")
        print()  # Bring cursor to new line.
    for i in range(fn_num-1,0,-1):
        for j in range(1,i+1,1):
            print("*", end=" ")
        print()

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print('''
    This script accepts a number between 1 to 10 &
    prints equivalent star pattern.
    ''')
    try:
        num = int(input("Enter number: "))
    except ValueError:
        print("Invalid input. Please enter an integer only. Exiting script!\n")
        sys.exit(1)
    else:
        if num not in range(1,11,1):
            print("Enter number not in range from 1 to 10. Exiting script!\n")
            sys.exit(1)
    print("\nThe pattern is:")
    print_star_pattern(num)
    print()  # Leave a line at the end.

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
