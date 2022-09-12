import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



word_list = ["ardvark" , "baboon" , "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6
display  = []
for each in chosen_word:
    display.append("_")
print(display)
game_end = False
while not game_end:
    
    guess = input("Guess a letter\n").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:
        lives = lives -1
        if lives == 0:
            game_end = True
            print("You lose")


    if "_" not in display:
        game_end = True
        print("You won")
    print(stages[lives])
    print(display)