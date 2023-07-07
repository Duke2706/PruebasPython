archivo = open('prueba.txt','a')

archivo.write('Bienvenido')

archivo.close()

archivo = open('prueba.txt','r')
print(archivo.read())

archivo.close()