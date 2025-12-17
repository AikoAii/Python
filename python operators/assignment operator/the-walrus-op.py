#Python 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a larger expression:
numbers = [1,2,3,4,5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)):
    print(f"List has {count} elements")