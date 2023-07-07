nombre = input("¿Cual es tu nombre? ")
ventas = float(input("¿Cuanto has vendido? "))
comision = round(ventas*0.13, 2)
print(f"Hola {nombre}, con unas ventas de {ventas} tu comisión es de {comision}")