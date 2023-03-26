"""Module to print chars on even index of a string"""

# Import modules.

import custom_module_clear_screen

# Define functions.

def print_even_index_chars(fnstr):
    """Function to print chars at even index of fnstr string"""
    index = 0
    count = 0
    print(f"Original string: {fnstr}")
    print("Printing only even index chars.")
    while index < len(fnstr):
        print(f"{fnstr[index]}")
        count = count + 1
        index = index + 2
    print()
    print(f"Total chars in string: {len(fnstr)}")
    print(f"Total chars at even index of the string: {count}")
    return None

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("This script accepts a string & prints chars at even index of it.\n")
    usrstr = input("Enter the string: ")
    print()
    print_even_index_chars(usrstr)
    print()
    return None

# Call main() when the script is executed explicitly.

if __name__ == "__main__":
    main()
