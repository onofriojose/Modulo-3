'''
INSTRUCCIONES 
Lee con atención cada uno de los requerimientos que se presentan a continuación, y desarrolla la prueba de acuerdo con lo solicitado.

DESCRIPCIÓN
Dada la siguiente lista de nombres:
• Harry Houdini
• Newton
• David Blaine
• Hawking
• Messi
• Teller
• Einstein
• Pele
• Juanes

Y sabiendo que Harry Houdini, David Blaine y Teller son magos. Y también que Newton, Hawking y Einstein son científicos. Debemos separar los nombres en tres grupos: magos, científicos y otros; y escribir una función llamada hacer_grandioso(), que modifique la lista de magos añadiendo la frase ‘El gran‘ antes del nombre de cada mago. Crear una función llamada imprimir_nombres(), que imprime el nombre de cada persona de la lista.
Finalmente, imprimir en pantalla la lista completa de nombres antes de ser modificados; luego imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes.
'''
magos = []
cientificos = []
otros = []
nombres = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']
# recorrer la lista de nombres para separarlos por grupo
for nombre in nombres:
    if nombre in ['Harry Houdini', 'David Blaine', 'Teller']:
        magos.append(nombre)
    elif nombre in ['Newton', 'Hawking', 'Einstein']:
        cientificos.append(nombre)
    else:
        otros.append(nombre)

#Funcion hacer_grandioso()+
def hacer_grandioso(lista_magos):
    print('** Magos **')
    for nombre in range(len(lista_magos)):
        lista_magos[nombre] = 'El gran ' + lista_magos[nombre]
    for nombre in lista_magos:
        print(nombre)

#funcion imprimir_nombres()
def imprimir_nombres(lista_completa):
    for nombre in lista_completa:
        print(nombre)

print('** Todos los Nombres: **')
imprimir_nombres(nombres)
hacer_grandioso(magos)
print('** Cientificos **')
imprimir_nombres(cientificos)
print('** Otros **')
imprimir_nombres(otros)
