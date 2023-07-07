from random import *

nombre = input("Dime tu nombre \n")
aleatorio = round(random()*100)
print(f'Hola {nombre} tienes 8 oportunidades para adivinar un número de 1 a 100 ambos inclusives')
numero = 0
counter = 0;
for n in range(1,9):
    numero = int(input(f'Di un número:\n'))
    counter += 1
    match numero:
        case _ if numero not in range(1,101):
            print(f'El número {numero} esta fuera del rango entre 1 y 100, marca yun número correcto. Te quedan {8-n} intentos')
        case _ if numero == aleatorio:
            print(f'Acertaste el número en el {n} intento, era {numero}')
            break
        case _ if numero < aleatorio:
            print(f'El número {numero} es menor. Te quedan {8 - n} intentos')
        case _ if numero > aleatorio:
            print(f'El número {numero} es mayor. Te quedan {8 - n} intentos')
        case _:
            print(f'{numero} no es un numero')

if counter == 8:
    print(f'Lo siento, has perdido , el número era {aleatorio} :(')