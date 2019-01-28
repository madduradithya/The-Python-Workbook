# Exercise 17: Heat Capacity
# The amount of energy required to increase the temperature of one gram of a material
# by one degree Celsius is the material’s specific heat capacity, C. The total amount
# of energy required to raise m grams of a material by delta T degrees Celsius can be
# computed using the formula:
# q = mC delta T.
# Write a program that reads the mass of some water and the temperature change
# from the user. Your program should display the total amount of energy that must be
# added or removed to achieve the desired temperature change.
# Hint: The specific heat capacity of water is 4.186 J / gC. Because water has a density
# of 1.0 gram per millilitre, you can use grams and millilitres interchangeably
# in this exercise.
# Extend your program so that it also computes the cost of heating the water. Electricity
# is normally billed using units of kilowatt hours rather than Joules. In this
# exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
# your program to compute the cost of boiling water for a cup of coffee.
# Hint: You will need to look up the factor for converting between Joules and
# kilowatt hours to complete the last part of this exercise.

mass_of_water = int(input("Enter the mass of water: "))
temp_change = int(input("Enter the temperature change: "))
heat_capacity_of_water = 4.186
total_energy = mass_of_water * heat_capacity_of_water * temp_change
print("Total energy (in joules):", total_energy)

kilowatts_quantity = total_energy * 0.0000002778
electricity_cost = kilowatts_quantity * 8.9
print("Cost of electricity (in cents):", electricity_cost)
