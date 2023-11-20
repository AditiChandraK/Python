#Given three sides of a triangle, check whether the triangle can be formed or not. If triangle can be formed, find the type of triangle 
x = int(input("enter number:"))
s=5
j=0
i=1
while True:
    for j in range(i,s):
        print(j,end="")
    s = s+4
    i = i+4
    x -= 1
    if x == 0:
        break
    print()