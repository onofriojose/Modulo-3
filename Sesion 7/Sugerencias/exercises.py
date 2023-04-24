'''
Debemos crear una variable a la que llamaremos contador, y le asignaremos valor cero. Esta
variable incrementará su valor en una unidad al final de cada iteración del ciclo. Crearemos dos
variables adicionales a las que llamaremos a y b, y les asignaremos el valor 5 y 10,
respectivamente. El ciclo while se ejecutará siempre y cuando contador sea menor que a y b.
En cada iteración imprimiremos el valor de contador, de a y de b.
'''
a = 5
b = 10
contador = 0
while contador < a and contador <= b:
    print(f"cuenta: { contador }, a: {a}, b: {b}")
    contador += 1

print("==================================================")

'''A continuación, recorreremos los valores de un diccionario utilizando la sentencia for.
Debemos recorrer los datos de un diccionario llamado acciones, que contiene tanto los tickets de
las acciones, como sus correspondientes precios'''

acciones = {'AAPL': 187.31,'MSFT': 124.06,'FB': 183.50}
for clave, valor in acciones.items():
    print(clave + " : " + str(valor))
