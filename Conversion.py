import Operaciones
def menu():
    print("------BIENVENIDO A LA CALCULADORA DE CONVERSIONES-------")
    print("1. Longitud")
    print("2. Masa")
    print("3. Temperatura")
    op=int(input("Selecciona una opcion: "))
    if (op==1):
        print("Conversion de m --> Km")
        n=float(input("Dame un numero en metros: "))
        print(f" Sale {Operaciones.longitud(n)} Km")
    elif (op==2):
        print("Conversion de g --> Kg")
        n=float(input("Dame un numero en gramos: "))
        print(f" Sale {Operaciones.masa(n)} Kg")
    elif (op==3):
        print("Conversion de °C --> °F")
        n=float(input("Dame un numero en Celsius: "))
        print(f" Sale {Operaciones.temp(n)} °F")
    else:
        return op
    
while True:
    menu()
    op=menu()
    if (op==4):
        break
