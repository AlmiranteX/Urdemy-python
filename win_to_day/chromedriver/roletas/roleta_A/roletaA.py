from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time, json
from pathlib import Path

def ler():
    path = Path('Numeros.json') 
    #lendo arquivo
    numero = path.read_text()
    num = json.loads(numero)
    num["status"] = "Esperando_Historico"
    return num

def status():
    ...
    
# Inicializa o WebDriver usando o Selenium Manager (compatível com o navegador Chrome, Firefox ou Edge)
driver = webdriver.Chrome()  # Selenium Manager lida com o download do driver

def Historico():
    def first():
        elemento = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[8]/div[2]/div[3]/div/div[1]/div"))
            )
        numero = elemento.text
        numero = numero.split()
        return numero
   
    return first()

def localizar():
    # Alterna para o primeiro iframe pelo índice (exemplo: primeiro iframe)
    WebDriverWait(driver, 20).until(
        EC.frame_to_be_available_and_switch_to_it(driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[1]/div/iframe"))
    )
    os.system('cls')
    print('Achei iframe 0')
    
    # Alterna para o primeiro iframe pelo índice (exemplo: primeiro iframe)
    WebDriverWait(driver, 20).until(
        EC.frame_to_be_available_and_switch_to_it(driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/iframe"))
    )
    print('Achei iframe 1')

def login():
    try:
        print('tentando Login..')
        user = driver.find_element(By.NAME, "username")
        user.send_keys("araujojonatasapc152018@gmail.com")
        senha = driver.find_element(By.NAME, "password")
        senha.send_keys("Jts.170922")
        senha.send_keys(Keys.ENTER)
    except Exception as e:
        print(f'Falha No Login\n\ttipo do Erro: {e}')
    localizar()

def navegar(url):
    # Acessa o Google
    driver.get(url)
    # Localiza o campo de pesquisa, insere o termo e pressiona Enter
    driver.implicitly_wait(20)
    login()
    
def  verificar(url):
    url_atual = driver.current_url
    if url_atual != url:
        navegar(url)
      
def arquivo(n):
    path = Path('Numeros.json') 
    def salvar():
        #armazenar numero
        if ler()["listaN"] != n:
            num = ler()
            num["listaN"] = n
            num["status"] = "ON"
            
            content = json.dumps(num)
            path.write_text(content)
            os.system('cls')
            print(f'{n}...Armazenado..')
        
    salvar()
        
try:
    
    link = "https://www.playpix.com/pb/live-casino/home/-1/All?openGames=40003094-real&gameNames=Roulette%20A"
    navegar(link)
    
    while True:
        verificar(link)
        try:
            
            numero = Historico()  
            arquivo(n=numero)
        
        except:
            os.system('cls')
            print('Esperando Historico...')
        
finally:
    pass   
    