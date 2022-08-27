suma = 0
resta = 0
mult = 0
num1 = int(input("Digite el numero 1: "))
num2 = int(input("Digite el numero 2: "))
menu = int(input("Elija una opcion\n1-Mostrar la suma de los dos numeros\n2-Mostrar la resta de los dos numeros\n3-Mostrar la multiplicacion de los dos numeros\n"))
if menu == 1:
    suma = num1 + num2
    print(f"El resultado de la suma es de {suma}")
    print(f"{num1} + {num2} = {suma}")

elif menu == 2:
    resta = num1 - num2
    print(f"El resultado de la resta es de {resta}")
    print(f"{num1} - {num2} = {resta}")

elif menu == 3:
    mult = num1 * num2
    print(f"El resultado de la multiplicacion es de {mult}")
    print(f"{num1} x {num2} = {mult}")

else:
    print("Digite una opcion Valida.")