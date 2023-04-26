'''EJERCICIO
Se solicita recorrer los datos numéricos que se encuentran dentro de la siguiente lista de listas:
lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
Hay que imprimir cada dato de las listas en pantalla con las siguientes excepciones:
• Si el primer número de la sublista es cero, omitir la impresión de toda la sublista,
• Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.
• Adicionalmente, crear un diccionario donde asignaremos la primera sublista a la clave A, la
segunda a la clave B, la tercera a la clave C, y la cuarta a la clave D.
• Finalmente, imprimiremos en pantalla el diccionario resultante.
'''
#Manipulacion de la lista para eliminar ceros segun enunciado
listas = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
for sublistas in listas:
    if sublistas[0] == 0:
        listas[listas.index(sublistas)] = [" "]
    elif 0 in sublistas:
        sublistas[sublistas.index(0)] = " "
    '''    
    if sublistas[0] == 0:
        listas[listas.index(sublistas)] = [" "] # asignamos una lista vacía a la sublista en la posición actual con el metodo index()
    elif sublistas[1] == 0:
        sublistas[1] = " " # asignamos un elem vacío a la sublista en la posición actual
    elif sublistas[2] == 0:
        sublistas[2] = " " # asignamos un elem vacío a la sublista en la posición actual
        '''
#Construccion de diccionario despues de hbaer modificado la lista en el codigo anterior
diccionario = {}        
for indice, sublistas in enumerate(listas):
    if indice == 0:
        diccionario["A"]=sublistas
    elif indice == 1:
        diccionario["B"]=sublistas
    elif indice == 2:
        diccionario["C"]=sublistas
    else:
        diccionario["D"]=sublistas
print(diccionario)