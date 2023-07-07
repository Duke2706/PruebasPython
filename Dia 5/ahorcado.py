import random


palabras = ['armario', ' juventud', 'parsimonia', 'ajedrez', 'pubertad', 'guatemala', 'proton', 'metafora', 'belleza',
            'transporte', 'usable']


def random_word(lista):

    return random.choice(lista)


def get_answer():
    letra = input(f"Dime una letra que piensas que esta en la palabra: ")
    while not letra.isalpha() or len(letra) > 1:
        if not letra.isalpha():
            letra = input(f"Eso no es una letra. Dime una letra que piensas que esta en la palabra: ")
        elif len(letra) > 1:
            letra = input(f"Usa solo una letra. Dime una letra que piensas que esta en la palabra: ")

    return letra.lower()


def check_letter(letter, palabra, copia):
    index = 0
    counter = 0
    lista = list()
    for letra in palabra:
        if letra == letter:
            copia[index] = letter
            counter = counter + 1
        index = index + 1
    print(f"Has tenido {counter} aciertos")
    lista.append(copia)
    lista.append(counter)
    return lista


def check_winner(copia, palabra):
    counter = 0
    index = 0
    for letra in palabra:
        if letra == copia[index]:
            counter = counter + 1
        index += 1

    if counter == len(palabra):
        return True
    else:
        return False


def genera_copia(palabra):
    copia = list()
    for letra in palabra:
        copia.append('_')

    return copia


def convert(s):
    new = ''
    for x in s:
        new += x
    return new


def start_game(words):
    word = random_word(words)
    copy = genera_copia(word)
    vidas = 6
    print(f"Adivina la palabra con {len(copy)} caracteres. Tienes {vidas} intentos")
    print(f"{convert(copy)}")
    result = False
    while not result and vidas > 0:
        answer = check_letter(get_answer(), word, copy)
        copy = answer[0]

        if answer[1] == 0:
            vidas = vidas - 1

        print(f'Te quedan {vidas} intentos')
        print(f"{convert(copy)}")
        result = check_winner(copy, word)

    if vidas == 0:
        print('Lo siento, agotaste el número de intentos posibles')
    else:
        print('Al fin adivinaste la palabra')


start_game(palabras)

