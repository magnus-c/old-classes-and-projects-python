'''
Magnus Chiu
CIS 41A Spring 2022
Unit G Exercise G
'''
import csv
f = open("ZenOfPython.txt", "w")
print("Beautiful is better than ugly.", file = f)
print("Explicit is better than implicit.", file =f)
f.close()
f = open("ZenOfPython.txt", "a")
print("Readability counts.", file = f)
print("If the implementation is hard to explain, it's a bad idea.", file =f)
f.close()
f = open("ZenOfPython.txt", "r")
print(f.read())
f.close()


with open("Cities.csv", newline='') as fin:
    csvin = csv.DictReader(fin)
    dictionary = {(rows["City"], rows["State"]): rows["Population"] for rows in csvin}
print(dictionary)
for sc, p in dictionary.items(): 
    print(sc[0], sc[1], p)
print()
city = input("Please enter a city: ")
state = input("Please enter a state: ")
if (city, state) in dictionary.keys():
    print(city, state,"has a population of", dictionary[(city, state)])
else:
    print("Cannot find", city, state)
          


'''
Beautiful is better than ugly.
Explicit is better than implicit.
Readability counts.
If the implementation is hard to explain, it's a bad idea.

Athens Georgia 115452
Athens Ohio 23832
Berlin Connecticut 19866
Berlin Wisconsin 5524
Dublin California 46036
Dublin Ohio 41751
Glasgow Connecticut 11951
Glasgow Kentucky 14028
London Kentucky 7993
London Ohio 9904
Milan Illinois 5099
Milan Michigan 5836
Milan Tennessee 7851
Paris Kentucky 8553
Paris Tennessee 10156
Paris Texas 25171
Warsaw Indiana 13559
Warsaw New York 5064

Please enter a city: Dublin
Please enter a state: California
Dublin California has a population of 46036

'''