# Exercise 33: Day Old Bread
# A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
# percent. Write a program that begins by reading the number of loaves of day old
# bread being purchased from the user. Then your program should display the regular
# price for the bread, the discount because it is a day old, and the total price. All of the
# values should be displayed using two decimal places, and the decimal points in all
# of the numbers should be aligned when reasonable values are entered by the user.

quantity_of_day_old_bread = int(input("Enter the number of day old bread being purchased: "))
regular_price = quantity_of_day_old_bread * 3.49
discount_factor = 0.6
discount_provided = regular_price * discount_factor
total_price = regular_price - discount_provided

print(f"Regular price of the bread: {regular_price:.2f}")
print(f"Discount provided: {discount_provided:.2f}")
print(f"Total price: {total_price:.2f}")
