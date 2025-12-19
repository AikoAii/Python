'''
There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.
'''
#two list
list1 = ["a", "b", "c", "d"]
list2 = [1,2,3,4,4]

list3 = list1 + list2
print(list3)

#append list2 into list1
for x in list2:
    list1.append(x)
print(list1)

#Or you can use the extend() method, where the purpose is to add elements from one list to another list:
list2.extend(list3)
print(list2)