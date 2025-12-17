#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.

#If you use the global keyword, the variable belongs to the global scope:
def myFunc():
    global x
    x = "Uhuyy"
    
myFunc()

print("python is " + x)

#Also, use the global keyword if you want to change a global variable inside a function.
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "Cihuyy1"

def myFunc1():
    global x
    x = "Uhuyy1"
    
myFunc1()

print("python is " + x)

