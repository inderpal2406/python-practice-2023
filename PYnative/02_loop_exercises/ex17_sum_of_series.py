"""Module to find sum of series upto n terms"""

# Import modules.

import sys
import custom_module_clear_screen

# Define functions.

def calculate_sum_of_series(a,b):
    """Function to calculate sum of series"""
    numlist = []
    for i in range(1,b+1,1):
        loopsum = 0
        for j in range(0,i,1):
            loopsum = loopsum + a * (10 ** j)
        numlist.append(loopsum)
    print(numlist)
    addsum = 0
    for num in numlist:
        addsum = addsum + num
    return numlist, addsum

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print('''
    This script accepts 2 numbers - x and y.
    Suppose x=2 and y=5, it'll then calculate sum of below series of numbers,
    2 + 22 + 222 + 2222 + 22222 = 24690
    Note: Number x should be between 1 and 9.
    Note: Number y should be > 0.
    ''')
    try:
        x = int(input("Enter number x: "))
        y = int(input("Enter number y: "))
    except ValueError:
        print("Invalid input. Please enter an integer only. Exiting script!\n")
        sys.exit(1)
    else:
        if x not in range(1,10,1):
            print("Number x is not in range from 1 to 9. Exiting script!\n")
            sys.exit(1)
        elif y <= 0:
            print("Number y is not > 0. Exiting script!\n")
            sys.exit(1)
    numseries, seriessum = calculate_sum_of_series(x,y)
    print(f"\nThe series is: {numseries}")
    print(f"Sum of numbers in the series: {seriessum}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
