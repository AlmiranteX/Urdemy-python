
class User:
    def __init__(self, **atributos):
        self.user=atributos['user']
        self.name=atributos['name']
        self.last_name=atributos['last_name']
        self.phone=atributos['phone']
        self.email=atributos['email']
        self.age=atributos['age']
    





client = User(
    user='almirante',
    name='jonatas',
    last_name='araujo de aquino',
    phone='71984785356',
    email='jonatasaraujox9@gmail.com',
    age='27'
    )

print(client.user)