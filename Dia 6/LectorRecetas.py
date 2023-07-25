from pathlib import Path
from os import system, name, listdir, remove, path, mkdir, makedirs
import shutil
directorio_base = Path("C:/Users/carlo/OneDrive/Escritorio/Recetas")


def elige_categoria():

    categorias = []
    for f in listdir(directorio_base):
        categorias.append(f)

    print("Estas son las categorias: ")
    for idx, c in enumerate(categorias):
        print(f"{( idx + 1)}. {c}");


    finished = False
    while not finished:
        selected = input("¿Que categoria eliges? escribe el número:\n")
        try:
            numero = int(selected)
            if 0 <= numero - 1 < len(categorias):
                clear()
                return categorias[numero - 1]
            else:
                print(f"'{selected}' no es un número correcto de categoria")
        except ValueError:
            print(f"'{selected}' no es un número correcto de categoria")

def elige_receta(directorio):

    categoria = Path(directorio_base, directorio)
    recetas = []
    for f in listdir(categoria):
        recetas.append(f)

    if len (recetas) > 0:
        print(f"Estas son las recetas de la categoria {categoria}: ")
        for idx, c in enumerate(recetas):
            print(f"{( idx + 1)}. {c}");

        finished = False
        while not finished:
            selected = input("¿Que receta eliges? escribe el número:\n")
            try:
                numero = int(selected)
                if 0 <= numero - 1 < len(recetas):
                    clear()
                    return recetas[numero-1]
                else:
                    print(f"'{selected}' no es un número correcto de receta")
            except ValueError:
                print(f"'{selected}' no es un número correcto de receta")
    else:
        print("Es una categoria sin recetas")
        return "0"


def muestra_receta():
    clear()
    categoria = elige_categoria()
    receta = elige_receta(categoria)
    if receta != "0":
        file = Path(directorio_base,categoria,receta)
        print(f"Receta: {receta}")
        print("-------------------------------------------------------")
        print(file.read_text())
        print("-------------------------------------------------------")

    else:
        print()

    input("Pulsa Enter para volver al menú")

def borrar_receta():

    print("Vamos a borrar una receta")
    categoria = elige_categoria()
    receta = elige_receta(categoria)
    answer = input(f"¿Estas seguro que quieres borrar la receta '{receta}' de la categoria '{categoria}'? SI/NO\n")
    if answer.upper() == "SI":
        file = Path(directorio_base, categoria, receta)
        remove(file)
        if not path.exists(file):
            print(f"Se borro correctamente la receta  '{receta}' de la categoria '{categoria}'")

    clear()


def borrar_categoria():

    print("Vamos a borrar una categoria")
    categoria = elige_categoria()
    answer = input(f"¿Estas seguro que quieres borrar la categoria '{categoria}'? SI/NO\n")
    if answer.upper() == "SI":
        file = Path(directorio_base, categoria)
        shutil.rmtree(file)
        if not path.exists(file):
            print(f"Se borro correctamente la categoria '{categoria}'")
    clear()


def crea_categoria():

    categoria = input(f"¿Que categoria quieres crear? escribe el nombre\n")
    answer = input(f"¿Estas seguro que quieres crear la categoria '{categoria}'? SI/NO\n")
    if answer.upper() == "SI":
        file = Path(directorio_base, categoria)
        mkdir(file)
        if path.exists(file):
            print(f"Se creo correctamente la categoria '{categoria}'")
    clear()

def crea_receta():
    print("Vamos a crear una receta")
    categoria = elige_categoria()
    nombre = input("¿Que nombre le vas a dar?\n")
    contenido = input("Escribe el texto de la receta\n")
    print(f"Nombre: {nombre}")
    print("-------------------------------------------------------")
    print(f"Contenido: {contenido}")
    print("-------------------------------------------------------")
    answer = input(f"¿Estas seguro que quieres crear la categoria '{categoria}'? SI/NO\n")
    if answer.upper() == "SI":
        finalname = nombre+".txt"
        file = Path(directorio_base, categoria, finalname)
        open(file, "w")
        if path.exists(file):
            file.write_text(contenido)
            print(f"Se creo correctamente la receta '{nombre}' en la categoria '{categoria}'")


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


finished = False
opciones = ['Leer receta', 'Crear receta', 'Crear categoria', 'Borrar receta', 'Borrar categoria', 'Finalizar']
while not finished:
    clear()
    print("Elija una opción del menú escribiendo el número")
    for idx, o in enumerate(opciones):
        print(f"{(idx+1)}. {o}")
    answer = input("Opcion:\n")
    match answer:
        case '1':
            muestra_receta()
        case '2':
            crea_receta()
        case '3':
            crea_categoria()
        case '4':
            borrar_receta()
        case '5':
            borrar_categoria()
        case '6':
            finished = True
            print("Gracias por usar nuestro programa")
        case _:
            print(f"'{answer}' no es una opción correcta")
            input("Pulsa Enter para continuar")



