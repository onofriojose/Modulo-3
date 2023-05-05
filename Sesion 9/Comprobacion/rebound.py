'''
Crear una función que acepte 3 números como parámetros, sume todos los valores, y
adicionalmente reste el segundo y tercer parámetro al primero.
Al invocar la función, debemos pasarle los parámetros en forma de lista. Esta devolverá ambos
resultados en una tupla. Los resultados se deben imprimir en pantalla.
'''

def operaciones(lista2):
    lista2 = [int(i) for i in lista2]#convertir los elementos de la lista a enteros
    suma = 0
    for i in lista2:
        suma = suma+i
    resta = lista2[0] - lista2[1] - lista2[2]
    return suma, resta

lista_numeros = input("Ingrese los números separados por espacios: ")
lista = lista_numeros.split()
resultado = operaciones(lista)
print(resultado)