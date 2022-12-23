#E.Secuencial.5
#Escribir un programa que lea un entero positivo, n, 
# introducido por el usuario y después muestre en pantalla 
# la suma de todos los enteros desde 1 hasta n. 

n = int(input("Introduzca un número entero:"))

suma = n * (n + 1)/2
print ("La suma de los primeros números enteros de 1 hasta ", n," es ", suma)
