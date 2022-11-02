import sys
import  tkinter as tk
from unicodedata import name
from controller.dbAccess import DbAccess
from model.Ingredient import Ingredient
from pip._vendor.typing_extensions import Self

class AIngredients(tk.Frame):
    def __init__(self, parent, controller,win):
        self.win=win
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bg= tk.PhotoImage(file="./img/sfondoAddIngredients.png")
        self._canvas= tk.Label(self,image=self.bg)
        self._name_var=tk.StringVar()
        self._fire_var=tk.StringVar()
        self._water_var=tk.StringVar()
        self._air_var=tk.StringVar()
        self._earth_var=tk.StringVar()
        self._id=0
        self._setElements_()


    def _add_elements_(self):
        self._txt_name=tk.Entry(self._canvas,textvariable=self._name_var,font=("Arial",15))
        self._txt_fire=tk.Entry(self._canvas,text="Fire>",textvariable=self._fire_var,font=("Arial",12))
        self._txt_air=tk.Entry(self._canvas,text=" Air ",textvariable=self._air_var,font=("Arial",12))
        self._txt_water=tk.Entry(self._canvas,text="Water",textvariable=self._water_var,font=("Arial",12))
        self._txt_earth=tk.Entry(self._canvas,text="Earth",textvariable=self._earth_var,font=("Arial",12))
        self._btn_confirm = tk.Button(self._canvas,text="confirm"  ,command=self._add_,font=("Arial",15))
        self._exitButton = tk.Button(self._canvas,text="exit", command=self._exit_,font=("Arial",15))
        self._menuButton = tk.Button(self._canvas,text="menu", command=self._menu_,font=("Arial",15))
        

    def _add_(self):
        name=self._name_var.get()
        fire=self._fire_var.get()
        water=self._water_var.get()
        air=self._air_var.get()
        earth=self._earth_var.get()
        try:
            f=int(fire)
            w=int(water)
            a=int(air)
            e=int(earth)
        
        except:
            self._name_var.set("ERROR IN INGREDIENTS VALUES")
        if(self._id==0):
            obj=Ingredient(name=name,fire=f,water=w,air=a,earth=e)
        else:
            obj=Ingredient(id=self._id,name=name,fire=f,water=w,air=a,earth=e)
        if self._id==0:
            DbAccess._add_ingredient(obj)
        else:
            DbAccess._modify_ingredients(self._id,obj)
        self._clearAll_()
        self._name_var.set("Your ingredient added")
        

    def _clearAll_(self):
        self._txt_air.delete(0, tk.END)
        self._txt_fire.delete(0, tk.END)
        self._txt_earth.delete(0, tk.END)
        self._txt_name.delete(0, tk.END)
        self._txt_water.delete(0, tk.END)
        self._id=0



    def _setElements_(self):
        
        self._add_elements_()
        self._canvas.place(x=0,y=0, relwidth=1, relheight=1)
        self._txt_name.place(relx=0.25,y=150,relwidth=0.5)
        self._txt_fire.place(x=180,y=220,width=100)
        self._txt_air.place(x=580,y=220,width=100)
        self._txt_earth.place(x=180,y=290,width=100)
        self._txt_water.place(x=580,y=290,width=100)
        self._btn_confirm.place(relx=0.15,rely=0.8,relwidth=0.7)
        self._menuButton.place(relx=0.15,rely=0.9,relwidth=0.7)

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
        self.controller.show_frame("MenuAdmin")