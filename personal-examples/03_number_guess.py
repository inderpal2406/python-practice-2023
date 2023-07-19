"""Module to implement a number guessing game"""

# Import modules.

import time
import random
import math
import custom_module_clear_screen

# Define functions.

def generate_random_num(fn_start_num,fn_end_num):
    """Function to generate random number"""
    #print("Generating random number",end="")  # Python prints this after execution of loop.
    print("\nGeneration of random number is in progress.")
    num = 1
    while num <= 3:
        time.sleep(1.5)
        #print(".",end="")  # Python prints all of this together after execution of the loop.
        print("Still in progress.")
        time.sleep(1.5)
        num = num + 1
    #print()  # Bring cursor to new line.
    fn_random_num = random.randint(fn_start_num,fn_end_num)
    print("\nRandom number generated.\n")
    return fn_random_num

def play_game(fn_start_num,fn_end_num):
    """Function to play the number guessing game"""
    random_num = generate_random_num(fn_start_num,fn_end_num)
    max_no_of_guess = int(round(math.log(fn_end_num - fn_start_num + 1, 2), 0))
    print(f"You've only {max_no_of_guess} chances to guess the number!\n")
    user_no_of_guess = 0
    success = False
    while user_no_of_guess < max_no_of_guess:
        try:
            user_input = int(input("Enter your guessed number: "))
        except ValueError:
            print("Invalid input. Please enter an integer number only. Try again!\n")
            continue
        if user_input < 0:
            print("Invalid input. Please enter a positive integer only. Try again!\n")
            continue
        if user_input < random_num:
            print("Try again! You guessed too small.")
            user_no_of_guess = user_no_of_guess + 1
            continue
        elif user_input > random_num:
            print("Try again! You guessed too high.")
            user_no_of_guess = user_no_of_guess + 1
            continue
        else:
            user_no_of_guess = user_no_of_guess + 1
            success = True
            break
    if success:
        print(f"\nRandom number generated was: {random_num}")
        print(f"Congratulations! You guessed it right in {user_no_of_guess} try!\n")
    else:
        print(f"\nRandom number generated was: {random_num}")
        print("You exhausted all of your tries. Better luck next time!\n")

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("""
    Welcome to the number guessing game!
    In this game you need to provide two numbers.
    Then a random number will be generated in the range between the two supplied numbers.
    You need to guess that random number in minimum number of guesses!
    Press ENTER key to continue.
    """)
    input()  # Read ENTER key.
    print("\n*** NOTE: For simplicity, please provide only positive integers. ***\n")
    while True:
        try:
            start_num = int(input("Enter the start number: "))
            end_num = int(input("Enter the end number: "))
        except ValueError:
            print("Invalid input. Please provide an integer number only. Accepting input again.\n")
            continue
        # Validate if start_num or end_num are not < 0.
        if start_num < 0 or end_num < 0:
            print("Please provide numbers greater than zero. Accepting input again.\n")
            continue
        # We introduce below condition as random.randint(x,y) works only if x<y.
        elif start_num > end_num:
            print("Starting number should be less than ending number. Accpeting input again.\n")
            continue
        else:
            break
    play_game(start_num,end_num)

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
