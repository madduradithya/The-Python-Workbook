# Exercise 13:Making Change
# Consider the software that runs on a self-checkout machine. One task that it must be
# able to perform is to determine how much change to provide when the shopper pays
# for a purchase with cash.
# Write a program that begins by reading a number of Indian Rupees from the user as an
# integer. Then your program should compute and display the denominations of the
# coins that should be used to give that amount of change to the shopper. The change
# should be given using as few coins as possible. Assume that the machine is loaded
# with 1, 2, 5, 10, 20, 50, 100 Indian Rupees.

user_amount = int(input("Enter the amount in Indian Rupees: "))

number_of_100 = int(user_amount / 100)
rem_amount = user_amount - number_of_100 * 100
number_of_50 = int(rem_amount / 50)
rem_amount = rem_amount - number_of_50 * 50
number_of_20 = int(rem_amount / 20)
rem_amount = rem_amount - number_of_20 * 20
number_of_10 = int(rem_amount / 10)
rem_amount = rem_amount - number_of_10 * 10
number_of_5 = int(rem_amount / 5)
rem_amount = rem_amount - number_of_5 * 5
number_of_2 = int(rem_amount / 2)
rem_amount = rem_amount - number_of_2 * 2
number_of_1 = int(rem_amount / 1)
rem_amount = rem_amount - number_of_1 * 1

print("Number of 100s given:",number_of_100)
print("Number of 50s given:",number_of_50)
print("Number of 20s given:",number_of_20)
print("Number of 10s given:",number_of_10)
print("Number of 5s given:",number_of_5)
print("Number of 2s given:",number_of_2)
print("Number of 1s given:",number_of_1)
print("Balance pending to be given:",rem_amount)
