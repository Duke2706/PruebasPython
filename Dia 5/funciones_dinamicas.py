

def chequear_3_cifras(lista):

    lista_tres = []
    for n in lista:
        if n in range(100,1000):
            lista_tres.append(n)
        else:
            pass
    return lista_tres


lista = [5, 99,6000, 46, 77, 457, 34, 12, 123]
resultado = chequear_3_cifras(lista)
print(resultado)




