
x = int(input("Enter a number "))
import math
print(round(math.sqrt(x), 2))
var1 = "python"
print(len(var1))

x = var1[2:4]
print(x)

y = var1[var1.index("h")]
print(y)

x = 8.9123
y = 123.452

print("{:>8.2f}".format(x))

print("{:>8.2f}".format(y))

list1 = [1,2,3,4]
print(max(list1))

x = list1.pop(2)
print(x)
print(list1)

list1 = [1, 2, 3]

list2 = list1

print(list1 == list2)
print(list1 is (list2))

import copy

list1 = [1, 2, 3]

list2 = copy.deepcopy(list1)
print(list1 == list2)
print(list1 is (list2))

list1 = [1, 2, 3]

list2 = list1

list3 = [list1, list2]
print(list3[0][1])
print(list3[1][0])