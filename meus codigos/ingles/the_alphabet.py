"""Aprenda como devem ser pronunciadas o alfabeto da língua inglesa:
"""
import os


titulo = 'Aprenda como devem ser pronunciadas o alfabeto da língua inglesa:'

alphabet = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', \
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' 

speak_aphabet = 'ei', 'bi', 'ci', 'di', 'i', 'éf', 'dji', 'êicht', 'ai', 'djêi', 'key', 'él', 'ém', 'én', 'ou', \
'pi', 'quiu', 'ar', 'és', 'ti', 'iu', 'vi', 'dãbliu', 'équis', 'uai', 'zi'

atition = 'O "t" e o "d" são pronunciados de forma seca, ou seja, é parecido com o sotaque de alguém do interior.\n Não deve conter o chiado que há, \n por exemplo, em palavras como “tia”, que sai com o som “tchia”.\
A pronúncia do "m" e "n" não são tão diferentes da língua portuguesa.\n O que vai diferenciar, é a retirada do "e" no final de "eme" e "ene".'

fonologia = 'Fonologia\n O alfabeto em inglês é formado por cinco vogais e 21 consoantes.\n \
- Vogais: a, e, i, o, u. Entre as mais usada é a letra "e"\n \
- Consoantes: b, c, d, f, g, h, j, k, l, m, n, p, q, e, r, t, v, w, z. As menos usadas são "j, q, x, e z".'

def menu(f, t, w, l, h):
    
    
    
    
    os.system('cls')
    
    
    print(t, '\n\n' ,f, end='\n'*3)
    
    print(f'Acertos: {w}, Errados: {l}', end='\n'*2)

    print('Historico de Erros')
    for i in h:
        print(i)
    
    
    
    

def quest_alphabet(alpha, speak, f, t):
    win, loss = 0, 0
    lossed = []
    i = 0
    for letter in alpha:
        
        L = input(f'how speak the letter ({letter}) ?')
        
        if L == speak[i]:
            win+=1
            i+=1
            continue
        
        loss+=1        
        lossed.append(f'{alpha[i]} = {speak[i]} - {L} é ({(L==speak[i])}) ')
        i+=1
        print(lossed)
            
        menu(\
            f=f, t=t,\
            w=win, l=loss, h=lossed
        )
        
                      
quest_alphabet(\
    
    alpha=alphabet, speak=speak_aphabet, \
    t=titulo, f=fonologia
)