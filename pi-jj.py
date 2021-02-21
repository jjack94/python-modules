# James Jack
# 2/19/21

# Problem 4:  Search on the internet for a way to calculate an approximation for pi.
# There are many that use simple arithmetic.
# Write a program to compute the approximation and
# then print that value as well as the value of math.pi from the math module.

import math

x = 1  # denominator

y = 0  # sum

for i in range(1000000):  # allows loop to occur to the point value is close to pi

    if i % 2 == 0:  # creates positive even numbers
        y += 4 / x
    else:

        y -= 4 / x   # creates negative odd numbers

    x += 2

print("pi from this program is: ")  # prints pi from formula
print(y)
print("pi from the module is: ")   # prints pi from included module
print(math.pi)
