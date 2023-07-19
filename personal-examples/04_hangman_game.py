"""Module to depict a hangman game"""

# Import modules.

import random
import custom_module_clear_screen

# Define functions.

def generate_secret_word_and_hint():
    """Function to generate a secret word & a hint for it"""
    our_dict = {
        "category_one": {
            "category_hint": "fruit",        
            "values": ["apple","mango","grapes","papaya","watermelon","litchi","cherry","banana"]
        },
        "category_two": {
            "category_hint": "vegetable",
            "values": ["brinjal","potato","beans","peas","tomato","carrot","cucumber","onion"]
        },
        "category_three": {
            "category_hint": "animal",
            "values": ["lion","tiger","cheetah","elephant","giraffe","kangaroo","rabbbit","fox"]
        },
        "category_four": {
            "category_hint": "flower",
            "values": ["rose","lily","lotus","sunflower","periwinkle","jasmine","tulip","orchid"]
        }
    }
    random_category = random.choice(list(our_dict.keys()))
    random_word = random.choice(our_dict.get(random_category).get("values"))
    hint = our_dict.get(random_category).get("category_hint")
    return random_word, hint

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print("""
    Welcome to the HANGMAN game!
    In this game, a secret word & a hint about it would be given.
    You need to guess the secret word by guessing the letters in it in minimum tries.
    Press ENTER key to proceed.
    """)
    input()  # Read the ENTER key.
    secret_word, secret_hint = generate_secret_word_and_hint()
    #fruits = ["mango","apple","grapes"]
    #secret_word = random.choice(fruits)
    secret_word_list = []
    for i in secret_word:
        secret_word_list.append(i)
    #hint = "fruit"
    print(f"Guess the word! HINT: word is name of a {secret_hint}.")
    guessed_word_list = []
    for i in secret_word:
        guessed_word_list.append("_")
    for i in guessed_word_list:
        print(f"{i}",end=" ")
    print()  # Bring cursor to new line after the above loop.
    max_tries = len(secret_word) + 2
    print(f"You have maximum {max_tries} tries to guess all the {len(secret_word)} letters as indicated by _ above.\n")
    count = 0
    success = False
    while count < max_tries:
        user_guess = input("Enter the guessed letter: ")
        if user_guess in secret_word_list:
            index = secret_word_list.index(user_guess)
            guessed_word_list.insert(index,user_guess)
            guessed_word_list.pop(index+1)
            for i in guessed_word_list:
                print(f"{i}",end=" ")
            print()  # Bring cursor to new line after the above loop.
            secret_word_list.insert(index,"_")
            secret_word_list.pop(index+1)
        count = count + 1
        if "_" not in guessed_word_list:
            success = True
            break
    if success:
        print(f"\nCongratulations! You've guessed the word correctly in {count} tries.\n")
    else:
        print(f"\nThe word was: {secret_word}")
        print("You've exhausted all the tries. Better luck next time!\n")
    #print(f"secret word list: {secret_word_list}")
    #print(f"guessed word list: {guessed_word_list}")

if __name__ == "__main__":
    main()
