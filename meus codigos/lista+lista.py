import time, os

dados = []
jon = []
on_of, password, login, i = True, None, None, 0


print(dados)
dados = [
    ['jon', '170922', ['araujo', 'aquino']],
    ['jerfinho', '1234', ['pinto', 'silva']],
    ['jennifer', '2004', ['santos', 'jesus']],
    ['adrian', '354072', ['miranda', 'araujo']]     
]

time.sleep(1)
while on_of:
    
    os.system('cls')
    #time.sleep(1)
    
    login = input('Login:\n\t') or None
   
    
   
   
    
    
    for i in range(len(dados)):
        if login == dados[i][0]:
            password = input('Senha:\n\t') or None
            
            if password == dados[i][1]:
                os.system('cls')
                print(f'\nSuceso no Login:\n\t{dados[i][0]}\n\t{dados[i][2]}')
                on_of = False
                break
            
            elif password != dados[i][1]:
                os.system('cls')
                print('Senha Incorreta\n')
                print(f'Login:\n\t{login}\n')
                password = input('Senha:\n\t') or None
                continue
                

                

                
        if login != dados[i][0] and password == None:
            print('Login Nao existir', end="\r")
            login = None
            time.sleep(1)
            continue
            
            
        