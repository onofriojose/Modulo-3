'''
EJERCICIO
Crear una función que sume dos números, otra que reste dos números, otra que multiplique dos
números, y otra que divida dos números. Adicionalmente, crear una función que acepte dos
números como parámetros y regrese el resultado en forma de tupla de su suma, resta,
multiplicación y división.
Los resultados se deben almacenar en un diccionario, cuyas claves serán: Suma, Resta,
Multiplicación y División, y los valores de cada clave serán los resultados obtenidos con la función
creada anteriormente.
'''
try:
    #Funcion Suma
    def sumar(a,b):
        suma = a+b
        return suma

    #Funcion Resta
    def restar(a,b):
        resta = a-b
        return resta

    #Funcion Multiplicación
    def multiplicar(a,b):
        multi = a*b
        return multi

    #Funcion Division
    def dividir(a,b):
        if b !=0:
            divi = a/b
        else:
            print("No se puede dividir por cero")
        return divi
          
    #Fcuncion Ingreso de datos
    def ingreso(a,b):
        a=int(input("Ingrese el primer valor: "))
        b=int(input("ingrese el segindo valor: "))
        return sumar(a,b), restar(a,b), multiplicar(a,b), dividir(a,b)
    a = 0
    b = 0
    ingreso(a,b)
except Exception as e:
    print("No se puede dividir entre cero ", e)

diccionario={}
diccionario["SUMA"] = sumar(a,b)
diccionario["RESTA"] = restar(a,b)
diccionario["MULTIPLICACION"] = multiplicar(a,b)
diccionario["DIVISION"] = dividir(a,b)
print(diccionario)
