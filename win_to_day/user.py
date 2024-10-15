import requests, json

link=('https://dia-de-pix-default-rtdb.firebaseio.com')

class User:
    """_summary_
    _Função_:
        _class usada para gerar novos usuarios, fazer login e registro,recuperar contas.
    _Metodos_: 
        _login()_
        _registre()_
        _recupera()_ 
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
        
        Users_userds = requests.get(f'{link}/dados/usuarios.json').json()
        
        if id_user in Users_userds.keys():
            password=requests.get(f'{link}/usuarios/{id_user}/senha.json').json()

            if id_password ==  password:
                return True
            return False
        
        return False
