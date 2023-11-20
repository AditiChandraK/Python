#Given 4 sides and two diagonals of a quadrilateral, classify the quadrilateral as square, rhombus, rectangle, parallelogram, kite, just quadrilateral. 
#Requirements 
'''read four sides and two diagonals 
store in different variables 
convert them to integer values 
conditions 
a. if all sides equal and diagonals equal 
display "it is a square" 
b. else if two opposite sides equal and diagonals equal 
display "it is a rectangle" 
c. else if '''
s1 = int(input("side1:"))
s2 = int(input("side2:"))
s3 = int(input("side3:"))
s4 = int(input("side4:"))
d2 = int(input("diagonal1:"))
d1 = int(input("diagonal2:"))
if s1 == s2 == s3 == s4 and d1 == d2:
    print("square")
elif s1 == s3 and s2 == s4 and d1 == d2:
    print("rectangle")
elif s1 == s3 and s2 == s4 and d1 != d2:
    print("parallelogram")
elif s1 == s2 == s3 == s4 and d1 != d2:
    print("rhombus")
elif s1 == s2 and s3 == s4 and d1 != d2:
    print("kite")
else:
    print("quadrilateral")