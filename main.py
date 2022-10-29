
import tkinter as tk
from Credits import Credits
from LoginPage import LoginPage
import Menu 

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
        for F in (Menu.Menu, LoginPage,Credits):
            page_name = F.__name__
            frame = F(parent=container, controller=self,win=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("Menu")

    

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()