# Importaçoes do kivy
import kivy
from kivy.app import *
from kivy.uix.boxlayout import *
from kivy.uix.button import *


class FirstLayout(BoxLayout):
    pass

class test(App):
    def build(self):
        layer1 = FirstLayout()
        layer1.add_widget(Button(text="First Kivy"))
        return layer1
    
test().run()

