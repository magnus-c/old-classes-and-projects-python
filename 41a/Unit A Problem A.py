'''
Magnus Chiu
CIS 41A Spring 2022
Unit A, Problem A
'''
import math;
#1
a = 3 ** 2.5;
b = 2;
b += 3;
c = 12;
c /= 4;
d = 5%3;
print("a =",a);
print("b =",b);
print("c =",c);
print("d =",d);

#2
print(abs(5-7));
print(round(3.14159, 4));
print(round(186282, -2));
print(min([6, -9, -3, 0]));

#3
num = float(input("Enter a number: "));
#first find the sqrt of num, then round to the second decimal place using the round function.
print(round(math.sqrt(num), 2)); 
#first find the log base 10 of num by doing math.log(num, (base number(which is 10 in the case of natural log.)), then round to the second decimal place using the round function.
print(round(math.log(num, 10), 2));

'''
Execution results:
a = 15.588457268119896
b = 5
c = 3.0
d = 2
2
3.1416
186300
-9
Enter a number: 7.6
2.76
0.88
'''