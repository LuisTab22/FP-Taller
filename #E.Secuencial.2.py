#E.Secuencial.2
#Una tienda ofrece un descuento del 15% sobre el total de 
#(...) la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.

compra_total = int(input("Gasto total en las compras: "))

desc = compra_total * 0.15
precio_final = compra_total - desc

print ("Con el descuento de la tienda, usted solo pagará", precio_final)
