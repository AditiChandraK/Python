# WAP to print all numbers between 1 and n which are ending with 9 in separate lines 
x = int(input("number:"))
for i in range(1,x+1):
    y = str(i)
    if y[-1] == "9":
        print(y)