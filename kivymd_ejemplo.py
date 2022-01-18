from kivymd.app import MDApp
from kivy.lang.builder import Builder

KV = '''
MDScreen:
    MDToolbar:
        title:'Probando KIVY MD'
        pos_hint:{'top':1}
    MDBoxLayout:
        orientation:'vertical'
        MDLabel:
            text:'Estamos aprendiendo KIVY MD'
            halign:'center'
    MDRaisedButton:
        elevation: 10
        
        text:'Aceptar'
        pos_hint:{'center_x':0.5,'center_y':0.2}
        on_press: app.presiona()
'''

class Aplicacion(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Teal' # esto es un ejemplo de unos de los temas que tiene
        return Builder.load_string(KV)
    def presiona(self):
        print('me presionaste')

Aplicacion().run()