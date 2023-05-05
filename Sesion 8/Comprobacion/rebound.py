'''
En esta actividad trabajaremos con listas. Tomando la lista que se entrega a continuación, se
solicita realizar las siguientes acciones en el orden indicado:
1. Eliminar los elementos duplicados.
2. Ordenar la lista resultante en orden ascendente.
La lista es:
1 mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]
'''

mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]
mi_lista = sorted(list(set(mi_lista)))
print(mi_lista)


'''
sorted es para listas nuevas y sort para arreglar listas existentes
mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]
mi_set = set(mi_lista)
mi_lista = list(mi_set)
mi_lista = sorted(mi_lista) #my_list.sort()
print(mi_lista)
'''
'''
para imprimir la liste en orden descendente:
mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]
mi_set = set(mi_lista)
mi_lista = list(mi_set)
mi_lista = sorted(mi_lista, reverse=True) #Para ordenar la lista en orden descendente, puedes utilizar el parámetro "reverse" en la función sorted() y establecer su valor en True
print(mi_lista)
'''