'''
Magnus Chiu
CIS 41A Spring 2022
Unit F Exercise F
'''

def hello():
    '''This function prints Hello World'''
    print("Hello World")
    
def printListElement(nlist, nindex):
    try:
        print(nlist[nindex])
              
    except:
        print("Error: bad index number.")
    
def byVal(num):
    print("Original ID of parameter in byVal",id(num))
    num =num + 7;
    print("ID of parameter in byVal after change",id(num))
    
def byRef(nlist):
    print("Original ID of parameter in byRef",id(nlist))
    print("Original ID of parameter's last element in byRef", id(nlist[-1]))
    nlist[-1] = nlist[-1] +7
    print("ID of parameter in byRef after change",id(nlist))
    print("ID of parameter's last element in byRef after change",id(nlist[-1]))

def main():
    hello()
    help(hello)
    myList = [0, 1, 2]
    printListElement(myList, 3)
    myInt = 3
    myList = [0, 1, 2]
    print("Original ID of myInt in main is",id(myInt))
    print("Original ID of myList in main is",id(myList))
    print("Original ID of myList's last element in main is",id(myList[-1]))
    byVal(myInt)
    byRef(myList)
    print("ID of myInt in main after call to byVal is",id(myInt))
    print("ID of myList in main after call to byRef is",id(myList))
    print("ID of myList's last element in main after call to byRef is",id(myList[-1]))
    print("myInt is now:",myInt)
    print("myList is now:",myList)
          
if __name__ == "__main__":
    main()
    
    
'''
Execution results:
Hello World
Help on function hello in module __main__:

hello()
    This function prints Hello World

Error: bad index number.
Original ID of myInt in main is 2741887959344
Original ID of myList in main is 2741940955136
Original ID of myList's last element in main is 2741887959312
Original ID of parameter in byVal 2741887959344
ID of parameter in byVal after change 2741887959568
Original ID of parameter in byRef 2741940955136
Original ID of parameter's last element in byRef 2741887959312
ID of parameter in byRef after change 2741940955136
ID of parameter's last element in byRef after change 2741887959536
ID of myInt in main after call to byVal is 2741887959344
ID of myList in main after call to byRef is 2741940955136
ID of myList's last element in main after call to byRef is 2741887959536
myInt is now: 3
myList is now: [0, 1, 9]
'''