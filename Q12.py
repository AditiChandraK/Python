#WAP to swap first and last digits of a given number and print the number
x = int(input("number:"))
le = len(str(x))
s = str(x)
f = s[0]
l = s[-1]
print(l+str(x)[1:le-1]+f)