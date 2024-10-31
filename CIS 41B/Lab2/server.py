import socket
from io import BytesIO
from bs4 import BeautifulSoup
import sqlite3
from collections import defaultdict
import socket
from urllib.request import urlopen
import pandas as pd
import os
import re
import numpy as np
from pathlib import Path
from tkinter import ttk
import tkinter as tk
from tkinter import *
import matplotlib.pyplot as py
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import json
import time

class ListboxThings():
    
    def __init__(self): 
        self.win = Tk()
        self.win.geometry("480x720")
        s = Scrollbar()
        self.label = Label(text = "States (use scroll bar to scroll)").pack(side=TOP,pady = 10)
        self.scrollbar = ttk.Scrollbar(self.win, orient= 'vertical')
        self.scrollbar.pack(side= RIGHT, fill= BOTH)
        self.lbox = Listbox(self.win, width= 150, height= 32, font= ("Arial", 12 ), selectmode = tk.SINGLE, background="grey")
        self.lbox.bind('<<ListboxSelect>>', self.getElement)
        self.lbox.selection_set(0)
        self.lbox.config(yscrollcommand= self.scrollbar.set)
        self.scrollbar.config(command= self.lbox.yview)
        self.lbox.pack()

        '''
        self.root = tk.Tk()
        self.listbox = Listbox(height = 32, width = 60, bg = "white", activestyle = 'dotbox', font = "Helvetica", fg = "black", selectmode='SINGLE')
        self.listbox.bind('<<ListboxSelect>>', self.getElement) #Select click
        self.label = Label(text = "States (scrollable)")   
        self.selection = Label(text="")        
        self.listbox.selection_set(0)
        self.label.pack()
        self.selection.pack()
        self.listbox.pack()
        '''
    def getElement(self,event):
        selection = event.widget.curselection()
        index = selection[0]
        value = event.widget.get(index)
        self.selection = value
        self.graphstate()

    def graphstate(self):
        if(str(self.selection) != ".!label2"): 
            s.send(str(self.selection).encode())
        reqData = s.recv(1024).decode()
        plotdata(reqData)   
                
    def Run(self):
        self.win.mainloop()
                   
libox = ListboxThings()            
        
        
def plotdata(r): 
    toGraph = r.split(",")
    res = [elem.strip("[]").lstrip(" \"").rstrip("\"") for elem in toGraph]
    for i in range(0, len(res)):
        res[i] = float(res[i])
    
    x = [i+1970 for i in range(0, 51)]
    y = res
    print(y)
    print(x)
    py.figure(figsize=(25, 51)) 
    py.plot(x, y)

    py.xlabel('Year', fontsize=10)
    py.ylabel("Metric Tons of Energy-Related Carbon Dioxide (in millions)", fontsize=10)
    py.xticks(np.arange(min(x), max(x)+1, 1), fontsize = 7)
    py.yticks(np.arange(min(y), max(y)+1, 10), fontsize = 10)
    
    py.show()

        

    
def endprog():
    s.send("Stop".encode())
    s.close()
    libox.win.destroy()



s = socket.socket()        

port = 11111               

s.connect(('127.0.0.1', port)) 


listOfStates = s.recv(1024).decode()
listofStates = listOfStates.strip("\"").split(",")

for elem in listofStates:
    libox.lbox.insert(END, elem)

button2 = Button(text="Close server connection and Stop Program",background='red',command=endprog).pack(side='bottom',pady=10)

libox.Run()


#cd C:\Users\magnu\CIS 41B\Lab2
#server.py
