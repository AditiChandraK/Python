#WAP to enter a number and print its reverse. 
x = int(input("Enter number:"))
y = str(x)
l = len(y)
for i in range(l-1,-1,-1):
    print(int(y[i]), end = "")