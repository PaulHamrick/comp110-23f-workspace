"""EX02 - Playing a single wordle instance."""

__author__ = "730556372"

secret: str = "python" #Choosing the secret word
secret_length: int = len(secret) # Making sure the code does not break 
                           # If the secret word has a different length
guess: str = input(f"What is your { secret_length }-letter guess? ") 
                                 # Getting an initial guess

# Storing the different emojis that will be output
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# Initializing the output boxes and the string's index
output_boxes: str = ""
string_idx: int = 0
does_letter_appear_elsewhere: bool = False
yellow_string_idx: int = 0 #String index to figure out if a box should be yellow

# I can't figure out how to merge this and the repeated block later
if (len(guess) == secret_length): # If the guess is the right length
    while (string_idx < secret_length): 
        # Iterating over each character of the strings
        if (guess[string_idx] == secret[string_idx]):
            output_boxes += GREEN_BOX
        else:
            yellow_string_idx = 0
            does_letter_appear_elsewhere = False
            while (yellow_string_idx < secret_length): # Iterating over possible indices of the secret word
                if (guess[string_idx] == secret[yellow_string_idx]): #Checking if the secret word matches the guess
                    does_letter_appear_elsewhere = True
                yellow_string_idx += 1
            # Adding whichever of YELLOW_BOX and WHITE_BOX is appropriate
            if (does_letter_appear_elsewhere == True):
                output_boxes += YELLOW_BOX
            else:
                output_boxes += WHITE_BOX
        string_idx += 1
    print(output_boxes)
    if (guess == secret):
        print("Woo! You got it!")
        exit() # Ending the program
    else:
        print("Not quite. Play again soon!")
        exit() # Ending the program

while (len(guess) != secret_length):
    guess = input(f"That was not { secret_length } letters! Try again: ")
                                      # Getting a new guess
    if (len(guess) == secret_length): # If the guess is the right length
        while (string_idx < secret_length): # The same thing as before
            if (guess[string_idx] == secret[string_idx]):
                output_boxes += GREEN_BOX
            else:
                yellow_string_idx = 0
                does_letter_appear_elsewhere = False
                while (yellow_string_idx < secret_length):
                    if (guess[string_idx] == secret[yellow_string_idx]):
                        does_letter_appear_elsewhere = True
                    yellow_string_idx += 1
                if (does_letter_appear_elsewhere == True):
                    output_boxes += YELLOW_BOX
                else:
                    output_boxes += WHITE_BOX
            string_idx += 1
        print(output_boxes)
        if (guess == secret):
            print("Woo! You got it!")
            exit()
        else:
            print("Not quite. Play again soon!")
            exit()