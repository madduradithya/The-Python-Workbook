# Exercise 5: Bottle Deposits
# In many jurisdictions a small deposit is added to drink containers to encourage people
# to recycle them. In one particular jurisdiction, drink containers holding one liter or
# less have a $0.10 deposit, and drink containers holding more than one liter have a
# $0.25 deposit.
# Write a program that reads the number of containers of each size from the user.
# Your program should continue by computing and displaying the refund that will be
# received for returning those containers. Format the output so that it includes a dollar
# sign and always displays exactly two decimal places.
less_than_one_liter = input("Enter the number of containers less than one liter: ")
more_than_one_liter = input("Enter the number of containers greater than one liter: ")
total_refund_amount = (float(less_than_one_liter) * 0.10) + (float(more_than_one_liter) * 0.25)
print(f"Total refund to be issued: ${total_refund_amount:.2f}")
