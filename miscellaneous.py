# Accepting Arguments from CLI
# print("Hello World!") # we can this python file using python ./miscellaneous.py

import sys
# print(sys.argv) # ['.\\miscellaneous.py', 'hello', '56'] if you run python ./miscellaneous.py hello 56
# name = sys.argv[1]
# print(name)

# another method(better method)
import argparse
parser = argparse.ArgumentParser(description="This program prints user inputted color")
parser.add_argument("-c", "--color", metavar="color", required=True, choices={"red", "blue", "green", "yellow", "orange", "pink", "purple", "black", "white", "brown",
                                                                              "grey"}, help="the color to search for")
args = parser.parse_args()
print(args.color)

# Lambda Functions(anonymous functions)
# tiny functions that have no name and have only one expression as their body
double = lambda num : num * 2 # here num is the argument and num * 2 is the expression, remember the expression always has to return something
multiply = lambda a, b : a * b # lambda functions can have multiple arguments
print(multiply(2, 4))
print(double(8))
# utility of lambda functions comes in with other functionality like map, filter and reduce

# map(), filter() and reduce()
# map() - runs a function individually on each item of a list
lists = [1, 2, 3]
result1 = map(lambda a : a * 2, lists) # map(functionName, collectionName)
print(list(result1))

# filter() - runs a filter function on each item of list and new list stores only those items that pass the filter
numbers = [1, 2, 3, 4, 5, 6]
result2 = filter(lambda n : n % 2 == 0, numbers)
print(list(result2))

# reduce() - calculates a value out of a sequence of list
from functools import reduce
expenses = [("Dinner", 80), ("Car Repair", 120)]
sum = reduce(lambda a, b : a[1] + b[1], expenses)
print(sum)

# Recursion - a function calls itself
def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)
print(factorial(3))
print(factorial(4))
print(factorial(5))

# Decorators - change or alter in any way a function works
# a decorator takes a function as an input and wraps it around an inner function
def logtime(func):
    def wrapper():
        print("before")
        val = func()
        print("after")
        return val
    return wrapper

@logtime # decorator
def hello():
    print("hello")

hello()




