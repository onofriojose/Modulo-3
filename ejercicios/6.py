'''Tenemos una lista de números
[3, 5, 2, 8, 1, 10]
Se requiere encontrar el primer número par en la lista utilizando un bucle while.'''

lista = [3, 5, 4, 8, 1, 10]
num = 0
while lista[num] %2 != 0:
    num +=1
print(f"El primer numero par es {lista[num]}")