#Leer N y calcular la suma de 1 + 2 + 3 + ... + N.
n = int(input("N: "))
suma = 0

for i in range(2, 101, 2):
    suma = suma + i

print(f"Suma: {suma}")