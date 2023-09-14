"""Chardle Assignment: Coding Part of Wordle."""

__author__ = "730556372"

word: str = input("Enter a 5-character word: ")  # Grabbing the word
if len(word) != 5:  # Code if the word is not the right length
    print("Error: Word must contain 5 characters")
    exit()

letter: str = input("Enter a single character: ")  # Grabbing the letter
if len(letter) != 1:  # Code if the letter is not one letter
    print("Error: Character must be a single character.")
    exit()

instances: int = 0  # Creating a variable to track instances of the letter
print("Searching for " + letter + " in " + word)

# Checking each index for the letter
if word[0] == letter:
    print(letter + " found at index 0")
    instances += 1  # Updating instances

if word[1] == letter:
    print(letter + " found at index 1")
    instances += 1

if word[2] == letter:
    print(letter + " found at index 2")
    instances += 1

if word[3] == letter:
    print(letter + " found at index 3")
    instances += 1

if word[4] == letter:
    print(letter + " found at index 4")
    instances += 1

# Cases depending on the number of matches
if instances == 0:
    print("No instances of " + letter + " found in " + word)

if instances == 1:
    print("1 instance of " + letter + " found in " + word)

if instances > 1:
    print(str(instances) + " instances of " + letter + " found in " + word)