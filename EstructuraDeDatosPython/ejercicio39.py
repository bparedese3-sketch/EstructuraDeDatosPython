#Dada una lista fija de notas [7, 8.5, 6, 9, 10, 5.5], calcula el promedio, la nota máxima y la mínima. Imprime los tres valores con 2 decimales
notas = [7, 8.5, 6, 9, 10, 5.5]
promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.2f}")
print(f"Máximo:   {max(notas):.2f}")
print(f"Mínimo:   {min(notas):.2f}")