def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Programa principal
monto1 = 500
monto2 = 800
descuento1 = calcular_descuento(monto1)  # Usa 10% por defecto
descuento2 = calcular_descuento(monto2, 15)  # Usa 15% explícito

print(f"Monto total: ${monto1}")
print(f"Descuento aplicado: ${descuento1}")
print(f"Monto final a pagar: ${monto1 - descuento1}\n")

print(f"Monto total: ${monto2}")
print(f"Descuento aplicado: ${descuento2}")
print(f"Monto final a pagar: ${monto2 - descuento2}")
