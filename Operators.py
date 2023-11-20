#An operator is a symbol that denotes and operation that is performed on data
#Data that is used with operators is called an operand.
#A combination of operators and operands can also be called an expression

#Please note the following.
#- An expression has a value
#- A statement does not
#- An expression is also a statement
#- A statement is not necessarily an expression



#arithmetic operators:
#Operator Expression Name
#-        -x         Negation
#+         x + y     Addition
#-         x - y     Subtraction
#*         x * y     Multiplication
#**        x ** y    Exponentiation
#/         x / y     Division
#//        x // y    Truncation Division
#%         x % y     Modulus



#operator precedance- the order which decides which operator has priority in being excecuted
#Operator Precendence table
#1. ** (exponentiation)
#2. - (negation)
#3. * (multiplication) , / (division) , // (truncation divison) , % (division)
#4. + (addition) , - (subtraction)



#bitwise operator
#These operators, when used operate on the binary value of the given operand.
#They operate on a bit-level, which means that each binary digit is considered.

#• & AND : result is 1 if the corresponding bits are one
#• | OR : result is 1 if even one of the bits is one
#• ^ Exclusive OR : result is 1 if and only if one of the bits is 1
#• << LEFT SHIFT : multiply by 2 for each left shift
#• >> RIGHT SHIFT : divide by 2 for each right shift
#• ~ ONE'S COMPLIMENT : change 0 to 1 and 1 to 0




#relational operators:

#Relational operators work on Boolean values. i.e, they form Boolean expressions
#The Boolean data type contains two Boolean values, denoted as True and False in
#Python
#A Boolean expression is an expression that evaluates to a Boolean value
#Relational operators are used to compare two values.

#Relational Operators     Example       Result
#== equal                 12 == 12      True
#!= not equal             12 != 12      False
#< Less than              10 < 10       False
#> Greater than           “Cat” > “Dog” False
#<= less than or equal to 12 <= 12      True
#>= greater than or equal to 12 >= 12   True




#Membership Operators
#These operators can be used to determine if a particular value occurs within a
#specified collection of values.

#Membership Operators     Example              Result
#in                       11 in (11,12,13)     True
#not in                   11 not in (11,12,13) False



# operators and polymorphism:
#Some operators behave differently based on the type of the operands. They exhibit
#different forms. These are said to be polymorphic.

#operator + on numbers is addition operator.
#operator + on strings, tuples, lists is concatenation operator - juxtapose the two items.
#operator * on numbers is multiplication operator.
#Operator * on strings, tuples, lists with an integer is replication operator - repeat the elements # of times.




#Identity Operators
#Checks if the operands on either side of the operator point to the same object or not Denoted by is and is not
#Example:
#10 is 10 #True
#10 is not 11 #True




#Assignment / Shorthand Operators
#Combines arithmetic and assignment operators

#Operator                 Expression           Short Hand
#+= (Addition)             a = a + b            a += b
#-= (Subtraction)          a = a - b            a -= b
#*= (Multiplication)       a = a * b            a *= b
#/= (Division)             a = a / b            a /= b
##//= (Truncation Division) a = a // b           a //= b
#%= (Modulus)              a = a % b            a %= b
#**= (Exponentiation)      a = a ** b           a **= b
