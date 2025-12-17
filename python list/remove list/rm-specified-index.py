#The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry", "demila", "eeeaaa"]
thislist.pop(2)
print(thislist)

#If you do not specify the index, the pop() method removes the last item.
thislist.pop()
print(thislist)

#The del keyword also removes the specified index:
thislista = ["apple", "banana", "cherry", "demila", "eeeaaa"]
del thislista[4]
print(thislista)

#The del keyword can also delete the list completely.
del thislista
print(thislista)