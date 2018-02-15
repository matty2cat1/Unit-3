#Matt Westelman
#reallyBadPsychic.py - because 42 is over used
#2/14/18

from random import randint
num = randint(1, 3)

input("You have journyed well! For your acomplishments, I shall answer questions for thee: Please ask me your questions: ")

while 1==1:
    num = randint(1,3)
    if num ==1:
       text = input("I can't answer that now, please ask another question: ")
    elif num ==2:
        text = input("I am sorry, but you aren't meant to know that. Please ask another question: ")
    else:
        text = input("You will find out in due time child. Please ask another question: ")
    if text == 'quit':
        break
