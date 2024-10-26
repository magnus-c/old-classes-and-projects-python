'''
Magnus Chiu
CIS 41A Spring 2022
Unit E, Problem E Script 1
'''
pname = input("Please enter the plant name: ");
ptype = input("Please enter the plant type: ");
pheight = int(input("Please enter the plant height: "));
if ptype == "Flower":
    if pheight <= 3:
        garden = "B";
    elif pheight <= 6:
        garden = "H";
    else:
        garden = "N";
elif ptype == "Vegetable":
    garden = "V";
    
else:
    garden = "N";
    
if garden == "B":
    print("A", pname, "can be planted in the Low Garden or the High Garden.");
elif garden == "H":
    print("A", pname, "can be planted in the High Garden.");
elif garden == "V":
    print(pname, "can be planted in the Vegtable Garden.");#no need for A as its all plurals
elif garden =="N":
    print("A", pname, "does not match the criteria for any of the Gardens.");

'''
Execution results (all 6 tests):
Please enter the plant name: Lily
Please enter the plant type: Flower
Please enter the plant height: 3
A Lily can be planted in the Low Garden or the High Garden.
Please enter the plant name: Bonsai
Please enter the plant type: Tree
Please enter the plant height: 2
A Bonsai does not match the criteria for any of the Gardens.
Please enter the plant name: Carrots
Please enter the plant type: Vegetable
Please enter the plant height: 1
Carrots can be planted in the Vegtable Garden.
Please enter the plant name: Corn
Please enter the plant type: Vegetable
Please enter the plant height: 8
Corn can be planted in the Vegtable Garden.
Please enter the plant name: Rose
Please enter the plant type: Flower
Please enter the plant height: 5
A Rose can be planted in the High Garden.
Please enter the plant name: Sunflower
Please enter the plant type: Flower
Please enter the plant height: 8
A Sunflower does not match the criteria for any of the Gardens.
'''
