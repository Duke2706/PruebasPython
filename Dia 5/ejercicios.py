
def devolver_distintos(num1, num2, num3 ):

    lista = list()

    lista.append(num1)
    lista.append(num2)
    lista.append(num3)

    lista.sort()

    if num1+num2+num3 > 15:
        return lista[2]
    elif num1+num2+num3 < 10:
        return lista[0]
    else:
        return lista[1]


def descompon_palabra(palabra):
    lista = list()
    for char in palabra:
        lista.append(char)

    lista_final = list(set(lista))
    lista_final.sort()
    return lista_final


def check_zero(*args):
    anterior = 1
    for index, item in enumerate(args):
        if index == 0:
            anterior = item
            continue
        elif index > 0:
            if item == 0 and anterior == 0:
                return True
            else:
                anterior = item

    return False


def contar_primos(num1):
    rango = range(0,(num1+1))
    primos = list()
    for num in rango:
        if num < 2:
            continue
        elif num == 2:
            primos.append(2)
        else:
            if is_prime(num):
                primos.append(num)

    print(primos)
    return len(primos)


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True



print(contar_primos(1))