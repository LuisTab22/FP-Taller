# E.Selectivas.4.Multiple
# Determinar si un número es mayor que 32

numero = int(input("Ingrese cualquier número: "))
if numero > 32:
    print ("El número "+ str(numero) + " es mayor que el 32")
elif numero == 32:
    print ("El número es igual a 32")
elif numero == 0:
    print ("El número es igual a 0")
else:
    print ("El número " + str(numero) + " es menor que el 32")
    