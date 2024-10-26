'''
Magnus Chiu
CIS 41A Spring 2022
Unit H Problem H
'''
import pickle
class BritCoins:
    __coinValues = {"pound":240, "shilling":12, "penny":1} #value of each type of coin in pennies
        
    def __init__(self, **kwargs):
        self.totalPennies = 0
        for coinType,amount in kwargs.items():
            self.totalPennies += BritCoins.__coinValues[coinType] * amount
     
    def __add__(self, other):
        total = self.totalPennies + other.totalPennies
        return str(BritCoins(**{"penny":total}))
    def __sub__(self, other):
        total = self.totalPennies - other.totalPennies
        return str(BritCoins(**{"penny":total}))
    def __str__(self):
        pounds = self.totalPennies // BritCoins.__coinValues["pound"]
        self.totalPennies = self.totalPennies% BritCoins.__coinValues["pound"]
        shillings = self.totalPennies// BritCoins.__coinValues["shilling"]
        self.totalPennies = self.totalPennies% BritCoins.__coinValues["shilling"]
        return str(pounds)+" pounds "+ str(shillings)+ " shillings "+ str(self.totalPennies)+ " pennies"

c1 = BritCoins(**{"pound": 4, "shilling":24, "penny": 3})
c2 = BritCoins(**{"pound": 3, "shilling":4, "penny": 5})
c3 = c1 + c2
c4 = c1 -c2
print(c1)
print(c2)
print(c3)
print(c4)

file = open("pickle1", "wb")
pickled = pickle.dump(c4, file)
file.close()
file = open("pickle1", "rb")
unpickled = pickle.load(file)
file.close()
print()
print(unpickled)

'''
Execution results:
5 pounds 4 shillings 3 pennies
3 pounds 4 shillings 5 pennies
8 pounds 8 shillings 8 pennies
1 pounds 19 shillings 10 pennies

1 pounds 19 shillings 10 pennies
'''