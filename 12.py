# Prime Number Checker
def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False

    # Loop through all the numbers between 2 and the number
    for i in range(2, num):
        # Check if the number (num) can be divided by the potential prime number
        if num % i == 0:
            return False

    # this return is outside the for loop which will only run once the loop finishes and none of the numbers are divisible. Therefore it is prime.
    return True

#Number Guessing Game Project
import random
from art_12 import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
random_number = random.randint(1, 100)
if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5
while attempts > 0:
    print("Attempts left:", attempts)
    guessed_number = int(input("Make a guess :"))
    if guessed_number > 100:
        print("Your guess is too high.")
    elif guessed_number < 0:
        print("Your guess is too low.")
    elif guessed_number == random_number:
        print("You got it right lets go!")
        break
    elif guessed_number > random_number:
        print("Your guess is too high.")
    elif guessed_number < random_number:
        print("Your guess is too low.")
    attempts -= 1

#Udemy Method of Guessing a Number Game Challenge
'''
from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
#Function to check users guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Your guess is too high.")
        return turns -= 1
    elif user_guess < actual_answer:
        print("Your guess is too low.")
        return turns -= 1
    else:
        print(f"You got it right. Answer is {actual_answer}")
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else :
        return HARD_LEVEL_TURNS
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"The correct answer is {answer}")
    
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} turns left to guess the number.")
        guess = int(input("Make a guess :"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have ran out of turns.")
            return
        else:
            guess != answer
            print("Guess Again.")
game()