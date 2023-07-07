from pathlib import Path, PureWindowsPath

carpeta = Path('C:/Users/carlo/OneDrive/Escritorio/Pitonisa/texto.txt')


win = PureWindowsPath(carpeta)
print(win)

if not carpeta.exists():
    print('No existe')
else:
    print('Existe')