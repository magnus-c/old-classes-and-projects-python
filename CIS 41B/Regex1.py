import re

def findAll(target,pattern):
    return re.findall(pattern,target)

def Search(target,pattern):
    return re.search(pattern,target)

def Span(target,pattern):
    s = Search(pattern,target)
    return s.span()

def Split(target,pattern):
    return re.split(pattern,target)

def Sub(target,replace,pattern):
    return re.sub(pattern,replace,target)

target = "the rain in spain falls mainly on the plain"
pattern = 'ai'
print( findAll(target,pattern))
pattern = 'france'
print( findAll(target,pattern))

pattern = '\s'
print( Search(target,pattern))
print( Span(target,r'\bS\w+'))

print( Split(target,pattern))

replace = '-'
print( Sub(target,replace,pattern))

