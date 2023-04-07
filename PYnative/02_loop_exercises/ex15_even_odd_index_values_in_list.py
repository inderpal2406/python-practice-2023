"""Module to print list items at even & odd indexes"""

# Import modules.

import custom_module_clear_screen

# Define functions.

def find_odd_index_values(fn_list):
    """Function to find list items at odd indexes of fn_list list"""
    length = len(fn_list)
    fn_odd_index_value_list = []
    for i in range(1,length,2):
        num = fn_list[i]
        fn_odd_index_value_list.append(num)
    return fn_odd_index_value_list

def find_even_index_values(fn_list):
    """Function to find list items at even indexes of fn_list list"""
    length = len(fn_list)
    fn_even_index_value_list = []
    for i in range(0,length,2):
        num = fn_list[i]
        fn_even_index_value_list.append(num)
    return fn_even_index_value_list

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print('''
    This script has a pre-defined list.
    It displays list items at even & odd indexes.
    ''')
    input("Press ENTER to proceed...")
    numlist = [10,20,30,40,50,60,70,80,90,100]
    even_index_value_list = find_even_index_values(numlist)
    odd_index_value_list = find_odd_index_values(numlist)
    print(f"\nOriginal list: {numlist}")
    print("Values at even indexes:", end=" ")
    for item in even_index_value_list:
        print(f"{item}", end=" ")
    print("\nValues at odd indexes:", end=" ")  # Bring cursor to new line & print.
    for item in odd_index_value_list:
        print(f"{item}", end=" ")
    print("\n")  # Bring cursor to new line and leave one more line at end.

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
