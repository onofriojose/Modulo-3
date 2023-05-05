def operaciones(lista):
    suma = 0
    for i in lista:
        suma += i
    resta = suma - lista[1] - lista[2]
    return (suma, resta)

lista_numeros = input("Ingrese los números separados por comas: ")
lista = lista_numeros.split(',')
lista = [int(i) for i in lista]
resultado = operaciones(lista)
print(lista)
