import tkinter as tk
from view.Credits import Credits
from view.LoginPage import LoginPage
from view.Admin.MenuAdmin import MenuAdmin
from view.Menu import Menu
from view.Admin.Ingredients import AIngredients
from view.Admin.AModify import AModify
from view.Admin.ADelete import ADelete
from view.User.UPotion import UPotion
from view.User.UModify import UModify
from view.User.UserMenu import MenuUser

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
        for F in (Menu, LoginPage,Credits):
            page_name = F.__name__
            frame = F(parent=container, controller=self,win=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self._add_special_class(container=container)
        self.show_frame("AModify")

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
        mPotion=UModify(parent=container,controller=self,win=self,potionwin=UPotion)
        self.frames["UModify"] = mPotion
        mPotion.grid(row=0, column=0, sticky="nsew")
        mAdm=MenuAdmin(parent=container,controller=self,win=self,ingPage=ingPage,editPage=mIng,delPage=aDel)
        self.frames["MenuAdmin"]= mAdm
        mAdm.grid(row=0, column=0, sticky="nsew")
        mUse=MenuUser(parent=container,controller=self,win=self,ingPage=potPage,editPage=mPotion,delPage=None)
        self.frames["MenuUser"]=mUse
        mUse.grid(row=0, column=0, sticky="nsew")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
