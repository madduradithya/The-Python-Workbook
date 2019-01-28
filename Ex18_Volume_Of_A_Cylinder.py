# Exercise 18:Volume of a Cylinder
# The volume of a cylinder can be computed by multiplying the area of its circular
# base by its height. Write a program that reads the radius of the cylinder, along with
# its height, from the user and computes its volume. Display the result rounded to one
# decimal place. V = pi * r square * h

from math import pi

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

area = pi * pow(radius, 2) * height

print(f"Area of the cylinder: {area:.1f}")
