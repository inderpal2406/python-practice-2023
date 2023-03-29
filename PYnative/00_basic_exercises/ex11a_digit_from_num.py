"""Module to extract each digit from an integer and display in reverse order"""

# Import modules.

import custom_module_clear_screen
import sys

# Define functions.

def digits_in_reverse(fn_num):
    """Function to display digits of a num in reverse order"""
    # If else loop to handle negative nums.
    if fn_num <  0:
        numstr = str(abs(fn_num))
    else:
        numstr = str(fn_num)
    charlist = []
    for char in numstr:
        charlist.append(char)
    charlist.reverse()
    print(f"Original number: {fn_num}")
    print("Digits in reverse order:", end=" ")
    for char in charlist:
        print(f"{char}", end=" ")
    print()
    return None

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script accepts a number & displays its digits in reverse order.\n")
    try:
        num = int(input("Enter number: "))
    except ValueError:
        print("Invalid input. Please enter an integer only. Exiting script!\n")
        sys.exit(1)
    print()
    digits_in_reverse(num)
    print()
    return None

# Call main() when the script is executed explicitly.

if __name__ == "__main__":
    main()
