import sys
import  tkinter as tk
from tkinter.ttk import Button

class Menu(tk.Frame):
    def __init__(self, parent, controller,win):
        self.win=win
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bg= tk.PhotoImage(file="./img/sfondoMenu.png")
        self._canvas= tk.Canvas(self,width= 799, height= 500)
        self._setElements_()

    def _add_elements_(self):
        self.start = tk.Button(self,text="start", width=20,command=self._start_)
        self.credits = tk.Button(self,text="credits" ,  width=20,command=self._credits_)
        self.exit = Button(self,text="exit", width=20,command=self._exit_)

    def _start_(self):
        self.controller.show_frame("LoginPage")
        self.win.geometry("500x400")


    def _setElements_(self):
        self._add_elements_()
        self._canvas.pack(expand=True, fill= tk.BOTH)
        self._canvas.create_image(0,0,image=self.bg, anchor="nw")
        self.start.place(relx=0.35, y=350)
        self.credits.place(relx=0.35, y=390)
        self.exit.place(relx=0.35, y=430)

    def on_closing(self):
        sys.exit(0)

    def _credits_(self):
        self.controller.show_frame("Credits")
        self.win.geometry("260x300")

    def _exit_(self):
        sys.exit()