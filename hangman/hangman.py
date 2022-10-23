# panel start
import random

import sys

print("HANGMAN""\nThe game will be available soon.")
a = 'play'
b = 'exit'
print("If you want start game type ""play")
print("If you want to finish the game press ""exit")
choice_input = (input(">"))
if choice_input == b:
    sys.exit("See you next time")

# hangman game
words = 'python', 'java', 'javascript', 'php'
guess_word = random.choice(words)
tries = 8
guesses = []
done = False

while not done:
    print('tries: ', tries)
    for letter in guess_word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("-", end=" ")
    print("")

    guess = input("Input a letter:")
    guesses.append(guess.lower())
    if guess.lower() not in guess_word.lower():
        print("That letter doesn't appear in the word")
        tries -= 1
        if tries == 0:
            break

    done = True
    for letter in guess_word:
        if letter.lower() not in guesses:
            done = False
if done:
    print(f"You win!!!")
else:
    print(f"Game over! The word was {guess_word}!")

