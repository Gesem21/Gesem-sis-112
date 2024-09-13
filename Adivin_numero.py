import random
print("-----ADIVINA EL NUMERO-----")
print("Selecciona la dificultad")
print("1. Facil (1-10)")
print("2. Medio (1-50)")
print("3. Dificil (1-100)")
op = int(input())
if (op==1):
    n = random.randint(1, 10)
    cont=0
    num=0
    print("Dame un numero")
    while num!=n:
        num = int(input())
        if(num<n):
            print("El numero es mas alto")
        elif(num>n):
            print("El numero es mas bajo")
        elif(num==n):
            print("Felicidades adivinaste el numero")
        cont+=1
    print(f"Hiciste {cont} intentos")
elif (op==2):
    n = random.randint(1, 50)
    cont=0
    num=0
    print("Dame un numero")
    while num!=n:
        num = int(input())
        if(num<n):
            print("El numero es mas alto")
        elif(num>n):
            print("El numero es mas bajo")
        elif(num==n):
            print("Felicidades adivinaste el numero")
        cont+=1
    print(f"Hiciste {cont} intentos")
elif (op==3):
    n = random.randint(1, 100)
    cont=0
    num=0
    print("Dame un numero")
    while num!=n:
        num = int(input())
        if(num<n):
            print("El numero es mas alto")
        elif(num>n):
            print("El numero es mas bajo")
        elif(num==n):
            print("Felicidades adivinaste el numero")
        cont+=1
    print(f"Hiciste {cont} intentos")
