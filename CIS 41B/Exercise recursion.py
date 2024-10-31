# Power was out on Wednesday, came back at 3/16 at 2 am
import os
from pathlib import Path
import shutil

def createFile(string):
    fdesc = "temp.txt"
    file = open(fdesc, 'w')
    file.write(string)
    file.close()
    return file

def readFile(fname):
    file = open(fname, 'r')
    text = file.read()
    file.close()
    return text

def shCopy(source,destination):
    dest = shutil.copy(source, destination)

#RECURSIVE FUNCTION
def printRec(oslist):
    while (len(oslist) >0):
        print(oslist[0])
        oslist.pop(0)
        printRec(oslist)

#Basically creating a test file
os.chdir("Sandbox")
createFile("text")
print("File contents",readFile("temp.txt"))
shCopy("temp.txt","copy1.txt")
shCopy("temp.txt","copy2.txt")
shCopy("temp.txt","copy3.txt")
print("File List", os.listdir())

#now do the os.listdir()
oslist = os.listdir()
print(oslist)

#run the recursive function
printRec(oslist)
