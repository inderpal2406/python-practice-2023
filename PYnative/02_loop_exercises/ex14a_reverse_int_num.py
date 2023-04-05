"""Module to reverse an integer number"""

# Import modules.

import sys
import custom_module_clear_screen

# Define functions.

def reverse_the_num(fn_num):
    """Function to reverse the fn_num number"""
    numstr = str(fn_num)
    numstr = numstr.lstrip("-")
    charlist = []
    for char in numstr:
        charlist.append(char)
    charlist.reverse()
    rev_numstr = ''.join(charlist)
    fn_rev_num = int(rev_numstr)
    if fn_num < 0:
        return 0-fn_rev_num
    else:
        return fn_rev_num

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script accepts an integer and reverses it.\n")
    try:
        num = int(input("Enter number: "))
    except ValueError:
        print("Invalid input. Please enter an integer only. Exiting script!\n")
        sys.exit(1)
    rev_num = reverse_the_num(num)
    print(f"\nOriginal number: {num}")
    print(f"Reverse number: {rev_num}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
