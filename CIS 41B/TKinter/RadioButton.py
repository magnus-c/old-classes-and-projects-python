from tkinter import ttk
import tkinter as tk
from tkinter import *

class RadioButtonDemo:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Languages")
        self.root.geometry('600x300')  
        self.values = {"C++" : "cyan","Java" : "light green", "Python" : "orange"}   
        self.vs = StringVar()
        self.label = Label( textvariable=self.vs, relief=SUNKEN,background = "light grey" )
    def print_selection(self):
        self.label.setvar(self.vs.get())
        self.label.config(bg=self.vs.get())
    def Run(self): 
        for (text, value) in self.values.items():
            Radiobutton(text = text, height=3,variable = self.vs, value = value, indicator = 0,background = "yellow",command=self.print_selection).pack(fill=X)
        self.label.pack(side='top',ipady=20,fill=X)
        self.root.mainloop()    
    
rbutton = RadioButtonDemo()
rbutton.Run()