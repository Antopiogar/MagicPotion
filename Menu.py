import sys
from tkinter import Button, Label, PhotoImage, Toplevel
from tkinter.tix import Tk
from LoginPage import LoginPage


class Menu():
    def __init__(self):
        self._window = Tk()

    def _add_elements_(self):
        self._bg = PhotoImage(file="./img/sfondoMenu.png")
        self._sfondo = Label(self._window, image=self._bg)
        self.start = Button(text="start", font=("arial", 14), width=20,command=self._start_)
        self.credits = Button(text="credits", font=("arial", 14), width=20,command=self._credits_)
        self.exit = Button(text="exit", font=("arial", 14), width=20,command=self._exit_)

    def _start_(self):
        lp=LoginPage()
        lp._setElements_()
        self._window.withdraw()

    def _setElements_(self):
        self._add_elements_()
        self._window.title("Magic potion")
        self._window.geometry("799x500")
        self._window.resizable(False, False)
        self._sfondo.place(x=0, y=0)
        self.start.place(relx=0.35, y=350)
        self.credits.place(relx=0.35, y=390)
        self.exit.place(relx=0.35, y=430)
        self._window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        sys.exit(0)

        
    
    def _startAll_(self):
        self._setElements_()
        return self._window

    def _credits_(self):
        top= Toplevel(self._window)
        top.geometry("260x300")
        top.title("Credits")
        top.resizable(False,False)
        str= "Team:\n Breaking Bad\n\nTeam-leader:\n Gargiulo Antonio Pio\n\nOther member:\n Longobardi Francesco\nMatrone Francesco\n Porpora Luigi"
        Label(top, text= str, font=('Helvetica', 18)).place(x=0,y=0)

    
    def _exit_(self):
        sys.exit()
