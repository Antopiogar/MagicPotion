import tkinter as tk
from view.Credits import Credits
from view.LoginPage import LoginPage
from view.Admin.MenuAdmin import MenuAdmin
from view.Menu import Menu
from view.Admin.Ingredients import AIngredients
from view.Admin.AModify import AModify
from view.Admin.ADelete import ADelete
from view.User.UPotion import UPotion
from view.User.USee import USee
from view.User.SeeIngredientsList import SeeIngredients
from view.User.UserMenu import MenuUser
from view.User.UDelete import UDelete
from view.User.UEditPotion import UEditPotion

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title=("Magic Potion")
        self.resizable(False,False)
        self.iconbitmap(r'./img/icona.ico')
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (Menu, LoginPage,Credits):
            page_name = F.__name__
            frame = F(parent=container, controller=self,win=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self._add_special_class(container=container)
        self.show_frame("Menu")

    def _add_special_class(self,container):
        aDel=ADelete(parent=container,controller=self,win=self)
        self.frames["ADelete"] = aDel
        aDel.grid(row=0, column=0, sticky="nsew")
        ingPage= AIngredients(parent=container,controller=self,win=self)
        self.frames["AIngredients"] = ingPage
        ingPage.grid(row=0, column=0, sticky="nsew")
        mIng=AModify(parent=container,controller=self,win=self,ingWin=ingPage)
        self.frames["AModify"] = mIng
        mIng.grid(row=0, column=0, sticky="nsew")
        potPage=UPotion(parent=container,controller=self,win=self)
        self.frames["UPotion"] = potPage
        potPage.grid(row=0, column=0, sticky="nsew")
        seeIngr=SeeIngredients(parent=container,controller=self,win=self)
        self.frames["SeeIngredientsList"]=seeIngr
        seeIngr.grid(row=0, column=0, sticky="nsew")
        uEdit=UEditPotion(parent=container,controller=self,win=self)
        self.frames["UEditPotion"]=uEdit
        uEdit.grid(row=0, column=0, sticky="nsew")
        mPotion=USee(parent=container,controller=self,win=self,seeIng=seeIngr,editP=uEdit)
        self.frames["USee"] = mPotion
        mPotion.grid(row=0, column=0, sticky="nsew")
        mAdm=MenuAdmin(parent=container,controller=self,win=self,ingPage=ingPage,editPage=mIng,delPage=aDel)
        self.frames["MenuAdmin"]= mAdm
        mAdm.grid(row=0, column=0, sticky="nsew")
        uDel=UDelete(parent=container,controller=self,win=self)
        self.frames["UDelete"] = uDel
        uDel.grid(row=0, column=0, sticky="nsew")
        mUse=MenuUser(parent=container,controller=self,win=self,ingPage=potPage,editPage=mPotion,delPage=uDel)
        self.frames["MenuUser"]=mUse
        mUse.grid(row=0, column=0, sticky="nsew")
        
        


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
