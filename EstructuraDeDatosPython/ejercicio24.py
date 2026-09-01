#Lee un número y cuenta cuántos dígitos tiene (sin convertir a string).
num = int(input("Ingrese un número: "))
n = abs(num)
digitos = 0

if n == 0:
    digitos = 1
else:
    while n > 0:
        digitos += 1
        n = n // 10
print(f"{digitos} dígitos")