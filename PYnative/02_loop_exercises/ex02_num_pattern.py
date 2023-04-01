"""Module to print pattern of numbers"""

import custom_module_clear_screen
import sys

def print_num_pattern(fn_num):
    """Function to print pattern of numbers"""
    print("The pattern is as below:")
    for i in range(1,fn_num+1,1):
        for j in range(1,i+1,1):
            print(f"{j}", end=" ")
        print()

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script accepts a num between 1 to 20 & prints corresponding pattern.\n")
    try:
        num = int(input("Enter number: "))
    except ValueError:
        print("Invalid input. Please enter an integer only. Exiting script!\n")
        sys.exit(1)
    else:
        if num not in range(1,21,1):
            print("Entered number not in range 1 to 20. Exiting script!\n")
            sys.exit(1)
    print()
    print_num_pattern(num)
    print()

if __name__ == "__main__":
    main()
