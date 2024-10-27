from kivy.config import Config
# Configurações de janela devem ser feitas antes de carregar o App ou Window
Config.set('graphics', 'width', '800')  # Largura fixa da janela
Config.set('graphics', 'height', '550')  # Altura fixa da janela
Config.set('graphics', 'resizable', False)  # Desabilita o redimensionamento

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
#from kivy.lang import Builder
from user import User


# Carrega o arquivo KV
#Builder.load_file("kv_foot.kv")

class  Tela_Login(Screen):
    
    def login(self):
        #Obter texto nos TextInput de login
        user = self.ids.username.text
        password=self.ids.userpassword.text
        #verificar se dados foram digitados
        if user and password:
            user = user.strip()
            password = password.strip()
            buscar = User(user=user, password=password, email='')
            #verificar se usuario existe e fazer login se True
            if buscar.logar():
                self.ids.aviso_login.text = 'Sucesso'
            else:
                self.ids.aviso_login.text = 'Dados Invalidos'
                
                
                
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




