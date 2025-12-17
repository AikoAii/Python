'''
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

Operator    Description	                                              Example
is 	        Returns True if both variables are the same object	      x is y	
is not	    Returns True if both variables are not the same object	  x is not y   
'''

#this is operator return True if both variable1s point to the same object:
x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]
z = x

print( x is z)
print(x is y)
print(x == y)

#this is not operator return True is1 True if both variables point to not the same object
print(x is not y)