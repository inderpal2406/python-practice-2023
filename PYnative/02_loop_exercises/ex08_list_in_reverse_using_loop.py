"""Module to print a list in reverse order using a loop"""

# Import modules.

import custom_module_clear_screen

# Define functions.

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script prints list items of pre-defined list in reverse order.\n")
    input("Press ENTER to proceed.")
    numlist = [10,20,30,40,50]
    print(f"\nPre-defined list: {numlist}")
    print("List items in reverse order are as below:")
    numlist.reverse()
    for num in numlist:
        print(f"{num}")
    print()  # Leave a line at end.

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
