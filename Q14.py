#Generate all three digit palindrome numbers 
x = int(input("number:"))
for i in range(x):
    le = len(str(i))
    s = str(i)
    f = s[0]
    l = s[-1]
    y = l+str(x)[1:le-1]+f
    if x == y:
        print(i)