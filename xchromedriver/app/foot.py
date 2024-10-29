from kivy.config import Config
# Configurações de janela devem ser feitas antes de carregar o App ou Window
Config.set('graphics', 'width', '800')  # Largura fixa da janela
Config.set('graphics', 'height', '550')  # Altura fixa da janela
Config.set('graphics', 'resizable', False)  # Desabilita o redimensionamento

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from user import User



#Oculta uma imagem e um texto de aviso
def aviso(self, **args):
    """_summary_
        args: receber 2 paramentros um elemento Image e Label
        ocultar(): funçao a ser chamada apos um tempo
    """
    def ocultar(self):
        
        args['banne'].opacity = 0
        args['aviso'].opacity = 0
    
    args['banne'].opacity = 1
    args['aviso'].opacity = 1
    
    Clock.schedule_once(ocultar, 3)
    
class  Tela_Login(Screen):
    
    def on_enter(self):
        self.ids.fundo.remove_widget(self.ids.rg)
          
    def login(self):
        
        #Obter texto nos TextInput de login
       
        user =self.ids.username.text
        password=self.ids.userpassword.text
      
        #verificar se dados foram digitados
        if user and password:
            print(user)
            user = user.strip()
            password = password.strip()
            
            buscar = User(user=user, password=password, email='')
            
            #verificar se usuario existe e fazer login se True
            if buscar.logar():
                self.ids.aviso_login.text = 'Sucesso'
                self.ids.banne_aviso.opacity = 1
                self.ids.aviso_login.opacity = 1
            else:
                
                self.ids.aviso_login.text = 'Dados Invalidos'
                aviso(self,
                    banne=self.ids.banne_aviso,
                    aviso=self.ids.aviso_login
                    )

    
    def recuper(self):
        if self.ids.lg not in self.children:
            self.ids.fundo.add_widget(self.ids.rg)
            self.ids.fundo.remove_widget(self.ids.lg)
            
    def back_login(self):
        def filtro():
            proibidos = '#$%&*()-+=!"`} ?:;,/\|][{'
            #Filtro dos dados
            
            user = self.ids.usernameR.text
            password = self.ids.passwordR.text
            email = self.ids.emailR.text
            
            #checar se algo foi digitado nos TextInput e se sao validos
            if user and password and email:
                #removendo espaços nas laterais
                user = user.strip()
                password = password.strip()
                email = email.strip()
                
                #tamano dos caracteres
                min_user = len(user) > 4 
                min_password = len(password) >= 4
                min_email = len(email) > 5 
              
                if min_user and min_email and min_password:
                    #checar caracteres
                    u_p_e = user+password+email
                    for n in range(len(u_p_e)):
                        
                        if u_p_e[n] in proibidos:
                            if u_p_e[n] == ' ':
                                pb=(f'Proibido usar: (ESPAÇOS)')
                                return False
                            else:
                                pb=('proibido usar: (', u_p_e[n],')')
                                return False
                            
                    return True

        print(filtro())
        #Verificar se Nome de usuario e email estao disponivel no baco de dados
        if filtro():
            #verificar se dados name e email nao estao em usor 
            user = self.ids.usernameR.text
            email = self.ids.emailR.text
            verificar_base=User.verificar(self, name=user, email=email)
            
            if verificar_base == (f'{email}@gmail.com Indisponivel !'):
                self.ids.avsio_login.text = verificar_base
                aviso(self,
                      banne=self.ids.banne_aviso,
                      aviso=self.ids.aviso_login
                      )
                return
            elif verificar_base == (f'{user} Indisponivel !'):
                self.ids.aviso_login.text = verificar_base
                aviso(self,
                      banne=self.ids.banne_aviso,
                      aviso=self.ids.aviso_login
                      )
                return
            
            #envia dados e volta para layout login
            if self.ids.rg not in self.children:
                self.ids.fundo.add_widget(self.ids.lg)
                self.ids.fundo.remove_widget(self.ids.rg)
            
            
class Registro(Screen):
    def fechar_tela(self):
        # Aqui você pode chamar o método `current` do ScreenManager para mudar de tela
        self.manager.current = 'Tela_Login'

class GerenciadorDeTelas(ScreenManager):
    pass

class kv_footApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Tela_Login(name='Tela_Login'))
        
        sm.add_widget(Registro(name='Registro'))
        return sm

if __name__ == '__main__':
    kv_footApp().run()




