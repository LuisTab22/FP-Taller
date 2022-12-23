#E.Secuencial.3
# Mostrar en pantalla como hallar el volumen, área y perímetro de un cubo con solo una arista conocida

arista = int(input("Ingrese la medida del cubo en centímetros: "))

volumen = arista * arista * arista
print ("El volumen del cubo es de", volumen,"centímetros al cubo")

area = 6 * arista * arista
print ("El área del cubo es de", area,"centímetros al cuadrado")

perimetro = 12 * arista
print ("El perímetro del cubo es de", perimetro,"centímetros")
