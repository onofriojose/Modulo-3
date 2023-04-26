'''
DRILLING: MAYOR A MENOR.
Para resolver este ejercicio, anteriormente debe haber revisado la lectura y los videos del CUE:
Sentencias condicionales.
EJERCICIO
Se requiere contar con un programa que, dados 3 números diferentes, los evalúe y entregue el
orden de mayor a menor.

'''


a = int(input("Ingrese primer número: "))
b = int(input("Ingrese segundo número: "))
c = int(input("Ingrese tercer número: "))
if a > b and a > c:
    print(a)
    if b > c:
        print(b)
        print(c)
    else:
        print(c)
        print(b)
elif b > a and b > c:
    print(b)
    if a > c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)
else:
    print(c)
    if a > b:
        print(a)
        print(b)
    else:
        print(b)
        print(a)

"""
a = int(input("Ingrese primer número: "))
b = int(input("Ingrese segundo número: "))
c = int(input("Ingrese tercer número: "))

lista_numeros = [a, b, c]
ordenados = sorted(lista_numeros, reverse=True)

print("El orden de mayor a menor es:")
for numero in ordenados:
    print(numero)
    
En este código, se crea una lista llamada lista_numeros que contiene los 3 números ingresados por el usuario. Luego, se utiliza la función sorted() para ordenar los números en orden descendente y se almacena en una nueva lista llamada ordenados. Finalmente, se recorre la lista ordenados con un ciclo for e imprime cada número en orden de mayor a menor.
"""
'''
a = int(input("Ingrese primer número: "))
b = int(input("Ingrese segundo número: "))
c = int(input("Ingrese tercer número: "))

lista_numeros = [a, b, c]
setDeNumeros = set(lista_numeros)
ordenados = list(setDeNumeros)

print("El orden de menor a mayor es:")
for numero in ordenados:
    print(numero)
'''