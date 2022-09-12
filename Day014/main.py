import random
from art import logo , vs
from data import data
import os



def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f" {account_name} , a {account_desc}, from {account_country}"

def answer(guess,A_followers,B_followers):

    if A_followers > B_followers:
        if guess == "a":
            return True
        else:
            return False
    else:
        if guess == "b":
            return True
        else:
            return False
score = 0
account_B = random.choice(data)
game_continue = True
while game_continue:
    print(logo)
    account_A= account_B
    account_B = random.choice(data)

    while account_A == account_B:
        account_B = random.choice(data)

    print(f" Compare A: {format_data(account_A)}")
    print(vs)
    print(f" Compare B: {format_data(account_B)}")

    A_follower_count = account_A["follower_count"]
    B_follower_count = account_B["follower_count"]
    guess = input("Who has more followers ? Type 'A' or 'B': \n").lower()
    os.system('clear')
    
    is_correct = answer(guess , A_follower_count, B_follower_count)

    if is_correct:
        score +=1

        print(f"You're right! Your score is {score}")
        
    else:
        game_continue = False
        print(f"Sorry You're wrong . Your score is {score}")


