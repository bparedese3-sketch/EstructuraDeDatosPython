# Leer un número entero y determinar si es par o impar.
num = int(input("Ingrese un numero: "))
resultado = "par" if num % 2 == 0 else "impar"
if num % 3 == 0 and num % 5 == 0:
    multiplo = "es múltiplo de ambos (3 y 5)"
elif num % 3 == 0:
    multiplo = "es múltiplo de 3"
elif num % 5 == 0:
    multiplo = "es múltiplo de 5"
else:
    multiplo = "no es múltiplo ni de 3 ni de 5"


print(f"{num} es {resultado} y {multiplo}.")


#Leer una cantidad total de segundos y mostrarla como hh:mm:ss. Ejemplo: 3725 segundos → 01:02:05.
total = int(input("Segundos totales: "))

horas = total // 3600
resto = total % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")