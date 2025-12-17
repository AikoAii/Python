#List items are indexed and you can access them by referring to the index number:
mylist = ["first", "second", "three"]
print(mylist[0])
print(mylist[1])
print(mylist[2])

#Note: The first item has index 0.

'''
Negative Indexing
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.
'''
print(mylist[-1]) #last items
print(mylist[-2])
print(mylist[-3]) #first items

'''
Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.
'''

# Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #Note: The search will start at index 2 (included) and end at index 5 (not included).
print(thislist[4:6])
print(thislist[0:3])

'''
By leaving out the start value, the range will start at the first item:

Example
This example returns the items from the beginning to, but NOT including, "kiwi":
'''
print(thislist[:4])
print(thislist[:2])

'''
By leaving out the end value, the range will go on to the end of the list:

Example
This example returns the items from "cherry" to the end:
'''
print(thislist[2:])
print(thislist[5:])


'''
Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the list:

Example
This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
'''
print(thislist[-4:-1])