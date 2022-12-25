#E.Repetitivas.For.4
#Imprima en pantalla los 10 primeros resultados de una tabla de multiplicación

n = int(input("Ingrese un número: "))
for i in range(10):
    resultado = i * n
    print(i,"x",n,"=",resultado)
