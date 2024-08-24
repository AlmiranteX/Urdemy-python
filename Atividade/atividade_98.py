"""
Atividade 98 Verificar CPF 
"""

cpf = '746.824.890-70'

mult = 10
registro = []
soma = []
resultado_soma = 0

def algoritimo_cpf():
    







for i in cpf:
    
    if i == '.':
        continue
    if i == '-':
        break
    registro.append(int(i))
 
    
for i in range(9):
      
    x = registro[i] * mult
    soma.append(x)
    print(f"{registro[i]}' X '{mult} = {x}")
    mult -= 1


resultado_soma = sum(soma)
    
resultado_soma = resultado_soma * 10

resultado = (resultado_soma % 11)

if resultado > 9:
    resultado = 0

print(resultado, (resultado == int(cpf[-2])))

  
        
    