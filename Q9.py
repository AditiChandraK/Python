#WAP to print all Armstrong numbers from 1 to n. If not available, display proper msg to the user. 
'''Armstrong number is a number if the sum of its own digits raised to 
the power number of digits gives the number itself. For example, 0, 
1, 153, 370, 371, 407 are three-digit Armstrong numbers and, 1634, 
8208, 9474 are four-digit Armstrong numbers and there are many 
more'''
x = int(input("number:"))
for i in range(1,x+1):
    l = len(str(i))
    s = 0
    for j in str(i):
        s += int(i)**l
        print(s)
    if i == s:
        print(i)