'''
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.'''
this1 = ("apple", "banana", "cherry")
this2 = list(this1) #Convert the tuple into a list to be able to change it:
this2[2] = "berry"
this1 = tuple(this2)
print(this1)
