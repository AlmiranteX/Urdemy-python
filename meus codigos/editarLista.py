import os
os.system('clear')




lista =  ['jonatas', 'araujo', 'aquino']

def editList(e, n, t):
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
        

lista[2] = editList(lista[2], 2, '0')



print(lista)







