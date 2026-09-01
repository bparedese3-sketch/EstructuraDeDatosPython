#Pide una frase al usuario y cuenta cuántas vocales (a, e, i, o, u) tiene. Ignora mayúsculas/minúsculas.
frase = input("Frase: ").lower()
vocales = {"a", "e", "i", "o", "u"}
total = 0
for ch in frase:
    if ch in vocales:
        total += 1
print(f"{total} vocales")