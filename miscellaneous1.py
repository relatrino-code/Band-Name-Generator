# Docstrings - used to add descriptions for various parts of the program to used when help is called for a program snippet
"""miscellaneous1 module

This module is a test module for testing out Docstrings
and provides the following classes:


- Dog
...
"""

class Dog:
    """A class representing a dog"""
    def __init__(self, name, age):
        """Initialize a new dog"""
        self.name = name
        self.age = age

    def bark(self):
        """Let the dog bark"""
        print("Woof!")

print(help(Dog))

# Annotations - optionally show type of value
def increment(n: int) -> int: # specifies that this function receives an int as a parameter and then returns an int
    return n + 1

count: int = 0 # specifies that this variable is of int type
# python actually ignores these types though

# Exceptions - try, except, finally
try:
    # some lines of code
    result = 2 / 0
except ZeroDivisionError:
    # handler <ERROR1>
    print("Cannot divide by zero!")
except EOFError:
    # handler <ERROR2>
    print("Could not read file!")
else:
    # no exceptions were raised, the code ran successfully
    print("Code ran successfully!")
finally:
    # do something in any case
    result = 1
print(result) # 1

# we can intentionally raise exceptions using:
try:
    raise Exception("An error!")
except Exception as error:
    print(error)

# we can also define our own class extending from exception
class DogNotFoundException(Exception):
    print("We are inside the class")
    pass

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print("Dog not found!")

# 'with' - makes working with exceptions easier, for example each time we open a file, we must close it
# code without 'with' statement
filename = '/Users/coder/test.txt'
try:
    file = open(filename, 'r')
    content = file.read()
    print(content)
finally:
    file.close()

# code with 'with' statement
with open(filename, 'r') as file:
    content1 = file.read()
    print(content1)
# 'with' will automatically close the file nce read, this is implicit exception handling

# Third Party Package
# pip - install third party packages using pip from pypi.org
# Do this in the shell(for example the requests HTTP server package)
# pip install requests - to install a package
# pip install -u requests - to update and install a package
# pip uninstall requests - to uninstall a package
# pip show requests - to show info regarding the package

# List Compressions - create lists in a very concise way
nums = [1, 2, 3, 4, 5]
nums_power_2 = [n**2 for n in nums] # list compressions
print(nums_power_2)
# we can also do this with a map
nums_power_2_2 = list(map(lambda n : n**2, nums))
print(nums_power_2_2)

# Polymorphism - generalises a functionality so that it can work on different types
class Dog:
    def eat(self):
        print("Eating dog food")

class Cat:
    def eat(self):
        print("Eating cat food")
animal1 = Dog()
animal2 = Cat()
animal1.eat()
animal2.eat()
# we can build a general interface for generalizing every animal

# Operator Overloading - we can make classes comparable and make them work with python operators
class Human:
    # the Human class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        # the __gt__(self, other) function compares a specific property of two class objects
        return True if self.age > other.age else False

roger = Human("Roger", 8)
sid = Human("Sid", 7)
print(roger > sid) # True, comparing the age property of roger and sid using __gt__(self, other)
# similarly we can create __lt__(self, other); etc.
# __add__() respond to + operator
# __sub__() respond to - operator
# __mul__() respond to * operator
# __truediv__() respond to / operator
# __floordiv__() respond to // operator
# __mod__() respond to % operator
# __pow__() respond to ** operator
# __rshift__() respond to >> operator
# __lshift__() respond to << operator
# __and__() respond to & operator
# __or__() respond to | operator
# __xor__() respond to ^ operator







