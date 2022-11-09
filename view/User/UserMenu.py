import sys
import tkinter as tk
from tkinter.ttk import Button

class MenuUser(tk.Frame):
    def __init__(self, parent, controller,win,ingPage,editPage,delPage):
        self._ingPage=ingPage
        self._editPage=editPage
        self._delPage = delPage
        self.win=win
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bg= tk.PhotoImage(file="./img/sfondoMenuUser.png")
        self._canvas= tk.Canvas(self,width= 799, height= 500)
        self._setElements_()

    def _add_elements_(self):
        self.start = tk.Button(self,text="Add Potion", width=20,command=self._add_)
        self.credits = tk.Button(self,text="See Potions" ,  width=20,command=self._edit_)
        self.delete = tk.Button(self,text="Delete Potion" ,  width=20,command=self._del_)
        self.exit = Button(self,text="EXIT", width=20,command=self._exit_)

    def _add_(self):
        self._ingPage._clearAll_()
        self.controller.show_frame("UPotion")
        self.win.geometry("800x500")

    def _setElements_(self):
        self._add_elements_()
        self._canvas.pack(expand=True, fill= tk.BOTH)
        self._canvas.create_image(0,0,image=self.bg, anchor="nw")
        self.start.place(relx=0.35, y=220,relwidth=0.3)
        self.credits.place(relx=0.35, y=260,relwidth=0.3)
        self.delete.place(relx=0.35,y=300,relwidth=0.3)
        self.exit.place(relx=0.35, y=340,relwidth=0.3)

    def _edit_(self):
        self._editPage._reinitialize_lb_()
        self.controller.show_frame("USee")
        self.win.geometry("800x500")

    def _del_(self):
        self._delPage._reinitialize_lb_()
        self.controller.show_frame("UDelete")
        self.win.geometry("800x500")

    def _exit_(self):
        sys.exit()