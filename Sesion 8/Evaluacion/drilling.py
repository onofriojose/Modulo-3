'''EJERCICIO
Se solicita recorrer los datos numéricos que se encuentran dentro de la siguiente lista de listas:
1 [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
Hay que imprimir cada dato de las listas en pantalla con las siguientes excepciones:
• Si el primer número de la sublista es cero, omitir la impresión de toda la sublista,
• Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.
• Adicionalmente, crear un diccionario donde asignaremos la primera sublista a la clave A, la
segunda a la clave B, la tercera a la clave C, y la cuarta a la clave D.
• Finalmente, imprimiremos en pantalla el diccionario resultante.
'''
listas = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
'''for i in listas:
    if i == listas[0]:
        listas.remove(i)'''


diccionario = {}        
for indice, sublista in enumerate(listas):
    print(indice)
    print(sublista)
    if indice == 0:
        diccionario["A"]=sublista
    elif indice == 1:
        diccionario["B"]=sublista
    elif indice == 2:
        diccionario["C"]=sublista
    else:
        diccionario["D"]=sublista
print(diccionario)