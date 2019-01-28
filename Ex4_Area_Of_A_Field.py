# Exercise 4:Area of a Field
# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.
# 43560 sq.ft. = 1 acre
length = input("Enter the length of the farm (in feet): ")
length_as_int = int(length)
width = input("Enter the width of the farm (in feet): ")
width_as_int = int(width)
area = length_as_int * width_as_int
print("Computed area of the farm (in acres): ", area/43560)
