"""
Atividade 98 Verificar CPF 
"""

cpf = '746.824.890-70'

mult = 10
registro = []
soma = []
resultado_soma = 0


for i in cpf:
    
    if i == '.':
        continue
    if i == '-':
        break
    registro.append(int(i))
    #print(registro)
    
for i in range(9):
      
    x = registro[i] * mult
    soma.append(x)
    print(f"{registro[i]}' X '{mult} = {x}")
    mult -= 1

for a in range(len(soma)):
    resultado_soma += soma[a]
    
resultado_soma = resultado_soma * 10

resultado = (resultado_soma % 11)

if resultado > 9:
    resultado = 0

print(resultado, (resultado == registro[0]))
        
        
    