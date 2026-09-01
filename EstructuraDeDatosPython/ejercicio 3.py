#Ejercicio3: #Leer la base y la altura de un rectángulo y mostrar
#su área y su perímetro. Recuerda: área = base × altura,
#perímetro = 2 × (base + altura).
# Ampliar para leer el radio de un círculo y mostrar área
# (π·r²) y perímetro (2·π·r) Usa import math y math.pi
import math
base = float(input("Base: "))
altura = float(input("Altura: "))

area = base * altura
perimetro = 2 * (base + altura)

print(f"Área del rectángulo: {area:.2f}")
print(f"Perímetro del rectángulo: {perimetro:.2f}")

print("--- Cálculo del Círculo ---")

radio = float(input("Radio del círculo: "))

area_circulo = math.pi * (radio * 2)
perimetro_circulo = 2 * math.pi * radio

print(f"Área del círculo: {area_circulo:.2f}")
print(f"Perímetro del círculo: {perimetro_circulo:.2f}")


