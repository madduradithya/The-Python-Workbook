# Exercise 22:Area of a Triangle (Again)
# In the previous exercise you created a program that computed the area of a triangle
# when the length of its base and its height were known. It is also possible to compute
# the area of a triangle when the lengths of all three sides are known. Let s1, s2 and s3
# be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
# can be calculated using the following formula:
# area = square root (s × (s − s1) × (s − s2) × (s − s3))
# Develop a program that reads the lengths of the sides of a triangle from the user and
# displays its area.

from math import sqrt

s1, s2, s3 = int(input("Enter s1: ")), int(input("Enter s2: ")), int(input("Enter s3: "))
s = (s1+s2+s3)/ 2
area = sqrt(s * (s-s1) * (s-s2) * (s-s3))

print("Area of the triangle:", area)
