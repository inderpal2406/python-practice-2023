"""Module to create a calculator to operate on 2 operands"""

# Import modules.

import custom_module_clear_screen
import sys

# Define functions.

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script accepts 2 nums & gives choice to operate on them.\n")
    # Accept 2 nums from user & exit script if invalid input is given.
    try:
        num1 = float(input("Enter number: "))
        num2 = float(input("Enter number: "))
    except ValueError:
        print("Invalid input. Enter a number only. Exiting script!\n")
        sys.exit(1)
    print('''
    Which operation do you want to execute?
    1. Add
    2. Subtract
    3. Multiple
    4. Divide
    ''')
    choice = input("Enter your choice [1|2|3|4]: ")
    print()  # Leave a line.
    if choice == "1":
        addition = round(num1 + num2,2)
        print(f"Sum of {num1} & {num2} is: {addition}\n")
    elif choice == "2":
        difference = round(num1 - num2,2)
        print(f"Difference of {num1} & {num2} is: {difference}\n")
    elif choice == "3":
        product = round(num1 * num2,2)
        print(f"Product of {num1} & {num2} is: {product}\n")
    elif choice == "4":
        try:
            division = round(num1 / num2,2)
        except ZeroDivisionError:
            print("Answer is infinity when divided by zero.\n")
        else:
            print(f"{num1} divided by {num2} gives quotient as: {division}\n")
    else:
        print("Invalid choice. Exiting script!\n")
        sys.exit(1)

# Call main() when the script is executed explicitly.

if __name__ == "__main__":
    main()
