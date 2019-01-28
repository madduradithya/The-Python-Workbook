# Exercise 6:Tax and Tip
# The program that you create for this exercise will begin by reading the cost of a meal
# ordered at a restaurant from the user. Then your program will compute the tax and
# tip for the meal. Use your local tax rate when computing the amount of tax owing.
# Compute the tip as 18 percent of the meal amount (without the tax). The output from
# your program should include the tax amount, the tip amount, and the grand total for
# the meal including both the tax and the tip. Format the output so that all of the values
# are displayed using two decimal places.
cost_of_the_meal = input("Please enter the cost of the meal (in dollars): ")
tax_for_the_meal = float(cost_of_the_meal) * (5/100)
tip_for_the_meal = float(cost_of_the_meal) * (18/100)
grand_total_of_the_meal = float(cost_of_the_meal) + tax_for_the_meal + tip_for_the_meal
print(f"Tax amount (in dollars): {tax_for_the_meal:.2f}")
print(f"Tip amount (in dollars): {tip_for_the_meal:.2f}")
print(f"Grand total (in dollars): {grand_total_of_the_meal:.2f}")
