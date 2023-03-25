"""Module to find product & sum of 2 nums"""

# Import modules.

import custom_module_clear_screen
import sys

# Define functions.

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script finds product & sum of 2 numbers.\n")
    # Accept 2 numbers & exit if invalid input given.
    try:
        num1 = float(input("Enter number: "))
        num2 = float(input("Enter number: "))
    except ValueError:
        print("Invalid input. Enter a number only. Exiting script!\n")
        sys.exit(1)
    product = round(num1 * num2,2)
    addition = round(num1 + num2,2)
    print(f"\nThe provided numbers are {num1} and {num2}.")
    print(f"Their product: {product}")
    print(f"Their sum: {addition}\n")

# Call main() when the script is explicitly executed.

if __name__ == "__main__":
    main()
