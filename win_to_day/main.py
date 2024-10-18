import user as us

client = us.User(
    user='AlmiranteX',
    name='jonata',
    last_name='araujo de aquino',
    phone='71984785356',
    email='jonatasaraujox9@gmail.com',
    age='27',
    password='Jts.1709'
    )

#logar = client.recuperar_conta(email='jonatasaraujox9@gmail.com')
logar = client.registre()
print(logar)