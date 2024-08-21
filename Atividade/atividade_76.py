"""
Atividades do jogo da palavra secreta!
"""



import os
def deleta():
    os.system('clear')


Palavra_secreta = ['m', 'a', 's', 's', 'a', ' ', 'o', 's', 's', 'i', 'a']
palavra_trancada = ['*', '*', '*', '*', '*', ' ', '*', '*', '*', '*', '*']
i = 1
j = 1
alerta = ""
fras = ""

letra = ""
tente = 30

def cabeca():
    deleta()
    print(f"BEM VIDO AO GAME ADIVINHE A PALAVRA SECRETA -- {palavra_trancada} --")
    print('\n'*2)
    print(f"Tentativas restante: {(tente-i)}")


cabeca()

while i in range(1, 32):
    #caso acerta a palavra
    if Palavra_secreta == palavra_trancada:
        deleta()
        for d in range(0, 11):
            fras+=Palavra_secreta[d]
            alerta = f" Parabenz por indentificar a frase ({fras}) Fim do game"
        print(alerta)
        exit()

    
         

    #letra digitada
    letra = input(f"({i}x) Adivinhe uma letra: ").lower()
    if letra == "" or letra == None:
       i+= -1
       cabeca()


       


    #se ouver apenas 1x letra no texto igual a digitada 
    if Palavra_secreta.count(letra) == 1:
       
        local = Palavra_secreta.index(letra)
        palavra_trancada[local] = letra
        cabeca()
        print(Palavra_secreta.count(letra))
        
    #se a letra digitada se repetir mais de 1x no texto secreto    
    if Palavra_secreta.count(letra) > 1:
            
            print("maior")
            for j in range(9):
                            
                local = Palavra_secreta.index(letra, j)
                palavra_trancada[local] = letra
                j+=1
                cabeca()
                

    i+=1

    #se as tentativas se esgota
    if i == 31:
        deleta()
        for d in range(0, 11):
            fras += Palavra_secreta[d]
            alerta = f"que pena voce nao acerto a frase ({fras}) Fim do game"
            
        print(alerta)
        exit()
    cabeca()




