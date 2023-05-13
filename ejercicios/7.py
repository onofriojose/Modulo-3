'''
Tienes la siguiente lista de números:

[45, 23, 67, 89, 12, 56, 78, 90]

Encontrar el número más grande en la lista utilizando un bucle for.
'''
lista = [45, 23, 67, 99, 12, 356, 78, 90]
num = lista[0]
for elemento in lista:
    if elemento > num:
        num= elemento
print(num)
