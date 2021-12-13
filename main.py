#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import Scale, HORIZONTAL, Canvas, Frame, Entry,LEFT,S,END,StringVar
# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Foo"

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

        self.lblR = tk.Label(self.frameR, text="R", font='Helvetica 18 bold')
        self.lblR.pack(side = LEFT,anchor=S)
        self.scaleR = Scale(self.frameR,from_=0, to=255, orient=HORIZONTAL,
                            length = 200, command=self.change,)
        self.varR = StringVar()
        self.scaleR.pack(side=LEFT, anchor = S)
        self.entryR = Entry(self.frameR,width = 6,textvariable = self.varR)
        self.entryR.pack(side = LEFT,anchor=S)
   

        self.lblG = tk.Label(self.frameG, text="G", font='Helvetica 18 bold')
        self.lblG.pack(side = LEFT,anchor=S)
        self.scaleG = Scale(self.frameG,from_=0, to=255, orient=HORIZONTAL,
                            length = 200,command=self.change,)
        self.varG = StringVar()                            
        self.scaleG.pack(side=LEFT)
        self.entryG = Entry(self.frameG,width = 6,textvariable = self.varG)
        self.entryG.pack(side = LEFT,anchor=S)


        self.lblB = tk.Label(self.frameB, text="B", font='Helvetica 18 bold')
        self.lblB.pack(side = LEFT,anchor=S)
        self.scaleB = Scale(self.frameB,from_=0, to=255, orient=HORIZONTAL,
                            length = 200, command=self.change,)
        self.varB = StringVar()                    
        self.scaleB.pack(side=LEFT)
        self.entryB = Entry(self.frameB,width = 6,textvariable = self.varB)
        self.entryB.pack(side=LEFT,anchor=S)

        self.entryMain = Entry(self)
        self.entryMain.pack(side=LEFT)

        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()

        self.geometry('350x350')
        self.configure(background='#000000')

    def change(self, event):
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()

        colorcode = f'#{r:02x}{g:02x}{b:02x}'

        self.entryMain.delete(0,END)
        self.entryMain.insert(0, colorcode)

        self.varR.set(r)
        self.varG.set(g)
        self.varB.set(b)


        self.configure(background=f'#{r:02x}{g:02x}{b:02x}')

        

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
