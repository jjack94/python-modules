# James Jack
# 2/19/21

# Problem 5: Search the internet for how to convert radians to degrees.
# Write a program to compute the conversion given a user input value.
# Print this value as well as the calculated value using the degrees function in the math module.

import math

x = int(input("enter the value to be converted to degrees: "))  # var assigned to input
degree = (x * 180) / math.pi  # formula is x (radian) * 180 degrees / pi
print("my formula's answer is ", degree)  # print created formula

print("the built in answer is ", math.degrees(x))  # print degrees module version
