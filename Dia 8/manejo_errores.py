def suma():

    num1 = int(input("Numero1: "))
    num2 = int(input("Numero2: "))
    print(num1+num2)
    print("Gracias por sumar " + num1)



'''try:
    suma()
except TypeError:
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    print("Tienes que pasar numeros no texto")
except:
    print("Es otro error")
else:
    print("Hicisteis todo bien")
finally:
    print("Terminamos")'''


def pedirnumero():

    while True:
        try:
           numero = int(input("Dame un número: "))
        except:
            print("Ese no es un número")
        else:
            print("El número era correcto")
            break
    print("Gracias")



pedirnumero()