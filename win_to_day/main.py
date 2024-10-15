import user as us

client = us.User(
    user='adm',
    name='jonatas',
    last_name='araujo de aquino',
    phone='71984785356',
    email='jonatasaraujox9@gmail.com',
    age='27',
    password='admin13'
    )

logar = client.login()

print(logar)