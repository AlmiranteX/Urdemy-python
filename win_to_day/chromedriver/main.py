from pathlib import Path
import json
def escrever_ler_txt():
    """_Sumary_
        - Escrever texto em um arquivo txt e ler o conteudo do arquivo
        __read_text() = Ler o texto dentro do arquivo txt
        __write_text() = Escreve textos dentro do arquivo txt
    """
    path = Path('menu.txt')
    content= path.write_text('bom dia jonatas')
    lendo = path.read_text()
    print(lendo)
  
def ler(path):
    import os
    os.system('cls')
    
    testo = path.read_text()
    name = json.loads(testo)

    for chave, valor in name.items():
        
        print(chave, valor)
    
def escrever_ler_json():
    listar = {'name':'jonatas', 'last':'araujo', 'ultimo':'aquino'}
    
    path = Path('win_to_day\chromedriver\memory.json')
    content = json.dumps(listar)
    path.write_text(content)
    
    ler(path)
escrever_ler_json()