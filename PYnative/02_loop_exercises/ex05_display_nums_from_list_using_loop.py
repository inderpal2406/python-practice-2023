"""Module to print nums from a list using loop & conditions"""

# Import modules.

import custom_module_clear_screen

# Define functions.

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print('''
    This script has a pre-defined list of numbers.
    It'll display numbers from the list which satisfy below conditions:
    1. The number is divisible by 5.
    2. If the number is greater than 150, then skip it and move to the next number.
    3. If the number is greater than 500, then stop the loop
    ''')
    input("Press ENTER to proceed.\n")
    nums = [12,75,150,180,145,525,50]
    print(f"Pre-defined list: {nums}")
    print("Numbers satisfying the 3 conditions are as below:")
    for num in nums:
        if num > 500:
            break
        elif num > 150:
            continue
        else:
            if num % 5 == 0:
                print(num)
    print()

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
