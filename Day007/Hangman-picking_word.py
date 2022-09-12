#Step 1
import random
word_list = ["ardvark" , "baboon" , "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter\n")

guess.lower()
for letter in chosen_word:
    if letter == guess:
        print("Match")
    else:
        print("Not a match")