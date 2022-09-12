rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
images = [rock , paper , scissors]
player_choose = int(input("What do you want to choose ?  For rock type '0' , for paper type'1' , for scissors type'2'\n"))
if player_choose >=3 or player_choose <0:
    print("You typed an invalid number")
else:
    print(f"You chose:" , images[player_choose])
    computer_choose = random.randint(0,2)
    print("Computer chose:")
    print(images[computer_choose])

    if player_choose == 0 and computer_choose == 2:
        print("You win")
    elif player_choose == 2 and computer_choose == 0:
        print("Computer won")
    elif computer_choose > player_choose:
        print('Computer won')
    elif computer_choose < player_choose:
        print('You win')
    elif computer_choose == player_choose:
        print("Its a draw")
