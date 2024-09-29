from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.clock import Clock
import random, os

# Define o tamanho da janela antes de carregar o App
Config.set('graphics', 'width', '320')
Config.set('graphics', 'heigth', '480')

contas = {
    'jonatas': {
        'sexo': 'M',
        'idade': 27,
        'contato': '71984785356',
        'email': 'araujojonatasapc152018@gmail.com',
        'cidade': 'salvador',
    },
    'jennifer': {
        'sexo': 'f',
        'idade': 20,
        'contato': '71983714620',
        'email': 'jennifeesantos062@gmail.com',
        'cidade': 'salvador',
    },
    }


# Define a main a classe app    
class screenApp(App):
    def build(self):
        return screenLayout()

#define a classe Layout
class screenLayout(BoxLayout):
    
    #Entrar:
    def bt_enter(self):
        ...
        
    #Registrar:
    def bt_registrar(self):
        ...

    
# Run the application
if __name__ == "__main__":
    screenApp().run()
    