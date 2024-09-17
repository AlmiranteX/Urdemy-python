# Importaçoes do kivy
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class FirstLayout(BoxLayout):
    pass

class test(App):
    def build(self):
        layer1 = FirstLayout()
        layer1.add_widget(Button(text="First Kivy"))
        return layer1
    
test().run()

