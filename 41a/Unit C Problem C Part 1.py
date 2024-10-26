'''
Magnus Chiu
CIS 41A Spring 2022
Unit C, Problem C Script 1
'''
list1 = [];
list1 = [1, 3, 5];
list1[1], list1[2] = list1[2], list1[1];
print("d) Items in list1:");
for i in range(len(list1)): 
    print(list1[i])
list2 = [1, 2, 3, 4];
list3 = list1 + list2;
print("g) list3 is:", list3);
print("h) list3 contains a 3:", 3 in list3); 
print("i) list3 contains",list3.count(3),"3s");
print("j) The index of the first 3 contained in list3 is",list3.index(3));
first3 = list3.pop(list3.index(3));
print("k) first3 =", first3);
list4 = sorted(list3);
print("m) list3 is now:", list3);  
print("n) list4 is:", list4);
print("o) Slice of list3 is:", list3[2:5]);
print("p) Length of list3 is", len(list3));
print("q) The max value in list3 is",max(list3));
list3.sort();
print("r) Sorted list3 is:", list3);
list5 = [list1, list2];
print("t) list5 is:", list5);
print("u) Value 4 from list5:", list5[1][3]);

'''
Execution results:
d) Items in list1:
1
5
3
g) list3 is: [1, 5, 3, 1, 2, 3, 4]
h) list3 contains a 3: True
i) list3 contains 2 3s
j) The index of the first 3 contained in list3 is 2
k) first3 = 3
m) list3 is now: [1, 5, 1, 2, 3, 4]
n) list4 is: [1, 1, 2, 3, 4, 5]
o) Slice of list3 is: [1, 2, 3]
p) Length of list3 is 6
q) The max value in list3 is 5
r) Sorted list3 is: [1, 1, 2, 3, 4, 5]
t) list5 is: [[1, 5, 3], [1, 2, 3, 4]]
u) Value 4 from list5: 4
'''