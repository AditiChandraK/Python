#WAP to print whether a given number is perfect number or not. 
#    A perfect number is a positive integer that is equal to the sum of its 
#    positive divisors, excluding the number itself.
x = int(input("number:"))
s=0
for i in range(1,x):
    if x%i==0:
        s+=i
if s == i:
    print("perfect")
    