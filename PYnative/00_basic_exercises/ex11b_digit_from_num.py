"""Module to extract each digit from an integer and display in reverse order"""

# Import modules.

import custom_module_clear_screen
import sys

# Define functions.

def digits_in_reverse(fn_num):
    """Function to display digits of a num in reverse order"""
    # If else loop to handle negative nums.
    if fn_num <  0:
        newnum = abs(fn_num)
    else:
        newnum = fn_num
    digitlist = []
    # Handle corner case of 0 as user input.
    # Without this, output of reverse nums becomes empty as it never appends
    # anything to digitlist because of while loop in else.
    if newnum == 0:
        digitlist.append(newnum)
    else:
        while newnum != 0:
            digit = newnum % 10
            digitlist.append(digit)
            newnum = newnum // 10
    print(f"Original number: {fn_num}")
    print("Digits in reverse order:", end=" ")
    for digit in digitlist:
        print(f"{digit}", end=" ")
    print()  # Bring cursor to new line.
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
