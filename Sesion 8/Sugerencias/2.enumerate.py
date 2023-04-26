'''
La función enumerate() en Python se utiliza para iterar sobre una secuencia (como una lista, una tupla, un diccionario, etc.) y, al mismo tiempo, tener acceso al índice actual en cada iteración.

La función enumerate() devuelve un objeto enumerado que es una secuencia de pares (tuplas) que contienen un contador (que por defecto comienza en 0) y el valor correspondiente obtenido de la secuencia en esa posición.
'''
frutas = ['manzana', 'banana', 'cereza', 'naranja']
for indice, fruta in enumerate(frutas):
    print(indice, fruta)
    
lista = [10, 50, 75, 83]
for x, val in enumerate(lista):
    print (val)

    
'''
En este ejemplo, estamos utilizando enumerate() para iterar sobre la lista frutas. En cada iteración, la variable indice contiene el índice actual de la lista (0, 1, 2, 3) y la variable fruta contiene el valor correspondiente de la lista ('manzana', 'banana', 'cereza', 'naranja'). El resultado de ejecutar este código sería:

0 manzana
1 banana
2 cereza
3 naranja

la función enumerate() es útil para obtener el índice de una secuencia mientras se itera sobre ella, lo que puede ser muy útil en muchos casos, como cuando necesitas saber la posición de un elemento específico en una lista o cuando necesitas hacer referencia a los elementos de una secuencia por índice en lugar de por valor.

'''