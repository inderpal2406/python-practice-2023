"""Module to create a list from 2 other lists based on a condition"""

# Import modules.

import custom_module_clear_screen

# Define functions.

def create_new_list(fn_list1,fn_list2):
    """Function to create new list from fn_list1 & fn_list2 based on a condition"""
    # Condition: New list will have odd nums from fn_list1 & even nums from fn_list2
    fn_new_list = []
    for num in fn_list1:
        if num % 2 != 0:
            fn_new_list.append(num)
    for num in fn_list2:
        if num % 2 == 0:
            fn_new_list.append(num)
    return fn_new_list

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print('''
    This script has 2 defined lists. It then creates a 3rd list.
    This 3rd list will have odd nums from 1st list & even nums from 2nd list.
    ''')
    input("Press ENTER key to continue.\n")
    list1 = [10,20,25,30,35]
    list2 = [40,45,60,75,90]
    print(f"The 2 pre-defined lists are,\nList1: {list1}\nList2: {list2}\n")
    new_list = create_new_list(list1,list2)
    print(f"Result list: {new_list}\n")
    return None

# Call main() when this script is executed explicitly.

if __name__ == "__main__":
    main()
