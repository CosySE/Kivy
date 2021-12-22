from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivy.uix.button import Button
from kivy.uix.label import Label 
from kivy.lang import Builder

KV ='''
#:import KivyLexer kivy.extras.highlight.KivyLexer
#:import HotReloadViewer kivymd.utils.hot_reload_viewer.HotReloadViewer

BoxLayout:
    HotReloadViewer:
        size_hint_x: .4
        path: app.camino_al_archivo_kivy
        errors: True
        errors_text_color: 1,1,0,1
        errors_background_color: app.theme_cls.bg_dark

'''
class Probando():
    pass

class Vivo(MDApp):
    camino_al_archivo_kivy = 'testing.kv' #nombre del archivo kv donde se guardaran 

    def build(self):
        return Builder.load_string(KV)

    def actualizar_archivo_kv(self,text):
        with open(self.camino_al_archivo_kivy,'w') as kv_archivo:
            kv_archivo.write(text)

Vivo().run()