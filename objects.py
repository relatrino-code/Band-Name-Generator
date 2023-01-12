# Objects
age = 8
print(age.real)
print(age.imag)
print(age.bit_length()) # bit_length = no. of bits necessary to represent this no. in binary notation

items = [1, 2]
items.append(3)
items.pop()
print(id(items)) #id() = prints the location in memory of the particular object
# ints, floats, strings, tuples are immutable objects

# Loops - while and for
# while condition: ;expression
for item in items:
    print(item)

it = True
while it:
    print("It's True")
    it = False

for x in range(15):
    print(x)
# range(15) returns a list from 0 to 14

for x in enumerate(items): # enumerate will return the index and the value in a list
    print(x)

for i, x in enumerate(items):
    print(i, x)

# break = exits out of the loop
# continue = skips the current iteration and proceeds to perform the next iteration

hello = [1, 2, 3, 4]
for x in hello:
    if x == 3:
        continue
    print(x)

for x in hello:
    if x == 3:
        break
    print(x)



