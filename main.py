from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class BoxLayoutEjemplo(BoxLayout):
    #  def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     b1 = Button(text='hola1')
    #     b2= Button(text='hola2')
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    pass
    

class WidgetPrincipal(Widget):
    pass

class Nuevo(App):
    def build(self):
        return Builder.load_file('LabGame.kv')
    
if __name__=='__main__':
    Nuevo().run()