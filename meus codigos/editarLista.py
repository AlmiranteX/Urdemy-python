import os
os.system('cls')


lista =  ['jonatas', 'araujo', 'aquino']

def editList(e, n, t):

    if type(n) == int:

        size_text = len(e)
        text = ""

        for i in range(size_text):
                
            if i == n:
                text += t
                i += 1
                continue

            else:
                text += e[i]
                i += 1
                
        return text
            
    else:
        print('\nA Referencia esta incorreta ex: lista[1] = editList(lista[1], 2, "texto") ')
        exit()
        

lista[1] = editList(lista[1], 2, "w")

print(lista)
