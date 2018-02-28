#Matt Westelman
#2/28/18
#warmup8.py  - divisibility

i=0
total=0
while i <=100001:
    if i%3==0 and i%10==0 and i%17==0:
        total=total+i
    i = i+1
print(total)
