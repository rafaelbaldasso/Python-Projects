'''
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''
import random

att = 0
guess = 0
num = random.randint(1, 10)

while guess != num:
    guess = input("\n Choose a random number from 1 to 9 (including) - type 'exit' to quit: ")
    if guess == "exit":
        quit()
    else:
        guess = int(guess)

    if guess < 1 or guess > 9:
        print("\n >>> Choose from 1 to 9!")
        continue
    elif guess < num:
        print("\n >>> Too low!")
        att += 1
        continue
    elif guess > num:
        print("\n >>> Too high!")
        att += 1
        continue

if guess == num:
    print("\n>>> Correct!")
    att += 1
    print("Total attempts:", att)