from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.config import Config
from kivy.clock import Clock
import random, os

# Define o tamanho da janela antes de carregar o App
Config.set('graphics', 'width', '320')
Config.set('graphics', 'heigth', '480')

contas = {
    'jonatas': {
        'senha': '19972024',
        'sexo': 'M',
        'idade': 27,
        'contato': '71984785356',
        'email': 'araujojonatasapc152018@gmail.com',
        'cidade': 'salvador',
    },
    'jennifer': {
        'senha': '20042024',
        'sexo': 'f',
        'idade': 20,
        'contato': '71983714620',
        'email': 'jennifeesantos062@gmail.com',
        'cidade': 'salvador',
    },
    }

#Tentar Login
def login(L, S, contas):
    
    #Verificar se Usuario existe
    if L in contas.keys():
        #verificar se a senha do user estar correta
        if S == contas[L]['senha']:
            aviso = f"Usuario'{L}' ..Logado.."
            return True, aviso
        else:
            aviso = f'Por favor {L} digite a senha correta!'
            return False, aviso      
    else:
        aviso = f'Usuario "{L}" Não Existe!'
        return False, aviso

class Screen_Login(Screen):
     #Entrar:
    def bt_enter(self):
        usuario = self.ids.user.text
        senha = self.ids.password.text

        check_login = login(
            L=usuario.lower(),
            S=senha.lower(),
            contas=contas)
        
        if check_login[0]:
            print('Logado...')
    
    def bt_registrar(self):
        self.manager.current = 'Screen_Registre'
        
class Screen_Registre(Screen):
    
    def Back_Login(self):
        self.manager.current = 'Screen_Login'
               
class GerenciadorDeTelas(ScreenManager):
    pass

class Save_App(App):
    def build(self):
        return GerenciadorDeTelas()
    
# Run the application
if __name__ == "__main__":
    Save_App().run()
    