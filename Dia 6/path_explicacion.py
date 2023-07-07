from pathlib import Path


base = Path.home()


ruta = Path('Users', 'OneDrive', 'Escritorio','Pitonisa', 'texto.txt')

en_europa = ruta.relative_to(Path('Users'))

en_espania = ruta.relative_to(Path('Users','OneDrive'))

print(en_europa)
print(en_espania)


