'''
You can loop through the list items by using a while loop.

Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

Remember to increase the index by 1 after each iteration.
'''
#print all items, using a while loop to go through all the index numbers:
thislist = ["12qw", "qe", "qeqD"]
i = 0
while i< len(thislist):
    print(thislist[i])
    i+=1