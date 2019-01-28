# Exercise 10:Arithmetic
# Create a program that reads two integers, a and b, from the user.Your program should compute and display:
# a. The sum of a and b
# b. The difference when b is subtracted from a
# c. The product of a and b
# d. The quotient when a is divided by b
# e. The remainder when a is divided by b
# f. The result of log10 a
# g. The result of a power b
# Hint: You will probably find the log10 function in the math module
# helpful for computing the second last item in the list.

from math import log10

a = int(input("Please enter the value for a: "))
b = int(input("Please enter the value for b: "))
print("Sum of a and b:", a+b)
print("Difference when b is subtracted from a:", a-b)
print("Product of a and b:", a*b)
print("Quotient when a is divided by b:", a/b)
print("Remainder when a is divided by b:", a%b)
print("log10 of a:", log10(a))
print("a power b:", a**b)
