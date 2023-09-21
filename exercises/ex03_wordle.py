"""EX03 - Wordle, the whole thing this time."""

__author__ = "730556372"

#Initializing the emoji boxes

secret_word: str = "codes"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(some_string: str, a_character: str) -> bool:  
    """Check for a particular character within a particular string."""
    assert len(a_character) == 1  #Checking if the character is, indeed, a character

    length_of_string: int = len(some_string)
    string_idx: int = 0
    while (string_idx < length_of_string):  
        #Looping over characters in the string to check if they are the given character
        if some_string[string_idx] == a_character:
            return True
        string_idx += 1
    return False

def emojified(guess_string: str, secret_string: str) -> str:
    """Generating a string of emoji boxes as in wordle out of two strings."""
    assert len(guess_string) == len(secret_string)  #Making sure the strings have the same length
    length: int = len(guess_string)
    string_idx: int = 0
    emoji_string: str = ""  #Initializing the return string
    while (string_idx < length):
        #Figuring out whether to add a green, yellow, or white box
        if guess_string[string_idx] == secret_string[string_idx]:
            emoji_string += GREEN_BOX
        else:
            if contains_char(secret_string, guess_string[string_idx]):
                emoji_string += YELLOW_BOX
            else:
                emoji_string += WHITE_BOX
        string_idx += 1
    return emoji_string

def input_guess(guess_length: int) -> str:
    """Getting a guess with a particular length."""
    guess = input(f"Enter a { guess_length } character word: ")
    if len(guess) == guess_length:
        return guess
    else:
        while len(guess) != guess_length:
            guess = input(f"That wasn't { guess_length } chars! Try again: ")
        return guess
    
def main() -> None:
    """The main loop using the previously defined functions."""
    turn_number: int = 1
    while (turn_number < 7):  #Iterating over turn number
        print(f"=== Turn { turn_number }/6 ===")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if (guess == secret_word):
            print(f"You won in { turn_number }/6 turns!")
            return
        turn_number += 1
    print("X/6 - Sorry, try again tomorrow!")
    return

if __name__ == "__main__":
    main()