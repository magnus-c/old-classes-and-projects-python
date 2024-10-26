'''
Magnus Chiu
CIS 41A Spring 2022
Unit G Problem G
'''

from collections import defaultdict
largest = 0
maxPop = 0
index = 0
data = []
states = []
d = defaultdict(list)
dd = defaultdict(list)
numofp = 0


def main():
    print("Start of program")
main()

    
with open("States.txt", "r") as f:
    content = f.readlines()
    for line in content:
        state, region, pop = line.split()
        if region == "Midwest":
            pop = int(pop) 
            if pop > maxPop:
                maxPop = pop 
                maxState = state
print("Highest population state in the Midwest is:", maxState, maxPop)
print()

with open("USPresidents.txt", "r") as f:
    content = f.readlines()
    for line in content:
        (key, value) = line.split()
        d[key].append(value)
        
    for s,p in d.items(): 
        if len(p) > numofp:
            numofp = len(p)
            maxState = s
            
print("The state with the most presidents is", maxState, "with", 
numofp,"presidents:")
for p in d[maxState]: 
    print(p)
print()

d2 = {k:len(v) for (k,v) in d.items()}
popstates = {"CA", "TX", "FL", "NY","IL", "PA", "OH", "GA","NC", "MI"}
presstates = d2.keys() & popstates
for s,p in d.items():
    for x in popstates:
        if s == x:
            presstates.add(s)
            
    
print(len(presstates), "of the 10 high population states have had presidents born in them:")
for y in sorted(presstates):
    print(y, len(d[y]))
    
    
'''
Execution results
Highest population state in the Midwest is: IL 12802000
The state with the most presidents is VA with 8 presidents:
George_Washington
James_Madison
James_Monroe
John_Tyler
Thomas_Jefferson
William_Henry_Harrison
Woodrow_Wilson
Zachary_Taylor
8 of the 10 high population states have had presidents born in them:
CA 1
GA 1
IL 1
NC 2
NY 5
OH 7
PA 1
TX 2
'''