#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import Scale, HORIZONTAL, Canvas

# from tkinter import ttk



class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Foo"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)

        self.bind("<Escape>", self.quit)

        self.lblR = tk.Label(self, text="R")
        self.lblR.pack()
        self.scaleR = Scale(from_=0, to=255,orient = HORIZONTAL, length = 200, command = self.change)
        self.scaleR.pack()

        self.lblG = tk.Label(self, text="G")
        self.lblG.pack()
        self.scaleG = Scale(from_=0, to=255,orient = HORIZONTAL, length = 200)
        self.scaleG.pack()

        self.lblB = tk.Label(self, text="B")
        self.lblB.pack()
        self.scaleB = Scale(from_=0, to=255,orient = HORIZONTAL, length = 100)
        self.scaleB.pack()

        self.canvas = Canvas(self,width = 256, height = 100, background = '#000000') 
        self.canvas.pack()  

        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()

    def change(self,event):
        r = self.scaleR.get()
        g = self.scaleR.get()
        b = self.scaleR.get()
        self.canvas.config(background =f'#{r:02x}{g:02x}{b:02x}')

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
