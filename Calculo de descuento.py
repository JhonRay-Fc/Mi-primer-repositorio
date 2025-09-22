#CalculoDescuentoPython.

#  Creación de la función

# Creación de la función que calcula el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento aplicando un porcentaje al monto total de la compra.

    Parámetros:
    monto_total (float): El monto total de la compra.
    porcentaje_descuento (int o float): El porcentaje de descuento a aplicar (por defecto es 10).

    Retorna:
    float: El monto del descuento calculado.
    """
    monto_descuento = monto_total * (porcentaje_descuento / 100)
    return monto_descuento

#Llamada a la función y salida de resultados

# Llamadas a la función desde el programa principal
print("--- Cliente 1 ---")
compra_cliente1 = 150.0  # Monto total de compra
# La función usa el 10% de descuento por defecto
descuento_1 = calcular_descuento(compra_cliente1)
monto_final_1 = compra_cliente1 - descuento_1

print(f"Monto total de la compra: ${compra_cliente1}")
print(f"Monto del descuento (10%): ${descuento_1}")
print(f"Monto final a pagar: ${monto_final_1}")

print("\n--- Cliente 2 ---")
compra_cliente2 = 250.0  # El monto total de la compra

# Se especifica un 15% de descuento
descuento_2 = calcular_descuento(compra_cliente2, 15)
monto_final_2 = compra_cliente2 - descuento_2

print(f"Monto total de la compra: ${compra_cliente2}")
print(f"Monto del descuento (15%): ${descuento_2}")
print(f"Monto final a pagar: ${monto_final_2}")