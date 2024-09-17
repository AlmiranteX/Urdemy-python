from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Inicializando o driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Acessando o Google
driver.get("https://www.google.com")

# Encontrando a caixa de pesquisa e realizando uma ação
search_box = driver.find_element(by=By.NAME, value="q")
search_box.send_keys("Asimov Academy")
search_box.submit()

# Fechando o navegador
driver.quit()

##
