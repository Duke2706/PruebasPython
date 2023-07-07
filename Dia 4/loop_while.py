respuesta = 0
while respuesta < 65:
    respuesta = int(input("¿Que edad tienes? "))
    if respuesta < 18:
        print("Putos menores")
        continue
    elif respuesta >= 18 and respuesta < 35:
        print("Hoy hay carne fresca en el menu")
        break
    else:
        print("Una sexy milf")
else:
    print("Esto no se un geriatrico")