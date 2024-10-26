import math
myLists = []

for row in range(1,6,2):

    newRow = []

    for col in range(1,6,2):

        newRow.append(row*col**2)

    myLists.append(newRow)

print(myLists)