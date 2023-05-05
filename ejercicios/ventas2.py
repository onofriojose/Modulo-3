ventas = {
    "producto_a": [100, 150, 200, 300, 250, 175, 125, 200, 300, 400, 500, 550],
    "producto_b": [50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325],
    "producto_c": [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
}

for producto, ventas_mensuales in ventas.items():
    total_ventas = 0  # Inicializar la variable en 0
    for venta in ventas_mensuales:
        total_ventas += venta  # Sumar cada venta a la variable
    print(f"Total de ventas de {producto}: {total_ventas}")