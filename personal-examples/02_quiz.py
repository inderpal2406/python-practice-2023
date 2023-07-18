"""Module to depict a quiz game"""

# Import modules.

import random
import time
import custom_module_clear_screen

# Define functions.

def play_game(fn_dict):
    """Function to play the quiz game"""
    fn_score = 0
    for key in fn_dict:
        print(f"{key}")
        answer = input("Answer: ")
        if answer.lower() == fn_dict.get(key).lower():
            fn_score = fn_score + 1
        print()     # Leave a line for next question.
    return fn_score

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("""
    Welcome to this QUIZ game!
    We'll ask you 5 questions and then display your score.
    Press ENTER key to proceed.
    """)
    input()  # Read ENTER key.
    # Initialize the 3 dictionaries with different set of question & answers.
    dict_one = {
        "What is India's capital?" : "New Delhi",
        "Which is the largest continent in the world?" : "Asia",
        "Which is the longest river in the world?" : "Nile",
        "What is the latitude at 0 degree called as?" : "Equator",
        "Which is the largest bird in the world?" : "Ostrich"
    }
    dict_two = {
        "Which is the highest mountain in the world?": "Mount Everest",
        "Which is the fastest land animal?": "Cheetah",   
        "What is the capital of U.S.A?" : "Washington D.C.",
        "Which is the largest country in the world in terms of area?" : "Russia",
        "Which animal has the largest eyes?" : "Giant Squid"
    }
    dict_three = {
        "Which is the tallest building in the world?": "Burj Khalifa",
        "What is Earth's only natural satellite called?": "Moon",
        "What is the capital of Australia?": "Canberra",
        "Which country is known as the 'Land of the thunder dragon'?": "Bhutan",
        "Which country gifted the 'Statue of Liberty' to the U.S.A?": "France"
    }
    #"How many colors are present in the rainbow? Give answer as a number." : 7,
    # We have not put questions which has answer as a number, bcoz accepting an
    # int number would require more logic in play_game().
    choice = random.randint(1,3)
    if choice == 1:
        our_dict = dict_one
    elif choice == 2:
        our_dict = dict_two
    else:
        our_dict = dict_three
    score = play_game(our_dict)
    if score == len(our_dict):
        print(f"Congratulations! You've scored {score}/{len(our_dict)}.\n")
    else:
        print(f"You've scored {score}/{len(our_dict)}. Better luck next time!\n")
    second_choice = input("Do you want to see the correct answers? [y|n]: ")
    if second_choice.lower() == "y":
        for key in our_dict:
            print(f"\n{key}")
            print(f"Answer: {our_dict.get(key)}")
            time.sleep(2)
    print("\nThat's it for now then. To play the quiz again, execute the script again.\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
