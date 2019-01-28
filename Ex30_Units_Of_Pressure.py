# Exercise 30: Units of Pressure
# In this exercise you will create a program that reads a pressure from the user in kilopascals.
# Once the pressure has been read your program should report the equivalent
# pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
# your research skills to determine the conversion factors between these units.

pressure = float(input("Enter the pressure (in kilopascals): "))

pressure_in_pounds_per_square_inch = pressure / 6.895
pressure_in_millimeters_of_mercury = pressure * 7.501
pressure_in_atmospheres = pressure = pressure / 101.325

print("Pressure in pounds per square inch:", pressure_in_pounds_per_square_inch)
print("Pressure in millimeters of mercury:", pressure_in_millimeters_of_mercury)
print("Pressure in atmospheres:", pressure_in_atmospheres)
