"""Module to count digits in a number"""

# Import modules.

import sys
import custom_module_clear_screen

# Define functions.

def count_digits(fn_num):
    """Function to count number of digits in fn_num number"""
    numstr = str(fn_num)
    numstr = numstr.lstrip("-")      # Remove negative symbol if present.
    strlist = numstr.split(sep=".")  # Split string based on decimal point.
    # Decimal point will always be present as input is typecasted to float.
    firststr = strlist[0]
    secondstr = strlist[1]
    # Count chars/digits in firststr.
    count = 0
    for char in firststr:
        count = count + 1
    # Test if secondstr has all zeroes.
    addsum = 0
    for char in secondstr:
        num = int(char)
        addsum = addsum + num
    # If all zeroes, then sum = 0. In this case don't count digits/chars in secondstr.
    # Else count it.
    if addsum != 0:
        for char in secondstr:
            count = count + 1
    return count

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script accepts a number and counts its digits.\n")
    try:
        num = float(input("Enter number: "))
    except ValueError:
        print("Invalid input. Please enter a number only. Exiting script!\n")
        sys.exit(1)
    digit_count = count_digits(num)
    print(f"\nEntered number: {num}")
    print(f"Number of digits: {digit_count}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
