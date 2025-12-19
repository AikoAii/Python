'''
If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

Example
Assign the rest of the values as a list called "red":
'''
fruits = ("apple", "banana", "cherry", "kiwi", "orange")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

'''
If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

Example
Add a list of values the "tropic" variable:

'''
(green, *yellow, red) = fruits
print(green)
print(yellow)
print(red)