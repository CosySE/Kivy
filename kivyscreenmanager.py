from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager,Screen


class Primera(Screen):
    pass

class Segunda(Screen):
    pass
class Tercera(Screen):
    pass
class Navegar (ScreenManager):
    pass

kv = Builder.load_file('kivyscreenmanager.kv')

class Aplicacion(App):
    def build(self):
        return kv

if __name__== '__main__':
    Aplicacion().run()