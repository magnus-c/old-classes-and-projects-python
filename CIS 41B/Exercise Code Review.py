def NumToRomanNumerals(num):
    ones = int(num%10)
    tens = int(num/10%10)
    hundereds = int(num/100%10)
    thousands = int(num/1000)
    oneR = ""
    tensR = ""
    hunderedsR = ""
    thousandsR = ""

    #Ones: 9 = IX, 5 = V , 4 = IV, add I's at the end to cover the other numbers
    if ones >= 9:
        oneR = oneR + "IX"
        ones = ones - 9
    elif ones >= 5:
        oneR = oneR+"V"
        ones = ones- 5
    elif ones == 4:
        oneR = oneR+ "IV"
        ones = ones- 4
    for i in range(ones):
        oneR = oneR+"I"
    
    #Tens: 9 = XC, 5 = L , 4 = XL, add X's at the end to cover the other numbers
    if tens >= 9:
        tensR = tensR + "XC"
        tens = tens - 9
    elif tens >= 5:
        tensR = tensR+"L"
        tens = tens- 5
    elif tens == 4:
        tensR = tensR+ "XL"
        tens = tens- 4
    for i in range(tens):
        tensR = tensR+"X"
    
    #Hundereds: 9 = CM, 5 = D , 4 = CD, add C's at the end to cover the other numbers
    if hundereds >= 9:
        hunderedsR = hunderedsR + "CM"
        hundereds = hundereds - 9
    elif hundereds >= 5:
        hunderedsR = hunderedsR+"D"
        hundereds = hundereds- 5
    elif hundereds == 4:
        hunderedsR = hunderedsR+ "CD"
        hundereds = hundereds- 4
    for i in range(hundereds):
        hunderedsR = hunderedsR+"C"
    #Thousands: if even exist max value can be 1
    if thousands == 1:
        thousandsR = thousandsR +"M"
    
    #print results
    print(thousandsR + hunderedsR + tensR +oneR)
    

if __name__ == "__main__":
    val = int(input("Enter a number from 1- 1000: "))
    NumToRomanNumerals(val)

'''
Output:

Enter a number from 1- 1000: 238
CCXXXVIII

Enter a number from 1- 1000: 603
DCIII
'''