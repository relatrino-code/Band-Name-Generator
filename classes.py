# Classes - we can declare our own types in addition to using the ones provided by python
# We can then instantiate these classes into objects
# Class is the type of an object

class Animal:
    def walk(self):
        print("Walking...")

class Dog(Animal):
    def __init__(self, name, age): # the __init__ method is the constructor of the class
        self.name = name
        self.age = age

    def bark(self): # self points to the current object instance
        print("Woof!")

roger = Dog("Roger", 8) # creating an object of type class
print(type(roger))
print(roger.name)
print(roger.age)
roger.bark()
roger.walk()

