from tkinter import BOTH, Button, Canvas, PhotoImage, Toplevel
from tkinter.tix import Tk

class LoginPage():

    def __init__(self):
        self._window = Toplevel()
        self.bg= PhotoImage(file="./img/sfondoMenu.png")

    def _add_elements_(self):
        
        
        canvas= Canvas(self._window,width= 799, height= 500)
        canvas.pack(expand=True, fill= BOTH)
        self._login = Button(canvas,text="login", font=("arial", 14), width=20,command=self._login_)
        #Add the image in the canvas
        canvas.create_image(0,0,image=self.bg, anchor="nw")
        #Add a text in canvas
        


    def _setElements_(self):
        self._add_elements_()
        self._window.title("Login")
        self._window.geometry("799x500")
        self._window.resizable(False, False)
        self._login.place(relx=0.35, y=350)
    
    def _startAll_(self):
        self._setElements_()
        self._window.mainloop()

    def _login_(self):
        pass

