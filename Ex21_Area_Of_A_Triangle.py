# Exercise 21:Area of a Triangle
# The area of a triangle can be computed using the following formula, where b is the
# length of the base of the triangle, and h is its height: area = b × h / 2
# Write a program that allows the user to enter values for b and h. The program
# should then compute and display the area of a triangle with base length b and height h.

b = float(input("Enter b: "))
h = float(input("Enter h: "))

area = (b * h) / 2

print("Area of a triangle:", area)
