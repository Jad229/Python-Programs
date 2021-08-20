import random

choices = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''','''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''','''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

computer_choice = random.randint(0, 2)
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors "))

if(computer_choice == 0 and player_choice == 1):
    print(choices[player_choice])
    print("Computer chose:\n" + choices[computer_choice])
    print("You Win!")
elif(computer_choice == 0 and player_choice == 2):
    print(choices[player_choice])
    print("Computer chose:\n" + choices[computer_choice])
    print("You Lose!")
elif(computer_choice == player_choice):
    print(choices[player_choice])
    print("Computer chose:\n" + choices[computer_choice])
    print("It's a Draw!")
elif(computer_choice == 1 and player_choice == 0):
    print(choices[player_choice])
    print("Computer chose:\n" + choices[computer_choice])
    print("You Lose!")
elif(computer_choice == 1 and player_choice == 2):
    print(choices[player_choice])
    print("Computer chose:\n" + choices[computer_choice])
    print("You Win!")
elif(computer_choice == 2 and player_choice == 0):
    print(choices[player_choice])
    print("Computer chose:\n" + choices[computer_choice])
    print("You Win!")
else:
    print(choices[player_choice])
    print("Computer chose:\n" + choices[computer_choice])
    print("You Lose!")



