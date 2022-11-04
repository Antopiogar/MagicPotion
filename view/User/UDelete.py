import sys
import  tkinter as tk
from controller.dbAccess import DbAccess

class UDelete(tk.Frame):
    def __init__(self, parent, controller,win):
        self.win=win
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bg= tk.PhotoImage(file="./img/sfondoEditIngredients.png")
        self._canvas= tk.Canvas(self,width= 799, height= 500)
        self._setElements_()

    def _add_ingredients_(self):
        for ing in DbAccess._see_potions():
            print(f"ingr={ing}")
            self._lb.insert(0,ing.__str__())

    def _add_elements_(self):
        self._lb=tk.Listbox(self._canvas,selectmode=tk.SINGLE)
        self._menu=tk.Button(self,text="Menu", width=20,command=self._menu_,font=("Arial",15))
        self._deleteButton = tk.Button(self,text="Delete", width=20,command=self._delete_,font=("Arial",15))
        self._exitButton = tk.Button(self,text="exit", width=20,command=self._exit_,font=("Arial",15))

    def _delete_(self):
        sel=None
        for i in self._lb.curselection():
            sel=self._lb.get(i)
            val=sel.split(",")
        id=val[0]
        DbAccess._delete_potions(id)
        self._reinitialize_lb_()
        
        print("MUORI")

    def _reinitialize_lb_(self):
        self._lb.delete(0,tk.END)
        self._add_ingredients_()
    
    def _menu_(self):
        self.controller.show_frame("MenuUser")

    def _setElements_(self):
        self._add_elements_()
        self._canvas.pack(expand=True, fill= tk.BOTH)
        self._canvas.create_image(0,0,image=self.bg, anchor="nw")
        x=0.3
        self._lb.place(relx=0.15,y=135,relwidth=0.7)
        self._deleteButton.place(relx=x, y=340, relwidth=0.4)
        self._menu.place(relx=x, y=380, relwidth=0.4)
        self._exitButton.place(relx=x, y=420, relwidth=0.4)  

    def _exit_(self):
        sys.exit()