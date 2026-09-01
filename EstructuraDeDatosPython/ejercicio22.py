#Genera una lista de todos los primos entre 2 y 100.
primos = []

for n in range(2, 101):
    es_primo = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            es_primo = False
            break

    if es_primo:
        primos.append(n)

print(f"Primos: {primos}")