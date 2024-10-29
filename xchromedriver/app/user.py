import json, requests
from send_main import Send_password as sd

LINK = ('https://dia-de-pix-default-rtdb.firebaseio.com')

class User:
    def __init__(self, **atributos):
        self.user = atributos['user']
        self.password = atributos['password']
        self.email = atributos['email']
    
    def logar(self):
        """_summary_
            def: fazer requisição dos dados de usuarios e checar login
        """
        user = self.user
        password = self.password
        dados = requests.get(f'{LINK}/usuarios/{user}.json').json()
        
        if dados:
            if password == dados['password']:
                return True
            else:
                return False
    
    def registrar(self):
        form={
            'user':self.user,
            'password':self.password,
            'email':self.email
        }
        form2={
            'user':self.user,
            'password':self.password,
        }
        #criar usuario no fire-base
        url = f'{LINK}/usuarios/{self.user}.json'
        enviar = requests.put(url, json=form)
        #criar email do usuario no fire-base
        
        email=self.email.removesuffix('@gmail.com')
        url = f'{LINK}/emails/{email}.json'
        enviar2 =requests.put(url, json=form2) 
        
    def verificar(self,name,email):
        retorno = None
        names = requests.get(f'{LINK}/usuarios.json').json()
        emails = requests.get(f'{LINK}/emails.json').json()
        
        if name in names.keys():
            retorno=(f'Usuario Indisponivel !')
            return retorno
        elif email in emails.keys():
            retorno=(f'Email Indisponivel !')
            return retorno
        
        retorno = 'Disponivel'
        return retorno
    
    def recuperar(self, email):
        dados = requests.get(f'{LINK}/emails/{email}.json').json()
        print(dados)
        if dados:
            user = dados['user']
            password = dados['password']
            return sd(
                destinatario=email+'@gmail.com',
                assunto='Dia de Pix. Recuperar Login',
                mensagem=f"Usuario: {user}\nSenha: {password}"
                )
            
        return False