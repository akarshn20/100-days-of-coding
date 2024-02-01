rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random

print("Welcome to rock, papers, scissors")
user_choice = int(
    input("What do you choose? Type 0 for rock, 1 for papers and 2 for scissors. \n")
)
comp_choice = random.randint(0, 2)
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("You typed an invalid choice, you lose!")

print("Computer Choose: ")
if comp_choice == 0:
    print(rock)
elif comp_choice == 1:
    print(paper)
elif comp_choice == 2:
    print(scissors)
else:
    print("You typed an invalid choice, you lose!")
if user_choice == 0 and comp_choice == 2:
    print("You win!")
elif user_choice == 1 and comp_choice == 0:
    print("You win!")
elif user_choice == 2 and comp_choice == 1:
    print("You win!")
elif user_choice == comp_choice:
    print("It's a draw!")
else:
    print("You lose!")
