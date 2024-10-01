from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager

class TelaPrincipal(Screen):
    pass

class TelaSecundaria(Screen):
    def fechar_tela(self):
        # Aqui você pode chamar o método `current` do ScreenManager para mudar de tela
        self.manager.current = 'tela_principal'

class GerenciadorDeTelas(ScreenManager):
    pass

class MeuApp(App):
    def build(self):
        return GerenciadorDeTelas()

if __name__ == '__main__':
    MeuApp().run()
