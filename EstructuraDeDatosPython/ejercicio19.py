#Leer N y calcular el factorial (N! = 1 × 2 × 3 × ... × N). Ejemplo: 5! = 120.
n = int(input("Ingrese un numero: "))
fact =  1

for i in range(1, n + 1):
    fact = fact * i

print(f"{n}! = {fact}")