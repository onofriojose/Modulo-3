'''
Usando la clave de acceso mediante la función .keys():
Esta función nos permite obtener todas las claves del diccionario. Luego usamos un ciclo for
para recorrer el resultado de keys() que debimos almacenar en una variable, y en cada
iteración utilizaremos la clave actual para acceder al valor del par con el operador corchetes.
'''

paises_y_capitales = {'Japon': 'Tokio', 'Inglaterra': 'Londres',
'Francia': 'Paris', 'Alemania': 'Berlin'}
keys = paises_y_capitales.keys() 
for clave in keys:
    print(f"{clave} - {paises_y_capitales[clave]}")

'''
Usando el ciclo for para iterar sobre las claves:
Al iterar sobre el diccionario de esta forma tendremos acceso a las claves de cada par
clave:valor. Así que luego, usando el operador corchetes, podemos acceder a cada valor del
par.
'''
paises_y_capitales = {'Japon': 'Tokio', 'Inglaterra': 'Londres',
'Francia': 'Paris', 'Alemania': 'Berlin'}
for pais in paises_y_capitales:
    print(f"{pais} - {paises_y_capitales[pais]}")
    
'''
Usando el ciclo for y la función values():
Esta función nos devuelve solo los valores del par clave:valor del diccionario
'''
paises_y_capitales = {'Japon': 'Tokio', 'Inglaterra': 'Londres',
'Francia': 'Paris', 'Alemania': 'Berlin'}
for capital in paises_y_capitales.values():
    print(capital)

'''Usando el ciclo for y la función ítems():
Esta función nos regresa el par clave:valor de cada elemento del diccionario. Haremos uso
del ciclo for para iterar sobre los valores que nos regresa la función.'''

paises_y_capitales = {'Japon': 'Tokio', 'Inglaterra': 'Londres',
'Francia': 'Paris', 'Alemania': 'Berlin'}
for pais, capital in paises_y_capitales.items():
    print(f"{pais} - {capital}")

