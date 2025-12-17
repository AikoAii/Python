# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.
# Any number is True, except 0
# Any list, tuple, set, and dictionary are True, except empty ones.

# Example
# The following will return True:

aa = bool("abc")
bb = bool(123)
cc = bool(["apple", "cherry", "banana"])
print(aa, bb, cc)