import pizza
from pizza import apaga as deleta

while True:
    deleta()
    try:
        tamnha_pizza = int(input('Boa Noite!\nQual o tamnanho da pizza ?'))
        break
    except:
        print('Tamnho em numero ex: 12')
        continue
    
ad_sabores=[]
ad_adicionais= {}
ad_ad=[]

for n in range(4):
    deleta()
    print('Escolha 4 sabopres:')
    sabor=input(f'\tSabor {n}:')
    sabor=sabor.strip()
    ad_sabores.append(sabor)
    ad_ad=[]
    while True:
        deleta()
        resp=input(f'colocar adicionais em {sabor} s/n')
        if resp=='s':
            deleta()
            ad = input('Digite o adicional desejado:')
            ad_ad.append(ad.strip())
            
        elif resp == 'n':
            ad_adicionais[sabor] = ad_ad
            break

pizza.make_pizza(
    sizer=tamnha_pizza,
    pizzas=ad_sabores,
    adiconais=ad_adicionais
    )