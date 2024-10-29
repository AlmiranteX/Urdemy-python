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
from user import User, requests


def internet():
    try:
        # Tenta fazer uma requisição para um site confiável
        response = requests.get("https://www.google.com", timeout=5)
        # Se o status da resposta for 200, está conectado
        return response.status_code == 200
    except requests.ConnectionError:
        return False
    
    

#Oculta uma imagem e um texto de aviso
def aviso(self, aviso):
    """_summary_
        args: receber 2 paramentros um elemento Image e Label
        ocultar(): funçao a ser chamada apos um tempo
    """
    av=self.ids.aviso_login
    bn=self.ids.banne_aviso
    
    def tamanho_bn(self):
        tm = len(aviso)
        
        if tm <= 20:
            bn.size = 200,50.0
            print(tm, bn.size)
        elif tm >= 21 and tm <= 35:
            bn.size = 250,50.0
            print(tm, bn.size)
        elif tm > 35:
            bn.size = 400,50.0
            print(tm, bn.size)
            
    def ocultar(self):
        av.text=''
        av.opacity = 0
        bn.opacity = 0
    
    
   

    av.text=aviso
    tamanho_bn(self)
    av.opacity = 1
    bn.opacity = 1
    
    Clock.schedule_once(ocultar, 3)
 
class  Tela_Login(Screen):
    
    def on_enter(self):
        self.ids.fundo.remove_widget(self.ids.rg)
        self.ids.fundo.remove_widget(self.ids.rc)
        if internet():
            ...
        else:
            aviso(self, aviso='Sem Rede')
        
    def login(self):
        
        #Obter texto nos TextInput de login
       
        user =self.ids.username.text
        password=self.ids.userpassword.text
        user = user.lower()
        password=password.lower()
        if internet():
            #verificar se dados foram digitados
            if user and password:
            
                user = user.strip()
                password = password.strip()
                
                buscar = User(user=user, password=password, email='')
                
                #verificar se usuario existe e fazer login se True
                if buscar.logar():
                    self.ids.aviso_login.text = 'Sucesso'
                    self.ids.banne_aviso.opacity = 1
                    self.ids.aviso_login.opacity = 1
                    self.manager.current = 'Menu_bot'
                else:
                    aviso(self,aviso='Dados Invalidos')
        else:
            aviso(self, aviso='Sem Rede..')
        
    def muda_layout(self):
        #mudar lyout
        try:
            if self.ids.lg not in self.children:
                    self.ids.fundo.add_widget(self.ids.rg)
                    self.ids.fundo.remove_widget(self.ids.lg)
                    
                    print('login X registro')
                
        except Exception as e:
            try:
                if self.ids.rg not in self.children:
                    self.ids.fundo.add_widget(self.ids.lg)
                    self.ids.fundo.remove_widget(self.ids.rg)
                    print('registo X login')
            except:
                print(f'Erro ao mudar Layout\n\t{e}')
                
    def recupera(self):
            try:
                if self.ids.lg not in self.children:
                    self.ids.fundo.add_widget(self.ids.rc)
                    self.ids.fundo.remove_widget(self.ids.lg)
                    
            except:
                try:
                    if self.ids.rc not in self.children:
                        self.ids.fundo.add_widget(self.ids.lg)
                        self.ids.fundo.remove_widget(self.ids.rc)
                        
                        self.ids.aviso_login.opacity = 0
                        self.ids.aviso_login.text = ''
                        self.ids.banne_aviso.opacity = 0
                        
                except:
                    ...
    
    def envia_conta(self):
        email = self.ids.emailC.text
        email = email.strip()
        if email and len(email) >= 5: 
            if email[-10:] == '@gmail.com':
                if email.count('@gmail.com') <= 1:
                    if internet():
                        try:
                            email= email.removesuffix('@gmail.com')
                            test=User.recuperar(self, email=email)
                            
                            self.ids.aviso_login.opacity=1
                            self.ids.aviso_login.text = test
                            self.ids.emailC.text = ''
                            self.ids.banne_aviso.opacity = 1
                            self.ids.banne_aviso.size = 450,55.0
                        except Exception as e:
                            aviso(self, aviso='Email não encontrado ou invalido!')
                    else:
                        aviso(self, aviso='Sem Rede!')
            else:
                aviso(self, aviso='Faltando (@gmail.com)')
        else:
            aviso(self, aviso='Email Invalido!')
            
            
    def registro_login(self):
           
        def filtro():
            proibidos = '#$%&*()-+=!"`} ?:;,/\|][{'
            #Filtro dos dados
            
            user = self.ids.usernameR.text.lower()
            password = self.ids.passwordR.text.lower()
            email = self.ids.emailR.text.lower()
            
            #checar se algo foi digitado nos TextInput e se sao validos
            if user and password and email:
                #removendo espaços nas laterais
                user = user.strip()
                password = password.strip()
                email = email.strip()
                
                #tamano dos caracteres
                min_user = len(user) > 4 
                min_password = len(password) >= 4
                min_email = len(email) > 4 
                if min_user and min_email and min_password:
                    #checar caracteres
                    u_p_e = user+password+email
                    for n in range(len(u_p_e)):
                        
                        if u_p_e[n] in proibidos:
                            if u_p_e[n] == ' ':
                                aviso(self,aviso=(f'Proibido usar: (ESPAÇOS)'))
                                return False
                            else:
                                aviso(self,aviso=(f'proibido usar: ({u_p_e[n]}'))
                                return False
                    
                    #verificar email valido
                    if email[-10:] == '@gmail.com':
                        if email.count("@gmail.com")>1:
                            aviso(self,aviso='Email Invalido')
                            return False
                        email = email.removesuffix('@gmail.com')
                        
                    else:
                        aviso(self,aviso='Faltor (@gmail.com)')
                        return False
                    
                    #Retorna verdade se passa pelos teste acima
                    return True
                else:
                    aviso(self,aviso='Minimo 4 Caracteres')
        
        #Verificar se Nome de usuario e email estao disponivel no baco de dados
        if filtro():
            #verificar se dados name e email nao estao em usor 
            user = self.ids.usernameR.text.lower()
            email = self.ids.emailR.text.lower()
            password=self.ids.passwordR.text.lower()
            password=password.strip()
            email = email.removesuffix('@gmail.com')
            if internet():
                verificar_base=User.verificar(self, name=user, email=email)
            
                if verificar_base == ('Email Indisponivel !'):
                    aviso(self,aviso=verificar_base)
                    return
                elif verificar_base == ('Usuario Indisponivel !'):
                    aviso(self,aviso=verificar_base)
                    return
                
                #envia dados e volta para layout login
                usuario=User(
                    user=user, password=password, email=email+'@gmail.com'
                )
                usuario.registrar()
                
                try:
                    if self.ids.rg not in self.children:
                        self.ids.fundo.add_widget(self.ids.lg)
                        self.ids.fundo.remove_widget(self.ids.rg)
                        self.ids.username.text=user
                        self.ids.userpassword.text=password

                except Exception as e:
                    print(f'Erro ao mostra Layout Login\n\t{e}')    
            else:
                aviso(self, aviso='Sem Rede!')
class Menu_bot(Screen):
    def fechar_tela(self):
        # Aqui você pode chamar o método `current` do ScreenManager para mudar de tela
        self.manager.current = 'Tela_Login'

class GerenciadorDeTelas(ScreenManager):
    pass

class kv_footApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Tela_Login(name='Tela_Login'))
        
        sm.add_widget(Menu_bot(name='Menu_bot'))
        return sm

if __name__ == '__main__':
    kv_footApp().run()




