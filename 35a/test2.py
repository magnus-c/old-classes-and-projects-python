x = (1,2,3)
x = [1,2,3]
x = {1,2,3}
x = {"a":1, "b":2, "c":3}

print(x)
for i in range(5, 3, -1):
    print(i)
    
list1 = [1,3,7,23,42,4673, 234]

print(42 in list1)
class1 = {"Li", "Audry", "Jia", "Migel", "Tanya"};
class2 = {"Sasha", "Migel", "Tanya", "Hiroto", "Audry"};
class3 = {"Migel", "Zhang", "Hiroto", "Anita", "Jia"};

print((class1.intersection(class2)).difference(class3));

for even in range(2,21,2):
    print(even)
    
def priceGuide(avgPrice):
    if avgPrice <= 10:
        print("Inexpensive")
    elif 10< avgPrice <= 30:
        print("Moderate")
    else:
        print("Pricey")
        
priceGuide(23);
priceGuide(1);
priceGuide(100)