"""Module to print first 10 natural nums"""

import custom_module_clear_screen

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    input("This script prints first 10 natural numbers. Press ENTER to continue.\n")
    print("First 10 natural numbers are as below:")
    for num in range(1,11,1):
        print(num)
    print()
    return None

# Call main() when the script is executed explicitly.

if __name__ == "__main__":
    main()
