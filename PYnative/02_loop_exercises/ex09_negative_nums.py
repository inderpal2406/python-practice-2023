"""Module to print numbers from -10 to -1"""

# Import modules.

import custom_module_clear_screen

# Define functions.

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script prints numbers from -10 to -1.\n")
    input("Press ENTER to proceed.\n")
    for num in range(-10,0,1):
        print(num)
    print()  # Leave a line at end.

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
