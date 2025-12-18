'''
You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first):
'''
#Sort the list based on how close the number is to 50:
def myFunction(n):
    return abs(n - 50)

listA = [100, 33, 76, 34, 86,45, 0, 22]
listA.sort(key=myFunction)
print(listA)