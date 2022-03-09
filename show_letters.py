def show_letters_in_word(word: str, letters: str):
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
   
    letterList = list(letters) 

    my_string = len(word) * "_ "
    for item in letterList:
        index = 0
        for char in word.upper():
            if char == item:
                my_string = my_string[:index] + char + my_string[index + 1:]
            index += 2
    

    return my_string


print(show_letters_in_word("Vancouver", ["A", "V"]))    