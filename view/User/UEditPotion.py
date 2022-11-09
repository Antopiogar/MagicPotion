import sys
import  tkinter as tk
from model.potion import potion 
from model.Ingredient import Ingredient
from controller.dbAccess import DbAccess

class UEditPotion(tk.Frame):
    def __init__(self, parent, controller,win):
        self.win=win
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bg= tk.PhotoImage(file="./img/sfondoEditIngredients.png")
        self._canvas= tk.Canvas(self,width= 799, height= 500)
        self._setElements_()
        self._edited=None

    
    def _add_ingredients_(self,id=0):
        if id!=0:
            self._edited=id
        for ing in DbAccess._see_Ingredients_of(self._edited):
            print(ing)
            self._lbIngredientsOf.insert(1,ing.__str__())
        for ing in DbAccess._see_ingredients():
            print(ing)
            self._lbIngredientsTotal.insert(1,ing.__str__())

    def _add_elements_(self):
        self._edit=tk.Button(self,text="Edit", width=20,command=self._edit_,font=("Arial",15))
        self._lbIngredientsTotal=tk.Listbox(self._canvas,selectmode=tk.SINGLE,exportselection=0)
        self._lbIngredientsOf=tk.Listbox(self._canvas,selectmode=tk.SINGLE,exportselection=0)
        self._menu=tk.Button(self,text="Menu", width=20,command=self._menu_,font=("Arial",15))
        self._exitButton = tk.Button(self,text="exit", width=20,command=self._exit_,font=("Arial",15))
        
    def _edit_(self):
        sel=None
        l=[]
        idOld=None
        idNew=None
        listIdtoEdit=[]
        for i in self._lbIngredientsOf.curselection():
            sel=self._lbIngredientsOf.get(i)
            val=sel.split(",")
            id=val[0]
            removeItem=Ingredient(id,val[1],val[2],val[3],val[4],val[5])
            idOld=id
        sel=None
        for i in self._lbIngredientsTotal.curselection():
            sel=self._lbIngredientsTotal.get(i)
            val=sel.split(",")
            id=val[0]
            newItem=(Ingredient(id,val[1],val[2],val[3],val[4],val[5]))
            idNew=id
        print(f"NUOVO INGREDIENTE = {newItem}")
        ingLst=[]
        for i in self._lbIngredientsOf.get(0, tk.END):
            val=i.split(",")
            id=val[0]
            a=Ingredient(id,val[1],val[2],val[3],val[4],val[5])
            if a.__str__() != removeItem.__str__():
                ingLst.append(a)
        
        ingLst.append(newItem)
        print("STAMPA ELEMENTI NUOVA POZIONE")
        for i in ingLst:
            print(i.__str__())

        
        p=potion("",ingLst)
        
        if p._cambia_ing(l):
            listIdtoEdit.append(idNew)
            listIdtoEdit.append(idOld)
            listIdtoEdit.append(self._edited)
            print(f"Elemeti da modificare={listIdtoEdit}")
            DbAccess._modify_potions(listIdtoEdit)
            self._reinitialize_lb_()
            self._add_ingredients_(0)
        else :
            lbl=tk.Label(self._lbIngredientsOf,text="ERROR", width=20,font=("Arial",15))
            lbl.place(x=0,y=0)
            
        

    def _reinitialize_lb_(self):
        self._lbIngredientsOf.delete(0,tk.END)
        self._lbIngredientsTotal.delete(0,tk.END)
    
    def _menu_(self):
        self.controller.show_frame("MenuUser")

    def _setElements_(self):
        self._add_elements_()
        self._canvas.pack(expand=True, fill= tk.BOTH)
        self._canvas.create_image(0,0,image=self.bg, anchor="nw")
        x=0.3
        self._lbIngredientsOf.place(relx=0.1,y=135,relwidth=0.3)
        self._lbIngredientsTotal.place(relx=0.6,y=135,relwidth=0.3)
        self._edit.place(relx=x, y=340, relwidth=0.4)
        self._menu.place(relx=x, y=380, relwidth=0.4)
        self._exitButton.place(relx=x, y=420, relwidth=0.4)  

    def _exit_(self):
        sys.exit()