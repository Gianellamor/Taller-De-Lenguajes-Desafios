def precio_con_descuento(precio,porcentaje):
    return precio - (precio * porcentaje / 100)

def precio_con_IVA(precio,porcentaje):
    return precio + (precio * porcentaje / 2)

def total_dela_compra(cesta,precio_con_IVA):
    total= 0
    for precio, porcentaje in cesta.items():
        total += precio_con_IVA(precio,porcentaje)
    return total

cesta = {24000: 20, 30000: 15, 12345: 25}

total_descuento = total_dela_compra(cesta, precio_con_descuento)
print(f"Total de la compra con sus descuentos: ${total_descuento:.2f}")

total_IVA = total_dela_compra(cesta, precio_con_IVA)
print(f"Total de la compra con IVA: ${total_IVA:.2f}")