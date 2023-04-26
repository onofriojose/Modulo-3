i = 0
j = 0

listas = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
for i in listas:
    if i == listas[0]:
        print("hola hola hola hola hola hola hola hola hola hola")


diccionario = {}        
for indice, sublista in enumerate(listas):
    if indice == 0:
        diccionario["A"]=sublista
    elif indice == 1:
        diccionario["B"]=sublista
    elif indice == 2:
        diccionario["C"]=sublista
    else:
        diccionario["D"]=sublista
print(diccionario)