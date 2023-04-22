
factorial = 1
i = 1
while True:
    numero = int(input("Ingrese un numero entero positivo para clacular factorial: "))
    if numero > 0:
        break
while True:
    factorial *= i
    i += 1
    if i > numero:
        break
print(factorial)