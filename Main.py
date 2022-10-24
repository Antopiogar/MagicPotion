from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder

class Credits(Screen):
    kivy = Builder.load_file("style2.kv")

    def _close_Credits_(self):
        screenMan.current="Menu"

class Menu(Screen):
    kivy = Builder.load_file("style2.kv")

    def _see_Credits_(self):
        screenMan.current="Credits"

class WindowManager(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        self.title= "Magic Poisons"
        return screenMan

screenMan=WindowManager()

schermate=[Menu(name="Menu"),Credits(name="Credits")]
for schermata in schermate:
    screenMan.add_widget(schermata)
screenMan.current="Menu"
sample_app=MainApp()
sample_app.run()