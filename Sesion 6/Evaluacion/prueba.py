while True:
    a = int(input("Ingrese primer número: "))
    b = int(input("Ingrese segundo número: "))
    c = int(input("Ingrese tercer número: "))
    lista_numeros = {a, b, c}
    
    if len(lista_numeros) < 3:
        print("Debe ingresar numeros diferentes")
    else:
        ordenados = sorted(lista_numeros, reverse=True)
        print("El orden de mayor a menor es:")
        for numero in ordenados:
            print(numero)
        break