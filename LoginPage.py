import sys
import  tkinter as tk

from dbAccess import DbAccess

class LoginPage(tk.Frame):
    def __init__(self, parent, controller,win):
        self.win=win
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bg= tk.PhotoImage(file="./img/sfondoCredits.png")
        self._canvas= tk.Canvas(self,width= 799, height= 500)
        self._user_var=tk.StringVar()
        self._pass_var=tk.StringVar()
        self._setElements_()


    def _add_elements_(self):
        self._lbl_user=tk.Label(self,text="Username",width=20,font=("Arial",15))
        self._txt_user=tk.Entry(self,textvariable=self._user_var,width=20,font=("Arial",15))
        self._lbl_pass=tk.Label(self,text="Pass",width=20,font=("Arial",15))
        self._txt_pass=tk.Entry(self,textvariable=self._pass_var,width=20,font=("Arial",15))
        self._login = tk.Button(self,text="login", width=20,command=self._start_,font=("Arial",15))
        self._exitButton = tk.Button(self,text="exit", width=20,command=self._exit_,font=("Arial",15))
        

    def _start_(self):
        if self._user_var.get()=="admin" and self._pass_var.get()=="admin":
            print("FUNZIONA")
            self.controller.show_frame("MenuAdmin")
        elif DbAccess.userInList():
            self.controller.show_frame("MenuUser")
        else:
            tk.Label(self,text="User not found",width=20).place(relx=0.3,y=160)
        self.controller.show_frame("Menu")


    def _setElements_(self):
        
        self._add_elements_()
        self._canvas.pack(expand=True, fill= tk.BOTH)
        self._canvas.create_image(0,0,image=self.bg, anchor="nw")
        x=0.3
        self._lbl_user.place(relx=x,y=20)
        self._txt_user.place(relx=x,y=60)
        self._lbl_pass.place(relx=x,y=100)
        self._txt_pass.place(relx=x,y=140)
        self._login.place(relx=x, y=240)
        self._exitButton.place(relx=x, y=290)  

    def on_closing(self):
        sys.exit(0)

    
    def _exit_(self):
        sys.exit()