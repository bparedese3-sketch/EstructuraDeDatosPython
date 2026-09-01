#Leer las notas de N estudiantes (una por una) y contar cuántos aprobaron (nota ≥ 70).
n = int(input("¿Cuántos estudiantes?: "))
aprobados = 0
reprobados = 0

for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    if nota >= 7:
        aprobados += 1
    else:
        reprobados += 1
porcentaje = (aprobados / n) * 100

print(f"Aprobados: {aprobados} de {n}")
print(f"Reprobados: {reprobados} de {n}")
print(f"Porcentaje: {porcentaje}%")