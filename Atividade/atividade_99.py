#atividade gerar cpf valido
cpf = ''
digitar = ''
import os, random
def digito_2():
  
  #print(f'CPF: {cpf[:9]}-{cpf[9:]}')
  nove_digito = cpf[:10]
  contador_regressivo = 11
  resultado = 0
  
  
  
  for digito in nove_digito:
    resultado += int(digito) * contador_regressivo
    #print(f'{digito} X {contador_regressivo} = {int(digito)*contador_regressivo}')
    contador_regressivo -= 1
  
  
  #print('......')
  #print(f'Toral = {resultado}')
  
  check_1_digito = (resultado * 10) % 11
  check_1_digito = check_1_digito if check_1_digito <= 9 else 0
  
  #print(f'{resultado} x 10 = {(resultado*10)} % 11 = {(resultado*10)%11}')
  #print('......')
  
  
  if check_1_digito == int(cpf[-1]):
      #print(f'{cpf[:9]}-{cpf[9]}-{check_1_digito} << Verdadeiro')
      #print('.....')
      print(f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]} .....Este CPF e valido')
      
      
  elif check_1_digito != int(cpf[-1]):
      #print(f'{cpf[:10]}-{check_1_digito} << Falso')
      
      quest()
      
def digito_1():
  
  #print(f'CPF: {cpf[:9]}-{cpf[9:]}')
  nove_digito = cpf[:9]
  contador_regressivo = 10
  resultado = 0
  
  
  
  for digito in nove_digito:
    resultado += int(digito) * contador_regressivo
    #print(f'{digito} X {contador_regressivo} = {int(digito)*contador_regressivo}')
    contador_regressivo -= 1
  
  
  #print('......')
  #print(f'Toral = {resultado}')
  
  check_1_digito = (resultado * 10) % 11
  check_1_digito = check_1_digito if check_1_digito <= 9 else 0
  
  #print(f'{resultado} x 10 = {(resultado*10)} % 11 = {(resultado*10)%11}')
  #print('......')
  
  
  if check_1_digito == int(cpf[-2]):
      #(f'{cpf[:9]}-{check_1_digito} << Verdadeiro')
      digito_2()
      
  elif check_1_digito != int(cpf[-2]):
      #print(f'{cpf[:9]}-{cpf[9:]}...Este CPF e Falso')
      
      quest()

def quest():
  global cpf
  
  os.system('cls')
  
  cpf = ''
  digitar = ''
  
  
  for i in range(0, 9):
     cpf += str(random.randint(0, 9))
    
  for index in range(0, 2):
      digitar += str(random.randint(0, 9))
    
  cpf += digitar
  
 
  
  #os.system('cls()')
  digito_1()


quest()