# ROCK PAPER SCISSOR
'''
RULES -
1. Rock wins against scissors.
2. Scissors win against paper.
3. Paper wins against rock.
'''

import random

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

user_score = 0
computer_score = 0

while True:
    print("What do you choose? Type 0 for 'Rock', 1 for 'Paper' or 2 for 'Scissors' or any other number to 'Exit'")
    user_choice = int(input())

    components = [rock, paper, scissors]
    
    if user_choice == 0:
        print(f"user choosed ROCK\n{components[0]}")
    elif user_choice == 1:
        print(f"user choosed PAPER\n{components[1]}")
    elif user_choice == 2:
        print(f"user choosed SCISSORS\n{components[2]}")
    else:
        print("You choosed to exit the game")
        break

    computer_choice = random.randint(0, 2)

    if computer_choice == 0:
        print(f"computer choosed ROCK\n{components[0]}")
    elif computer_choice == 1:
        print(f"computer choosed PAPER\n{components[1]}")
    elif computer_choice == 2:
        print(f"computer choosed SCISSORS\n{components[2]}")

    # logic of rock, paper and scissors game
    if (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
        print("COMPUTER WINS!")
        computer_score += 1
    elif (user_choice == computer_choice):
        print("its a draw")
    else:
        print("USER WINS!")
        user_score += 1
    
    print(f"User Score = {user_score}")
    print(f"Computer Score = {computer_score}")

if user_score > computer_score:
    print("User WON!!")
elif computer_score > user_score:
    print("Computer WON!!")
else:
    print("DRAW")