"""
atividade multiplicar valores numa def com parametros
nao nomeados

e verificar se o resultado e impa ou par    
"""
num = (1, 2, 3, 4, 5)

def multiplicar(*numeros):
<<<<<<< HEAD
    
    n = 1

    for i in numeros:
        n *= i
=======
    n = numeros[0]

    for i in range(len(numeros)):
        n = n*int(numeros[i])
>>>>>>> 91eb3c4c0cdea5802e0b82d6387014939f9ac2d2
        print(n)

    v = ("par")if int(n) % 2 == 0 else "impar"
    
    return v, n
    
resul = multiplicar(*num)

print(*resul)