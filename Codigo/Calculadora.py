print("Bienvenido a la calculadora")
def numeros():
    n1 = int(input("Dame un numero: "))
    n2 = int(input("Dame otro numero: "))
    return n1,n2
def suma(n1,n2):
    print(n1+n2)
def resta(n1,n2):
    print(n1-n2)
def multi(n1,n2):
    print(n1*n2)
def division(n1,n2):
    print(n1/n2)
def resultado():
    print("Escoge laoperacion")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    opcion=input()
    if opcion==1:
        suma()
    elif opcion==2:
        resta()
    elif opcion==3:
        multi()
    elif opcion==4:
        division()

numeros()
resultado()