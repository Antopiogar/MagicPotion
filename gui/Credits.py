import tkinter as tk

class Credits(tk.Frame):
    def __init__(self, parent, controller,win):
        self.win=win
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bg= tk.PhotoImage(file="./img/sfondoCredits.png")
        str= "Team:\n Breaking Bad\n\nTeam-leader:\n Gargiulo Antonio Pio\n\nOther member:\n Longobardi Francesco\nMatrone Francesco\n Porpora Luigi"
        self.lbl=tk.Label(self, text=str, image=self.bg, compound='center',fg="white")
        self._btn_menu=tk.Button(self.lbl,text="Menu",command=self._credits_)
        self.lbl.place(x=0,y=0)
        self._btn_menu.place(relx=0,rely=0.85,relwidth=1)


    def _credits_(self):
        self.controller.show_frame("Menu")
        self.win.geometry("800x500")