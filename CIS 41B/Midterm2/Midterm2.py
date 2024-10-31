from io import BytesIO
from bs4 import BeautifulSoup
from collections import defaultdict
import urllib.request
from urllib.request import urlopen
import pandas as pd
import json

data = []
arr = []
from collections import defaultdict
d = defaultdict(list)
urllib.request.urlretrieve("https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt","text_file.txt")
with open("text_file.txt", "r") as f:
    while True:
        content = f.readline()
        if not content.startswith('#'):
            break
        
    while(content):
        data.append(content.split())
        content = f.readline()

for i in data:
    d["year"].append(i[0])
    d["month"].append(i[1])
    d["DecDat"].append(i[2])
    d["MonAVG"].append(i[3])
    d["DeSes"].append(i[4])
    d["days"].append(i[5])
    d["stDEV"].append(i[6])
    d["uncmean"].append(i[7])
    
import pickle
class jsontodata:
    def __init__(self, json):
        self.json = json
        self.dicti = defaultdict(list)
    def createDict(self):
        change = (self.json).replace(":", ",").split(",")
        strip = [s.replace("[", "").replace("]", "").lstrip("\" \'").rstrip("\'\"").strip("\"{}") for s in change]
        for i in range(0, len(strip),780):
            for j in range(i+1, i+780):
                self.dicti[strip[i]].append(float(strip[j]))
            
        return(self.dicti)
    def search(self, key):
        return self.dicti[key]
    def createJSON(self):
        return json.dumps(self.dicti)
    def giveDict(self):
        return self.dicti

#inpu = c.recv(1024).decode() 

q = jsontodata(json.dumps(d))
q.createDict()

import socket
s = socket.socket()        

port = 11111               

s.connect(('127.0.0.1', port)) 
msg = pickle.dumps(q)
s.send(msg)