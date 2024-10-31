from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

class TKPlot:
    def __init__(self,title):
        self.window = Tk()
        self.window.title(title)
        self.window.geometry("500x500")
        self.fig = Figure(figsize = (5, 5), dpi = 100)
        self.plot1 = self.fig.add_subplot()
        self.canvas = FigureCanvasTkAgg(self.fig,master = self.window)
    def getWindow(self):
        return self.window
    def axis(self):
        self.x = ["a", "b", "c", "d","e"]
        self.y = [i+5 for i in range(len(self.x))] #list of squares
        return self.x, self.y
    def plot(self):
        a, b = self.axis()
        self.plot1.plot(a,b)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
    def Run(self):
        plot_button = Button(master = self.window,background='orange',command = self.plot,height = 2,width = 10,text = "Plot")
        plot_button.pack()
        self.window.mainloop()
    
tkplot = TKPlot("Plotting squares")
tkplot.Run()
