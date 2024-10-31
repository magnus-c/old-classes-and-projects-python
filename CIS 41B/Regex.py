import re

address = "<De Anza College>,<12250 Stevens Creek Blvd>,<Cupertino>,<95014>,<864-5300>"
morse = ".--. -.-- - .... ---','-.'"
letters = ['P','Y','T','H','O','N']
    
def RemoveAlphabetic(target,pattern):
    print("Before: ",target)
    numbers = re.sub(pattern,"",target)
    print("After:   ",numbers)
    return numbers

def RemoveNumbers(target,pattern):
    print("Before: ",target)
    alphabetic = re.sub(r'\d',"",target)
    return alphabetic

def RemoveAlphaNumeric(target):
    print("Before: ",target)
    alphabetic = re.sub(r'\w',"",target)
    return alphabetic
    
def RemovePunctuation(target,pattern):
    print("Before: ",target)
    alphabetic = re.sub(pattern,"",target)
    return alphabetic

def SubstituteLetter(target,letter,substitute):
    print("Before: ",target)
    regex = re.compile(r''+letter)
    elist = regex.sub(substitute,target)
    print(elist)

def SearchWord(target,word):
    print("Before: ",target)
    regex = re.compile(r''+word)
    find = regex.search(target)
    return find

def MatchPattern(target,pattern):
    print("Before: ",target)
    regex = re.compile(r''+pattern)
    found = regex.search(target)
    return found

def Splitter(target,pattern):
    print("Before: ",target)
    regex = re.compile(pattern)
    mlist = regex.split(target)
    print(mlist)
    
def isRegexPhone(target,pattern):
    print("Before: ",target)
    phone = re.compile(pattern)
    number = phone.search(target) 
    if number != None:
        return number.group()
    else:
        return "not found"
    
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print("String Processing Version")
print(isPhoneNumber('408-864-5300'))
print(25*'*','\n''Regex Processing Version')
print(isRegexPhone('My number is 408-864-5300.',r'\d\d\d-\d\d\d-\d\d\d\d'))
print(25*'*','\n''Pattern matching')
print(MatchPattern(address,r'\d{3}-\d{4}'))
print(25*'*','\n''Remove alphabetical characters')
print(RemoveAlphabetic(address,r'\D'))
print(25*'*','\n''Remove numeric characters')
print(RemoveNumbers(address,r'\d'))
print(25*'*','\n''Remove white space characters')
print(RemovePunctuation(address,r'\W'))
print(25*'*','\n''Splitting string')
print(Splitter(morse,r'[\s{4}]*'))
print(25*'*','\n''Substituting characters')
print(SubstituteLetter(address,'e','E'))
print(25*'*','\n''Searching for words')
print(SearchWord(address,'Anza'))
print(25*'*')
