"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

nasceu, atual = 1997, 2024

print(f"Estar no ano: {atual} nasceu no ano: {nasceu}")

def idade(*idade):
    return idade[1] - idade[0]

ano = idade(nasceu, atual)

print(f"Com idade: {ano}")
