'''Pedir el ingreso de dos textos al usuario por consola y comparar si son iguales o del mismo tamaño'''
texto1 = input("Ingrese el primer texto: ")
texto2 = input("Ingrese el segundo texto: ")

if len(texto1) == len(texto2):
    if texto1 == texto2:
        print("Textos iguales y misma longitud")
    else:
        print("Textos diferentes misma longitud")
else:
    print("Textos diferentes")