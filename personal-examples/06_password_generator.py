"""Module to generate a password adhering to security policies"""

# Import modules.

import random
import time
import custom_module_clear_screen

# Define functions.

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("""
    This script can generate a password of 8/16/24 characters.
    Such a password will adhere to below mentioned policies:
    1. It'll have atleast one upper case character.
    2. It'll have atleast one lower case character.
    3. It'll have atleast one special character like !,@,#,etc.
    4. It'll have atleast one number.
    """)
    while True:
        try:
            no_of_chars = int(input("Password should have how many characters [8|16|24]: "))
        except ValueError:
            print("Invalid input. Please provide the numbers 8 or 16 or 24 only. Try again.")
            continue
        if no_of_chars not in [8,16,24]:
            print("Invalid input. Please provide the numbers 8 or 16 or 24 only. Try again.")
            continue
        else:
            break
    #char_list = []
    #count = 0
    #success1 = False
    #success2 = False
    while True:
        # In each iteration, char list needs to be initiated as empty list.
        # Else, the chars will get appended to the list from last iteration.
        char_list = []
        # In each iteration, countneeds to be initiated as 0.
        # Else, count value comes as (no_of_chars - 1) from last run and
        # in next iteration it never enters the while loop, and same
        # char list is being taken for next iteration which results in endless loops.
        count = 0
        # Similarly, success1 & success2 should also be reset to avoid having
        # their values from last iteration.
        success1 = False
        success2 = False
        while count < no_of_chars:
            random_num = random.randint(33,126)
            our_char = chr(random_num)
            char_list.append(our_char)
            count = count + 1
        for char in char_list:
            if ord(char) in range(65,91,1):
                success1 = True
                break
        for char in char_list:
            if ord(char) in range(97,123,1):
                success2 = True
                break
        if success1 and success2:
            password = "".join(char_list)
            print(f"Random password generated is: {password}")
            break
        else:
            # After multiple iterations of the script, a time comes when script goes for 
            # next iteration continuously. I thought that maybe same random charlist is 
            # being generated each time due to which this is happening. This could be
            # related to random module giving same values due to some issue. So, used
            # setstate() method from random module. But this method requires an 
            # argument to be passed. That arg is a state. We didn't try that.
            # I though that maybe introducing a time gap would make random generate random
            # values. But it is also behaving in the same way of continuous iterations. 
            #random.setstate()
            print("Going for next iteration.")
            print(char_list)  # In output same charlist is getting generated in each iteration.
            #time.sleep(1)
            continue

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
