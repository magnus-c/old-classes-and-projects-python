import os
import re
from pathlib import Path
from tkinter import ttk
import tkinter as tk
from tkinter import *

class ListBoxDemo():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Lab 2")
        self.root.config(bg='white')
        self.root.geometry('600x400')    
        self.listbox = Listbox(height = 8, width = 15, bg = "white", activestyle = 'dotbox', font = "Helvetica", fg = "black", selectmode='SINGLE')
        self.listbox.bind('<<ListboxSelect>>', self.getElement) #Select click
        self.label = Label(text = "U.S. States (scroll inside box to see more)")   
        self.selection = Label(text="")
        # self.text = tk.Text(height=5, width=25, bg='orange',wrap=WORD)                
        self.listbox.selection_set(0)
        self.label2 = Label(text="Selected Country: NONE")

        # pack the widgets
        self.label.pack()
        self.selection.pack()
        self.listbox.pack()
        # self.text.pack()
        self.label2.pack()
    def getElement(self,event):
        selection = event.widget.curselection()
        index = selection[0]
        value = event.widget.get(index)
        self.selection = value
        self.label2.config(text = "Selected Country: " + self.selection)
        # self.text.insert(tk.END,self.selection) #adds last selection to end of text (ORIGINAL FEATURE)
  
    def getSelection(self):
        if(str(self.selection) != ".!label2"): #no printing when no there is no selection
            print(self.selection)
            return str(self.selection)

    def Run(self):
        self.root.mainloop()

lbox = ListBoxDemo()
lbox.Run()
lbox.getSelection()