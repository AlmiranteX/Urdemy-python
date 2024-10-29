from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Carregar o arquivo main.kv
Builder.load_file("main.kv")
# Carregar o arquivo outra_tela.kv
Builder.load_file("outra_tela.kv")

class MainScreen(Screen):
    pass

class OutraTela(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        return MyScreenManager()

if __name__ == '__main__':
    MyApp().run()
