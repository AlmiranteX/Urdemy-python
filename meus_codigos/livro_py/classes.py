
class Player:
    
    def __init__(self, nome='João', sexo='Masculino', idade=6):
        self.nome=nome
        self.sexo=sexo
        self.idade=idade
    
    def correr(self):
        return f'{self.nome} Correndo...'
    
    def about(self):
        sobre = f'Player: {self.nome}, idade: {self.idade}, Genero: {self.sexo}'
        return sobre
    
jogador_padrao = Player()

print(jogador_padrao.about())

jogador_jonatas = Player(nome='Jonatas', idade=27)

print(jogador_jonatas.about())

print(jogador_jonatas.nome)

def gamer(**kwargs):
    
    for k, v in kwargs.items():
        print(f'{k}: {v},')


valor = gamer(jonatas='araujo', jennifer='santos', adrian='miranda')
