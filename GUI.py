from tkinter import *
from tkinter import Tk



class MainCanvas:
    """Canvas with links to each cell grid"""
    def __init__(self, master: Tk, width: int = 1280, height: int = 720):
        self.master = master
        self.canvas_width = width
        self.canvas_height = height
        self.main_canvas = Canvas(self.master, background='black', height=height, width=width)

        self.master.title("Metaballs")
        self.master.resizable(width=False, height=False)
        self.master.configure(background='black')

        self.main_canvas.pack()










root = Tk()
root.mainloop()
