#E.REPETITIVA.WHILE.5
#SUMA DE NUMEROS NATURALES (Desde 0 hasta N)

#Definimos el valor máximo
num = int(input("Ingrese un númeor entero:"))

suma = 0
contador = 0

#Asignamos cuando el ciclo se acabara con la variable previamente escrita
while contador <= num:
    suma += contador
    contador += 1
    
    #Con el contador en 0, podemos empezar a guardar valores que se iran sumando posteriormente

print("La suma de los ",num, "los numeros naturales es ",suma)
