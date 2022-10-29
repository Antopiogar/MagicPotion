import sys
import  tkinter as tk
from tkinter.ttk import Button

class MenuAdmin(tk.Frame):
    def __init__(self, parent, controller,win):
        self.win=win
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bg= tk.PhotoImage(file="./img/sfondoBase.png")
        self._canvas= tk.Canvas(self,width= 799, height= 500)
        self._setElements_()

    def _add_elements_(self):
        self._lbl_admin=tk.Label(self,text="WELCOME MY ADMIN",font=("Arial",20),width=20)
        self.start = tk.Button(self,text="Add Ingredient", width=20,command=self._add_)
        self.credits = tk.Button(self,text="Edit Ingredient" ,  width=20,command=self._edit_)
        self.exit = Button(self,text="exit", width=20,command=self._exit_)

    def _add_(self):
        self.controller.show_frame("Ingredients")
        self.win.geometry("600x200")

    def _setElements_(self):
        self._add_elements_()
        self._canvas.pack(expand=True, fill= tk.BOTH)
        self._canvas.create_image(0,0,image=self.bg, anchor="nw")
        self.start.place(relx=0.35, y=350)
        self.credits.place(relx=0.35, y=390)
        self.exit.place(relx=0.35, y=430)
        self._lbl_admin.place(relx=0.35,y=10)

    def _edit_(self):
        self.controller.show_frame("EditIngredients")
        self.win.geometry("260x300")

    def _exit_(self):
        sys.exit()