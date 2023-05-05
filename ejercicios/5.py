'''Realizar la ejecución de un menú utilizando el lenguaje Python, donde se le indiquen varias opciones a seleccionar por el usuario y una opción para salir del menú.
Utilizar ciclos y estructuras condicionales.'''
#importar libreria de expresiones regulares

opcion = ''
while opcion != "5":
    #impresion del menú
    print('1. opcion 1')
    print('2. opcion 2')
    print('3. opcion 3')
    print('4. opcion 4')
    print('5. Opcion 5 Salir de menú')
    opcion = str(input('Ingrese una opcion: '))
    if opcion == '1':
        print('opcion 1')
    elif opcion == '2':
        print('opcion 2')
    elif opcion == '3':
        print('opcion 3')
    elif opcion == '4':
        print('opcion 4')
    elif opcion == '5':
        break
    else:
        print("Ha ingresado una opcion invalida")
        
    