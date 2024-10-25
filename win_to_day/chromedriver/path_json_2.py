from pathlib import Path
import json

def get_name_user(path):
    name=input("what's your name ?")
    username = json.dumps(name)
    path.write_text(username)
    return name

def hello_name(path):
    
    if path.exists():
        name = path.read_text()
        username = json.loads(name)
        print(f"hello welcome {username}")
        return name
    else:
        name = get_name_user(path)
        print(f"Seja bem vindo ao programa {name}\nSalvamos o seu nome para quando voltar eu me lenbrar")
        return name
    
path=Path('win_to_day/chromedriver/name.json')
hello_name(path)