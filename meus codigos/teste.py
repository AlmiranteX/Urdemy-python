"""
List:
    metodo wrapper.
    Caso queria criar uma list Numerica e possivel usar um for com um range() dentro para adcionar numeros na lista.
    caso o numero adicionado a lista precise ser do type string e possivel converte no momento da adção do numero na lista.
Clousures:
    funçoes que retornan uma função.
    
"""
def saudar(nome=''):
    def funcao():
        return f'Bom dia! {nome}'
    return funcao()



print(saudar('jonatas').title(), 'araujo')
i = 1

pizza3 = [str(i) for i in range(3, 37, 3)]
pizza2 = [str(i) for i in range(2, 36, 3)]
pizza1 = [str(i) for i in range(1, 35, 3)]

print(
    pizza3, '\n', pizza2, '\n', pizza1
)