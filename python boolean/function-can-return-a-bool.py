#You can create functions that returns a Boolean Value:

# Example
# Print the answer of a function:

def myFunction() :
  return True

print(myFunction())

if myFunction():
    print("hidup jokowi")
else:
    print("adili jokowi")
    
#Python also has many built-in functions that return a boolean value, like the isinstance() function, 
# which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int))