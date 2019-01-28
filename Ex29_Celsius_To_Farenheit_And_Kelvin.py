# Exercise 29: Celsius to Fahrenheit and Kelvin
# Write a program that begins by reading a temperature from the user in degrees
# Celsius. Then your program should display the equivalent temperature in degrees
# Fahrenheit and degrees Kelvin. The calculations needed to convert between different
# units of temperature can be found on the internet.

celsius = float(input("Enter the temperature (in celsius): "))

fahrenheit_temp = (celsius * 9/5) + 32
kelvin_temp = celsius + 273.15

print("Temperature in Fahrenheit:", fahrenheit_temp)
print("Temperature in Kelvin:", kelvin_temp)
