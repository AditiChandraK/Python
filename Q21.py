#Given 3 points A(x1, y1), B(x2, y2) and C(x3, y3), find whether they are collinear. If no, find the centroid. 
#a. Logic: Slope of AB = Slope of BC = Slope of AC 
#b. Centroid = ((x1+x2+x3)/3 , (y1+y2+y3)/3) 
x1 = int(input("x1:"))
x2 = int(input("x2:"))
x3 = int(input("x3:"))
y1 = int(input("y1:"))
y2 = int(input("y2:"))
y3 = int(input("y3:"))

if (y2-y1)/(x2-x1) == (y3-y2)/(x3-x2) == (y3-y1)/(x3-x1):
    print("collinear")
else:
    print("centroid", (x1+x2+x3)/3,",",(y1+y2+y3)/3)