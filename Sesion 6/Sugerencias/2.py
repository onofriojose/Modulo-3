var1 = int(input("Ingrear primer número: "))
var2 = int(input("Ingrear segundo número: "))
var3 = int(input("Ingrear tercer número: "))
if var1 > 0 and var2 > 0 and var3 > 0:
    print("Todos los números son positivos")
elif var1 > 0 or var2 > 0 or var3 > 0:
    print("Alguna de las variables es positiva")
