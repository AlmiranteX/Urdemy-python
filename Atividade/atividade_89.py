""" 
Atividade lista de compras 
"""
import os, time

compras = ['pao', 'arros']
qtd_itens = 0
iten = None
aviso = None

# Função adicionar novo item a Lista de compras.
def adicionar_iten():

        global aviso, iten, compras
        iten = None

        os.system('clear')

        #verificar e notificar se ouver um erro
        if aviso == None:
            ...
        else:
            print(aviso)
            aviso = None
       
        while iten != 'sair':

            iten = input('\nAdicionar iten a lista de compras\n\nNome do iten ou (sair) : ') or None

            #verificar se foi nada foi digitado ou digito digitado.
            if iten == None:
                    aviso = '[Erro], Nada digitado!'
                    adicionar_iten()
            elif iten != None:
                    for i in range(len(iten)):
                        if iten[i].isdigit():
                        
                            aviso = '[Erro],proibido Nome com digito'
                            adicionar_iten()
                            
                #verificar se o nome tem o tamanho adequado
            
            #verificar se o nome tem o tamanho adequado.
            if len(iten) < 3:    
                aviso = 'O nome digitado e muito curto'
                adicionar_iten()
            elif len(iten) > 15:
                    aviso = 'O nome digitado e muito longo'
                    adicionar_iten()

            #verificar se o iten ja existir na lista
            if iten in compras:
                aviso = 'Este iten ja esta em sua lista !'
                adicionar_iten()

            #sair
            if iten == 'sair':
                menu()

            #Nome valido adicionar a lista de compras
            else:
                os.system('clear')
                compras.append(iten) 
                print(f'({iten}) adicionado\n{len(compras)} itens em sua lista')
# Função apaga itens da Lista de compras.
def apaga_itens():
    os.system('clear')
    print('-- Apaga itens da lista de compras --\n\n-- Digite [S] para voltar --\n')
    escolha = None

    for indice, nome in enumerate(compras):
        print(indice, nome)

    while escolha != 's':
        
        if len(compras) <= 0:
            menu()

        escolha = input('\nDigite o indice do item a ser apagado ') or None
        qtd_itens = len(compras)

        #se digitado um digito correto
        if escolha.isdigit():
            escolha = int(escolha)

            if escolha > qtd_itens or escolha < 0:
                os.system('clear')
                print('Este indice não existe !')
                time.sleep(2)
                apaga_itens()
            else:
                try:
                    compras.pop(escolha)
                    apaga_itens()
                except:
                    os.system('clea')
                    print('Este indice não existe !')
                    time.sleep(2)
                    apaga_itens()
                                

        #se digitado outra coisa ou nada
        else:
            if escolha == 's':
                menu()
            else:
                os.system('clear')
                print('Digite um indice correspondente ao item !')
                time.sleep(2)
                apaga_itens()
# Função Editar item da Lista de compras.    
def edita_itens():
    global aviso, iten, compras
    iten = None 

    os.system('clear')

    #verificar e notificar se ouver um erro
    if aviso == None:
        ...
    else:
        print(aviso)
        aviso = None
       

    print('-- Edite itens selecionando pelo indice: --\n-  Digite [s] para voltar  -\n')

    for indice, nome in enumerate(compras):
        print(indice, nome)
    
    escolha = input('\nDigite o indice do item para editar: ')

    try:
        
        escolha = int(escolha)

        os.system('clear')
        print(f'Editando o iten ({compras[escolha]}):\n')

        

        while iten != 's':

            iten = input('\nEditar: ') or None

            #verificar se foi nada foi digitado ou digito digitado.
            if iten == None:
                    aviso = '[Erro], Nada digitado!\n'
                    edita_itens()
            elif iten != None:
                    for i in range(len(iten)):
                        if iten[i].isdigit():
                        
                            aviso = '[Erro],proibido Nome com digito\n'
                            edita_itens()
                            
                #verificar se o nome tem o tamanho adequado
            
            #verificar se o nome tem o tamanho adequado.
            if len(iten) < 3:    
                aviso = 'O nome digitado e muito curto\n'
                edita_itens()
            elif len(iten) > 15:
                    aviso = 'O nome digitado e muito longo\n'
                    edita_itens()


            #verificar se o iten ja existir na lista
            if iten in compras:
                aviso = 'Este iten ja esta em sua lista !\n'
                edita_itens()

            

            else:
                aviso = ''
                compras[escolha] = iten
                edita_itens()
            

    except:
        #sair

        if escolha == 's':
            menu()
        os.system('clear')
        print('indice incorreto !')
        time.sleep(2)
        edita_itens()



def menu():
    os.system("clear")
    qtd_itens = len(compras)
    print(f"-- Listas de Compras --\n\nitens na lista: {qtd_itens}\n")
    print("Funçoẽs:")
    print("[0] Lista itens")
    print("[1] Adicionar itens")
    print("[2] Apaga itens")
    print("[3] Editar itens\n") 

    escolha =  input("Digite o N° da opção para selecionala: ") or None

    #Selecionado [0] Lista compras.
    if escolha == '0':

        #verificar se existe itens na compras e lista compras
        if qtd_itens != 0:
            os.system("clear")
            for indice, N_iten in enumerate(compras):
                print(indice, N_iten)
            input('\nAperte qualquer teclar para volta.')
            menu()
        else:
            os.system('clear')
            print("Sua Lista de compras estar vazia !!!\n\n")
            time.sleep(2)
            menu()

    #Selecionado [1] Adicionar itens.
    if escolha == '1':
        adicionar_iten()
    
    #Selecionado [2] Apaga itens
    if escolha == '2':
        if qtd_itens > 0:
            apaga_itens()
        else:
            os.system('clear')
            print('Nada para apaga, Lista vazia')
            time.sleep(2)
            menu()

    #Selecionado [3] Editar itens
    if escolha == '3':
        if qtd_itens > 0:
            edita_itens()
        else:
            os.system('clear')
            print('Nada para Editar, Lista vazia')
            time.sleep(2)
            menu()


    return escolha








menu()

