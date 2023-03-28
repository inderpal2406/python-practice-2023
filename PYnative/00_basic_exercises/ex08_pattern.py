"""Module to print a pattern"""

# Import modules.

import custom_module_clear_screen
import sys

# Define functions.

def print_num_pattern(fn_num):
    """Module to print a pattern of numbers"""
    print("The pattern is:")
    for i in range(1,fn_num+1,1):
        j = 1
        while j <= i:
            print(i,end="")
            j = j + 1
        print()
    return None

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script accepts a number upto 10 and prints corresponding pattern.\n")
    try:
        num = int(input("Enter a number between 1 to 10: "))
    except ValueError:
        print("Invalid input. Please enter an integer only. Exiting script!\n")
        sys.exit(1)
    else:
        if num < 1 or num > 10:
            print("Given number is not between 1 to 10. Exiting script!\n")
            sys.exit()
    print()
    print_num_pattern(num)
    print()
    return None

# Call main() when the script is executed explicitly.

if __name__ == "__main__":
    main()
