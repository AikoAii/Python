# Some Values are False
# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

# Example
# The following will return False:

a=bool(False)
b=bool(None)
c=bool(0)
d=bool("")
e=bool(())
f=bool([])
g=bool({})

print(a, b, c, d, e, g)