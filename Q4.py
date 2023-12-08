#Create a program that prompts the user to input the radius of
#a circle. The program should then compute and display the area of the circle using
#the formula: Area = π * (radius^2), use the math module for π (pi) 

import math
r=float(input("enter the radius of circle"))
a= math.pi*r*r
print(a)