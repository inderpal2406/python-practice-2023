"""Module to check if a num is a palindrome num or not"""

# Import modules.

import custom_module_clear_screen
import sys

# Define functions.

def check_palindrome_num(fn_num):
    """Function to check if num is palindrome"""
    print(f"Original number: {fn_num}")
    digit_list = []
    #while fn_num != 0:
        #digit = fn_num % 10
        #digit_list.append(digit)
        #fn_num = fn_num // 10
    #print(fn_num)
    #With above commented logic, list gets prepared properly but fn_num becomes 0 at end.
    #This results in fn_num != addsum at end & a palindrome is also shown as no palindrome.
    #So, we store fn_num into another var and operate on that var.
    quotient = fn_num
    while quotient != 0:
        digit = quotient % 10
        digit_list.append(digit)
        quotient = quotient // 10
    addsum = 0
    index = 0
    for digit in digit_list:
        #power = digit_list.index(digit)
        #addsum = digit*(10**power) + addsum
        # With above logic, when duplicate values are present in list,
        # It'll take index of first occurrence of the digit in the list.
        # This results in wrong last sum. 
        # This occurs for plaindrome only, as it will have repetetive num in list.
        addsum = digit*(10**index) + addsum
        index = index + 1
    if fn_num == addsum:
        print("Yes. Given number is a palindrome number.")
    else:
        print("No. Given number is not a palindrome number.")
    return None

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script accepts a number and checks if it is a palindrome.\n")
    try:
        num = int(input("Enter number: "))
    except ValueError:
        print("Invalid input. Please enter an integer only. Exiting script!\n")
        sys.exit(1)
    else:
        if num < 0:
            print("Please enter a non-negative integer only. Exiting script!\n")
            sys.exit(1)
    print()
    check_palindrome_num(num)
    print()
    return None

# Call main() when the script is executed explicitly.

if __name__ == "__main__":
    main()
