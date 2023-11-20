#Given n=4, display as below. 
'''a 
   ab 
   abc 
   abcd '''

x = int(input("enter number:"))
for i in range(1,x+1):
    for j in range(i):
        print(chr(97+j), end="")
    print()
