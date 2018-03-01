#Matt Westelman
#3/1/2018
#capitalLetters.py - this stuff

word = input("enter text ")
for ch in word:
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" or ch=="y":
        print(ch.upper())
    else:
        print(ch)
    
