'''
DRILLING: MAYOR A MENOR.
Para resolver este ejercicio, anteriormente debe haber revisado la lectura y los videos del CUE:
Sentencias condicionales.
EJERCICIO
Se requiere contar con un programa que, dados 3 números diferentes, los evalúe y entregue el
orden de mayor a menor.
'''
a = int(input("Ingrese primer número: "))
b = int(input("Ingrese segundo número: "))
c = int(input("Ingrese tercer número: "))
if a > b and a > c:
    print(a)
    if b > c:
        print(b)
        print(c)
    else:
        print(c)
        print(b)
elif b > a and b > c:
    print(b)
    if a > c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)
else:
    print(c)
    if a > b:
        print(a)
        print(b)
    else:
        print(b)
        print(a)