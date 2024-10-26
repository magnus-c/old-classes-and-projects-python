'''
Magnus Chiu
CIS 41A Spring 2022
Unit B, Problem B Script 2
'''
SMALL_BEADS = 10.20;
MEDIUM_BEADS = 8.52;
LARGE_BEADS = 7.98;
smallAmt = int(input("How many boxes of small beads: "));
meduimAmt = int(input("How many boxes of meduim beads: "));
largeAmt = int(input("How many boxes of large beads: "));
smallTotal = smallAmt * SMALL_BEADS;
meduiumTotal = meduimAmt * MEDIUM_BEADS;
largeTotal = largeAmt * LARGE_BEADS;
fullTotal = smallTotal + meduiumTotal + largeTotal;

print("{:<10s}{:<7s}{:<18s}{:s}".format("SIZE", "QTY", "COST PER BOX", "TOTALS"));
print("Small{:8d}{:16.2f}{:12.2f}".format(smallAmt, SMALL_BEADS, smallTotal)); 
print("Medium{:7d}{:16.2f}{:12.2f}".format(meduimAmt, MEDIUM_BEADS, meduiumTotal)); 
print("Large{:8d}{:16.2f}{:12.2f}".format(largeAmt, LARGE_BEADS, largeTotal)); 
print("TOTAL{:36.2f}".format(fullTotal));

'''
Execution results:
Test 1:
How many boxes of small beads: 10
How many boxes of meduim beads: 9
How many boxes of large beads: 8
SIZE      QTY    COST PER BOX      TOTALS
Small      10           10.20      102.00
Medium      9            8.52       76.68
Large       8            7.98       63.84
TOTAL                              242.52

Test 2:
How many boxes of small beads: 5
How many boxes of meduim beads: 10
How many boxes of large beads: 15
SIZE      QTY    COST PER BOX      TOTALS
Small       5           10.20       51.00
Medium     10            8.52       85.20
Large      15            7.98      119.70
TOTAL                              255.90
'''