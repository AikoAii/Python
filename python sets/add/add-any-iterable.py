#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

#add elementn of list to at sets:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)