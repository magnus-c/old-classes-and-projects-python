import re

xmlstring = """<Element>
    <Number>54</Number>
    <Abbr>Xe</Abbr>
    <Name>Xenon</Name>
</Element>"""

print(xmlstring)
print("Match")
xmltag = "<Number>54</Number>"
result = re.match(r"[\<A-Za-z\>0-9\</A-Za-z\>]", xmltag)
print(result)
print("Findall")
result = re.findall(r"\d+", xmlstring)
print(result)
result = re.findall(r"\D+", xmlstring)
print(result)

print("Split")
result = re.split(r"[a-z]+", xmlstring)
print(result)
result = re.split(r"[\<\>]+", xmlstring)
print(result)

print("Search")
result = re.search(r"Xenon", xmlstring)
print(result)
result = re.search(r"\w{6}", xmlstring)
print(result)
result = re.search(r"[0-9]+", xmlstring)
print(result)

print("Sub")
result1 = re.sub(r"[A-Z]+","X", xmlstring)
print(result1)
result2 = re.sub(r"[\>\<]+","", result1)
print(result2)
