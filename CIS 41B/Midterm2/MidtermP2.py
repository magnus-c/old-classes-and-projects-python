from io import BytesIO
from bs4 import BeautifulSoup
from collections import defaultdict
import urllib.request
from urllib.request import urlopen
import pandas as pd
import json
from tkinter import ttk
import tkinter as tk
from tkinter import *
import socket            

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
    
s = socket.socket()        
print ("Socket successfully created")



port = 11111               
s.bind(('', port))        
print ("socket binded to %s" %(port))
 

s.listen(5)    
print ("socket is listening")
unp = b''
while True:
 
    c, addr = s.accept()    
    print ('Got connection from', addr )
    inpu = c.recv(10000000)
    unp = pickle.loads(inpu)
    
    c.close()
    break

print(unp.giveDict())
class tkinterstuff():
    def __init__(self, dicti): 
        self.root = tk.Tk()
        self.root.title("Dictionary")
        self.root.geometry("1280x900")
        self.root.config(bg='white')
        self.text = tk.Text(height=128, width=90, bg='white',wrap=NONE) 
        self.scroll = tk.Scrollbar()
        self.text.configure(xscrollcommand=self.scroll.set)
        self.text.configure(yscrollcommand=self.scroll.set)
        self.text.pack(side=tk.RIGHT)
        self.scroll.config(command=self.text.xview)
        self.scroll.config(command=self.text.yview) 
        self.text.pack(side='left',pady=10) 
        self.dicti = dicti
    def Run(self):
        texta ="year, month , DecDat, MonAVG, DeSes, days, stDEV, ucmean\n"
        self.text.insert(tk.END, texta)
        for i in range(len(self.dicti["year"])):
            textb = (str(self.dicti["year"][i]), ",", str(self.dicti["month"][i]), ",", str(self.dicti["DecDat"][i]), ",", str(self.dicti["MonAVG"][i]), ",", str(self.dicti["DeSes"][i]), ",", str(self.dicti["days"][i]), ",", str(self.dicti["stDEV"][i]), ",", str(self.dicti["uncmean"][i]),"\n")
            self.text.insert(tk.END, textb)
            self.text.info()
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y) 
        self.root.mainloop()
        

tbox = tkinterstuff(unp.giveDict())
tbox.Run()        