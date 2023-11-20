#WAP to find all factors of a given number.
x = int(input("enter number:"))
for i in range(1,x):
    if i%x == 0:
        print(i)