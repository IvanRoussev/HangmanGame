"""
ACIT2515 Lab
Week 2 -- complete this file!
Author: Ivan Roussev
Set: A
ID: A01287751
"""

 
from cgitb import text
from operator import contains, index
import random
import string
from xml.dom import WrongDocumentErr

NB_TURNS = 10


def pick_random_word():
    with open('week02/words.txt', 'r') as file:
        text = file.read()
        words = list(map(str, text.split()))

        selected_word = (random.choice(words))

    return selected_word


def show_letters_in_word(word: str, letters: list):
    """
    First, make sure word is uppercase, and all letters are uppercase.
    This function scans the word letter by letter.
    If the letter of the word is in the list of letters, display it.
    Otherwise, display an underscore (_).

    Example:
    >>> show_letters_in_word("VANCOUVER", ["A", "V"])
    'V A _ _ _ _ V _ _'
    >>> show_letters_in_word("TIM", ["G", "V"])
    '_ _ _'
    >>> show_letters_in_word("PIZZA", ["A", "I", "P", "Z"])
    'P I Z Z A'
    """
    my_string = word.upper()

    my_string = len(word) * "_ "
    for item in letters:
        index = 0
        for char in word.upper():
            if char == item:
                my_string = my_string[:index] + char + my_string[index + 1:]
            index += 2
    my_string = my_string[:-1]

    return my_string



    

def all_letters_found(word: str, letters: list):
    """Returns True if all letters in word are in the list 'letters'
    This should return TRUE if all the letters are found in word (if contains underscore means false) """
    if all(chars in letters for chars in word):
        return True
    else:
        return False
    


def main(turns):
    """
    Runs the game. Allows for "turns" loops (attempts).
    At each turn:
    1. Ask the user for a letter
    2. Add the letter to the list of letters already tried by the player
    3. If the letter was already tried, ask again
    4. Use the show_letters_in_word function to display hints about the word
    5. Remove 1 to the number of tries left
    6. Check if the player
        - won (= word has been found)
        - lost (= word has not been found, no tries left)

    Do not forget to pick a random word first :-)

    """
    guessed_letters = []
    turns = 10

    randomWord = pick_random_word()
    print(show_letters_in_word(randomWord, guessed_letters)[:-1])


    for turn in range(turns):


        userInput = input("Guess a letter that the word might contain:").upper()
        
        if userInput in guessed_letters:
            userInput = input(f'This letter has already been picked {userInput} ENTER A NEW LETTER: ').upper()
        else:
            guessed_letters.append(userInput)
            if userInput.upper() in randomWord.upper():
                print(show_letters_in_word(randomWord, guessed_letters))
            else:
                print(f"Letter Not in Word \nGuesses: {guessed_letters}")
        turns -= 1
        
        print(f'{turns} turns left')

        if all_letters_found(randomWord, guessed_letters) == True:
            print("Winner")
        

    
    if all_letters_found(randomWord, guessed_letters) == False:
        print(f"You Lost \n {randomWord} was the word")     



    
    



if __name__ == "__main__":
    main(NB_TURNS)
