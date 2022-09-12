import random
word_list = ["ardvark" , "baboon" , "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

display  = []
for each in chosen_word:
    display.append("_")
print(display)

guess = input("Guess a letter\n").lower()

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
        # print(display)
    # else:
    #     print()

print(display) 