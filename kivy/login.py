users ={
    'jonatas': {
        'password': 19972024,
        'idade': 27,
        'sexo': 'M',
        'fihos': 1,
        'casado': 'sim',
    },
    'jennifer': {
        'password': 20042024,
        'idade': 20,
        'sexo': 'F',
        'fihos': 1,
        'casado': 'sim',
    },
    }

def usuarios(users):
    
    user = input('Usuario\n\t: ') or None
    
    if user.lower() in users.keys():
        senha = input('Senha\n\t: ') or None
        print(end='\n')
        user = users[user.lower()]
        
        if int(senha) == user['password']:
            
           for dados, valo in user.items():
               if dados == 'password':
                   continue
               print(f'{dados}: {valo}')
               
usuarios(users)
            



