import random
lista=['brasil', 'mexico', 'italia', 'suecia']
pala=random.choice(lista)
lis=[]
for i in range(0,6):
    lis.append(pala[i])
print("ADIVINA LA PALABRA")
print(f"Adivina la palabra dentro de estas opciones")
print(lista)
print("1. Empezar")
print("2. Salir")
op= int(input())
if (op==1):
    juego= ['_','_','_','_','_','_']
    vidas = 8
    while (juego!=lis):
        print("Dame una letra")
        letra= input('')
        if (vidas!=0):
            if (letra in pala):
                indice = pala.index(letra)
                juego[indice] = letra
                marca = "".join(juego) 
                print(marca)
                vidas -=1
                print(f"Te quedan {vidas} vidas")
            else:
                marca = "".join(juego) 
                print(marca)
                vidas -=1
                print(f"Te quedan {vidas} vidas")
        else:
            break
            print("Te quedaste sin vidas")
    print("Adivinaste la palabra")
    print(f"Te sobraron {vidas} vidas")
else:
    print("Saliste")
