#Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

#Create a variable outside of a function, and use it inside the function
x = "Cihuyy" #global variable

def myFunc():
    x = "Uhuyy" #local variable 
    print("pyhon is " + x)
    
myFunc()

#Create a variable inside a function, with the same name as the global variable
print("pyhon is " + x)