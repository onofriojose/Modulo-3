strNum = input("Ingresar numeros separados por espacios: ")
try:
    listaNum = strNum.split()
    tuplaNum = tuple(listaNum)
    print(tuplaNum)
    setNum = set(listaNum)
    print(setNum)
    listaNum = list(setNum)
except ValueError:
    print("No es numero separado por espacio")
print(listaNum)

"""
Puedes agregar una validación para asegurarte de que el usuario ingrese solo números. Puedes hacer esto utilizando una declaración try-except y la función int() para intentar convertir cada elemento de la lista a un número entero. Si ocurre un error, entonces el elemento no es un número y se puede imprimir un mensaje de error y pedirle al usuario que vuelva a ingresar la lista.

Puedes agregar la funcionalidad de ordenar la lista de números ingresados por el usuario en orden ascendente o descendente utilizando las funciones sorted() o sort(). Por ejemplo, para ordenar la lista de forma ascendente, puedes usar:

listaNum.sort() """

"""
Y para ordenar de forma descendente:

listaNum.sort(reverse=True)
"""
"""
Puedes agregar la funcionalidad de calcular la suma o el promedio de la lista de números ingresados por el usuario utilizando la función sum() y la función len().

Puedes agregar la funcionalidad de buscar un número específico en la lista de números ingresados por el usuario utilizando la palabra clave in y una declaración if. Por ejemplo:

num_buscado = input("Ingrese el número que desea buscar: ")
if num_buscado in listaNum:
    print(f"{num_buscado} se encuentra en la lista.")
else:
    print(f"{num_buscado} no se encuentra en la lista.")
    
Estas son solo algunas sugerencias para mejorar tu proyecto y practicar diferentes aspectos de Python. ¡Buena suerte con tu proyecto!
"""