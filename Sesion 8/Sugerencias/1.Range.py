vals = range(5,-110,-2)
print(list(vals))

vals2 = range(0, 10, 3)
print(list(vals2))
'''
vals = range(5)
print(vals)
#Resultado:
[0, 1, 2, 3, 4]
vals = range(2, 3, 3)
print(vals)
#Resultado:
[2, 5, 8]

pero mis resultados son estos:
range(2, 3, 3)
range(0, 5)


cual es el problema?

*******************************
El problema es que en Python 3, range no devuelve una lista sino un objeto de tipo range, que es una secuencia inmutable de números enteros. Si deseas imprimir los valores de range, debes convertir el objeto en una lista usando la función list().

Por lo tanto, si deseas imprimir los valores en forma de lista, debes hacer lo siguiente:

vals = range(5)
print(list(vals))
# Resultado: [0, 1, 2, 3, 4]

vals = range(2, 9, 3)
print(list(vals))
# Resultado: [2, 5, 8]

'''