#Matt Westelman
#gauss.py - adding lots of numbers
#2/14/18

num = int(input("Please enter a number"))
num2 = int(input("Enter another!"))

total = 0
for i in range(num,num2+1):
    total= total+i
print(total)
