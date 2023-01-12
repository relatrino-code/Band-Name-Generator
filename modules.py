# Modules - every python file s a module, we can import any module file into a program
import dogModule

dogModule.bark()
# if we want to import just some functions and nor the whole module we can write from dogModule import bark instead of import dogModule at the start
# if we do so then we should just have to write bark() instead of dogModule.bark() to call the function
# if the module is in a folder then you'll have to create an __init__.py file in the folder to tell python that this folder contains modules
# then we can use from folderName import dogModule and use dogModule.bark() to call the function
# if you ant to directly call the function, then use from lib.dogModule import bark and use bark() for function call

# Python Standard Library
# math for math utilities
# re for regular expressions
# json to work with JSON
# datetime to work with dates
# sqlite3 to use SQLite
# os for Operating System utilities
# random for random number generation
# statistics for statistics utilities
# requests to perform HTTP network requests
# http to create HTTP servers
# urllib to manage URLs

import math
print(math.sqrt(4))
# or
# from math import sqrt
# print(sqrt(4))
