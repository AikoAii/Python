#Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

#1. Convert into a list: Just like the workaround for changing a tuple, you can convert it 
# into a list, add your item(s), and convert it back into a tuple.

thistuple = ("apple", "banana", "cherry")
y = list(thistuple) #Convert the tuple into a list, add "orange", and convert it back into a tuple
y.append("berry")
thistuple = tuple(y)

print(thistuple)

#2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, 
# (or many), create a new tuple with the item(s), and add it to the existing tuple:

#Create a new tuple with the value "orange", and add that tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#Note: When creating a tuple with only one item, remember to include a comma after 
# the item, otherwise it will not be identified as a tuple.

'''
Remove Items
Note: You cannot remove items in a tuple.'''

# Example
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# Or you can delete the tuple completely:

# Example
# The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists