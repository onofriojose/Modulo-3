r1 = input("Ingresa el valor de la resistencia 1: ")
r2 = input("Ingresa el valor de la resistencia 2: ")
r3 = input("Ingresa el valor de la resistencia 3: ")
r1 = float(r1)
r2 = float(r2)
r3= float(r3)
if r1.isdigit() and r2.isdigit() and r3.isdigit():

    if (r1 > 0 and r2 > 0 and r3 > 0):
        rt = 1 / ((1 / r1) + (1 / r2) + (1 / r3))
        print(f"La resistencia total es: {rt:.2f}")
    else:
        print('los numeros deben ser positivos')
else:
    print("debe ingresar solo numeros")