#WAP to Classify the number entered by the user as even number or odd number. 
#Till user says stop, he must be able to enter the number for checking its oddness or evenness
while True:
    x = int(input("number:"))
    if x%2 == 1:
        print("odd")
    else:
        print("even")
    q = input("continue?(y/n):")
    if q == "n":
        False