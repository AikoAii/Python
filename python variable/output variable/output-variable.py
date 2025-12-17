#The print() function is often used to output variables.
a = "python is cihuyy"
print(a) 

#In the print() function, you output multiple variables, separated by a comma:
x = "python"
y = "is"
z = "cihuyy"
print(x)
print(y)
print(z)

#You can also use the + operator to output multiple variables:
x = "python "
y = "is "
z = "cihuyy"
print(x + y + z)

#Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

#For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
# x = 5
# y = "John"
# print(x + y)

#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 5
y = "John"
print(x , y)