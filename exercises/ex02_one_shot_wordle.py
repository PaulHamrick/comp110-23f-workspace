"""EX02 - Playing a single wordle instance."""

__author__ = "730556372"

secret: str = "python" #Choosing the secret word
secret_length: int = len(secret) #Making sure the code does not break 
                           #if the secret word has a different length
guess: str = input(f"What is your { secret_length }-letter guess? ")
print(secret_length)

if (len(guess) == secret_length): # If the guess is the right length
    if (guess == secret):
        print("Woo! You got it!")
        exit() # Ending the program
    else:
        print("Not quite. Play again soon!")
        exit() # Ending the program

while (len(guess) != secret_length):
    guess = input(f"That was not { secret_length } letters! Try again: ")
    if (len(guess) == secret_length): # If the guess is the right length
        if (guess == secret):
            print("Woo! You got it!")
            exit()
        else:
            print("Not quite. Play again soon!")
            exit()