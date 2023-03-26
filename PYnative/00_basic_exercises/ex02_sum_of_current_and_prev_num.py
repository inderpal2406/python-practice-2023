"""Module to iterate over 10 nums & calculate sum of current & prev num"""

# Import modules.

import custom_module_clear_screen
import sys

# Define functions.

def calculate_and_print_sum(fn_num):
    """Function to iterate over 10 nums, calculate sum of current & prev num"""
    addition = 0
    for i in range(1,11,1):
        current_num = fn_num
        previous_num = fn_num - 1
        addition = current_num + previous_num
        print(f"Current Number {current_num} Previous Number {previous_num} Sum: {addition}")
        fn_num = fn_num + 1
    return()

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script iterates over 10 nums & calculates sum of current & prev num.\n")
    # Accept user input & exit if non-int num is provided.
    try:
        num = int(input("Enter number to start with: "))
    except ValueError:
        print("Invalid input. Enter an integer only. Exiting script!\n")
        sys.exit(1)
    print()  # Leave a line in output.
    calculate_and_print_sum(num)
    print()
    return()

# Call main() when the script is executed explicitly.

if __name__ == "__main__":
    main()
