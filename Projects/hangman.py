#hangman

import random

hangman = {
    0:("   ",
       "   ",
       "   "),
    1:(" o ",
       "   ",
       "   "),
    2:(" o ",
       " | ",
       "   "),
    3:(" o ",
       "/| ",
       "   "),
    4:(" o ",
       "/|\\",
       "   "),
    5:(" o ",
       "/|\\",
       "/  "),
    6:(" o ",
       "/|\\",
       "/ \\"),}

incorrect_guess = 0
guesses = 0
words = ["apple","timber","bear","propane","aromatic","centripetal"]

sentence_to_guess = random.choice(words)

hidden_word = ["_"] * len(sentence_to_guess)
guessed_letter = []

for i in hangman[incorrect_guess]:
    print(i)

for i in hidden_word:
    print(i, end= " ")

print("\n")

while incorrect_guess < 7:
    guess_letter = str(input("Guess a letter: "))
    if guess_letter in guessed_letter:
        print("You have already guess that letter retry!")
        continue
    guesses += 1
    guessed_letter.append(guess_letter)
    if guess_letter in sentence_to_guess:
        for i in range(len(sentence_to_guess)):
            if guess_letter == sentence_to_guess[i]:
                hidden_word[i] = guess_letter
    else:
        incorrect_guess += 1
        print("You guessed wrong!")

    for i in hangman[incorrect_guess]:
        print(i)
    for i in hidden_word:
        print(i, end= " ")
    print("\n")

    if hidden_word == list(sentence_to_guess):
        print("Congratulations")
        
        break
    elif incorrect_guess == 6:
        print("You lost the game")
        break
print(f"you guesses: {guesses} times.")
print(f"you incorrect guesses: {incorrect_guess}")
print("Letters you guessed:")
print(",".join(guessed_letter))