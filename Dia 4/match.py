cliente = {'nombre': 'Carlos', 'edad': '41', 'ocupacion':'informatico'}

pelicula = {'titulo': 'Matrix', 'ficha_tecnica': {'protagonista': 'Keanu Reeves', 'director': 'Lana y Lilly Wachowski'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print(f'Es un cliente: {nombre} , {edad} años, trabaja como {ocupacion}')
        case {'titulo': titulo, 'ficha_tecnica': {'protagonista': protagonista, 'director': director}}:
            print(f'La pelicula {titulo} con el protagonista {protagonista} y el director {director}')
        case _:
            print('no se que es')
