#Matt Westelman
#2/28/18
#betterAdditonGameDemo.py  - more loops

from random import randint

numCorrect = 0
while numCorrect < 5:
    num1 = randint(-10,10)
    num2 = randint(-10,10)
    answer= int(input("What is " + str(num1) + " + " + str(num2) + "? "))
    if answer == num1 + num2:
        numCorrect += 1
    else:
        while true:
        print("wrong")

print("you win!")
