# Exercise 31:Sum of the Digits in an Integer
# Develop a program that reads a four-digit integer from the user and displays the sum
# of the digits in the number. For example, if the user enters 3141 then your program
# should display 3+1+4+1=9.

input_number = input("Enter a four-digit integer: ")

if len(input_number) < 4:
    print("Error")
else:
    addition_sum = int(input_number[0]) + int(input_number[1]) + int(input_number[2]) + int(input_number[3])
    print("Sum of the digits:", addition_sum)
