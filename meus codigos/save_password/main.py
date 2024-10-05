from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.config import Config
from kivy.clock import Clock
import requests, json
import random, os


# Define o tamanho da janela antes de carregar o App
Config.set('graphics', 'width', '320')
Config.set('graphics', 'heigth', '480')

#baco de dados
banco_dados= ('https://dia-de-pix-default-rtdb.firebaseio.com/usuarios.json')

   
#zera avisos
def none_av(av, t):
    """_summary_
    Args:
        av: (indereço 'Label'): aviso que quero ocultar
        t: (Number):  tempo de esperar pra chama a funcao zera
    Function:
        chama a funçao zera() para Define valor '' a um elemento (av) apos um certo intervalo (t) 
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
        _Boolean_: _Retorna 'True' se Usuario digitado Existir no banco de dados (Users)_
        _Boolean_: _Retorna 'False' se Usuario digitado Não existir ou a senha estiver errada_
    
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

#verificar dados de registro
def registro(inputs, avisos, bt, bc):
    """_summary_

    Args:
        inputs (_dict_): _Dicionario com elementos Textinputs da tela (screen_registre)_
        avisos (_dict_): _Dicionario com elementos Label da tela (screen_registre)_
        bt (_indereço button_): _Elemento Button (Continuar) da tela (screen_registre)_

    Returns:
        _Boolean_:  Retorna a Função dados() com valor True ou False 
    
    Funçãos:
        _Retorna a função dados() que trabalhar chamando a funcão yes_no()
    """
    def verify_flags():

            if inputs['R_user'].text.lower() in bc['usuarios']:
                inputs['R_user'].background_color='ffbdbd'
                avisos['av_R_user'].text = 'Em uso!'
                bt.disabled = True
                return False
            if inputs['R_Ncompleto'].text.lower() in bc['Ncompletos']:
                inputs['R_Ncompleto'].background_color='ffbdbd'
                avisos['av_R_Ncompleto'].text = 'Em uso!'
                bt.disabled = True
                return False
            if inputs['R_email'].text.lower() in bc['emails']:
                inputs['R_email'].background_color='ffbdbd'
                avisos['av_R_email'].text = 'Em uso!'
                bt.disabled = True
                return False
            if inputs['R_telefone'].text.lower() in bc['telefones']:
                inputs['R_telefone'].background_color='ffbdbd'
                avisos['av_R_telefone'].text = 'Em uso!'
                bt.disabled = True
                return False
            
            return True
       
    #teste de dados permitiveis
    def yes_no(campo, aviso, qt_carct, yes):
        """_summary_

        Args:
            campo (_indereço Textinput_): _Indereço do elemento Textinput da tela (screen_registre)_
            aviso (_indereço Label_): _Indereço do elemento Label (usado para aviso sobre o campo) da tela (screen_registre)_
            qt_carct (_Tuple_): _Tuple com 2 valores, 1°valor para quantidade minima, 2°valor para quantidade maxima\
                para controlar quantidade de strings dentro do Textinput da tela (screen_registre)_
            yes (_Strings_): _Strings com caracteres permitidos usar no Textinput determinado da tela (screen_registre)_

        Returns:
            _Boolean_: _Retorna True ou False dentro da variavel solicitada dentro da função dados()_
        """
        
        #exceçao Nome completo
        if campo != inputs['R_Ncompleto']:
            campo.text = campo.text.strip()
        else:
            campo.text = campo.text.lstrip()
            
        texto = campo.text.lower()
        menor = len(texto) > qt_carct[0]
        maior = len(texto) <= qt_carct[1]
        
        #excesão para o textinput email
        if campo == inputs['R_email']:
        
            if texto[-10:] =='@gmail.com':
                pass
            else:
                inputs['R_email'].background_color= 'ffbdbd'
                avisos['av_R_email'].text = 'Invalide!'
                bt.disabled = True
                return False
        #................................._Fim_excesões_
        
        if menor and maior:
            n=0
            
            for caractere in texto:
                
                if caractere not in yes:
                    aviso.text = 'Invalide!'
                    campo.background_color = 'ffbdbd'
                    bt.disabled = True
                    return False
                #controlar uso de espaços
                elif caractere == ' ':
                    n+=1
                    if n > 2 and campo != inputs['R_Ncompleto']:
                        aviso.text = 'Invalide!'
                        campo.background_color = 'ffbdbd'
                        bt.disabled = True
                        n=0
                        return False
                    #excesão Nome completo
                    elif n > 3 and campo == inputs['R_Ncompleto']:
                        campo.text = campo.text.rstrip()
                        aviso.text = 'Invalide!'
                        campo.background_color = 'ffbdbd'
                        bt.disabled = True
                        n=0
                        return False
                else:
                    continue
            if verify_flags():   
                campo.background_color = 255, 255, 255, 255
                none_av(aviso, t=0)
                return True
            else:
                return False
        else:
            aviso.text = 'Invalide!'
            campo.background_color = 'ffbdbd'
            bt.disabled = True
            
    #chama yes_no() passando o campo e valores   
    def dados():
        """_summary_

        Returns:
            _Boolean_: _True ou False_
        Função:
            _Verificar se os dados inserito no compo textinput da tela (screen_registre) pelo usuario e validos _
        """
        usuario = yes_no(
            campo=inputs['R_user'],
            aviso=avisos['av_R_user'],
            qt_carct=(5, 14),
            yes='abcdefghijklmnopqrstuvwxyz@._&0123456789'
            )
        Nome_completo = yes_no(
            campo=inputs['R_Ncompleto'],
            aviso=avisos['av_R_Ncompleto'],
            qt_carct=(13, 60),
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
            yes="abcdefghijklmnopqrstuvwxyz@.-_&0123456789"
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

        if usuario and Nome_completo:
            if telefone and email:
                if senha and pin:
                    bt.disabled = False
                    return True
                   
                    
                
                    
    return dados()
    

class Screen_Login(Screen):
    #Entrar:
    def on_enter(self):
        os.system('cls')
    
        
    def bt_enter(self):
        usuario = self.ids.user
        senha = self.ids.password
        aviso_user = self.ids.aviso_user
        aviso_senha = self.ids.aviso_senha
        
        user= requests.get(banco_dados)
        conta= user.json()
        users={}
        for k, v in conta.items():
            users[k]={'senha': v['senha']}
        print(users)

         
        login(
            L=usuario.text.lower(),
            S=senha.text.lower(),
            contas=users,
            av_u=aviso_user,
            av_s=aviso_senha,

            )    
    
    def bt_registrar(self):
        self.manager.current = 'Screen_Registre'
    
            
class Screen_Registre(Screen):
    
        
    #Inicio tela cadastro
    def on_enter(self):
        os.system('cls')
        banco = {}
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
        R_bt_continue = self.ids.bt_continue
        
        #get usuarios dados       
        usuarios = requests.get('https://dia-de-pix-default-rtdb.firebaseio.com/dados/usuarios.json')
        banco['usuarios'] = usuarios.json()
        Ncompletos = requests.get('https://dia-de-pix-default-rtdb.firebaseio.com/dados/Ncompletos.json')
        banco['Ncompletos']= Ncompletos.json() 
        telefones = requests.get('https://dia-de-pix-default-rtdb.firebaseio.com/dados/telefones.json')
        banco['telefones'] = telefones.json()
        emails = requests.get('https://dia-de-pix-default-rtdb.firebaseio.com/dados/emails.json')
        banco['emails']= emails.json()
        
        def chama_cadastro(dt):
           return registro(inputs=R_Inputs, avisos=R_av, bt=R_bt_continue, bc=banco)
        Clock.schedule_interval(chama_cadastro, 0.5)
        
        
    def Back_Login(self):
        self.manager.current = 'Screen_Login'
    #Enviar cadastro
    def bt_R_continuar(self):
        #TextsInputs
        R_Inputs = {
            'R_user': self.ids.R_user.text.lower(),
            'R_Ncompleto': self.ids.R_Ncompleto.text.lower(),
            'R_telefone': self.ids.R_telefone.text.lower(),
            'R_email': self.ids.R_email.text.lower(),
            'R_senha': self.ids.R_senha.text.lower(),
            'R_pin': self.ids.R_pin.text.lower(),
        }
        novo_user = {
            'nome completo': R_Inputs['R_Ncompleto'],
            'telefone': R_Inputs['R_telefone'],
            'email': R_Inputs['R_email'],
            'senha': R_Inputs['R_senha'],
            'pin': R_Inputs['R_pin']  
        }
                      
        def send_dados():
            """_summary_
                Função:
                    Chava a função enviar_dados() para enviar o cadastro pra o banco de dados,
                    passa os dados nercessarios como argumentos (chave/valor/indereço)
            """
            def enviar_dados(chave, valor, cep):
                """_summary_

                Args:
                    chave (_chave do valor a ser armazendado_): _chave de acesso do valor ex: chave = 'jonatas': 'valor'_
                    valor (_valor para ser armazendado na chave_): _valor a ser armazendado ex: 'chave': valor= 'araujo'_
                    cep (_indereço de um dicionario no firebase Realtime_Database_): _'dados/usuarios'_
                Função:
                    Recebe os dados indereço/chave nos paramentros para enviar o valor para o banco de dados 
                """
                #condiçao para email
                if '@gmail.com' in chave:
                    chave = chave.removesuffix('@gmail.com')
                                   
                url = f'https://dia-de-pix-default-rtdb.firebaseio.com/{cep}/{chave}.json'
                response = requests.put(url, json=valor)
                return response.status_code
            
            #Criar usuario
            enviar_dados(
                R_Inputs['R_user'],
                novo_user,
                'usuarios'
                )
            #Criar dados do usuario
            cont = requests.get('https://dia-de-pix-default-rtdb.firebaseio.com/usuarios.json')
            cont = len(cont.json())
            
            #---usuarios
            enviar_dados(
                R_Inputs['R_user'],
                cont,
                'dados/usuarios'
                )
            #---Ncompletos
            enviar_dados(
                R_Inputs['R_Ncompleto'],
                R_Inputs['R_user'],
                'dados/Ncompletos'
            )
            #---emails
            enviar_dados(
                R_Inputs['R_email'],
                R_Inputs['R_user'],
                'dados/emails'
            )
            #---telefones
            enviar_dados(
                R_Inputs['R_telefone'],
                R_Inputs['R_user'],
                'dados/telefones'
            )

            return True
        
        resposta = send_dados()
        if resposta:
            self.manager.current = 'Screen_Login'
            
class GerenciadorDeTelas(ScreenManager):
    pass

class Save_App(App):
    def build(self):
        return GerenciadorDeTelas()

# Run the application
if __name__ == "__main__":
    Save_App().run()


