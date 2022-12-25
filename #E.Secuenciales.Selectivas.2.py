#E.Secuenciales.Selectiva.2
#El mayor entre 3 números

num1 = float (input("Ingrese el primer número: "))
num2 = float (input("Ingrese el segundo número: "))
num3 = float (input("Ingrese el tercer número: "))

if num1 > num2 and num1 > num3:
    print (num1, " es mayor")
elif num2 > num3 and num2 > num1:
    print (num2, " es mayor")
else:
    print(num3, " es mayor")
    