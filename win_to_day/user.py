import requests, json
from send_main import Send_password as sp

LINK=('https://dia-de-pix-default-rtdb.firebaseio.com')

class User:
    """_summary_
    _Função_:
        _class usada para gerar novos usuarios, fazer login e registro,recuperar contas.
    _Metodos_: 
        _login()_
        _registre()_
        _recupera_conta()_ 
    _Parametros_:
        _deve ser passado: (user='',name='',last_name='',phone='',email='',age='',password='') 
    """
    def __init__(self, **atributos):
        self.user=atributos['user']
        self.name=atributos['name']
        self.last_name=atributos['last_name']
        self.phone=atributos['phone']
        self.email=atributos['email']
        self.age=atributos['age']
        self.password=atributos['password']
    
    def login(self):
        """_summary_
        Returns:
            _type_: _boolean_ False or True.
        Funçao:
            _Checar usuario e a Senha do usuario e retorna um valor se corretos ou incorretos.
        """
        id_user = self.user
        id_password = self.password
        Users_userds = requests.get(f'{LINK}/dados/usuarios.json').json()
        
        if id_user in Users_userds.keys():
            password=requests.get(f'{LINK}/usuarios/{id_user}/senha.json').json()

            if id_password ==  password:
                return True
            return False
        return False

    def registre(self):
        """_summary_
        """
        def send():
            try:
                #---Registrar usuario---#
                url=(f'{LINK}/usuarios/{self.user}.json')
                dados={
                    'user':self.user,
                    'name':self.name,
                    'last_name':self.last_name,
                    'age':self.age,
                    'email':self.email,
                    'telefone':self.phone,
                    'password':self.password
                }
                response=requests.put(url, json=dados,)
                
                #registrar o user na pasta dados/usuarios
                url = (f'{LINK}/dados/usuarios/{self.user}.json')
                N_users=requests.get(f'{LINK}/dados/usuarios.json').json()
                response=requests.put(url, json=len(N_users))
                
                #registrar o user na pasta dados/Ncompletos
                url = (f'{LINK}/dados/Ncompletos/{self.name} {self.last_name}.json')
                response=requests.put(url, json=self.user)
                
                #registrar o user na pasta dados/emails
                email = self.email
                email = email.removesuffix('@gmail.com')
                url = (f'{LINK}/dados/emails/{email}.json')
                response=requests.put(url, json=self.user)
            
                #registrar o user na pasta dados/telefones
                url=(f'{LINK}/dados/telefones/{self.phone}.json')
                response=requests.put(url, json=self.user)
 
                return True
            except:
                return 'Erro de Envio..'

        def verific():
            dados = requests.get(f'{LINK}/dados.json').json()
            
            #verificar se dados nao existem
            if self.user not in dados['usuarios']:
                fullname = f'{self.name} {self.last_name}'
                if fullname not in dados['Ncompletos']:
                    if self.phone not in dados['telefones']:
                        email = self.email.removesuffix('@gmail.com')
                        if email not in dados['emails']:
                            usuarios = requests.get(f'{LINK}/usuarios.json').json()
                            usuarios = usuarios.keys()
                            if self.user not in usuarios:
                                send()
                                return True
            return False
        verific()
        
    def recuperar_conta(self, email):
        vmail = email.removesuffix('@gmail.com')
        
        usuario = requests.get(f'{LINK}/dados/emails/{vmail}.json').json()
        if usuario:
            senha = requests.get(f'{LINK}/usuarios/{usuario}/password.json').json()
            
            #envia argumentos nercessarios para enviar email
            destinatario = email
            assunto = "Win to Day"
            mensagem = f'Apos ler esse email o delete por segurança:\nUsuario: {usuario}\nSenha: {senha}'
        
            send = sp(destinatario, assunto, mensagem)
            return send
        return 'Email não registrado'