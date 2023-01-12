# Tuples
# immutable groups of objects, can't even add or remove items from tuples
names = ("Roger", "Sid", "Beau") # tuples just like lists are ordered
print(names[0]) # "Roger
print(names.index("Roger")) # 0
print(names[-1]) # "Beau"
print(len(names)) # 3
print("Roger" in names) # True
print(names[0:2]) # ("Roger", "Sid")
print(sorted(names)) # ["BEau", "Roger", "Sid"], global sorted function always returns a list
# cannot use names.sort() because tuples are immutable
newTuple = names + ("Tina", "Quincy") # created a new tuple from an existing tuple
print(newTuple)

# Dictionaries
# store data in key-value pairs
dog = { "name": "Roger" } # the key can be any immutable value(string, number, tuple), the value can be anything(even a variable)
cats = { "Stuart": "Little", "Roger": "Amphibian", "Hey": "There", "Kyle": "Smith" }
print(cats["Stuart"]) # "Little"
cats["Stuart"] = "Big"
print(cats)
print(cats.get("Kyle")) # "Smith"
print(cats.get("color", "brown")) # print(cats.get(key, defaultValue)), the default value will be used if the compiler cannot find a value corresponding to the key
# the pop method returns the specified element and then deletes it
print(cats.pop("Stuart"))
print(cats)
print(cats.popitem()) # returns and removes the last element of the dictionary
print(cats)
print("Roger" in dog) # check if a key is present in a dictionary
print(cats.keys()) # return all keys in a dictionary
print(list(cats.keys())) # return a list of all keys in a dictionary
print(list(cats.values())) # return a list of all values in a dictionary
print(list(cats.items())) # return a list of all key-value pairs in a dictionary
print(len(cats)) # prnt length of the dictionary
cats["Furry cat"] = "Black" # add a key-value pair to a dictionary
print(cats)
del cats["Furry cat"] # delete a specified key-value pair from a dictionary
cats1 = cats.copy() # create a copy of  a dictionary
print(cats)
print(cats1)

# Sets - are unordered and mutable
# Immutable version of a set - Frozen set
names = {"Abhinav", "Raju"}
names1 = {"Raju"}
intersect = names & names1 # intersection of 2 sets
print(intersect)
union = names | names1 # union of 2 sets
print(union)
diff = names - names1 # difference of 2 sets
print(diff)
sub1 = names > names1 # check if names1 is a subset of names
print(sub1)
sub2 = names < names1 # check if names is a subset of names1
print(sub2)
print(len(names)) # print the length of  a set
print(list(names)) # print a list of elements of a set
print("Roger" in names) # check if an item is contained in a set or not
# A set cannot have repeated items
mySet = {"Hello", "Hello", "Hello", "How"}
print(mySet)
print(len(mySet))

