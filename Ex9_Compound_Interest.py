# Exercise 9: Compound Interest
# Pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added
# to the balance of the savings account. Write a program that begins by reading the
# amount of money deposited into the account from the user. Then your program should
# compute and display the amount in the savings account after 1, 2, and 3 years. Display
# each amount so that it is rounded to 2 decimal places.
deposit_money = float(input("Enter the deposit amount: "))
interest_for_first_year = float(deposit_money * (4/100))
balance_post_first_year = deposit_money + interest_for_first_year
interest_for_second_year = float(balance_post_first_year * (4/100))
balance_post_second_year = balance_post_first_year + interest_for_second_year
interest_for_third_year = float(balance_post_second_year * (4/100))
balance_post_third_year = balance_post_second_year + interest_for_third_year
print(f"Balance after first year: {balance_post_first_year:.2f}")
print(f"Balance after second year: {balance_post_second_year:.2f}")
print(f"Balance after third year: {balance_post_third_year:.2f}")
