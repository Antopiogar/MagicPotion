
import tkinter as tk
from gui.Credits import Credits
from gui.LoginPage import LoginPage
from gui.MenuAdmin import MenuAdmin
from gui.Menu import Menu
from gui.Ingredients import Ingredients

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title=("Magic Potion")
        self.resizable(False,False)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (Menu, LoginPage,Credits,MenuAdmin,Ingredients):
            page_name = F.__name__
            frame = F(parent=container, controller=self,win=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("Ingredients")

    

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
