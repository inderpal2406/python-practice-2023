"""Module to check if a num is a palindrome num or not"""

# Import modules.

import custom_module_clear_screen
import sys

# Define functions.

def check_palindrome_num(fn_num):
    """Function to check if num is palindrome"""
    numstr = str(fn_num)
    charlist = []
    for char in numstr:
        charlist.append(char)
    charlist.reverse()
    rev_numstr = "".join(charlist)
    rev_fn_num = int(rev_numstr)
    print(f"Original number: {fn_num}")
    if fn_num == rev_fn_num:
        print("Yes. Given number is palindrome number.")
    else:
        print("No. Given number is not palindrome number.")
    return None

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script accepts a number and checks if it is a palindrome.\n")
    try:
        num = int(input("Enter number: "))
    except ValueError:
        print("Invalid input. Please enter an integer only. Exiting script!\n")
        sys.exit(1)
    else:
        if num < 0:
            print("Please enter a non-negative integer only. Exiting script!\n")
            sys.exit(1)
    print()
    check_palindrome_num(num)
    print()
    return None

# Call main() when the script is executed explicitly.

if __name__ == "__main__":
    main()
