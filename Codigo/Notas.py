lista=[],[]
while True:
    print("Que desea anadir")
    print("1.Nombre")
    print("2.Nota")
    print("3.Imprimir datos")
    print("4.Salir")
    op=int(input("Ingrese el nombre: "))
    if(op==1):
        nombre=input()
        lista[0].append(nombre)
    elif op==2:
        nota=int(input("Ingrese la nota: "))
        lista[1].append(nota)
    elif op==3:
        print(lista)
    else:
        break
