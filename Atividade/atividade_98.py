"""
Atividade 98 Verificar CPF 
"""

cpf = '746.824.890-70'


def second_algoritimo(REgistro):
    
    mult = 11
    resultado_soma = 0

    for i in range(9):
      
        x = REgistro[i] * mult
        soma.append(x)
        print(f"{REgistro[i]}' X '{mult} = {x}")
        mult -= 1
    
    resultado_soma = sum(soma)
        
    resultado_soma = resultado_soma * 10

    resultado = (resultado_soma % 11)
    
    if resultado > 9:
        resultado = 0
 
        
    if resultado == (int(cpf[-2]):)    
         
        print(f"O digito: {resultado} é {resultado == int(cpf[-2])}")
        REgitro.append(resultado)
        print(REgistro)
        
    else:
        print(f"O digito: {resultado} é {resultado == int(cpf[-2])}")
    


def first_algoritimo(registro):
    """_summary_
        A funçao "first_algoritimo()" foi criada para validar o 1° digito do cpf.
        a validação do digito e feita por meios de calculos baseado no algoritimo do cpf.
    """
    mult = 10
    resultado_soma = 0
    
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
 
        
    if resultado == (int(cpf[-2]):)    
         
        print(f"O digito: {resultado} é {resultado == int(cpf[-2])}")
        regitro.append(resultado)
        print(registro)
        second_algoritimo(registro)
    else:
        print(f"O digito: {resultado} é {resultado == int(cpf[-2])}")
    
    
        
for i in cpf:
    
    if i == '.':
        continue
    if i == '-':
        break
    Registro.append(int(i))

first_algoritimo(Registro)
 
    






  
        
    