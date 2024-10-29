from kivy.app import App
from kivy.uix.button import Button
#from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        return RootWidget()

class RootWidget(BoxLayout):
    pass

if __name__ == "__main__":
    MyApp().run()
