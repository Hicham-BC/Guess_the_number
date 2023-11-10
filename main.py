from art import logo
import random as rd

def check_guess(guess):
    if guess == number:
        print(f"*****Congratulation, You Guessed The Right Number: {number}*****")
        return True
    elif guess > number:
        print(f"Your Guessed Number {guess} is Greater Than The Actual Number")
        return False
    else:
        print(f"Your Guessed Number {guess} is Smaller Than The Actual Number")
        return False

print(logo)
print("*****Welcome To The Number Guessing Game*****")
print("\nI'm Thinking of a Number Between 1 and 100.")

dificulty = input('Choose a Dificulty Level. type "Easy", "Normal" or "Hard": ').lower()

game_level = {"easy" : 10, 
              "normal" : 6, 
              "hard" : 3, 
              }

number = rd.randint(1, 100)
attempts = game_level[dificulty]

correct_number = False
while (not correct_number) and (attempts > 0):
    print(f"\nYou Have {attempts} attempts to Guess The Number.")
    guess = int(input("\tGuess The Number: "))
    correct_number = check_guess(guess)
    attempts -= 1
    if attempts == 0 and not correct_number:
        print("*****Sorry, You weren't successful. Try Another Round.*****")