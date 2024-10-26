'''
Magnus Chiu
CIS 41A Spring 2022
Unit J Problem J
'''
import re
data = input("Enter president name: ")
pat = r"a"
match = re.search(pat,data) 
if match:
    print("Found")
else:
    print("Not found")
    
print()

data = input("Enter Harry Potter characters: ")
pat = r"b."
lists = re.findall(pat,data) 
print(lists)
    
print()

data = input("Enter Harry Potter characters: ")
pat = r"\s"
lists = re.split(pat,data) 
print(lists)

print()
    
data = input("Enter some strings: ")
pat = r"th"
lists = re.sub(pat, "lore", data)
print(lists)
    
    
    
    
'''
Execution results:
Enter president name: Harry S. Truman
Found

Enter president name: Dwight D. Eisenhower
Not found

Enter Harry Potter characters: Dobby Rebeus Longbottom Gabrielle Albus
['bb', 'be', 'bo', 'br', 'bu']

Enter Harry Potter characters: Bill Charlie Percy Fred George Ron Ginny
['Bill', 'Charlie', 'Percy', 'Fred', 'George', 'Ron', 'Ginny']

Enter some strings: thlei, th, and folk tales
lorelei, lore, and folk tales
'''