# Exercise 32: Sort 3 Integers
# Create a program that reads three integers from the user and displays them in sorted
# order (from smallest to largest). Use the min and max functions to find the smallest
# and largest values. The middle value can be found by computing the sum of all three
# values, and then subtracting the minimum value and the maximum value.

a, b, c = int(input("Enter a: ")), int(input("Enter b: ")), int(input("Enter c: "))
smallest = min(a, b, c)
largest = max(a, b, c)
middle = (a + b + c) - smallest - largest

print("Numbers in sorted order (ascending):", smallest, middle, largest)
