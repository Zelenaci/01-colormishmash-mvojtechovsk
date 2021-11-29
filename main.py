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

        self.lblR = tk.Label(self, text="R", font='Helvetica 18 bold')
        self.lblR.pack()
        self.scaleR = Scale(from_=0, to=255,orient = HORIZONTAL, length = 200, command = self.change,background='#000000')
        self.scaleR.pack()

        self.lblG = tk.Label(self, text="G", font='Helvetica 18 bold')
        self.lblG.pack()
        self.scaleG = Scale(from_=0, to=255,orient = HORIZONTAL, length = 200, command = self.change,background='#000000')
        self.scaleG.pack()

        self.lblB = tk.Label(self, text="B", font='Helvetica 18 bold')
        self.lblB.pack()
        self.scaleB = Scale(from_=0, to=255,orient = HORIZONTAL, length = 200, command = self.change,background='#000000')
        self.scaleB.pack()


        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()

        self.geometry('350x350')
        self.configure(background = '#000000')

    def change(self,event):
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()

        self.configure(background =f'#{r:02x}{g:02x}{b:02x}')
        
        self.scaleR.configure(background =f'#{r:02x}{g:02x}{b:02x}')
        self.scaleG.configure(background =f'#{r:02x}{g:02x}{b:02x}')
        self.scaleB.configure(background =f'#{r:02x}{g:02x}{b:02x}')

        self.lblR.configure(background =f'#{r:02x}{g:02x}{b:02x}')
        self.lblG.configure(background =f'#{r:02x}{g:02x}{b:02x}')
        self.lblB.configure(background =f'#{r:02x}{g:02x}{b:02x}')

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
