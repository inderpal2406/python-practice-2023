"""Module to count no. of occurrences of a substring in a string"""

# Import modules.

import custom_module_clear_screen
import sys

# Define functions.

def count_word_in_sentence(fn_word,fn_sentence):
    """Function to count occurrences of fn_word in fn_sentence."""
    # Convert to upper case as count() is case sensitive and we want
    # to count a word irrespective of its case.
    #fn_word = fn_word.upper()
    #fn_sentence = fn_sentence.upper()
    # With above statements, word & sentence gets updated to upper case
    # and gets printed in upper case at last. So, we commented it and
    # included upper() in below statement itself.
    count = fn_sentence.upper().count(fn_word.upper())
    # Original above statement.
    #count = fn_sentence.count(fn_word)
    print(f"Sentence: {fn_sentence}")
    if count == 0:
        print(f"The word {fn_word} is not present in the sentence.\n")
    elif count == 1:
        print(f"The word {fn_word} appeared {count} time in the sentence.\n")
    else:
        print(f"The word {fn_word} appeared {count} times in the sentence.\n")
    return None

def main():
    """First function to be called"""
    custom_module_clear_screen.clear_screen()
    print('''
    This script accepts a sentence and a word.
    It then counts no. of occurrences of the word in the sentence.
    ''')
    sentence = input("Enter the sentence: ")
    if sentence == "":
        print("As no sentence is entered, nothing to do further. Exiting script!\n")
        sys.exit(1)
    word = input("Enter the word: ")
    if word == "":
        print("As no word is entered, nothing to search in the sentence. Exiting script!\n")
        sys.exit(1)
    print()
    count_word_in_sentence(word,sentence)
    print()
    return None

# Call main() when the script is executed explicitly.

if __name__ == "__main__":
    main()
