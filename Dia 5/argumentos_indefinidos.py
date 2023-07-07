def suma(*args):

    return sum(args)


def suma2(*args):
    suma = 0
    for num in args:
        suma = suma + num
    return suma


print(suma(5,6,9, 23, 5, 78, 90, 543, 23))
print(suma2(5,6,9, 23, 5, 78, 90, 543, 23))