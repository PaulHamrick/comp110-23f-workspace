"""Chardle Assignment: Coding Part of Wordle"""

__author__ = "730556372"

word : str = input("Enter a 5-character word: ") # Grabbing the word
letter : str = input("Enter a single character: ") # Grabbing the letter
print("Searching for " + letter + " in " + word)

if word[0] == letter:
    print("letter" + " found at index 0")

if word[1] == letter:
    print("letter" + " found at index 1")

if word[2] == letter:
    print("letter" + " found at index 2")

if word[3] == letter:
    print("letter" + " found at index 3")

if word[4] == letter:
    print("letter" + " found at index 4")