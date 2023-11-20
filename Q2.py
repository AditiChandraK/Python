#WAP to print all odd numbers from 1 to n in separate lines 
x = int(input("number:"))
for i in range(1,x+1):
    if i%2 == 1:
        print(i)