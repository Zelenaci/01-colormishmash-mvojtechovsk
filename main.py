from os.path import basename, splitext
import tkinter as tk
from tkinter import Scale, HORIZONTAL, Canvas, Frame, Entry,LEFT,S,END,StringVar
from turtle import color
# from tkinter import ttk






class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "ColorMM"
    
    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)

        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.frameR = Frame(self)
        self.frameR.pack()
        self.frameG = Frame(self)
        self.frameG.pack()
        self.frameB = Frame(self)
        self.frameB.pack()

        self.bind("<Escape>", self.quit)


        ###R
        self.varR = StringVar()
        self.lblR = tk.Label(self.frameR, text="R", font='Helvetica 18 bold')
        self.lblR.pack(side = LEFT,anchor=S)
        self.scaleR = Scale(self.frameR,from_=0, to=255, orient=HORIZONTAL,
                            length = 200, variable = self.varR,)
        self.scaleR.pack(side=LEFT, anchor = S)
        self.entryR = Entry(self.frameR,width = 6,textvariable = self.varR)
        self.entryR.pack(side = LEFT,anchor=S)
   
        ###G
        self.varG = StringVar() 
        self.lblG = tk.Label(self.frameG, text="G", font='Helvetica 18 bold')
        self.lblG.pack(side = LEFT,anchor=S)
        self.scaleG = Scale(self.frameG,from_=0, to=255, orient=HORIZONTAL,
                            length = 200,variable = self.varG,)                           
        self.scaleG.pack(side=LEFT)
        self.entryG = Entry(self.frameG,width = 6,textvariable = self.varG)
        self.entryG.pack(side = LEFT,anchor=S)

        ###B
        self.varB = StringVar() 
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
        self.canvasMem = []
        for row in range(6):
            for column in range(10):
                canvas = Canvas(self.frameMem,width = 50, height = 50, background = "#ffffff")
                canvas.grid(row = row, column= column)
                canvas.bind("<Button-1>",self.cliclHandler)
                self.canvasMem.append(canvas)
            


        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()


        ###self.geometry('350x500')
        ###self.configure(background='#000000')

        self.varR.trace("w",self.change)
        self.varB.trace("w",self.change)
        self.varG.trace("w",self.change)
        self.load()
        self.canvasMain2scales()
        

        
    def setup():    
        f= open("SavedColors", "r")
        f.close()
        


    def change(self,var, index,mode):
        if(self.ignoreChange):
            return
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()

        colorcode = f'#{r:02x}{g:02x}{b:02x}'

        self.entryMain.delete(0,END)
        self.entryMain.insert(0, colorcode)
        self.canvasMain.config(background = colorcode)

    def cliclHandler(self, event):
        if self.cget("cursor") != "pencil":
            self.config(cursor = "pencil")
            self.color = event.widget.cget("background")
        elif self.cget("cursor")=="pencil":    
            self.config(cursor="")
            event.widget.config()
            event.widget.config(background=self.color)

        else:
            self.color = event.widget.cget("background")
        if event.widget == self.canvasMain:
           self.canvasMain2scales()


    def canvasMain2scales(self):
        color = self.canvasMain.cget("background")
        r = int(color[1:3],16)
        g = int(color[3:5],16)
        b = int(color[5:7],16)
        self.ignoreChange = True
        self.varR.set(r)
        self.varG.set(g)
        self.varB.set(b)
        self.scaleR.set(r)
        self.scaleG.set(g)
        self.scaleB.set(b)
        self.ignoreChange = False

    def load(self):
        try:
            with open("paleta.txt","r") as f:
                color = f.readline().strip()
                self.canvasMain.config(background=color)
                for canvas in self.canvasMem:
                    color = f.readline().strip()
                    canvas.config(background=color)
        except FileNotFoundError:
            print("soubor neni")


    def quit(self, event=None):
        with open("paleta.txt", "w") as f :
            f.write(self.canvasMain.cget("background")+"\n")
            for canvas in self.canvasMem:
                f.write(canvas.cget("background")+"\n")
        super().quit()


app = Application()
app.mainloop()