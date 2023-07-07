texto = input("Introduce un texto de cualquier longitud para ser analizado:\n").lower()
letras = []
letras.append(input("Ingresa la primera letra:"))
letras.append(input("Ingresa la segunda letra:"))
letras.append(input("Ingresa la tercera letra:"))
print("\n")
count = []
count.append(texto.lower().count(letras[0].lower()))
count.append(texto.lower().count(letras[1].lower()))
count.append(texto.lower().count(letras[2].lower()))
palabras = texto.split()
primera = texto[0]
ultima = texto[- 1]
palabras.reverse()
reverse = " ".join(palabras)
exist = "python" in texto.lower()
dic = {True: 'si', False: 'no'}
print("\nLa letra " + letras[0] + " aparece " + str(count[0]) + " veces en el texto")
print("La letra " + letras[1] + " aparece " + str(count[1]) + " veces en el texto")
print("La letra " + letras[2] + " aparece " + str(count[2]) + " veces en el texto")

print("El texto contiene " + str(len(palabras)) + " palabras")
print("La primera letra es " + primera + " y la última es " + ultima)
print("Este es el texto invertido:")
print(reverse)

print(f"La palabra 'Python' {dic[exist]} esta en el texto")









