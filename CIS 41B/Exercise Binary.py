from bitstring import BitArray
with open('romannumerals.txt') as f:
    lines = f.read()


def numtointtohex(line):
    numval = 0
    pval = 1000
    #convert each character in the line into a number value
    for i in line.split():
        for j in i:
            
            if (j == 'I'):
                val = 1
            elif (j == 'V'):
                val = 5
            elif (j == 'X'):
                val = 10
            elif (j == 'L'):
                val = 50
            elif (j == 'C'):
                val = 100
            elif (j == 'D'):
                val = 500
            elif (j == 'M'):
                val = 1000            
            else: 
                val = 0
            #checking for numbers like CM = 900 or like IV = 4
            if val <= pval:
                numval = numval + val
            else:
                numval = abs(numval - val)
            pval = val
        #convert to bits and hexidecimal
        a = BitArray(uint=numval, length=16)
        print(a.hex)
        #reset for next number
        pval = 1000
        numval = 0
        
numtointtohex(lines)

