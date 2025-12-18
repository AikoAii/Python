'''
newlist = [expression for item in iterable if condition == True]

The return value is a new list, leaving the old list unchanged.
'''

'''
Condition
The condition is like a filter that only accepts the items that evaluate to True.
'''
#Example
# Only accept items that are not "apple":
fruits = ["apple", "banana", "cerry", "kiwi", "melon"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

'''
The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

The condition is optional and can be omitted:
'''
#with no if statement:
newlistA = [x for x in fruits]
print(newlistA)

'''
Iterable
The iterable can be any iterable object, like a list, tuple, set etc.
'''
#you can use range() funct to create an iterable:
listA = [x for x in range(10)]
print(listA)

#same with condition:
listB = [x for x in range(11) if x < 5]
print(listB)

'''
Expression
The expression is the current item in the iteration, but it is also the outcome, which you can 
manipulate before it ends up like a list item in the new list:
'''

#set the new value to upper case:
listC = [x.upper() for x in fruits]
print(listC)

#You can set the outcome to whatever you like.
#Set all values in the new list to 'hello'::
listC = ['hello' for x in fruits]
print(listC)

#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
#return "orange" instead of "banana":
listD = [x if x != "banana" else "moloko" for x in fruits]
print(listD)

'''
The expression in the example above says:

"Return the item if it is not banana, if it is banana return orange".'''