import os
from pathlib import Path

carpeta = Path('/Users/carlo/OneDrive/Escritorio/Pitonisa/')

archivo = carpeta / 'texto.txt'

texto = open(archivo)

print(texto.read())




