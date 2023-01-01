#E.REPETITIVA.WHILE.4
#SUMAR MULTIPLOS DE 5

contador = 0
suma = 0

num_maximo = int(input("Introduce el número máximo: "))

while contador < num_maximo:
    
    suma = suma + contador 
    contador = contador + 5 
    
    #PRIMER CICLO
    #El contador = 0, pasa a contador = 5; por consiguiente...
    #La suma = 0, pasa a ser (suma = 0 + 5) suma = 5; donde...
    #WHILE al ser verdadero, vuelve a repetir la secuencia en un segundo ciclo, con los valores ahora perteneciente al primer ciclo
    
    #SEGUNDO CICLO
    #El contador = 5, pasa a contador = 10; por consiguiente...
    #La suma = 5, pasa a ser (suma = 5 + 10) suma = 15; y así sucesivamente hasta que...
    
print("La suma es: ", suma)
#Cuando el WHILE sea falso, se detiene el contador, dejando como resultado la suma de multiplos de 5
