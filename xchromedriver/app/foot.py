from kivy.config import Config
# Configurações de janela devem ser feitas antes de carregar o App ou Window
Config.set('graphics', 'width', '800')  # Largura fixa da janela
Config.set('graphics', 'height', '550')  # Altura fixa da janela
Config.set('graphics', 'resizable', False)  # Desabilita o redimensionamento

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager


class  Tela_Login(Screen):
    pass


class TelaSecundaria(Screen):
    def fechar_tela(self):
        # Aqui você pode chamar o método `current` do ScreenManager para mudar de tela
        self.manager.current = 'Tela_Login'

class GerenciadorDeTelas(ScreenManager):
    pass

class kv_footApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Tela_Login(name='Tela_Login'))
        sm.add_widget(TelaSecundaria(name='tela_secundaria'))
        return sm

if __name__ == '__main__':
    kv_footApp().run()




