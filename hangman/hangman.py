import sys
print("HANGMAN""\nThe game will be available soon.")
a = 'play'
b = 'exit'
print("If you want start game type ""play")
print("If you want to finish the game press ""exit")

user_input = (input(">"))
if user_input == b:
    sys.exit("See you next time")
# panel start

word = "python"
answer = input("Guess the word: >")
if answer == word:
    print("You survived!")
else:
    print("You lost!")
# guess word

print("Level random")
words = 'python', 'java', 'javascript', 'php'
words1 = words
import random
words = random.choice(words)
answer_1 = input("Guess the word: >")
if answer_1 == words:
    print("You survived!")
else:
    print("You lost!")
# random lvl

print("Level with hints")
import random
user_1 = random.choice(words1)
word_1 = user_1
far = '-' * len(user_1)
print('Guess the word:',word_1[:3],far)
answer = input(">")
if answer == user_1:
    print("You survived!")
else:
    print("You lost!")
# hints

import random
user_2 = random.choice(words1)
tries = 8
guesses = []
done = False

while not done:
    for letter in user_2:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("-", end=" ")
    print("")

    guess = input("Input a letter:")
    guesses.append(guess.lower())
    if guess.lower() not in user_2.lower():
        print("That letter doesn't appear in the word")
        tries -= 1
        if tries == 0:
            break

    done = True
    for letter in user_2:
        if letter.lower() not in guesses:
            done = False


if done:
    print(f"Thanks for playing!We'll see how well you did in the next stage!")
else:
    print(f"Game over! The word was {user_2}!")
# hangman game
