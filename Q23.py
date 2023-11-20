#Given n, display the following (say 4) 
'''
1 0 0 0 
0 1 0 0 
0 0 1 0 
0 0 0 1 '''
 
'''n = 4 
1 2 3 4 
5 6 7 8 
9 10 11 12 
13 14 15 16 '''


x = int(input("enter number:"))
s=0
for j in range(x):
    print("0"*(s)+"1"+"0"*(4-s-1))
    s+=1