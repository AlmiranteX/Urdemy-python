"""
Atividades do jogo da palavra secreta!
"""

import os
def deleta():
    os.system('clear')


Palavra_secreta = ['m', 'a', 's', 's', 'a', ' ', 'o', 's', 's', 'i', 'a']
palavra_trancada = ['*', '*', '*', '*', '*', ' ', '*', '*', '*', '*', '*']
i = 1
j = 0
tente = 30
def cabeca():
    deleta()
    print(f"BEM VIDO AO GAME ADIVINHE A PALAVRA SECRETA -- {palavra_trancada} --")
    print('\n'*2)
    print(f"Tentativas restante: {(tente-i)}")


cabeca()

while i in range(1, 31):
    letra = input(f"({i}x) Adivinhe uma letra: ").lower()

    if Palavra_secreta.count(letra):
        if Palavra_secreta.count(letra) > 1:

            while j in range(Palavra_secreta.count(letra)):

                local = Palavra_secreta.index(letra)
                palavra_trancada[local] = letra


        else:
            local = Palavra_secreta.index(letra)
            palavra_trancada[local] = letra
            cabeca()
            print(Palavra_secreta.count(letra))
            break
        
        
        



    i+=1
    cabeca()