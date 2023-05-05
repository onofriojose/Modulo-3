'''Simulación de una bomba de tiempo. Irá el tiempo desde el 5 al 1 en decremento. Al ejecutar el programa, se imprimirá el mensaje "Booom"'''

for i in range(5,0,-1):
    print(i)
print("Booom")




'''Aquí te explico los argumentos de la función range(start, stop, step):

start: el valor inicial de la secuencia. En este caso, es 5.
stop: el valor final de la secuencia. En este caso, es 0. Pero como el límite superior no se incluye, la secuencia termina antes de llegar a 0.
step: la cantidad en la que se incrementa o decrementa la secuencia. En este caso, es -1, lo que indica que la secuencia se genera en decremento de 1 en 1.'''