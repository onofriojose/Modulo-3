ventas = {
    "producto_a": [100, 150, 200, 300, 250, 175, 125, 200, 300, 400, 500, 550],
    "producto_b": [50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325],
    "producto_c": [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
}

for producto in ventas.keys():
    total_ventas = 0
    for venta in ventas[producto]:
        total_ventas += venta
    print(f"Total de ventas de {producto}: {total_ventas}")