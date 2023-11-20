#control structures 

#Collectively a set of instructions and the control statements controlling their execution is called a control structure.

#Sequential control is a form of control in which instructions are executed in the order that they are written.
#Selection control is provided by a control statement that selectively executes instructions based on a given condition.
#Iterative control is provided by an iterative control statement that repeatedly executes instructions based on a given condition.

#In Python, the grouping is controlled by indentation.



# WHILE 
#A while statement is an iterative control statement that repeatedly executes a set
#of statements based on a provided condition. All iterative control needed in a
#program can be achieved by use of the while statement.

#syntax
#While condition:
#    Statement(s)

#example

#write a Program that tells us that it has stopped raining

'''raining = True
while(raining):
    print("stay indores")
print("rain has stoped you can go out now")'''

# 1---> Write a program to print the numbers from 1 to 10.
'''i=1
while i<11:
    print(i)
    i=i+1
print ("end of loop")'''
# prints the required output.

#2---->Program to find the sum of 10 natural numbers.
'''i=1
sum=0
while i<=10:
    sum=sum+i
    i=i+1
print(sum)'''
#output- 55




#There are 3 ingredients to any iterative statement:
#1. Initial value of the iterative counter or condition
#2. Final Iterative condition
#3. Updating the iterative counter or condition in order to reach the final iterative condition



#selection

#In looping, we execute the body repeatedly. In selection, we choose one of the alternates. Like in the English statement, if this
#__, then that___

#syntax :
#if <expr> :
#    <suite>

#if <expr> :
#   <suite>
#else:
#   <suite>

#Program to check whether given two strings are same
'''a = input("enter string 1 ")
b = input("enter string 2 ")
if a == b :
    print("equal")
else:
    print("not equal")'''

#Program to find whether a given number is positive, negative or zero.
'''num=int(input("enter a number"))
if num>0:
    print("its positive")
elif num<0:
    print("its negative")
else:
    print("its zero")'''



#Dangling else problem:

#If we have two ifs and a single else, to which if should we associate the else.
#This is called dangling else problem. In Python, else matches the if with the same indentation as else.

#The code with comments is self-evident.
# dangling else problem
# two if and single else
# else is paired with the if based on indentation
'''a = int(input())
b = int(input())
c = int(input())
if a == b :
    if b == c :
        print("what?")


else: # paired with the outer if; control reaches here if a not equal to b

    print("what else?")'''


'''if a == b :
    if b == c :
        print("what")
    else: # paired with the inner if; control reaches here if a equals b and b is not equal to c

        print("what else")'''

