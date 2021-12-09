from kivy.lang import Builder
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty
#from kivy.uix.scrollview import ScrollView

class WidgetsEjemplos(GridLayout):
    contador = 1
    mitexto = StringProperty('1')
    def presiona_boton(self):
        self.contador = self.contador + 1
        self.mitexto= str(self.contador)

    def toggleboton(self,elemento):
        print('me presionaste ' + elemento.state )
        if elemento.state == 'normal':
            elemento.text = 'OFF'
        else:
            elemento.text = 'ON'
    def switchbton(self,elemento):
        print('Switch: '+ str(elemento.active))

    def slidervalue(self,elemento):
        print('Slider: '+ str(int(elemento.value)))

class StackLayoutEjemplo(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0,100):
            size = dp(80)
            b= Button(text=str(i+1),size_hint=(None,None),size =(size,size))
            self.add_widget(b)
     
class AnchorLayoutEjempo(AnchorLayout):
    pass

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
        return Builder.load_file('main.kv')
    
if __name__=='__main__':
    Nuevo().run()