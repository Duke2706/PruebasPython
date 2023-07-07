from random import shuffle
# Lista inicial
palitos = ['-','--','---','----']


# Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista


# Pedir input números
def probar_suerte():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input('Elige un número del 1 al 4: ')
    return int(intento)


# Comprobar intento
def comprobar_intento(lista, intento):
    if lista[intento - 1] == '-':
        print('A lavar los platos')
    else:
        print('Esta vez te has librado')

    print(f'Te ha tocado {lista[intento-1]}')


comprobar_intento(mezclar(palitos), probar_suerte())
