"""Module to demonstrate normal termination of a loop"""

# Import modules.

import custom_module_clear_screen

# Define functions.

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script shows normal termination of a loop using else block.\n")
    input("Press ENTER to continue.\n")
    for num in range(1,6,1):
        print(num)
    else:
        print("Done!")
    print()

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
