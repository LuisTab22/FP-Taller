#E.REPETITIVA.WHILE.2
#SUMA DE NUMEROS PARES

#Introducimos el rango de los números a analizar
num_inicial = int(input("Introduce el número inicial:"))
num_final = int(input("Introduce el número final:"))

cantidad = 0 #Definimos nuestro CONTADOR de datos

while num_inicial < num_final: #Con este while definimos cuando acaba la secuencia
    
    #Aqui empieza la secuencia que determinara si un numero es par y debe ser considerado
    if num_inicial % 2 == 0: 
        
        print(num_inicial)
        cantidad = cantidad + 1  #cantidad += 1 / #Como definimos la cantidad inicial como 0, y gracias al IF confirmamos que es par, el contador aumenta en 1
   
    num_inicial += 1 #Y con esta linea, la secuencia se repetira hasta que se cumpla la linea 10 

print("Hay", cantidad, "números pares")
#Al final se procede a colocar la CANTIDAD de veces que el IF fue verdadero, osea par
