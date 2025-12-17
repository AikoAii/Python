#The remove() method removes the specified item.
fruits = ["apple", "banana", "cherry"]
fruits.remove("apple")
print(fruits)

#If there are more than one item with the specified value, the remove() method removes the first occurrence:
this = ["apple", "banana", "cherry", "banana"]
this.remove("banana")
print(this)