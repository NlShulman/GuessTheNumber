import random
import guessTheNumber_art
logo = guessTheNumber_art.logo
from os import system 
clear = lambda: system('cls')
clear()
print(logo)
print("Welcome to the Number Guessing Game! ")

user_choice = input("I'm thinking of a number between 1 and 100.\n Choose difficulty, type 'Easy' or 'Hard' : ").lower()
number = random.randint(1,100)
end_game = False
if user_choice == "easy":
    attempts = 10 
elif user_choice == "hard":
    attempts = 5
while not end_game:
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess > number:
        print("Too high")
        attempts -= 1
    elif user_guess < number:
        print("Too low")
        attempts -=1
    else: 
        print(f"You got it the answer was {number}")
        end_game = True
    if attempts == 0:
        print("You've run out of guesses, you lose")
        end_game = True
