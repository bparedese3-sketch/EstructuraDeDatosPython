#Escribir una función calcular_iva(precio) que reciba un precio y retorne el IVA (15%). Usarla desde el programa principal.
def calcular_iva(precio):
    return precio * 0.15
def calcular_total(precio):
    return precio + calcular_iva(precio)

precio = float(input("Precio: $"))
iva = calcular_iva(precio)
total = calcular_total(precio)

print(f"IVA de ${precio}: ${iva:.2f}")
print(f"Total a pagar: {total:.2f}")