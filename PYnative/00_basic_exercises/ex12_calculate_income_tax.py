"""Module to calculate income tax on given income"""

# Import modules.

import custom_module_clear_screen
import sys

# Define functions.

def calculate_tax(fn_income):
    """Function to calculate tax in given income fn_income"""
    if fn_income <= 10000:
        return 0
    else:
        tax1 = 0
        tax2 = 0
        taxable_amt = fn_income - 10000
        if taxable_amt < 10000:
            tax1 = 0.1 * taxable_amt
        else:
            tax1 = 0.1 * 10000
            remaining_amt = taxable_amt - 10000
            tax2 = 0.2 * remaining_amt
        total_tax = tax1 + tax2
        return round(total_tax,2)  # Round to 2 decimal points if needed.

def print_tax_rules():
    """Function to display income tax rules"""
    print('''
    Income tax is calculated based on below rules:
    For first 10000 rupees of income -> Rate of income tax is 0%
    For next 10000 rupees of income  -> Rate of income tax is 10%
    For remaining income             -> Rate of income tax is 20%
    ''')
    return None

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script accepts income & calculates income tax for it.\n")
    print_tax_rules()
    try:
        income = int(input("Enter income: "))
    except ValueError:
        print("Invalid input. Please enter an integer only. Exiting script!\n")
        sys.exit(1)
    else:
        if income < 0:
            print("Please enter positive integer only. Exiting script!\n")
            sys.exit(1)
    print()
    tax = calculate_tax(income)
    print(f"Income: {income}\nIncome Tax on given income: {tax}\n")
    return None

# Call main() when the script is executed explicitly.

if __name__ == "__main__":
    main()
