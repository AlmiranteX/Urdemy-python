from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time, json
from pathlib import Path
from selenium.webdriver.chrome.options import Options



def ler():
    path = Path('xchromedriver/roletas/roleta_A/Numeros.json') 
    #lendo arquivo
    numero = path.read_text()
    num = json.loads(numero)
    num["status"] = "Esperando_Historico"
    return num

def status(stt):
    #lendo o dicionario Numeros.json
    dicionario = ler()
    dicionario["status"] = stt
    
    #atualizando o dicionario
    path = Path('xchromedriver/roletas/roleta_A/Numeros.json')
    content = json.dumps(dicionario, indent=4, ensure_ascii=False)
    path.write_text(content) 
    
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
    status('Coletando o (iframe 0)')
    
    # Alterna para o primeiro iframe pelo índice (exemplo: primeiro iframe)
    WebDriverWait(driver, 20).until(
        EC.frame_to_be_available_and_switch_to_it(driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/iframe"))
    )
    status('Coletando o (iframe 1)')

def login():
    try:
        conta = ler()
        status('Fazendo Login...')
        user = driver.find_element(By.NAME, "username")
        user.send_keys(conta["user"])
        senha = driver.find_element(By.NAME, "password")
        senha.send_keys(conta["senha"])
        senha.send_keys(Keys.ENTER)
    except Exception as e:
        status('Falha No Login!')
        
        
    localizar()

def navegar(url):
    
    # Acessa o Google
    status('Acessando o site...')
    driver.get(url)
    # Localiza o campo de pesquisa, insere o termo e pressiona Enter
    driver.implicitly_wait(20)
    login()
    
def  verificar(url):
    url_atual = driver.current_url
    if url_atual != url:
        status('Reiniciando...')
        navegar(url)
      
def arquivo(n):
    path = Path('xchromedriver/roletas/roleta_A/Numeros.json') 
    def salvar():
        #armazenar dicionario Numeros.json
        if ler()["listaN"] != n:
            num = ler()
            num["listaN"] = n
            num["status"] = "ON"
            num["meta"] += 1
            
            content = json.dumps(num, indent=4, ensure_ascii=False)
            path.write_text(content)
        
        
    salvar()
    
rl=0    
try:
    
    link = "https://www.playpix.com/pb/live-casino/home/-1/All?openGames=40003094-real&gameNames=Roulette%20A"
    navegar(link)
    
    while True:
        verificar(link)
        
        try:
            
            numero = Historico()  
            arquivo(n=numero)
            os.system('cls')
            print(numero)
            rl=0
           
        except:
            os.system('cls')
            print('Esperando (Historico)...')
            status('Esperando (Historico)..')
            rl+=1
            print(rl)
            
            if rl > 3:
                print(rl)
                driver.get(link)
                localizar()
                rl=0
        
finally:
    pass   
    