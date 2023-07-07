nombres = ['Carlos','Chorong','Rafael']
edades = [41,36,73]
ciudades =['Madrid','Anseong','Mostoles']
lista = list(zip(nombres,edades, ciudades))


for nombre, edad, ciudad in lista:
    print(f"{nombre} tiene {edad} y vive en {ciudad}")