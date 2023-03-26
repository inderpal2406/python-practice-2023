"""Module to remove first n chars from a string"""

# Import modules.

import custom_module_clear_screen
import sys

# Define functions.

def remove_chars(fnstr,fn_num_n):
    """Function to remove first n chars from a string"""
    print(f"User input string: {fnstr}")
    print(f"No. of chars in user string: {len(fnstr)}")
    print(f"Number n i.e. no. of chars to be removed: {fn_num_n}")
    if fn_num_n > len(fnstr):
        print("Number n should be less than total no. of chars in the string.")
        print("Hence, nothing will be done here!")
        return None
    charlist = []
    for char in fnstr:
        charlist.append(char)
    index = 0
    while index < fn_num_n:
        charlist.pop(0)
        index = index + 1
    ansstr = ''.join(charlist)
    print(f"String after removal of chars: {ansstr}")
    return None

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script removes first n chars from a string.\n")
    usrstr = input("Enter the string: ")
    # Accept num n from user. Exit if non-int value is given.
    try:
        num_n = int(input("Enter number n: "))
    except ValueError:
        print("Invalid input. Enter an integer only. Exiting script!\n")
        sys.exit(1)
    else:
        # Check num n provided b user is negative. Exit script in such a case.
        if num_n < 0:
            print("Please give a positive integer only. Exiting script!\n")
            sys.exit(1)
    print()
    remove_chars(usrstr,num_n)
    print()
    return None

# Call main() when the script is executed explicitly.

if __name__ == "__main__":
    main()
