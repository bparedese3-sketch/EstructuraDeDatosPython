#Lee dos números y muéstralos intercambiados. Python permite hacerlo en una sola línea, muy diferente a JS.
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

num1, num2 = num2, num1

print(f"num1 = {num1}, num2 = {num2}")