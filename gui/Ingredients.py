import sys
import  tkinter as tk

class Ingredients(tk.Frame):
    def __init__(self, parent, controller,win):
        self.win=win
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bg= tk.PhotoImage(file="./img/sfondoBase.png")
        self._canvas= tk.Label(self,image=self.bg)
        self._user_var=tk.StringVar()
        self._pass_var=tk.StringVar()
        self._setElements_()


    def _add_elements_(self):
        self._lbl_name=tk.Label(self,text="Name", font=("Arial",15))
        self._txt_name=tk.Entry(self,textvariable=self._user_var,font=("Arial",15))
        self._lbl_fire=tk.Label(self,text="Fire", font=("Arial",12))
        self._txt_fire=tk.Entry(self,text="Fire",textvariable=self._pass_var,font=("Arial",12))
        self._lbl_air=tk.Label(self,text="Air", font=("Arial",12))
        self._txt_air=tk.Entry(self,text="Air",textvariable=self._pass_var,font=("Arial",12))
        self._lbl_water=tk.Label(self,text="Water" ,font=("Arial",12))
        self._txt_water=tk.Entry(self,text="Water",textvariable=self._pass_var,font=("Arial",12))
        self._lbl_earth=tk.Label(self,text="Earth" ,font=("Arial",12))
        self._txt_earth=tk.Entry(self,text="Fire",textvariable=self._pass_var,font=("Arial",12))
        self._btn_confirm = tk.Button(self,text="confirm"  ,command=self._start_,font=("Arial",15))
        self._exitButton = tk.Button(self,text="exit", command=self._exit_,font=("Arial",15))
        self._lbl_empty= tk.Label(self,text="",height=5)
        

    def _start_(self):
        if self._user_var.get()=="admin" and self._pass_var.get()=="admin":
            print("FUNZIONA")
            self.controller.show_frame("MenuAdmin")
            self.win.geometry("800x500")
        #elif DbAccess.userInList():
        elif self._user_var.get()=="user" and self._pass_var.get()=="user":
            self.controller.show_frame("MenuUser")
        else:
            tk.Label(self,text="User not found", ).place(relx=0.3,y=160)


    def _setElements_(self):
        
        self._add_elements_()
        self.grid()
        self._canvas.place(x=0,y=0, relwidth=1, relheight=1)
        self._lbl_name.grid(row=0,column=3,sticky=tk.N,pady=2)
        self._lbl_empty.grid(row=2,column=1,sticky=tk.N,pady=2)
        self._lbl_fire.grid(row=4,column=1,sticky=tk.N,pady=2)
        self._txt_fire.grid(row=4,column=2,sticky=tk.N,pady=2)

        self._lbl_air.grid(row=4,column=5,sticky=tk.N,pady=2)
        self._txt_air.grid(row=4,column=6,sticky=tk.N,pady=2)

        self._lbl_water.grid(row=5,column=1,sticky=tk.N,pady=2)
        self._txt_water.grid(row=5,column=2,sticky=tk.N,pady=2)

        self._lbl_earth.grid(row=5,column=5,sticky=tk.N,pady=2)
        self._txt_earth.grid(row=5,column=6,sticky=tk.N,pady=2)

        self._exitButton.grid(row=5,column=3,pady=24)
        
    
    def _exit_(self):
        sys.exit()