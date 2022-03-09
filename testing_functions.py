"""
ACIT2515 Lab

Week 2 -- complete this file!

"""
from ntpath import join
import random
from string import ascii_letters
import string

# The number of turns allowed is a global constant
NB_TURNS = 10

def pick_random_word(filename:str) -> str:
    """Opens the words.txt file, picks and returns a random word from the file"""
    # WRITE YOUR CODE HERE !
    words = open(filename, "r")
    wordsList = list(words)
    selected_word = random.choice(wordsList)
    return selected_word


    

def show_letters_in_word(word:str, letters:str):
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
    # WRITE YOUR CODE HERE
    my_string = word.upper()
    letterList = list(letters) 


    for letter in my_string:
        if letter not in letterList:
            my_string = my_string.replace(letter ,"_")

    l = list(my_string)
    my_string = " ".join(l)
    return my_string

def all_letters_found(word, letters):
    """Returns True if all letters in word are in the list 'letters'"""
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
    # WRITE YOUR CODE HERE
    #word = pick_random_word("week02/words.txt")
    word = 'VANCOUVER'

    alphabet = string.ascii_letters
    triedletters = []
    turns = 10
    
    for turn in range(turns):

        guess = input("Please input a letter: ").upper()
        
        if guess in triedletters:
            guess = input(f"You Already Guessed This \nGuesses: {triedletters} \nPlease input another letter: ").upper()
        elif guess not in alphabet:
            guess = input(f"Guesses: {triedletters} \nGuess is not a letter Please input a letter: ").upper()
        else:
            triedletters.append(guess)
            if guess.upper() in word.upper():
                print(show_letters_in_word(word, triedletters)[:-1])
            else:
                print(f"Letter Not in Word \nGuesses: {triedletters}")
        
        if all_letters_found(word, triedletters) == True:
            print("Winner")
        

    
    if all_letters_found(word, triedletters) == False:
        print(f"You Lost \nThe Word Was {word}")

if __name__ == "__main__":
    main(NB_TURNS)