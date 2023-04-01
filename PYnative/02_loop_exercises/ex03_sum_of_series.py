"""Module to calculate sum of nums from 1 to a given number"""

# Import modules.

import sys
import custom_module_clear_screen

# Define functions.

def sum_of_series(fn_num):
    """Function to calculate sum of nums from 1 to fn_num"""
    fn_ans_sum = 0
    for i in range(1,fn_num+1,1):
        fn_ans_sum = fn_ans_sum + i
    return fn_ans_sum

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print('''
    This script accepts a number between 1 to 100.
    Then calculates sum of all numbers from 1 to given number.
    ''')
    try:
        num = int(input("Enter number: "))
    except ValueError:
        print("Invalid input. Please enter an integer only. Exiting script!\n")
        sys.exit(1)
    else:
        if num not in range(1,101,1):
            print("Entered number not in range 1 to 100. Exiting script!\n")
            sys.exit(1)
    ans_sum = sum_of_series(num)
    print(f"Sum is: {ans_sum}\n")

# Call main() when the script is executed explicitly.

if __name__ == "__main__":
    main()
