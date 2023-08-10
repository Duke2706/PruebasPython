def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x




def mi_generador():
    vidas = 3
    if vidas == 3:
        vidas -= 1
        yield "Te quedan 3 vidas"
    if vidas == 2:
        vidas -= 1
        yield "Te quedan 2 vidas"
    if vidas == 1:
        vidas -= 1
        yield "Te queda 1 vida"
    if vidas == 0:
        yield "Game Over"


perder_vida = mi_generador()

print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))

