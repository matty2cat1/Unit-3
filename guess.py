#Matt Westelman
#3/1/2018
#numberGuess.py - guess a number

from random import randint

num = randint(1,100)

total = 0
guess = int(input("Guess a number "))
if guess>num:
    print("lower, try again")
    total=total+1
    guess = int(input("Guess a number "))
elif guess<num:
    print("Higher, try again")
    total=total+1
    guess = int(input("Guess a number "))
else:
    print("congrats!")
    print("You got the number in ", total, "guesses.")
