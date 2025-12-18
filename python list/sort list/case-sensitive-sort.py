'''
By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

Example
Case sensitive sorting can give an unexpected result:'''

thislist = ["banana", "Orange", "kiwi", "Cherry"]
thislist.sort()
print(thislist)

# Luckily we can use built-in functions as key functions when sorting a list.

# So if you want a case-insensitive sort function, use str.lower as a key function:

# Example
# Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)