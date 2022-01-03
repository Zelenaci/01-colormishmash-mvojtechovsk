#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import Scale, HORIZONTAL, Canvas, Frame, Entry,LEFT,S,END,StringVar
# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "ColorMM"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)

        self.frameR = Frame(self)
        self.frameR.pack()
        self.frameG = Frame(self)
        self.frameG.pack()
        self.frameB = Frame(self)
        self.frameB.pack()

        self.bind("<Escape>", self.quit)

        ###R
        self.varR = StringVar()
        self.varR.trace("w",self.change)
        self.lblR = tk.Label(self.frameR, text="R", font='Helvetica 18 bold')
        self.lblR.pack(side = LEFT,anchor=S)
        self.scaleR = Scale(self.frameR,from_=0, to=255, orient=HORIZONTAL,
                            length = 200, variable = self.varR,)
        self.scaleR.pack(side=LEFT, anchor = S)
        self.entryR = Entry(self.frameR,width = 6,textvariable = self.varR)
        self.entryR.pack(side = LEFT,anchor=S)
   
        ###G
        self.varG = StringVar() 
        self.varG.trace("w",self.change)
        self.lblG = tk.Label(self.frameG, text="G", font='Helvetica 18 bold')
        self.lblG.pack(side = LEFT,anchor=S)
        self.scaleG = Scale(self.frameG,from_=0, to=255, orient=HORIZONTAL,
                            length = 200,variable = self.varG,)                           
        self.scaleG.pack(side=LEFT)
        self.entryG = Entry(self.frameG,width = 6,textvariable = self.varG)
        self.entryG.pack(side = LEFT,anchor=S)

        ###B
        self.varB = StringVar() 
        self.varB.trace("w",self.change)
        self.lblB = tk.Label(self.frameB, text="B", font='Helvetica 18 bold')
        self.lblB.pack(side = LEFT,anchor=S)
        self.scaleB = Scale(self.frameB,from_=0, to=255, orient=HORIZONTAL,
                            length = 200, variable = self.varB,)
                            
        self.canvasMain = Canvas(self,width = 256, height = 100, background="#000000")   
        self.canvasMain.pack()
        self.canvasMain.bind("<Button-1>",self.cliclHandler)
                


        self.scaleB.pack(side=LEFT)
        self.entryB = Entry(self.frameB,width = 6,textvariable = self.varB)
        self.entryB.pack(side=LEFT,anchor=S)

        self.entryMain = Entry(self)
        self.entryMain.pack()


        ###self.btn2 = tk.Button(self, text="Cnhh", command=self.change)
        ###self.btn2.pack()


        self.frameMem = Frame(self)
        self.frameMem.pack()
        for row in range(10):
            for column in range(10):
                canvas = Canvas(self.frameMem,width = 50, height = 50, background = "#ffffff")
                canvas.grid(row = row, column= column)
                canvas.bind("<Button-1>",self.cliclHandler) 
            


        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()

        ###self.geometry('350x500')
        ###self.configure(background='#000000')

    def change(self,var, index,mode):
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()

        colorcode = f'#{r:02x}{g:02x}{b:02x}'

        self.entryMain.delete(0,END)
        self.entryMain.insert(0, colorcode)
        self.canvasMain.config(background = colorcode)
        ###self.configure(background=f'#{r:02x}{g:02x}{b:02x}')

    def cliclHandler(self, event):
        if self.cget("cursor") != "pencil":
            self.config(cursor = "pencil")
            self.color = event.widget.cget("background")
        elif self.cget("cursor")=="pencil":    
            self.config(cursor ="")
            event.widget.config(background = self.color)
        if event.widget is self.canvasMain:
            self.varR.set(value)
            self.varG.set(value)
            self.varB.set(value)
    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
