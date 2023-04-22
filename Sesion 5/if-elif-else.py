#estructuras condicionales para evaluar cierta condicion declarada o varias
numero = int(input("Ingrese un numero: "))

#if (condicion), donde condicion siempre es True, al menos que se cambie o modifique
if numero > 5 :
    print(f"El numero {numero} es mayor que 5")
elif(numero == 5):
    print(f"El numero {numero} es igual a 5")
else:
    print(f"El numero {numero} es menor que 5")