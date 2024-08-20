String = input("Digite algo: ")

i = 0
letra_a = 0
win = None

while i < len(String):
    
    letra = String[i]

    if letra == "a":
        letra_a += 1

        
        win = True
    
    if letra != "a" and i == len(String):
        win = False
        print(win)
        

    i+=1

if win:
        
    la = str(letra_a)
    texto = " O texto (" + String + ") contem a letra (a) "
    print(texto + la + " vezes!" )

else:

    la = str(letra_a)
    texto = "O texto (" + String + ") Não contem a letra (a)  "
    print(texto)

