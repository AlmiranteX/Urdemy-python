"""_summary_
        O game assasino
        descubrar quem é o assasino
"""
import random, os
os.system('cls')
Players = {}

class Player:
    
    def __init__(self, nome, idade, genero, local):
        self.name = nome
        self.age = idade
        self.gender = genero
        self.location = local
        
    def about(self):
        print(
            f'Player: {self.name}\n',
            f'Idade: {self.age} {self.gender}\n',
            f'Local: {self.location}\n'
            )
        
jonatas = Player('jonatas', 27, 'masculino', 'sala')

jonatas.about()
        
class Player_filho(Player):
    def __init__(self, nome, idade, genero, local, pai):
        super().__init__(nome, idade, genero, local)
        self.pai=pai

filha = Player_filho('Marya', 1, 'feminino', 'sala', jonatas.name)

filha.about()
print('Filha de',filha.pai)
         
        
        