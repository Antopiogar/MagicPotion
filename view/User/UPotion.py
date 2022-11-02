import sys
import  tkinter as tk
from controller.dbAccess import DbAccess
from model.Ingredient import Ingredient
from model.potion import potion

class UPotion(tk.Frame):
    def __init__(self, parent, controller,win):
        self.win=win
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bg= tk.PhotoImage(file="./img/sfondoPotion.png")
        self._canvas= tk.Label(self,image=self.bg)
        self._name_var=tk.StringVar()
        self._id=0
        self._setElements_()


    def _add_elements_(self):
        self._lb=tk.Listbox(self._canvas,selectmode=tk.MULTIPLE)
        self._txt_name=tk.Entry(self._canvas,textvariable=self._name_var,font=("Arial",15))
        self._btn_confirm = tk.Button(self._canvas,text="confirm"  ,command=self._add_,font=("Arial",15))
        self._exitButton = tk.Button(self._canvas,text="exit", command=self._exit_,font=("Arial",15))
        self._menuButton = tk.Button(self._canvas,text="menu", command=self._menu_,font=("Arial",15))
        

    def _add_(self):
        name=self._name_var.get()
        p=potion()
    def _clearAll_(self):
        self._txt_name.delete(0, tk.END)
        self._id=0

    def _add_ingredients_(self):
        for ing in DbAccess._see_ingredients():
            self._lb.insert(1,ing.__str__())

    def _reinitialize_lb_(self):
        self._lb.delete(0,tk.END)
        self._add_ingredients_()

    def _setElements_(self):
        
        self._add_elements_()
        self._add_ingredients_()
        self._canvas.place(x=0,y=0, relwidth=1, relheight=1)
        self._txt_name.place(relx=0.25,y=150,relwidth=0.5)
        self._btn_confirm.place(relx=0.15,rely=0.8,relwidth=0.7)
        self._menuButton.place(relx=0.15,rely=0.9,relwidth=0.7)
        self._lb.place(relx=0.15,y=240,relwidth=0.7,relheight=0.3)

    def _set_values(self,n,f,w,a,e,id):
        self._id=id
        self._txt_air.delete(0, tk.END)
        self._txt_fire.delete(0, tk.END)
        self._txt_earth.delete(0, tk.END)
        self._txt_name.delete(0, tk.END)
        self._txt_water.delete(0, tk.END)
        self._txt_air.insert(0,a)
        self._txt_fire.insert(0,f)
        self._txt_earth.insert(0,e)
        self._txt_name.insert(0,n)
        self._txt_water.insert(0,w)

    def _exit_(self):
        sys.exit()

    def _menu_(self):
        self.controller.show_frame("MenuUser")