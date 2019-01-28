# Exercise 16:Area and Volume
# Write a program that begins by reading a radius, r, from the user. The program will
# continue by computing and displaying the area of a circle with radius r and the
# volume of a sphere with radius r . Use the pi constant in the math module in your
# calculations.
# Hint: The area of a circle is computed using the formula area = πr square. The
# volume of a sphere is computed using the formula volume = 4/3πr cube.

from math import pi

radius = float(input("Enter the radius value: "))
circle_area = pi * pow(radius, 2)
cube_area = 4/3 * pi * pow(radius, 3)

print("Area of the circle is:", circle_area)
print("Area of the cube is:", cube_area)
