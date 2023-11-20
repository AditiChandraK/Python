#WAP to check whether a given number is palindrome or not. 
x = int(input("number:"))
le = len(str(x))
s = str(x)
f = s[0]
l = s[-1]
y = l+str(x)[1:le-1]+f
if x == y:
    print("palindrome")
