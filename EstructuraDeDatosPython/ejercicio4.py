#Pide una temperatura en grados Celsius  muéstrala en Fahrenheit. Fórmula: F = C × 9/5 + 32.
celsius = float(input("Ingrese la temperatura en celsius: "))
fahrenheit = celsius * 9/5 + 32
print(f"{fahrenheit:.1f} °F")


