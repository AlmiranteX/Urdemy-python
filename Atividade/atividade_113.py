"""
atividade multiplicar valores numa def com parametros
nao nomeados

e verificar se o resultado e impa ou par    
"""
num = (1, 2, 3, 4, 5)

def multiplicar(*numeros):
    
    n = 1

    for i in numeros:
        n *= i
        pi = "par" if n % 2 == 0 else "impa"
        print(f'{n}--{pi}')

    v = ("par")if int(n) % 2 == 0 else "impar"
    
    return v, n
    
resul = multiplicar(*num)
