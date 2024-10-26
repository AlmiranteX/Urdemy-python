from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.config import Config

# Define o tamanho da janela antes de carregar o App
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '550')

class  Tela_Login(Screen):
    pass








class TelaSecundaria(Screen):
    def fechar_tela(self):
        # Aqui você pode chamar o método `current` do ScreenManager para mudar de tela
        self.manager.current = 'tela_principal'

class GerenciadorDeTelas(ScreenManager):
    pass

class kv_footApp(App):
    def build(self):
        return GerenciadorDeTelas()

if __name__ == '__main__':
    kv_footApp().run()




