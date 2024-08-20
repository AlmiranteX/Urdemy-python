# Importa o app, Builder
# Criar o app
# Criar a funcao Builder

from kivy.app import App
from kivy.lang import Builder

tela = Builder.load_file("tela.kv")

class MeuAplicativo(App):
    def build(self):
        return tela


MeuAplicativo().run()