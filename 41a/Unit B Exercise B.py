'''
Magnus Chiu
CIS 41A Spring 2022
Unit B, Exercise B 
'''
name = str(input("Enter a name: "));
print(name.upper());
print(len(name));
print(name[3]);
name2 = name.replace("o", "x");
print(name2);
print(name);

quote = "Believe you can and you're halfway there."
print(quote);
print("Count = ", quote.count("a"));
index = quote.index("a");
print("a found at ", index);
index = quote.index("a", index +1);
print("a found at ", index);
index = quote.index("a", index +1);
print("a found at ", index);
index = quote.index("a", index +1);
print("a found at ", index);

'''
Execution results:
Enter a name: George Washington
GEORGE WASHINGTON
17
r
Gexrge Washingtxn
George Washington
Believe you can and you're halfway there.
Count =  4
a found at  13
a found at  16
a found at  28
a found at  32
'''