from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
 



def openHtmlFile(htmlfile):
    f = open(htmlfile, "r")
    contents = f.read()
    return BeautifulSoup(contents, 'html.parser')

#should be a string to do Regex
soupf = str(openHtmlFile("index.html"))
#finding the things in <li> strings, <li>(.*)</li> but added the ? to make it not greedy
pattern = '<li>(.*?)</li>'

lithings = re.findall(pattern,soupf)


print(lithings)
