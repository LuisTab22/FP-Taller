#E.Selectivas.4.Multiple
#Conforme a la siguiente tabla:

#EDAD EN AÑOS                MENSAJE
#HASTA 12            ESTAS EN LA EDAD INFANTIL
#DE 13 A 17          ESTAS EN LA ADOLESCENCIA
#18 A 30             LLEGASTE A LA MADUREZ
#DE 31 A 60          ERES ADULTO JOVEN
#MAS DE 60           ERES ADULTO MAYOR

edad = int(input("Cuántos años tienes: "))
if edad < 12:
    print("Estas en la edad infantil")
elif edad > 12 and edad < 18:
    print("Estas en la adolescencia")
elif edad >= 18 and edad <=30:
    print("Eres un adulto joven")
elif edad > 60:
    print("Eres un adulto mayor")
print("Pase un buen día")