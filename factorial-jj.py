# James Jack
# 2/19/21

# Problem 6: Use a for statement to calculate the factorial of a user input value.
# Print this value as well as the calculated value using the factorial function in the math module

import math

numb = int(input("enter number to calculate factorial of"))  # create inout prompt


def factorial(n):  # creates function called factorial with (n)
    fact = 1  # variable setting value to one
    for num in range(2, n + 1):  # for loop for performing func by starting range at 2 and adding 1 to user value
        fact *= num  # operator that acts as 1 * num
    return fact  # returns the result of function to beginning, factorials are recursive


print("the factorial is: ", factorial(numb))  # prints the function to be performed with user input
print("the built in answer is ", math.factorial(numb))  # prints module included
