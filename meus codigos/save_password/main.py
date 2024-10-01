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
#zera avisos
def none_av(av, t):
    """_summary_
    Args:
        av (indereço 'Label'): aviso que quero ocultar
        t (Number):  tempo para esperar pra chama a funcao zera
    """
    def zera(dt):
        av.text=''
    Clock.schedule_once(zera,t)

 
#Tentar Login
def login(L, S, contas, av_u, av_s):
    """_summary_

    Args:
        L (_String_): _Chave digitada pelo Usuario no Textinput Usuario na tela (Screen_Login)_
        S (_String_): _Valor digitado pelo Usuario no Textinput Senha na tela (Screen_Login)_
        contas (_Dict_): _Banco de dados de Usuarios_
        av_u (_indereço label_): _aviso de usuario (self.ids.aviso_user) na tela (Screen_Login)_
        av_s (_indereço label_): _aviso de senha (self.ids.aviso_senha) na tela (Screen_Login)_
        
    Returns:
        _Boolean_: _Retorna 'True' se Usuario digitado Existir no dict(contas)_
        _Boolean_: _Retorna 'False' se Usuario digitado Não existir ou a senha estiver 
    
    Funçãos:
        _Avisa com testo caso usuario não existir ou a senha estiver errada_
        _Chama função none_av() para zera os avisos pasando argumento aviso desejado eo tempo de espera_
    """
    
    #Verificar se Usuario existe
    if L in contas.keys():
        #verificar se a senha do user estar correta
        if S == contas[L]['senha']:
            av_u.text = f"..Logado.."
            return True
        else:
            av_s.text = 'Senha errada'
            none_av(av_s, t=2)
            return False
    else:
        av_u.text = 'Não Existe'
        none_av(av_u, t=2)
        return False

def registro(inputs, avisos):
    #teste compatibilidade
    def yes_no(campo, aviso, qt_carct, yes):
        
        campo.text = campo.text.strip()
        texto = campo.text.lower()
        menor = len(texto) > qt_carct[0]
        maior = len(texto) <= qt_carct[1]
        
        if menor and maior:
            n=0
            
            for caractere in texto:
                if caractere not in yes:
                    aviso.text = 'Invalide!'
                    campo.background_color = 'ffbdbd'
                    none_av(aviso, t=3)
                    return False
                #controlar uso de espaços
                elif caractere == ' ':
                    n+=1
                    if n > 2:
                        aviso.text = 'Invalide!'
                        campo.background_color = 'ffbdbd'
                        none_av(aviso, t=3)
                        n=0
                        return False
                else:
                    continue
            campo.background_color = 255, 255, 255, 255
            return True
        
        else:
            aviso.text = 'Invalide!'
            campo.background_color = 'ffbdbd'
            none_av(aviso, t=3)
    
    #chama yes_no() passando o campo e valores   
    def dados():       
        usuario = yes_no(
            campo=inputs['R_user'],
            aviso=avisos['av_R_user'],
            qt_carct=(5, 14),
            yes='abcdefghijklmnopqrstuvwxyz@._&0123456789'
            )
        Nome_completo = yes_no(
            campo=inputs['R_Ncompleto'],
            aviso=avisos['av_R_Ncompleto'],
            qt_carct=(13, 35),
            yes='abcdefghijklmnopqrstuvwxyz '
            )
        telefone = yes_no(
            campo=inputs['R_telefone'],
            aviso=avisos['av_R_telefone'],
            qt_carct=(10, 11),
            yes='0123456789'
            )
        email = yes_no(
            campo=inputs['R_email'],
            aviso=avisos['av_R_email'],
            qt_carct=(13, 50),
            yes='abcdefghijklmnopqrstuvwxyz@.-_&0123456789'
            )
        senha = yes_no(
            campo=inputs['R_senha'],
            aviso=avisos['av_R_senha'],
            qt_carct=(7, 8),
            yes='abcdefghijklmnopqrstuvwxyz.@0123456789'
            )
        pin = yes_no(
            campo=inputs['R_pin'],
            aviso=avisos['av_R_pin'],
            qt_carct=(3, 4),
            yes='0123456789'
            )
    
    return dados()

class Screen_Login(Screen):
     #Entrar:
    def bt_enter(self):
        usuario = self.ids.user
        senha = self.ids.password
        aviso_user = self.ids.aviso_user
        aviso_senha = self.ids.aviso_senha
               
        login(
            L=usuario.text.lower(),
            S=senha.text.lower(),
            contas=contas,
            av_u=aviso_user,
            av_s=aviso_senha,
            
            )    
    
    def bt_registrar(self):
        self.manager.current = 'Screen_Registre'
        
class Screen_Registre(Screen):
    
    def Back_Login(self):
        self.manager.current = 'Screen_Login'
    #Enviar cadastro
    def bt_R_continuar(self):
        #TextsInputs
        R_Inputs = {
            'R_user': self.ids.R_user,
            'R_Ncompleto': self.ids.R_Ncompleto,
            'R_telefone': self.ids.R_telefone,
            'R_email': self.ids.R_email,
            'R_senha': self.ids.R_senha,
            'R_pin': self.ids.R_pin,
        }
        #Label de avisos
        R_av = {
            'av_R_user': self.ids.av_R_user,
            'av_R_Ncompleto': self.ids.av_R_Ncompleto,
            'av_R_telefone': self.ids.av_R_telefone,
            'av_R_email': self.ids.av_R_email,
            'av_R_senha': self.ids.av_R_senha,
            'av_R_pin': self.ids.av_R_pin,
        }
        registro(inputs=R_Inputs, avisos=R_av)
        
       
               
class GerenciadorDeTelas(ScreenManager):
    pass

class Save_App(App):
    def build(self):
        return GerenciadorDeTelas()

# Run the application
if __name__ == "__main__":
    Save_App().run()


