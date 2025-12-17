'''
Logical operators are used to combine conditional statements:

Operator	Description	                                                   Example
and 	    Returns True if both statements are true	                 x < 5 and  x < 10	
or	        Returns True if one of the statements is true	             x < 5 or x < 4	
not	        Reverse the result, returns False if the result is true	     not(x < 5 and x < 10)
'''
x = 5

#Test if a number is greater than 0 and less than 10:
print(x > 0 and x < 10)

#Test if a number is less than 5 or greater than 10:
print(x < 0 or x > 10)

#Reverse the result with not:
print(not(x > 3 and x < 10))