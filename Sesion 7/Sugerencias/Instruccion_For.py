x = (10, 20, 30, 40, 50)
for var in x:
    print(f"Índice {str(x.index(var))} : {var}")#x.index(var) es para acceder al indice de un elemento dentro de un arreglo (en este caso, una tupla)
    
'''Si tenemos una lista de tuplas, podemos acceder a los elementos individuales de cada tupla de
nuestra lista incluyendo ambos como variables en el bucle for, de esta manera: '''
x = [(4,2,7), (3,6,8), (5,5,9)]
for v, n, p in x:
    print(f"{v}, plus {n}, plus {p} equals {v+n+p}")
    
'''Los bucles for también pueden iterar a través de cada carácter de una cadena. Así es como
funciona:'''
print("Ciencia")
for caracter in "Ciencia ":
    print(caracter)

'''Un bucle for puede tener también un bloque else opcional. La parte else se ejecuta al agotarse los
elementos de la secuencia en el bucle for.'''
digitos = [0, 1, 5]
for i in digitos:
    print(i)
else:
    print("No quedan elementos en la lista.")
