import random
from art import logo

EASY_LEVEL_TURNS = 10
DIFFICULT_LEVEL_TURNS = 5

def check_answer(guess, number, turns):
    if guess > number:
        print("too high")
        return turns - 1
    elif guess < number:
        print("too low")
        return turns - 1
    elif guess == number:
        print(f"You got it! The answer is {number}")

def set_difficulty():
    difficulty = input("Choose a difficulty, Type 'easy' or 'hard':  ")
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return DIFFICULT_LEVEL_TURNS
    
def game():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100. ")
    number = random.randint(1,100)
    #print(f"Pssst, the correct answer is {number}")

    turns = set_difficulty()
    guess = 0

    while guess != number:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))
        turns = check_answer(guess, number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again. ")

game()
