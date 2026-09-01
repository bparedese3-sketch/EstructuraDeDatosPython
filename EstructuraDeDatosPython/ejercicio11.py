#Un cajero solo tiene billetes de $20, $10, $5 y $1. Dado un monto, mostrar cuántos billetes de cada uno se necesitan (usando la mínima cantidad).
monto = float(input("Monto: $"))

centavos = round(monto * 100)
resto = centavos

b50 = resto // 5000
resto = resto % 5000

b20 = resto // 2000
resto = resto % 2000

b10 = resto // 1000
resto = resto % 1000

b5 = resto // 500
resto = resto % 500

b1 = resto // 100
resto = resto % 100

m25 = resto // 25
resto = resto % 25

m10 = resto // 10
resto = resto % 10

m05 = resto // 5
resto = resto % 5

m01 = resto // 1
resto = resto % 1

print(f"$50 × {b50}")
print(f"$20 × {b20}")
print(f"$10 × {b10}")
print(f"$5  × {b5}")
print(f"$1  × {b1}")
print(f"$0.25 × {m25}")
print(f"$0.10 × {m10}")
print(f"$0.05 × {m05}")
print(f"$0.01 × {m01}")