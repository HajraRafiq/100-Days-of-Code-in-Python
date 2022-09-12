from art import logo
import random
easy_level_turns = 10
hard_level_turns = 5

def check_answer(guess,answer,turns):
    
    if guess > answer:
        print("Too High.")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f'You guessed it right. The answer was {answer}')

def difficulty():
    difficulty_level = input("Choose a difficulty. Type easy or hard :")
    if difficulty_level == "easy":
        return easy_level_turns
    elif difficulty_level == "hard":
        return hard_level_turns


def play_game():
    print("WELCOME TO GUESSING GAME!")
    print("I am thinking a number between 1 and 100")
    answer = random.randint(1,100)
    print(f"The answer was {answer}")
    turns = difficulty()


    guess = 0

    while guess != answer:
        print(f'You have {turns} attempts remaining to guess the number.')
        guess = int(input("Make a guess : "))
        turns=check_answer(guess,answer,turns)
        if turns == 0:
            print("You've run out of turns. You lose")
            return 0
        elif guess!=answer:
            print("Guess again: ")
    

play_game()