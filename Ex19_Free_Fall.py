# Exercise 19: Free Fall
# Create a program that determines how quickly an object is traveling when it hits the
# ground. The user will enter the height from which the object is dropped in meters (m).
# Because the object is dropped its initial speed is 0m/s. Assume that the acceleration
# due to gravity is 9.8m/s2. You can use the formula vf = square root of vi square + 2*a*d
# to compute the final speed vf, when the initial speed vi, accelaration a, and distance d
# are known

from math import sqrt

height = float(input("Enter the height from which the object will be dropped (in meters): "))
velocity_initial = 0
velocity_final = sqrt(pow(velocity_initial,2) + (2 * 9.8 * height))

print("Velocity with which the object hits the ground (m/s):", velocity_final)
