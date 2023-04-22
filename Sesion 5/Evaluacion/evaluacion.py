palabra = 'paralelepipedo'
consonantes = ""
patron = "aAeEiIoOuU"
for i in range(len(palabra)):
    if palabra[i] not in patron:
        consonantes += palabra[i]
        print(f"La ubicacion de la letra {palabra[i]} es: {i}")
print(consonantes)