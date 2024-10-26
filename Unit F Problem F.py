'''
Magnus Chiu
CIS 41A Spring 2022
Unit F Problem F
'''
import random
def invoice(unitPrice, quantity, shipping = 10, handling = 5):
    print("Cost (unitPrice x quantity) =", unitPrice*quantity)
    print("Shipping =", shipping)
    print("Handling =", handling)
    print("Total =", unitPrice*quantity + shipping + handling)
    print()
def printGroupMembers(groupName, *args):
    print("Members of", groupName)
    for i in args:
        print(i)
def overseerSystem(**kwargs):
    if "temperature" in kwargs:
        if kwargs.get("temperature") > 500:
            print("Warning: temperature is", kwargs.get("temperature"))
    if "CO2level" in kwargs:
        if kwargs.get("CO2level") > 0.15:
            print("Warning: CO2level is", kwargs.get("CO2level"))
    if "miscError" in kwargs:
        print("Misc error #"+ str(kwargs.get("miscError")))    
def out():
    print("Out")
    return 0
def single():
    print("Single")
    return 1
def double():
    print("Double")
    return 2
def triple():
    print("Triple")
    return 3
def homerun():
    print("Homerun")
    return 4

def main():
    invoice(20, 4, shipping= 8)
    invoice(15, 3, handling = 15)
    printGroupMembers("Group A", "Li", "Audry", "Jia")
    groupB = ["Group B", "Sasha", "Migel", "Tanya", "Hiroto"]
    printGroupMembers(*groupB)
    print()
    Message1 = {"temperature":550}
    Message2 = {"temperature":475}
    Message3 = {"temperature":450, "miscError":404}
    Message4 = {"CO2level":.17}
    Message5 = {"CO2level":.2, "miscError":418}    
    overseerSystem(**Message1)
    overseerSystem(**Message2)
    overseerSystem(**Message3)
    overseerSystem(**Message4)
    overseerSystem(**Message5)
    print()
    outcomes = ["out", "single", "double", "triple", "homerun"]
    probabilities = [70, 18, 5, 1, 6]
    outs = 0
    while outs < 3:
        outcome = random.choices(outcomes, weights = probabilities, k = 1)
        if outcome[0] == "out":
            outs += 1
            out()
        elif outcome[0] == "single":
            single()
        elif outcome[0] =="double":
            double()
        elif outcome[0] =="triple":
            triple()
        elif outcome[0] =="homerun":
            homerun()
if __name__ == "__main__":
    main()
    
    
    
'''
Execution results:
Cost (unitPrice x quantity) = 80
Shipping = 8
Handling = 5
Total = 93

Cost (unitPrice x quantity) = 45
Shipping = 10
Handling = 15
Total = 70

Members of Group A
Li
Audry
Jia
Members of Group B
Sasha
Migel
Tanya
Hiroto

Warning: temperature is 550
Misc error #404
Warning: CO2level is 0.17
Warning: CO2level is 0.2
Misc error #418

Double
Single
Out
Out
Out
'''
