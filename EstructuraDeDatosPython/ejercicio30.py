#Escribe una función contar_primos(a, b) que cuente cuántos primos hay entre a y b.
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos(a, b):
    contador = 0

    for k in range(a, b + 1):
        if es_primo(k):
            contador += 1

    return contador

a = int(input("Inicio: "))
b = int(input("Fin: "))

cantidad = contar_primos(a, b)

print(f"Hay {cantidad} números primos entre {a} y {b}.")