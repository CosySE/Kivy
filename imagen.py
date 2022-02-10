from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.gridlayout import GridLayout


class EjemploImagen(GridLayout):
    pass


class Principal(App):
    def build(self):
        return Builder.load_file('imagen.kv')


Principal().run()