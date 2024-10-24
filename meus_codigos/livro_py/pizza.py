import os
os.system('cls')
def apaga():
    os.system('cls')
    
def make_pizza(pizzas, sizer=12, adiconais={}):
    if pizzas:
        print(f'Pizza: tamanho {sizer}')
        for piza in pizzas:
            print(f'\n\tSabor _{piza}_')
            
            if piza in adiconais.keys():
                for ad in adiconais[piza]:
                    print(f'\t\t-{ad}')
                    
    else:
        print(f'please enter the flavor of the pizza')

""" 
make_pizza(
    pizzas=['four_queijos', 'calabresa', 'carne'],
    sizer=24,
    four_queijos=['pimenta', 'cebola'],
    carne=['tomate', 'pimentao', 'quento'],
    
)
"""