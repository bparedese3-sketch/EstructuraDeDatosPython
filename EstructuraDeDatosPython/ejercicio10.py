#Leer una cantidad total de segundos y mostrarla como hh:mm:ss. Ejemplo: 3725 segundos → 01:02:05.
total = int(input("Segundos totales: "))

horas = total // 3600
resto = total % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")


