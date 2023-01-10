print(""""Priyam

is

20
years



old""")

# String methods :
print("Priyam".upper()) # all uppercase
print("HELLO".lower()) # all lowercase
print("this IS A tITLE".title()) # make first letter of each word as uppercase, rest all lowercase
print("Hi i'm here!".islower()) # similarly we also have isupper()
# isalpha() to check if a string contains only alphabets
# isalnum() to check if a string contains alphabets and digts
# isdecimal() to check if a string contains digits
print("Hi there 23".isalnum()) # False as it contains " "
print("23".isdecimal())
print("Hithere23".isalnum())
print("Hi I am here!".startswith("Hi")) # to check if a string starts with a particular substring
# endswith() to check if a string ends with a particular substring
# replace() to replace a part of a string
# split() to split a string on a specific character seperator
# strip() to trim the whitespaces from a string
# join() to append new letters to a string
# find() to find the position of a substring within a string

# All these functions return a new altered string without modifying the original string ==>> strings are immutable

name = "Beau"
print(len("Beau")) # or print(len(name)) returns the length of the specified string
print("au" in name) # in operator checks for a substring within a string

# Escape Sequences
print("Beauty and the \"Beast\"") # the \" is used to print a "(double quote) onto the console
# \n prints a new line onto the console
# \t prints a tab onto the console
# \\ prints a '\' onto the console

# Get a specific character of a string(using square brackets[])(string slicing)
print(name[0]) # prints 'B'
print(name[3]) # prints 'u'
print(name[-1]) # prints 'u'
print(name[-2]) # prints 'a'
# we can also use ranges inside[]
print(name[1:3]) # prints 'ea' as [inclusive:exclusive]
print(name[1:]) # prints 'eau' (end inclusive)(all up till the end)
print(name[:2]) # prints 'Be' (end exclusive)(from the beginning of the string)

# Booleans
done = True
# all numbers except 0 are evaluated as True(even negative numbers)
# 0 is evaluated as False
# Strings are False only when empty
# List, tuples, dictionaries are false if empty
book1 = True
book2 = False
book3 = any([book1, book2]) # returns True if any one value is True
book4 = all([book1, book2]) # returns True only if one value is True
print(book3); print(book4)

# Complex Numbers
complex1 = 2+3j # direct way to store complex numbers
complex_num = complex(2, 3) # store complex numbers using the complex() constructor
print(complex_num.real, complex_num.imag) # we can print the real and imaginary parts of a complex number
print(complex1.real)
print(complex_num)

# Built-in functions
# abs() returns the absolute value of an function
# round() returns the value of a number rounded to the nearest integer(or otherwise specified)
print(round(5.5))
print(round(5.49))
print(round(5.49, 1))


