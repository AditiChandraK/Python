#WAP to print all numbers divisible by 3 and 5 between 1 and n in separate  lines 
x = int(input("number:"))
for i in range(1,x+1):
    if i%3 == 0 and i%5==0:
        print(i)