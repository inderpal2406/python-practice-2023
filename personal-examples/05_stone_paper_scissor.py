"""Module to depict stone-paper-scissor game"""

# Import modules.

import time
import random
import custom_module_clear_screen

# Define functions.

def generate_comp_choice(our_dict,user_choice):
    """Function to generate computer choice from stone/paper/scissor"""
    choice_list = list(our_dict.values())
    # Computer choice should be between other 2 choices, left after removal os user's choice.
    choice_list.remove(user_choice)
    comp_choice = random.choice(choice_list)
    return comp_choice

def accept_user_choice(our_dict):
    """Function to accept user choice from stone/paper/scissor"""
    while True:
        for our_key in list(our_dict.keys()):
            print(f"{our_key}. {our_dict.get(our_key)}")
        try:
            user_input = int(input("Enter your choice [1|2|3]: "))
        except ValueError:
            print("Invalid input! Please enter an integer number only. Try again.\n")
            continue
        if user_input in [1,2,3]:
            break
        else:
            print("Invalid input! Please enter a digit as 1 or 2 or 3 only. Try again.\n")
            continue
    return our_dict.get(user_input)

def play_game():
    """Function to play stone-paper-scissor game"""
    choice_dict = {1: "Stone", 2: "Paper", 3: "Scissor"}
    user_score = 0
    comp_score = 0
    for count in range(1,6,1):
        print(f"Round {count}:\n")
        time.sleep(1.5)
        user_choice_str = accept_user_choice(choice_dict)
        print(f"\nYou selected {user_choice_str}.\n")
        time.sleep(1.5)
        comp_choice_str = generate_comp_choice(choice_dict,user_choice_str)
        print(f"\nComputer selected {comp_choice_str}.\n")
        time.sleep(1.5)
        if (user_choice_str == "Stone" and comp_choice_str == "Scissor") or \
        (user_choice_str == "Scissor" and comp_choice_str == "Paper") or \
        (user_choice_str == "Paper" and comp_choice_str == "Stone"):
            user_score = user_score + 1
            print("You've won this round!\n")
        else:
            comp_score = comp_score + 1
            print("The computer has won this round!\n")
        time.sleep(1.5)
        print(f"Round {count} scores:\nPlayer: {user_score}\tComputer: {comp_score}\n")
        time.sleep(1.5)
    print(f"Final scores after {count} rounds:")
    print(f"Player: {user_score}\tComputer: {comp_score}")
    if user_score > comp_score:
        print("Congratulations! You've won this game!\n")
    else:
        print("The computer has won this game! Better luck next time!\n")

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("""
    ********************************************
                      WELCOME
              Stone-Paper-Scissor Game
    ************ Rules for the game: ***********
    Stone vs scissor -> Stone wins
    Scissor vs paper -> Scissor wins
    Paper vs stone   -> Paper wins
    ************    Instructions:    ***********
    - This'll be played between you & the computer.
    - Total 5 rounds will be played.
    - The player who scores the most will be the winner.
    *********************************************
    Press ENTER key to proceed.
    """)
    input()  # Read ENTER key.
    play_game()

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
