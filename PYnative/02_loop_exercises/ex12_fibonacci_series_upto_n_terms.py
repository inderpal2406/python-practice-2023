"""Module to print fibonacci series upto n terms"""

# Import modules.

import sys
import custom_module_clear_screen

# Define functions.

def print_fibonacci_series(fn_num):
    """Function to print fibonacci series up to fn_num terms"""
    print(f"Fibonacci series up to {fn_num} terms:")
    fibonacci_list = [0,1]
    if fn_num == 0:
        print("Nothing to print.")
    elif fn_num == 1:
        print(f"{fibonacci_list[0]}")
    else:
        for i in range(2,fn_num,1):
            firstterm = fibonacci_list[i-2]
            secondterm = fibonacci_list[i-1]
            thirdterm = firstterm + secondterm
            fibonacci_list.append(thirdterm)
        for i in fibonacci_list:
            print(f"{i}", end=" ")
        print()  # Bring cursor to new line.

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script prints fibonacci series up to n terms.\n")
    try:
        num = int(input("Enter n: "))
    except ValueError:
        print("Invalid input. Please enter an integer only. Exiting script!\n")
        sys.exit(1)
    else:
        if num < 0:
            print("Please enter a positive integer only. Exiting script!\n")
            sys.exit(1)
    print()
    print_fibonacci_series(num)
    print()

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
