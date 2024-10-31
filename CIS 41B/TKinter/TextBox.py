from tkinter import ttk
import tkinter as tk
from tkinter import *

def StartSim():
    print("Starting Simulation ...")

class TextBoxDemo:
    def __init__(self,txt):
        self.root = tk.Tk()
        self.root.title("Files")
        self.root.geometry('600x300')    
        self.root.config(bg='orange')
        self.text = tk.Text(height=18, width=50, bg='cyan',wrap=NONE) 
        self.scroll = tk.Scrollbar()
        self.text.configure(xscrollcommand=self.scroll.set)
        self.text.configure(yscrollcommand=self.scroll.set)
        self.text.pack(side=tk.RIGHT)
        self.scroll.config(command=self.text.xview)
        self.scroll.config(command=self.text.yview) 
        self.text.insert(tk.END,txt)
        self.text.pack(side='left',pady=10) 
    def Run(self):
        button1 = Button(text="Start",background='yellow',command=StartSim).pack(side='top',pady=10)  
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)     
        self.root.mainloop()    

txt = "The Quick Brown Fox Jumps Over The Lazy Poodle"        
tbox = TextBoxDemo(txt)
tbox.Run()
