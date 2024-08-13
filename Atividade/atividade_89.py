""" 
Atividade lista de compras 
"""
import os, time

compras = []
qtd_itens = 0
iten = None
aviso = None

# Função adicionar novo item a lista de compras
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
       





    return escolha








menu()

