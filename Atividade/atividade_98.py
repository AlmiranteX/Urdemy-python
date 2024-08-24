""" 23/08/24
Atividade 98 Verificar CPF 
"""

cpf = '088.171.959-65'
registro = []

def second_algoritimo(REgistro):
        
    print(REgistro)
    
    mult = 10
    resultado_soma = 0
    soma = []
    resultado = 0

    """_summary_
        A funçao "second_algoritimo()" foi criada para validar o 2° digito do cpf.
        a validação do digito e feita por meios de calculos baseado no algoritimo do cpf.
    """
   

        
    for i in range(len(REgistro)):
        
            x = REgistro[i] * mult
            soma.append(x)
            print(f"{REgistro[i]}' X '{mult} = {x}")
            mult -= 1

    resultado_soma = sum(soma)
    
    resultado = (resultado_soma % len(REgistro))
    print(f"{resultado_soma} % 11 :resta {resultado}")
    
    
    if resultado > 9:
           resultado = 0
        
   
        
    if resultado == int(cpf[-1]):    
          
            
            print(f"O digito: {resultado} é {resultado == int(cpf[-1])}")
            registro.append(resultado)
            print(registro)
           
    else:
            registro.append(resultado)
       
            print(f"O digito: {resultado} é {resultado == int(cpf[-2])}")
            print(registro)
            
for i in cpf:
    
    if i == '.':
        continue
    if i == '-':
        break
    registro.append(int(i))

def first_algoritimo():
    """_summary_
            A funçao "first_algoritimo()" foi criada para validar o 1° digito do cpf.
            a validação do digito e feita por meios de calculos baseado no algoritimo do cpf.
    """
    mult = 10
    resultado_soma = 0
    soma = []

        
    for i in range(len(registro)):
        
            x = registro[i] * mult
            soma.append(x)
            print(f"{registro[i]}' X '{mult} = {x}")
            mult -= 1

    resultado_soma = sum(soma)


        
    resultado = (resultado_soma % 11)

    if resultado > 9:
          resultado = 0

        
    if resultado == int(cpf[-2]):    
        
            
            print(f"O digito: {resultado} é {resultado == int(cpf[-2])}")
            registro.append(resultado)
        
            second_algoritimo(registro)
    else:
            registro.append(resultado)
        
            print(f"O digito: {resultado} é {resultado == int(cpf[-2])}")
           
first_algoritimo()