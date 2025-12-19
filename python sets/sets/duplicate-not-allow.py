'''
Sets cannot have two items with the same value.

Example
Duplicate values will be ignored:
'''
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
# True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:
# Example
# False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)