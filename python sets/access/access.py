'''
You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.'''
thisset = {"apple", "banana", "cherry"}
for i in thisset:
    print(i)

#Check if "banana" is present in the set:
if "banana" in thisset:
    print(thisset)
    
#Check if "banana" is NOT present in the set:
print("banana" not in thisset)