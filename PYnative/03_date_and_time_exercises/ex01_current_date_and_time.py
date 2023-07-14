"""Module to print current date and time"""

# Import modules.

from datetime import datetime
import custom_module_clear_screen

# Define functions.

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("Current date and time is:")
    print(f"{datetime.now().strftime('%a %d-%m-%Y %H:%M:%S')}")
    print()

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
