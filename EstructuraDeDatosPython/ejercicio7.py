#Variables
# Leer el precio de un producto sin IVA y mostrar el IVA y el precio final

IVA = 0.15
DESCUENTO = 0.10
precio = float(input("Ingrese el precio sin IVA: "))
descuento = precio * DESCUENTO
precio_con_descuento = precio - descuento
iva = (precio_con_descuento * IVA)
total = precio_con_descuento + iva
print(f"El precio total es: {total:.2f}")
print(f"IVA:   ${iva:.2f}")
print(f"Descuento: ${descuento:.2f}")

#Ejercicio4: Lee el precio de un producto sin IVA y muestra el IVA (15%) y el total.
precio = float(input("Ingrese precio sin IVA: "))
iva = precio * 0.15
total = precio + iva

print(f"total = {total}, iva = {iva}")