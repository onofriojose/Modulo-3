r1 = float(input("Ingrese la Resistencia 1 : "))

r2 = float(input("Ingrese la Resistencia 2 : "))

r3 = float(input("Ingrese la Resistencia 3 : "))

rT = (1/((1/r1)+(1/r2)+(1/r3)))




print("La resistancia total es: {:.3f}".format(rT)) #print(f"La resistancia total es: {rT}") tambien funciona con el formato de la variable