"""
Atividade 98 Verificar CPF 
"""

cpf = '746.824.890-70'

mult = 10
registro = []
soma = []
resultado_soma = 0

<<<<<<< HEAD
def algoritimo_cpf():
    







for i in cpf:
    
=======

for i in cpf:
    
>>>>>>> 5c42e0a9a22f74d053a26b050d6138f5dde97772
    if i == '.':
        continue
    if i == '-':
        break
    registro.append(int(i))
<<<<<<< HEAD
 
=======
    #print(registro)
>>>>>>> 5c42e0a9a22f74d053a26b050d6138f5dde97772
    
for i in range(9):
      
    x = registro[i] * mult
    soma.append(x)
    print(f"{registro[i]}' X '{mult} = {x}")
    mult -= 1

<<<<<<< HEAD

resultado_soma = sum(soma)
=======
for a in range(len(soma)):
    resultado_soma += soma[a]
>>>>>>> 5c42e0a9a22f74d053a26b050d6138f5dde97772
    
resultado_soma = resultado_soma * 10

resultado = (resultado_soma % 11)

if resultado > 9:
    resultado = 0

<<<<<<< HEAD
print(resultado, (resultado == int(cpf[-2])))

  
=======
print(resultado, (resultado == registro[0]))
        
>>>>>>> 5c42e0a9a22f74d053a26b050d6138f5dde97772
        
    