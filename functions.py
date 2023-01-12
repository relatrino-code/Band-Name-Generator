def hello(name):
    print("Hello " + name)

hello("Kane")

def hello1(name = "my friend"): # "my friend" is the default value of the name parameter if nothing is passed to the function
    print("Hello " + name)

hello1("Raze")
hello1()

# pass by value(for immutable types)
def pbv(val):
    val = 1
value = 2
pbv(value)
print(value)

# pass by reference(for mutable types)
def pbr(val):
    val["name"] = 2
value1 = { "name": "Sachin" }
pbr(value1)
print(value1)

def ciao(name):
    if not name:
        return
    print("Ciao " + name + "!")
ciao(False)
ciao("Risk")

# a return statement can also return multiple values
def meme(name):
    print("Mr. " + name + ", you are officially a meme!")
    return name, "Risk", 6
print(meme("Joe"))

phrase = "I am going to buy some milk"
words = phrase.split(" ") # the split function can split a string into a list at the specified seperator
print(words)

# to access a variable of the outer function in the inner function in case of nested functions,
# use the nonlocal keyword in-front oof the variable name before using it
def count():
    count = 5

    def increment():
        nonlocal count
        count = count + 1
        print(count)

    increment()

count()

# Closures - inner function has access to variable declared in outer function even after the outer function call is over and we're just calling the inner one
def counter():
    cc = 0

    def inc():
        nonlocal cc
        cc = cc + 1
        return cc

    return inc

c1 = counter()
c2 = counter()
print(c1()) # 1
print(c1()) # 2
print(c2()) # 1
print(c2()) # 2













