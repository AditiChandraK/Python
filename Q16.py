#WAP to print all Strong numbers between 1 to n. 
#   Strong number is a special number whose sum of the factorial of 
#   digits is equal to the original number. For Example: 145 is strong number. Since, 1! + 4! + 5!
x = int(input("Enter number:"))
for i in range(x):
    f = str(x)
    s = 0
    for i in f:
        s1 = 1
        for j in range(1,int(i)+1):
            s1 = s1 * j
        s += s1
if s == x:
    print("strong")
    