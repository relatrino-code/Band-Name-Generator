# Enums
from enum import Enum # import Enum from the enum standard library module
# they are a method to create constants in python

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE.value) # or print(State['ACTIVE'].value)
print(list(State)) # prints all the possible values of State
print(len(State)) # prints the number of values of State

# User Input
age = input("What is your age? ")
print(f"Your age is {age}")

# Lists
dogs = ["Roger", "Sid", "Tom", 1, True] # a single list can have different data types inside it
print("Roger" in dogs)# we can check if an item is contained in a list using the in operator
print(1 in dogs) # True
print(2 in dogs) # False
cats = []
print(dogs[2])# we can reference items in a list by their index
dogs[2] = "Penelope"# we can also use this to update an item in a list
print(dogs)
print(dogs[-3]) # we can also use negative numbers inside the [] where -1 is the last element of the list
# List slicing is exactly similar to string slicing
print(dogs[1:4])
print(len(dogs))
# Items can be added to a list using the append method
dogs.append("Judo")
print(dogs)
# We make use of the extend function to combine 2 lists together
dogs.extend(["Judah", "Hello", "Tommy"])
print(dogs)
# alternatively we can use +=
dogs += ["oh", "my", "gosh"] # this will add this list to the existing list
dogs += "oh my gosh" # this will add each character as a separate list element
print(dogs)
# The remove function removes an element from the list
dogs.remove("Roger")
print(dogs)
# The pop function returns and removes the last element from the list
print(dogs.pop())
print(dogs)








