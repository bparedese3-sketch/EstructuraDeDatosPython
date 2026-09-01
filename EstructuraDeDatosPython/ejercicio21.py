#Leer las notas de N estudiantes y mostrar la nota más alta.
n = int(input("¿Cuántas notas?: "))
minima = float("inf")

for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    if nota < minima:
        minima = nota

print(f"Minima: {minima}")