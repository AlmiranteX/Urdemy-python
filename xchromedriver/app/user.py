import json, requests

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
    
    
