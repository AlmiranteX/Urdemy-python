#operaçao ternaria
import os
os.system('clear')


a, b, c = False, False, False

resultado = "Valor (A)" if a else "Valor (B)" if b else "Valor (c)" if c else 'Nenhum valor'

print(resultado, end='\n'*2)
