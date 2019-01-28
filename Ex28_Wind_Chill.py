# Exercise 28:Wind Chill
# When the wind blows in cold weather, the air feels even colder than it actually is
# because the movement of the air increases the rate of cooling for warm objects, like
# people. This effect is known as wind chill.
# In 2001, Canada, the United Kingdom and the United States adopted the following
# formula for computing the wind chill index. Within the formula Ta is the
# air temperature in degrees Celsius and V is the wind speed in kilometers per hour.
# A similar formula with different constant values can be used with temperatures in
# degrees Fahrenheit and wind speeds in miles per hour.
# WCI = 13.12 + 0.6215Ta − 11.37 V power 0.16 + 0.3965Ta V power 0.16
# Write a program that begins by reading the air temperature and wind speed from the
# user. Once these values have been read your program should display the wind chill
# index rounded to the closest integer.
# The wind chill index is only considered valid for temperatures less than or
# equal to 10 degrees Celsius and wind speeds exceeding 4.8 kilometers per
# hour.

from math import ceil

air_temperature = float(input("Enter the air temperature (in celsius): "))
wind_speed = float(input("Enter the wind speed (in km/hr): "))

if air_temperature > 10.0 or wind_speed <= 4.8:
    print("Error")
else:
    wind_chill_index = ceil(13.12 + (0.6215 * air_temperature) - (11.37 * pow(wind_speed,0.16)) + (0.3965 * air_temperature * pow(wind_speed,0.16)))
    print("Wind chill index:", wind_chill_index)
