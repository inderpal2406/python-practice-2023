"""Module to print prime numbers within a range"""

# Import modules.

import sys
import custom_module_clear_screen

# Define functions.

def print_prime_nums(start, end):
    """Function to print prime nums between start & end numbers"""
    print(f"Prime numbers between {start} to {end} are:")
    count = 0
    for i in range(start,end+1,1):
        factors = 0
        for j in range(1,i+1,1):
            if i % j == 0:
                factors = factors + 1
        if factors == 2:
            print(i)
            count = count + 1
    print(f"\nTotal number of prime numbers between {start} to {end}: {count}")

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script accepts 2 numbers & displays all prime numbers between them.\n")
    try:
        startnum = int(input("Enter start number: "))
        endnum = int(input("Enter end number: "))
    except ValueError:
        print("Invalid input. Please enter an integer only. Exiting script!\n")
        sys.exit(1)
    else:
        if startnum < 0 or endnum < 0:
            print("Please enter only positive integers. Exiting script!\n")
            sys.exit(1)
        if startnum > endnum:
            print("Start number should be lesser than end number. Exiting script!\n")
            sys.exit(1)
    print()
    print_prime_nums(startnum, endnum)
    print()

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
