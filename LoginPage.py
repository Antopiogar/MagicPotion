import sys
from tkinter import BOTH, Button, Canvas, Entry, Label, PhotoImage, StringVar, Toplevel
from MenuAdmin import MenuAdmin

class LoginPage():

    def __init__(self):
        self._window = Toplevel()
        self.bg= PhotoImage(file="./img/sfondoMenu.png")
        self._canvas= Canvas(self._window,width= 799, height= 500)
        self._user_var = StringVar()
        self._pass_var = StringVar()
        self._lbl_user=Label(self._canvas,text="Username",font=("Arial",17), width=20)
        self._txt_user = Entry(self._canvas, font=('Arial',17), width=20,textvariable=self._user_var)
        self._lbl_pass=Label(self._canvas,text="Password",font=("Arial",17), width=20)
        self._txt_pass = Entry(self._canvas,font=('Arial',17),width=20, show='*',textvariable=self._pass_var)   
        
         
        

    def _add_elements_(self):
        
        
        
        self._canvas.pack(expand=True, fill= BOTH)
        self._login = Button(self._canvas,text="login", font=('Arial',17), width=20,command=self._login_)
        self._exit = Button(self._canvas,text="exit", font=('Arial',17), width=20,command=self._exit_)
        #Add the image in the canvas
        self._canvas.create_image(0,0,image=self.bg, anchor="nw")
        #Add a text in canvas
        


    def _setElements_(self):
        x=0.25
        self._add_elements_()
        self._window.title("Login")
        self._window.geometry("500x500")
        self._window.resizable(False, False)
        self._lbl_user.place(relx=x,y=20)
        self._txt_user.place(relx=x,y=60)
        self._lbl_pass.place(relx=x,y=100)
        self._txt_pass.place(relx=x,y=140)
        self._login.place(relx=x, y=340)
        self._exit.place(relx=x, y=390)    

    def _startAll_(self):
        self._setElements_()
        self._window.mainloop()

    def _login_(self):
        print(f"user:{self._user_var.get}, pass: {self._pass_var.get}")
        if self._user_var=="admin" and self._pass_var=="admin":
            print("FUNZIONA")
            ma=MenuAdmin()
            ma._setElements_()
            ma.__getattribute__(self._window).mainloop()
            self._window.withdraw()

    def _exit_(self):
        sys.exit()

