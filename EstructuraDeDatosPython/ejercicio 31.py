#Escribe es_narcisista(n): retorna True si el número es igual a la suma de sus dígitos elevados al número de dígitos. Ej.: 153 = 1³+5³+3³.
def es_narcisista(n):
    n = abs(n)
    original = n
    digitos = len(str(n))
    suma = 0

    while n > 0:
        digito = n % 10
        suma += digito ** digitos
        n = n // 10

    return suma == original


# Uso
num = int(input("Número: "))

if es_narcisista(num):
    print(f"{num} es narcisista")
else:
    print(f"{num} NO es narcisista")