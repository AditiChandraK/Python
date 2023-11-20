#Given a number, find whether the number is armstrong number or not
x = int(input("number:"))
l = len(str(x))
s = 0
for j in str(x):
    s += int(j)
print(s**l)
if x == s**l:
    print("yes")