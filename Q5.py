#Build a program that requests the user to input their weight in
#kilograms and their height in meters. The program should then calculate and display
#their Body Mass Index (BMI) using the formula: BMI = weight / (height * height


w=int(input("enter weight"))
h=int(input("enter height"))
bmi=w/(h*h)
print(bmi)