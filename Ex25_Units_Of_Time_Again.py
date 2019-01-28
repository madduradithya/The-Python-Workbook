# Exercise 25: Units of Time (Again)
# In this exercise you will reverse the process described in the previous exercise.
# Develop a program that begins by reading a number of seconds from the user.
# Then your program should display the equivalent amount of time in the form
# D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds
# respectively. The hours, minutes and seconds should all be formatted so that
# they occupy exactly two digits, with a leading 0 displayed if necessary.

number_of_seconds = int(input("Enter the number of seconds: "))
number_of_days = int(number_of_seconds / 86400)
number_of_seconds = number_of_seconds - number_of_days * 86400
number_of_hours = int(number_of_seconds / 3600)
number_of_seconds = number_of_seconds - number_of_hours * 3600
number_of_minutes = int(number_of_seconds / 60)
number_of_seconds = number_of_seconds - number_of_minutes * 60
number_of_secs = int(number_of_seconds)

print("Number of days:", number_of_days)
print("Number of hours:", number_of_hours)
print("Number of minutes:", number_of_minutes)
print("Number of seconds:", number_of_secs)

final_format = "%d:%02d:%02d:%02d" % (number_of_days, number_of_hours, number_of_minutes, number_of_secs)

print("D:HH:MM:SS", final_format)
