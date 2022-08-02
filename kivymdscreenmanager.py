from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager,Screen

KV='''
ScreenManager:
    Primera:
    Segunda:
    Tercera:

<Primera>:
    name:'1'
    MDLabel :
        text: 'Hola Pantalla 1'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Siguiente'
        pos_hint: {'center_x': 0.5,'center_y':0.2}
        on_press:
            root.manager.current ='2'
            root.manager.transition.direction = 'left'

<Segunda>:
    name:'2'
    MDLabel :
        text: 'Hola Pantalla 2'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Atras'
        pos_hint: {'center_x':0.2,'center_y':0.2}
        on_press:
            root.manager.current = '1'
            root.manager.transition.direction = 'right'
    MDRectangleFlatButton:
        text: 'Siguiente'
        pos_hint: {'center_x': 0.7,'center_y':0.2}
        on_press:
            root.manager.current = '3'
            root.manager.transition.direction = 'left'

<Tercera>:
    name:'3'
    MDLabel :
        text:'Hola Pantalla 3 y Final'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Regresar'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:
            root.manager.current = '1'
            root.manager.transition.direction = 'up'

'''

class Primera(Screen):
    pass

class Segunda(Screen):
    pass
class Tercera(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Primera(name='1'))
sm.add_widget(Segunda(name='2'))
sm.add_widget(Tercera(name='3'))

class Aplicacion(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Teal'
        kv = Builder.load_string(KV)
        return kv

if __name__== '__main__':
    Aplicacion().run()