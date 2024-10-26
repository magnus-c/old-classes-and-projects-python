'''
Magnus Chiu
CIS 41A Spring 2022
Unit D, Exercise D
'''
dessertFruits = {"apple":"sauce", "peach":"cobbler", "carrot":"cake", "strawberry":"sorbet", "banana":"cream pie"};
dessertFruits["mango"] = "sticky rice";
dessertFruits["strawberry"] = "shortcake";
dessertFruits.pop("carrot");
print("apple dessert is:", dessertFruits["apple"]);
print("banana dessert exists:", "banana" in dessertFruits); 
print("pear dessert exists:", "pear" in dessertFruits);
print(dessertFruits.keys());
print(dessertFruits.values());
print(dessertFruits.items());

capitols1 = {"Alabama":"Montgomery", "Alaska":"Juneau", "Arizona":"Phoenix", "Arkansas":"Little Rock", "California":"Sacremento"};
capitols2 = {"California":"Sac.", "Colorado":"Denver", "Connecticut":"Hartford"};
capitols1.update(capitols2);
print("Sorted state capitols:", sorted(capitols1.values()));

class1 = {"Li", "Audry", "Jia", "Migel", "Tanya"};
class2 = {"Sasha", "Migel", "Tanya", "Hiroto", "Audry"};
class1.add("John");
print("Students in both classes:", sorted(class1.intersection(class2)));
print("All students:", sorted(class1.union(class2)));
print("Sasha is in class1:", "Sasha" in class1);

'''
Execution results:
apple dessert is: sauce
banana dessert exists: True
pear dessert exists: False
dict_keys(['apple', 'peach', 'strawberry', 'banana', 'mango'])
dict_values(['sauce', 'cobbler', 'shortcake', 'cream pie', 'sticky rice'])
dict_items([('apple', 'sauce'), ('peach', 'cobbler'), ('strawberry', 'shortcake'), ('banana', 'cream pie'), ('mango', 'sticky rice')])
Sorted state capitols: ['Denver', 'Hartford', 'Juneau', 'Little Rock', 'Montgomery', 'Phoenix', 'Sac.']
Students in both classes: ['Audry', 'Migel', 'Tanya']
All students: ['Audry', 'Hiroto', 'Jia', 'John', 'Li', 'Migel', 'Sasha', 'Tanya']
Sasha is in class1: False
'''