#E.REPETITIVA.WHILE.3
#Tabla de multiplicar

#Asignamos un valor a nuestra tabla
tabla = int(input("Introduce el número del que desea conocer su tabla de multiplicar: "))
inicio = 1  #Definimos un valor incial con el cual iniciar la tabla

while inicio <= 10: #Asignamos la condición para finalizar
    resultado = tabla * inicio #Asignamos la operación a realizar
    print(tabla, "*",inicio,"=",resultado) #Se procede a imprimir la multiplicación con el valor inicial
    inicio +=1 #Asignamos la regla que permitira ACUMULAR tabla del valor deseado
    