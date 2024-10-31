import os
import re
from pathlib import Path
from tkinter import ttk
import tkinter as tk
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
    
def StartSim():
        print("Starting Simulation ...")
    
class TextBoxDemo:
        def __init__(self,tab,txt):  
            self.tab = tab
            self.text = tk.Text(tab,height=18, width=50, bg='light blue',wrap=NONE)
            self.scroll = tk.Scrollbar()
            self.text.configure(xscrollcommand=self.scroll.set)
            self.text.configure(yscrollcommand=self.scroll.set)
            self.text.pack(side=tk.RIGHT)
            self.scroll.config(command=self.text.xview)
            self.scroll.config(command=self.text.yview) 
            self.text.insert(tk.END, txt)
        def Run(self):
            button = ttk.Button(self.tab,text="Start",command=StartSim).pack(side='top',pady=10)  
            self.scroll.pack(side=tk.RIGHT, fill=tk.Y)     
    
class ListBoxDemo:
    def __init__(self,tab,txt):
        self.listbox = Listbox(tab,height = 10, width = 15, bg = "light blue", activestyle = 'dotbox', font = "Helvetica", fg = "black", selectmode='SINGLE')
        self.listbox.bind('<<ListboxSelect>>', self.getElement) #Select click
        self.label = Label(tab,text = "TXT Files")   
        self.selection = Label(text="")
        self.text = tk.Text(tab,height=10, width=25, bg='orange',wrap=WORD)
        self.listbox.selection_set(0)
        self.label.pack()
        self.selection.pack()
        self.listbox.pack()
        self.text.pack(side='left',pady=10)
    def getElement(self,event):
        selection = event.widget.curselection()
        index = selection[0]
        value = event.widget.get(index)
        self.selection = value
        self.text.insert(tk.END, self.selection)
    def getFiles(self):
        # insert elements by their index and names.
        path = Path(os.getcwd())
        for file in path.iterdir():
            # screen .cpp file
            match = re.search("\.txt$", file.name)
            if match:
                self.listbox.insert(END,file.name)   
    def Run(self):
        self.getFiles()
        
class RadioButtonDemo:
    def __init__(self,tab):
        self.tab = tab
        self.values = {"C++" : "cyan","Java" : "light green", "Python" : "orange"}   
        self.vs = StringVar()
        self.label = Label( textvariable=self.vs, relief=SUNKEN,background = "light grey" )
    def print_selection(self):
        self.label.setvar(self.vs.get())
    def Run(self): 
        for (text, value) in self.values.items():
            Radiobutton(self.tab, text = text, variable = self.vs, value = value, indicator = 0,background = "light blue",command=self.print_selection).pack(fill=X)
        self.label.pack(side='top',ipady=10,fill=X)
        
class TKPlot:
        def __init__(self,tab,title):
                self.tab = tab
                self.title = title
                self.window = None
        def getWindow(self):
                return self.window
        def axis(self):
                self.y = [i**2 for i in range(101)] #list of squares
                return self.y
        def plot(self):
                self.fig = Figure(figsize = (5, 5), dpi = 100)
                self.plot1 = self.fig.add_subplot()
                self.canvas = FigureCanvasTkAgg(self.fig,master = self.tab)                
                self.plot1.plot(self.axis())
                self.canvas.draw()
                self.canvas.get_tk_widget().pack()
        def Run(self):
                plot_button = Button(master = self.tab,background='orange',command = self.plot,height = 2,width = 10,text = "Plot")
                plot_button.pack()
        
class TabControlDemo:
    blackboard = None
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tab Control")
        self.root.geometry('600x300')
        self.tabControl = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tab4 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text ='List Box')
        self.tabControl.add(self.tab2, text ='Radio Button')
        self.tabControl.add(self.tab3, text ='Text Box')
        self.tabControl.add(self.tab4, text ='Plot')
        self.tabControl.pack(expand = 1, fill ="both") 
    def Run(self):
        txt = "The Quick Brown Fox Jumps Over The Lazy Poodle"
        lbox = ListBoxDemo(self.tab1,txt).Run()
        rbutton = RadioButtonDemo(self.tab2).Run()
        tbox = TextBoxDemo(self.tab3,txt).Run()
        txt = "Plot Demo"
        plot = TKPlot(self.tab4,txt).Run()
        self.root.mainloop()       
        
tabcontrol = TabControlDemo()
tabcontrol.Run()